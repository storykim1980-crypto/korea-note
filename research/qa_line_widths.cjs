/* npm install playwright; build and serve public bundle before running.
   BASE_URL=http://127.0.0.1:4173 node research/qa_line_widths.cjs
   Range.getClientRects measures actual laid-out characters, not estimated string widths.
   Warnings are editorial candidates, not proof of incorrect Japanese. */
const {chromium}=require('playwright');
const fs=require('fs'), path=require('path');
const root=path.resolve(__dirname,'..');
const routes=['/','/en/','/contact.html','/en/contact.html','/404.html',...['guides','en/guides'].flatMap(d=>fs.readdirSync(path.join(root,d)).filter(x=>x.endsWith('.html')).map(x=>'/'+d+'/'+x))];
(async()=>{
 const b=await chromium.launch({headless:true}); const report={method:'DOM Range character rectangles grouped by rendered line; fonts.ready awaited',limitations:'Installed fallback fonts vary by OS. This is Chromium layout QA, not native-speaker review. Short final lines are warnings, not automatic failures.',checks:[],errors:[],warnings:[]};
 for(const width of [320,390,768,1024,1280,1440]) for(const route of routes){
  const p=await b.newPage({viewport:{width,height:900}});
  await p.goto((process.env.BASE_URL||'http://127.0.0.1:4173')+route,{waitUntil:'networkidle'});
  await p.evaluate(()=>document.fonts.ready);
  const data=await p.evaluate(()=>{
   const rows=[];
   for(const e of document.querySelectorAll('h1,h2,h3,h4,p,.article li,.term-list dd')){
    const box=e.getBoundingClientRect(), style=getComputedStyle(e);
    if(!box.width||!box.height||e.closest('[hidden]')||style.visibility==='hidden')continue;
    const lines=[];const walker=document.createTreeWalker(e,NodeFilter.SHOW_TEXT);let n;
    while(n=walker.nextNode())for(let i=0;i<n.length;i++){
     const char=n.textContent[i];if(!char.trim())continue;
     const range=document.createRange();range.setStart(n,i);range.setEnd(n,i+1);
     const rect=range.getClientRects()[0];if(!rect||!rect.width||!rect.height)continue;
     let line=lines.find(l=>Math.abs(l.top-rect.top)<3);
     if(!line){line={top:rect.top,left:rect.left,right:rect.right,text:''};lines.push(line);}
     line.left=Math.min(line.left,rect.left);line.right=Math.max(line.right,rect.right);line.text+=char;
    }
    const available=box.width-parseFloat(style.paddingLeft)-parseFloat(style.paddingRight);
    const detail=lines.map(l=>({text:l.text,width:+(l.right-l.left).toFixed(1),fill:+((l.right-l.left)/available).toFixed(2),left:+l.left.toFixed(1),right:+l.right.toFixed(1)}));
    rows.push({tag:e.tagName,id:e.id,cls:e.className,text:e.innerText.slice(0,160),font:style.fontFamily,size:style.fontSize,available:+available.toFixed(1),lines:detail,overflow:detail.some(l=>l.left<box.left-2||l.right>box.right+2)});
   }
   return {documentOverflow:document.documentElement.scrollWidth>innerWidth+1,rows};
  });
  for(const r of data.rows){
   if(r.overflow)report.errors.push({route,width,...r});
   const last=r.lines.at(-1);
   if(r.lines.length>1 && last && (last.text.length<=2||(/^H/.test(r.tag)&&last.fill<.18)))report.warnings.push({route,width,kind:'short-final-line',...r});
  }
  if(data.documentOverflow)report.errors.push({route,width,kind:'document-overflow'});
  report.checks.push({route,width,measuredBlocks:data.rows.length,headings:data.rows.filter(r=>/^H/.test(r.tag))});
  await p.close();
 }
 await b.close();
 const dest=path.join(__dirname,'line-width-report.json');fs.writeFileSync(dest,JSON.stringify(report,null,2));
 console.log(JSON.stringify({combinations:report.checks.length,errors:report.errors.length,editorialWarnings:report.warnings.length,report:dest},null,2));
 if(report.errors.length)process.exitCode=1;
})();
