const button=document.querySelector('.menu');const nav=document.querySelector('#nav');button.addEventListener('click',()=>{const open=button.getAttribute('aria-expanded')==='true';button.setAttribute('aria-expanded',String(!open));nav.classList.toggle('open',!open)});document.addEventListener('keydown',event=>{if(event.key==='Escape'){button.setAttribute('aria-expanded','false');nav.classList.remove('open')}});
document.querySelectorAll('footer h3').forEach(heading=>{
 const frame=document.createElement('div');frame.className='footer-heading-frame';
 heading.replaceWith(frame);frame.append(heading);
});
// Recessed dark steel behind bright headings preserves the approved silver material.
document.querySelectorAll('.page-head,.dispatch-band,.resource-hero').forEach(surface=>{
 const children=[...surface.children].filter(child=>!child.matches('.source-header-photo,.policy-header-panel'));
 if(!children.length)return;
 const panel=document.createElement('div');panel.className='bright-steel-copy';
 children.forEach(child=>panel.append(child));
 surface.prepend(panel);
});
// Keep contact choices available without JavaScript; enhance them into native dialogs.
[
 ['.office-image-button','office-call-options','office-call-dialog','office-call-title'],
 ['.joy-image-button','joy-contact-options','joy-contact-dialog','joy-contact-title']
].forEach(([selector,optionsId,dialogId,titleId])=>{
 const trigger=document.querySelector(selector),options=document.getElementById(optionsId);
 if(!trigger||!options)return;
 const dialog=document.createElement('dialog');
 dialog.id=dialogId;dialog.className='office-call-dialog';
 dialog.setAttribute('aria-labelledby',titleId);
 options.before(dialog);dialog.append(options);
 const close=document.createElement('button');close.type='button';close.className='office-call-close';close.textContent='Close';
 options.append(close);
 trigger.setAttribute('aria-haspopup','dialog');trigger.setAttribute('aria-controls',dialog.id);
 trigger.setAttribute('role','button');
 trigger.addEventListener('keydown',event=>{if(event.key===' '){event.preventDefault();trigger.click()}});
 trigger.addEventListener('click',event=>{event.preventDefault();dialog.showModal();options.querySelector('a').focus()});
 close.addEventListener('click',()=>dialog.close());
 dialog.addEventListener('click',event=>{if(event.target===dialog)dialog.close()});
 dialog.addEventListener('close',()=>trigger.focus());
});
// Independent, newly randomized sunlight passes rather than synchronized loops.
const steelSurfaces=document.querySelectorAll('.masthead,.resource-hero,.service,.story-photo span,.dispatch-band,.bottom-cta,footer,.page-head,.notice,.contact-panel a,.fleet-gallery figure,.secondary-button,.summary,.menu');
steelSurfaces.forEach(element=>element.classList.add('steel-surface'));
const steelTitles=[...document.querySelectorAll('h1,h2,h3,h4,.hero-lead,.hero h1 span,.command-copy h1 span,.resource-hero h1 span')].filter(element=>!element.closest('.contact-disclosure,.document-folder'));
steelTitles.forEach(element=>element.classList.add('steel-text'));
const motionPreference=matchMedia('(prefers-reduced-motion: reduce)');
// Border reflections and plate reflections have separate clocks, even on the same panel.
const borders=document.querySelectorAll('.brand-logo-frame,.contact-keep-moving,.assurance-image,.put-work-image-button,.fuel-solution-image-button,.team-image-button,.document-folder,.connection-file,.connection-choice,.connection-open,.directions-image-button,.fuel-supply-image-button,.contact-disclosure,.email-image-button,.office-image-button,.dispatch-image-button,.document-search-hero,.resource-hero,.service,.industrial-window,.story-photo,.fleet-gallery figure,.command-photo,.office-console,.email-console,.team-card,.contact-hours,.contact-address,.resource-tool,.document-card,.notice,.summary,.secondary-button,.page-head,.dispatch-band,.bottom-cta,footer,.source-header-photo,.source-photo-rail figure,.familiar-photo,.policy-navigator,.policy-header-panel,.fleet-action,.bottom-cta .button,.history-card,.fleet-image-button,.hero-dispatch,.cardlock-action,.cardlock-sales,.joy-image-button');
const plates=document.querySelectorAll('.bottom-cta,footer,.connection-choice,.office-call-choice,.office-call-close,.contact-disclosure>summary,.document-folder>summary,.cardlock-action-label,.company-assurance,.page-head,.resource-hero,.dispatch-band,.contact-address');
const metalLayers=[];
function addReflection(element,kind){
  element.classList.add('metal-host');
  const layer=document.createElement('span');
  layer.className=`metal-reflection metal-${kind}`;
  layer.setAttribute('aria-hidden','true');
  element.append(layer);
  metalLayers.push(layer);
}
borders.forEach(element=>addReflection(element,'border'));
plates.forEach(element=>addReflection(element,'plate'));
const glintElements=[...steelSurfaces,...steelTitles,...metalLayers];
const inView=new WeakSet();
const observer=new IntersectionObserver(entries=>entries.forEach(entry=>entry.isIntersecting?inView.add(entry.target):inView.delete(entry.target)));
glintElements.forEach(element=>{
  observer.observe(element.classList.contains('metal-reflection')?element.parentElement:element);
  function nextPass(){
    setTimeout(()=>{
      if(!motionPreference.matches&&!document.hidden&&inView.has(element.classList.contains('metal-reflection')?element.parentElement:element)){
        element.style.setProperty('--steel-duration',`${element.classList.contains('metal-plate')?2.6+Math.random()*2.2:1.8+Math.random()*2.1}s`);
        element.style.setProperty('--glint-angle',`${95+Math.random()*35}deg`);
        element.classList.remove('steel-glint');
        void element.offsetWidth;
        element.classList.add('steel-glint');
      }
      nextPass();
    },2800+Math.random()*14500);
  }
  nextPass();
});
const teamFilters=document.querySelectorAll('[data-team-filter]');
teamFilters.forEach(filter=>filter.addEventListener('click',()=>{
  teamFilters.forEach(button=>button.setAttribute('aria-pressed',String(button===filter)));
  let visible=0;
  document.querySelectorAll('.team-card').forEach(card=>{card.hidden=filter.dataset.teamFilter!=='all'&&card.dataset.department!==filter.dataset.teamFilter;if(!card.hidden)visible++});
  document.querySelector('.team-result').textContent=`${visible} contacts shown`;
}));

document.querySelectorAll('.command-copy h1 span,.team-heading h2').forEach(element=>element.classList.add('steel-text'));
const resourceSearch=document.querySelector('#resource-search');
if(resourceSearch){
 let resourceCategory='all';
 const resourceButtons=document.querySelectorAll('[data-resource-filter]');
 const resourceCards=document.querySelectorAll('[data-resource]');
 function filterResources(){let count=0;const query=resourceSearch.value.trim().toLocaleLowerCase();resourceCards.forEach(card=>{card.hidden=!(resourceCategory==='all'||card.dataset.resource===resourceCategory)||!card.textContent.toLocaleLowerCase().includes(query);if(!card.hidden)count++});const shown=[...resourceCards].filter(card=>!card.hidden);resourceCards.forEach(card=>card.classList.remove('document-last'));if(shown.length%2)shown.at(-1).classList.add('document-last');document.querySelector('#resource-count').textContent=`${count} of ${resourceCards.length} ${document.querySelector('.resource-library').dataset.resourceKind||'Resources'}`;document.querySelectorAll('.document-folder').forEach(folder=>{const matches=[...folder.querySelectorAll('[data-resource]')].filter(card=>!card.hidden).length;folder.hidden=matches===0;if(query||resourceCategory!=='all'){folder.open=matches>0;folder.dataset.searchOpened='true'}else if(folder.dataset.searchOpened){folder.open=false;delete folder.dataset.searchOpened}});document.querySelector('#resource-empty').hidden=count!==0;resourceButtons.forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.resourceFilter===resourceCategory)))}
 filterResources();
 resourceSearch.addEventListener('input',filterResources);
 resourceButtons.forEach(button=>button.addEventListener('click',()=>{resourceCategory=button.dataset.resourceFilter;filterResources()}));
 document.querySelector('#resource-reset').addEventListener('click',()=>{resourceCategory='all';resourceSearch.value='';filterResources();resourceSearch.focus()});
}

const historyButton=document.querySelector('.story-copy .history-card');
if(historyButton){
 const historyFont=getComputedStyle(document.querySelector('.story-copy p:not(.eyebrow)')).font;
 const historyMeasure=document.createElement('canvas').getContext('2d');
 historyMeasure.font=historyFont;
 historyButton.style.setProperty('--history-button-width',`${Math.ceil(historyMeasure.measureText('principles that started this business still drive it.').width)}px`);
}

// Alpha-inspired resource selection, using Rinehart's compact steel components.
const connectionSelect=document.querySelector('#connection-select');
if(connectionSelect){
 const choices=[...document.querySelectorAll('.connection-choice')];
 const files=[...document.querySelectorAll('.connection-file')];
 const filters=[...document.querySelectorAll('[data-connection-filter]')];
 let connectionPulseTimer,connectionScrollTimer;
 function transferConnection(source,destination){
  if(motionPreference.matches||!source)return;
  document.querySelectorAll('.connection-transfer').forEach(e=>{e.getAnimations().forEach(a=>a.cancel());e.remove()});
  const start=source.getBoundingClientRect(),target=destination.getBoundingClientRect();
  const sx=start.left+start.width*.75,sy=start.top+start.height/2;
  const ex=target.left+Math.min(48,target.width*.15),ey=Math.max(24,Math.min(innerHeight-24,target.top+Math.min(170,target.height*.4)));
  const angle=Math.atan2(ey-sy,ex-sx)*180/Math.PI;
  const move=(x,y,scale)=>`translate(${x}px,${y}px) rotate(${angle}deg) scale(${scale})`;
  const spark=document.createElement('span');spark.className='connection-transfer';spark.setAttribute('aria-hidden','true');document.body.append(spark);
  const flight=spark.animate([{opacity:0,transform:move(sx,sy,.6)},{opacity:1,transform:move(sx+(ex-sx)*.1,sy+(ey-sy)*.1,1),offset:.12},{opacity:1,transform:move(ex,ey,1),offset:.8},{opacity:0,transform:move(ex,ey,1.7)}],{duration:520,easing:'cubic-bezier(.19,.74,.24,1)',fill:'forwards'});
  flight.finished.then(()=>{destination.classList.remove('is-receiving');void destination.offsetWidth;destination.classList.add('is-receiving');clearTimeout(connectionPulseTimer);connectionPulseTimer=setTimeout(()=>destination.classList.remove('is-receiving'),700)}).catch(()=>{}).finally(()=>spark.remove());
 }
 function chooseConnection(id,source){
  const chosen=files.find(file=>file.id===id);if(!chosen)return;
  files.forEach(file=>file.classList.remove('is-receiving'));
  files.forEach(file=>file.hidden=file!==chosen);
  choices.forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.connection===id)));
  connectionSelect.value=id;
  filters.forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.connectionFilter===chosen.dataset.group)));
  document.querySelectorAll('.connection-choice-group').forEach(group=>group.hidden=group.dataset.connectionGroup!==chosen.dataset.group);
  transferConnection(source,chosen);
  clearTimeout(connectionScrollTimer);
  // Reveal the complete selected card after its transfer effect, for every control.
  // Oversized cards start at the top so their content remains readable in order.
  if(source){connectionScrollTimer=setTimeout(()=>{
   if(chosen.hidden)return;
   const fits=chosen.getBoundingClientRect().height<=innerHeight-32;
   chosen.scrollIntoView({block:fits?'center':'start',behavior:motionPreference.matches?'instant':'smooth'});
  },motionPreference.matches?0:540)}
 }
 function chooseCategory(group,source){const first=choices.find(button=>button.dataset.group===group);if(first)chooseConnection(first.dataset.connection,source)}
 choices.forEach(button=>button.addEventListener('click',()=>chooseConnection(button.dataset.connection,button)));
 filters.forEach(button=>button.addEventListener('click',()=>chooseCategory(button.dataset.connectionFilter,button)));
 connectionSelect.addEventListener('change',()=>chooseConnection(connectionSelect.value,connectionSelect));
 function readCategoryHash(){const group=location.hash.slice(1);chooseCategory(['industry','government','sds'].includes(group)?group:'industry')}
 window.addEventListener('hashchange',readCategoryHash);readCategoryHash();
}
