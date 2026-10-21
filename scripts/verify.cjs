const {chromium}=require('playwright');
const fs=require('fs'),path=require('path'),assert=require('assert/strict');
(async()=>{
 const root=path.resolve(__dirname,'..'),base=process.argv[2]||'http://127.0.0.1:8770/';
 const routes=JSON.parse(fs.readFileSync(path.join(root,'route-map.json'),'utf8'));
 const browser=await chromium.launch({headless:true,channel:'msedge'}),results=[],errors=[];
 try{for(const width of [1440,768,390,320]){
  const page=await browser.newPage({viewport:{width,height:950}});page.on('pageerror',e=>errors.push(e.message));
  for(const route of routes){
   const response=await page.goto(base+route.target,{waitUntil:'domcontentloaded'});assert.equal(response.status(),200,route.target);
   if(route.disposition==='redirect'){await page.waitForURL(new URL(route.redirectTo,base).href);assert.equal(await page.locator('body.transport-site').count(),1);continue}
   await page.evaluate(async()=>{await Promise.all([...document.images].map(async i=>{i.loading='eager';try{await i.decode()}catch{}}))});
   const r=await page.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth,broken:[...document.images].filter(i=>!i.naturalWidth).map(i=>i.src),noindex:document.querySelector('meta[name="robots"]').content,h1:document.querySelectorAll('h1').length,forms:document.forms.length,colophon:document.querySelectorAll('#cwu-colophon').length,height:document.documentElement.scrollHeight,footer:Math.round(document.querySelector('footer').getBoundingClientRect().height)}));
   results.push({route:route.target,width,...r});assert(!r.overflow&&!r.broken.length&&r.h1===1&&r.colophon===1&&r.forms===0&&r.noindex.includes('noindex'),JSON.stringify(results.at(-1)));
   if(width<=390){await page.locator('.menu').click();assert(await page.locator('#nav').isVisible());await page.keyboard.press('Escape');assert(!(await page.locator('#nav').isVisible()))}
   if(route.target==='contact/index.html'){
    await page.locator('.office-image-button').click();assert(await page.locator('#office-call-dialog').evaluate(d=>d.open));assert.equal(await page.locator('#office-call-dialog a').count(),2);await page.keyboard.press('Escape');assert(await page.locator('.office-image-button').evaluate(a=>a===document.activeElement));
    await page.locator('.team-directory details').first().locator('summary').click();assert.equal(await page.locator('.team-directory details[open] .team-card').count(),2);
    await page.locator('.transport-map summary').click();assert(await page.locator('.transport-map iframe').isVisible());
   }
   if(route.target==='pacific-pride-card-lock/index.html'){await page.locator('.joy-image-button').click();assert(await page.locator('#joy-contact-dialog').evaluate(d=>d.open));assert.equal(await page.locator('#joy-contact-dialog a').count(),2);await page.keyboard.press('Escape')}
   const details=page.locator('main details');for(let i=0;i<await details.count();i++){const d=details.nth(i);if(!await d.evaluate(d=>d.open)){await d.locator('summary').click();assert(await d.evaluate(d=>d.open));assert(!(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth)))}}
  }await page.close()
 }
 const reduced=await browser.newPage({reducedMotion:'reduce'});await reduced.goto(base+'index.html');assert(await reduced.locator('.metal-reflection').evaluateAll(nodes=>nodes.every(n=>getComputedStyle(n).display==='none')));await reduced.close();assert.equal(errors.length,0,errors.join('\n'));
 console.log(JSON.stringify({base,renderChecks:results.length,redirectChecks:40,interactionViewports:4,errors,results},null,2));
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exit(1)});
