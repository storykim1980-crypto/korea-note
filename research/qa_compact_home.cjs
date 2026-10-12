// Run with Playwright and @axe-core/playwright installed; serve public on port 4173.
const {chromium,webkit}=require('playwright');
const AxeBuilder=require('@axe-core/playwright').default;
const fs=require('fs'),path=require('path');
(async()=>{
 const results=[],failures=[],accessibility=[];
 for(const [engineName,engine]of Object.entries({chromium,webkit})){
  const b=await engine.launch();
  for(const route of ['/','/en/'])for(const width of [320,390,844]){
   const context=await b.newContext({viewport:{width,height:900},isMobile:true,hasTouch:true});
   const p=await context.newPage();
   try{
    await p.goto('http://127.0.0.1:4173'+route,{waitUntil:'networkidle'});
    if(await p.locator('.home-detail[open]').count()!==0)throw Error('Panels not initially closed');
    if(await p.locator('.story-card:visible').count()!==9)throw Error('Nine guides not visible');
    const ids=await p.locator('.home-detail').evaluateAll(es=>es.map(e=>e.id));
    for(const id of ids){
     await p.locator('#'+id+'>summary').tap();
     if(!await p.locator('#'+id).evaluate(e=>e.open))throw Error('Panel did not open '+id);
     if(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1))throw Error('Panel overflow '+id);
     if(engineName==='chromium'&&width===390){
      const a=await new AxeBuilder({page:p}).withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa']).analyze();
      accessibility.push({route,panel:id,violations:a.violations.map(v=>({id:v.id,nodes:v.nodes.map(n=>n.target)}))});
      if(a.violations.length)throw Error('Axe violations '+id);
     }
     await p.locator('#'+id+'>summary').tap();
    }
    // Open a tool from the always-visible strip, then generate a plan.
    await p.locator('.home-quick-actions a[href="#planner"]').tap();
    if(!await p.locator('#panel-planner').evaluate(e=>e.open))throw Error('Planner quick action failed');
    await p.locator('#buildPlan').tap();
    if(!await p.locator('#plannerResult').isVisible())throw Error('Planner output missing');
    await p.goto('http://127.0.0.1:4173'+route+'#travelHelp',{waitUntil:'networkidle'});
    if(!await p.locator('#panel-travel').evaluate(e=>e.open))throw Error('Deep link did not open travel');
    const visible=await p.locator('#travelHelp').evaluate(e=>e.getBoundingClientRect().top>=document.querySelector('.site-header').getBoundingClientRect().bottom-1);
    if(!visible)throw Error('Deep link covered by header');
    results.push({engine:engineName,route,width,panels:ids.length,planner:true,deepLink:true});
   }catch(e){failures.push({engine:engineName,route,width,error:e.message});}
   await context.close();
  }
  // Native details stay operable without JavaScript.
  const p=await b.newPage({javaScriptEnabled:false,viewport:{width:390,height:844}});
  await p.goto('http://127.0.0.1:4173/');await p.locator('#panel-travel>summary').click();
  if(!await p.locator('#travelHelp').isVisible())failures.push({engine:engineName,error:'No-JS disclosure failed'});
  await p.close();await b.close();
 }
 const report={results,expandedAxe:accessibility,failures};
 fs.writeFileSync(path.join(__dirname,'compact-home-results.json'),JSON.stringify(report,null,2));
 console.log(JSON.stringify({states:results.length,expandedAxe:accessibility.length,failures},null,2));
 if(failures.length)process.exitCode=1;
})();
