// Requires playwright with Chromium and WebKit. Serve public build on port 4173.
// These are touch/viewport browser simulations, NOT real iPhone or Samsung hardware tests.
const {chromium,webkit}=require('playwright');
const fs=require('fs'),path=require('path');
const sizes=[[320,480],[360,800],[384,832],[390,844],[393,852],[402,874],[412,915],[430,932],[440,956],[844,390],[915,412]];
(async()=>{
 const results=[],failures=[];
 for(const [engineName,engine] of Object.entries({chromium,webkit})){
  const browser=await engine.launch();
  for(const [width,height]of sizes)for(const route of ['/','/en/']){
   const page=await browser.newPage({viewport:{width,height},isMobile:true,hasTouch:true,reducedMotion:'reduce'});
   const label={engine:engineName,width,height,route};let actions=0;
   try{
    await page.goto('http://127.0.0.1:4173'+route,{waitUntil:'networkidle'});
    const headerFits = await page.evaluate(() => [...document.querySelectorAll('.nav-actions button')].filter(e=>getComputedStyle(e).display!=='none').every(e=>{const r=e.getBoundingClientRect();return r.left>=0&&r.right<=innerWidth+1;}));
    if(!headerFits)throw Error('Header touch target outside screen');
    const links=await page.locator('#mainNav a[href^="#"]').evaluateAll(as=>as.map(a=>a.getAttribute('href')));
    for(let i=0;i<links.length;i++){
     await page.evaluate(()=>window.scrollTo({top:0,behavior:'instant'}));
     await page.locator('#menuToggle').tap();
     const panel=await page.locator('#mainNav').evaluate(e=>({bottom:e.getBoundingClientRect().bottom,height:innerHeight,overflow:getComputedStyle(e).overflowY}));
     if(panel.bottom>panel.height+1)throw Error('Menu exceeds visual viewport '+JSON.stringify(panel));
     await page.locator('#mainNav a[href^="#"]').nth(i).tap();
     const state=await page.evaluate(href=>{
      const nav=document.querySelector('#mainNav'),target=document.querySelector(href),header=document.querySelector('.site-header');
      const heading=target.querySelector('h1,h2,h3')||target;
      return {expanded:document.querySelector('#menuToggle').getAttribute('aria-expanded'),hidden:getComputedStyle(nav).display==='none',targetTop:target.getBoundingClientRect().top,headingTop:heading.getBoundingClientRect().top,headerBottom:header.getBoundingClientRect().bottom,focusVisible:!nav.contains(document.activeElement),scroll:scrollY};
     },links[i]);
     if(state.expanded!=='false'||!state.hidden||!state.focusVisible||state.targetTop<state.headerBottom-1||state.headingTop<state.headerBottom)throw Error('Covered target '+links[i]+' '+JSON.stringify(state));
     actions++;
    }
    await page.locator('#menuToggle').tap();
    await page.setViewportSize({width,height:Math.max(280,height-120)});
    await page.waitForTimeout(100);
    if(await page.locator('#menuToggle').getAttribute('aria-expanded')!=='true')throw Error('Height-only viewport change unexpectedly closed menu');
    const bounded=await page.locator('#mainNav').evaluate(e=>e.getBoundingClientRect().bottom<=innerHeight+1);
    if(!bounded)throw Error('Menu not bounded after viewport height change');
    await page.locator('#menuToggle').tap();
    await page.setViewportSize({width,height});
    actions++;
    // Large UI text forces an independently scrolling menu, including in landscape.
    await page.addStyleTag({content:'#mainNav a {font-size:32px!important;line-height:1.6!important;}'});
    await page.locator('#menuToggle').tap();
    await page.locator('#mainNav a').last().scrollIntoViewIfNeeded();
    const last=await page.locator('#mainNav a').last().evaluate(e=>{const a=e.getBoundingClientRect(),n=e.parentElement.getBoundingClientRect();return {top:a.top,bottom:a.bottom,navTop:n.top,navBottom:n.bottom,screen:innerHeight}});
    if(last.top<last.navTop-1||last.bottom>last.screen+1)throw Error('Last item unreachable '+JSON.stringify(last));
    await page.keyboard.press('Escape');
    if(await page.locator('#menuToggle').getAttribute('aria-expanded')!=='false')throw Error('Escape did not close');
    if(!await page.locator('#menuToggle').evaluate(e=>e===document.activeElement))throw Error('Escape focus not restored');
    actions++;
    await page.locator('#menuToggle').tap();
    await page.locator('.brand').first().tap();
    if(await page.locator('#menuToggle').getAttribute('aria-expanded')!=='false')throw Error('Outside did not close');
    actions++;
    await page.locator('#menuToggle').tap();
    await page.setViewportSize({width:height,height:width});
    await page.waitForFunction(()=>document.querySelector('#menuToggle').getAttribute('aria-expanded')==='false');
    actions++;
    results.push({...label,actions,passed:true});
   }catch(e){failures.push({...label,error:e.message});}
   await page.close();
  }
  await browser.close();
 }
 const report={limitations:'Chromium/WebKit touch simulations with generic viewport sizes; no physical Galaxy S26, Samsung Internet or iPhone device tested.',states:results.length+failures.length,actions:results.reduce((n,r)=>n+r.actions,0),results,failures};
 fs.writeFileSync(path.join(__dirname,'mobile-navigation-results.json'),JSON.stringify(report,null,2));
 console.log(JSON.stringify({states:report.states,actions:report.actions,failures},null,2));
 if(failures.length)process.exitCode=1;
})();
