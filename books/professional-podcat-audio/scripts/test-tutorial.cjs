// Set PODCAT_PLAYWRIGHT_MODULE to a Playwright package path when it is not on NODE_PATH.
// Optionally set PODCAT_BROWSER_PATH to an existing Chromium executable.
const {chromium}=require(process.env.PODCAT_PLAYWRIGHT_MODULE||'playwright');
const path=require('node:path');
const {pathToFileURL}=require('node:url');
const os=require('node:os');
const qa=process.env.PODCAT_QA_DIR||os.tmpdir();
const assert=require('node:assert/strict');
(async()=>{
const browser=await chromium.launch({headless:true,...(process.env.PODCAT_BROWSER_PATH?{executablePath:process.env.PODCAT_BROWSER_PATH}:{})});const context=await browser.newContext({viewport:{width:1360,height:980},acceptDownloads:true});const page=await context.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));await page.goto(pathToFileURL(path.resolve(__dirname,'../tutorial.html')).href);
assert.equal(await page.locator('#guide').isVisible(),false);
await page.selectOption('#mic','bees');assert.equal(await page.locator('#guide').isVisible(),true);assert.equal(await page.locator('#mode option').count(),5);assert.equal(await page.locator('#stepNav button').count(),10);assert.match(await page.locator('#selectionNote').innerText(),/48V OFF/);
await page.locator('#check').check();assert.equal(await page.locator('#progress').getAttribute('value'),'1');assert.equal(await page.locator('#progress').evaluate(e=>e.value),1);
await page.reload();assert.equal(await page.locator('#check').isChecked(),true);
await page.selectOption('#mic','twin');assert.equal(await page.locator('#mode option').count(),2);assert.equal(await page.locator('#check').isChecked(),false);assert.match(await page.locator('#selectionNote').innerText(),/48V ON/);
let combinations=0;for(const mic of ['bees','twin']){await page.selectOption('#mic',mic);const modes=await page.locator('#mode option').allTextContents();for(const mode of modes){await page.selectOption('#mode',mode);for(const preset of ['raw','spoken','dynamic']){await page.selectOption('#preset',preset);for(const daw of ['garageband','live']){await page.selectOption('#daw',daw);assert.match(await page.locator('#recallSummary').innerText(),mic==='bees'?/BeesNeez/:/Twin87/);assert.equal(await page.locator('#stepNav button').count(),10);assert.equal(await page.locator('#recallBody .setting').count()>40,true);combinations++;}}}}
await page.locator('#lufsA').fill('-22');await page.locator('#lufsB').fill('-19.5');assert.match(await page.locator('#matchResult').innerText(),/take B down 2.5 dB/);
await page.locator('[name=take]').fill('=MY_TEST');await page.locator('[name=notes]').fill('Quote "test", comma\nNewline test');await page.locator('[name=peak]').fill('-12');await page.locator('[name=lufs]').fill('-22');await page.locator('#logForm button[type=submit]').click();assert.match(await page.locator('#logRows').innerText(),/=MY_TEST/);
const down=page.waitForEvent('download');await page.locator('#exportCsv').click();const d=await down;const stream=await d.createReadStream();let bytes='';for await(const ch of stream)bytes+=ch;assert.match(bytes,/\r\n/);assert.match(bytes,/'=MY_TEST/);assert.match(bytes,/""test""/);assert.equal(bytes.startsWith('\uFEFF'),true);assert.equal(bytes.includes('\\r\\n'),false);
await page.reload();assert.match(await page.locator('#logRows').innerText(),/=MY_TEST/);await page.locator('#check').check();await page.locator('#reset').click();assert.equal(await page.locator('#check').isChecked(),false);assert.match(await page.locator('#logRows').innerText(),/=MY_TEST/);
await page.selectOption('#mic','bees');await page.selectOption('#preset','spoken');await page.selectOption('#daw','live');await page.locator('[data-step="3"]').click();await page.screenshot({path:path.join(qa,'podcat-desktop.png'),fullPage:false});
await page.emulateMedia({media:'print'});await page.evaluate(()=>document.body.classList.add('print-full'));await page.pdf({path:path.join(qa,'podcat-tutorial-print.pdf'),format:'A4',printBackground:true,margin:{top:'15mm',bottom:'15mm',left:'15mm',right:'15mm'}});await page.emulateMedia({media:'screen'});await page.evaluate(()=>document.body.classList.remove('print-full'));
await page.setViewportSize({width:390,height:844});await page.screenshot({path:path.join(qa,'podcat-mobile.png'),fullPage:false});assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
for(let i=0;i<10;i++){await page.locator(`[data-step="${i}"]`).click();assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);}
assert.deepEqual(errors,[]);console.log(JSON.stringify({passed:true,combinations,jsErrors:errors,csvBytes:bytes.length},null,2));await browser.close();
})().catch(e=>{console.error(e);process.exitCode=1;});
