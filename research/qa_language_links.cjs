// npm install playwright; public build must be served on port 4173.
// Also tests extraction to a subdirectory and direct file:// opening.
const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),{fileURLToPath}=require('url');
const root=path.resolve(__dirname,'../../seoul-note-public');
(async()=>{
 const b=await chromium.launch();const results=[];
 for(const mode of ['http','subdirectory','file'])for(const width of [320,390,1440]){
  const p=await b.newPage({viewport:{width,height:900}});
  const base=mode==='http'?'http://127.0.0.1:4173/':mode==='subdirectory'?'http://127.0.0.1:4180/seoul-note-public/':'file://'+root+'/';
  await p.goto(base+'index.html');
  if(!await p.locator('.language-switch').isVisible())await p.locator('#menuToggle').click();
  await Promise.all([p.waitForURL('**/en/index.html'),p.locator('.language-switch').click()]);
  if(await p.locator('html').getAttribute('lang')!=='en')throw Error('English navigation failed');
  const links=await p.locator('a[href]').evaluateAll(as=>as.map(a=>a.href));
  let checked=0;
  for(const url of [...new Set(links)]){
   if(!url.startsWith(base))continue;
   const u=new URL(url);u.hash='';
   if(mode==='file'){if(!fs.existsSync(fileURLToPath(u)))throw Error('Missing local target '+url);}
   else{const res=await p.request.get(u.href);if(!res.ok())throw Error('HTTP '+res.status()+' '+url);}
   checked++;
  }
  await Promise.all([p.waitForURL('**/en/guides/*.html'),p.locator('.story-card-link').first().click()]);
  await Promise.all([p.waitForURL('**/guides/*.html'),p.locator('.header-links a[lang="ja"]').click()]);
  if(await p.locator('html').getAttribute('lang')!=='ja')throw Error('Guide alternate failed');
  await p.goto(base+'en/index.html');
  if(!await p.locator('.language-switch').isVisible())await p.locator('#menuToggle').click();
  await Promise.all([p.waitForURL(base+'index.html'),p.locator('.language-switch').click()]);
  results.push({mode,width,englishLocalTargets:checked,roundTrip:true,guideAlternate:true});
  await p.close();
 }
 await b.close(); console.log(JSON.stringify({results},null,2));
})();
