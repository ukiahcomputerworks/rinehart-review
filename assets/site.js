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
// Independent, newly randomized sunlight passes rather than synchronized loops.
const steelSurfaces=document.querySelectorAll('.masthead,.resource-hero,.proof-strip,.service,.story-photo span,.dispatch-band,.bottom-cta,footer,.page-head,.notice,.contact-panel a,.fleet-gallery figure,.secondary-button,.summary,.hero-stamp,.menu');
steelSurfaces.forEach(element=>element.classList.add('steel-surface'));
const steelTitles=document.querySelectorAll('h1,h2,h3,h4,.hero-lead,.hero h1 span,.command-copy h1 span,.resource-hero h1 span');
steelTitles.forEach(element=>element.classList.add('steel-text'));
const motionPreference=matchMedia('(prefers-reduced-motion: reduce)');
// Border reflections and plate reflections have separate clocks, even on the same panel.
const borders=document.querySelectorAll('.document-folder,.connection-file,.connection-choice,.connection-open,.directions-image-button,.fuel-supply-image-button,.contact-disclosure,.email-image-button,.office-image-button,.dispatch-image-button,.document-search-hero,.resource-hero,.service,.industrial-window,.story-photo,.fleet-gallery figure,.command-photo,.office-console,.email-console,.team-card,.contact-hours,.contact-address,.resource-tool,.document-card,.notice,.hero-stamp,.summary,.secondary-button,.page-head,.dispatch-band,.bottom-cta,.proof-strip,footer,.source-header-photo,.source-photo-rail figure,.familiar-photo,.policy-navigator,.policy-header-panel,.fleet-action,.bottom-cta .button,.history-card,.fleet-image-button,.hero-dispatch,.cardlock-action,.cardlock-sales,.cardlock-sales-actions a');
const plates=document.querySelectorAll('.page-head,.resource-hero,.dispatch-band,.contact-address');
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
 function chooseConnection(id){
  const chosen=files.find(file=>file.id===id);if(!chosen)return;
  files.forEach(file=>file.hidden=file!==chosen);
  choices.forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.connection===id)));
  connectionSelect.value=id;
  filters.forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.connectionFilter===chosen.dataset.group)));
  document.querySelectorAll('.connection-choice-group').forEach(group=>group.hidden=group.dataset.connectionGroup!==chosen.dataset.group);
 }
 function chooseCategory(group){const first=choices.find(button=>button.dataset.group===group);if(first)chooseConnection(first.dataset.connection)}
 choices.forEach(button=>button.addEventListener('click',()=>chooseConnection(button.dataset.connection)));
 filters.forEach(button=>button.addEventListener('click',()=>chooseCategory(button.dataset.connectionFilter)));
 connectionSelect.addEventListener('change',()=>chooseConnection(connectionSelect.value));
 function readCategoryHash(){const group=location.hash.slice(1);chooseCategory(['industry','government','sds'].includes(group)?group:'industry')}
 window.addEventListener('hashchange',readCategoryHash);readCategoryHash();
}
