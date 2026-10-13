const button=document.querySelector('.menu');const nav=document.querySelector('#nav');button.addEventListener('click',()=>{const open=button.getAttribute('aria-expanded')==='true';button.setAttribute('aria-expanded',String(!open));nav.classList.toggle('open',!open)});document.addEventListener('keydown',event=>{if(event.key==='Escape'){button.setAttribute('aria-expanded','false');nav.classList.remove('open')}});
// Independent, newly randomized sunlight passes rather than synchronized loops.
const steelSurfaces=document.querySelectorAll('.masthead,.proof-strip,.service,.story-photo span,.dispatch-band,.bottom-cta,footer,.page-head,.notice,.contact-panel a,.fleet-gallery figure,.secondary-button,.summary,.hero-stamp,.menu');
steelSurfaces.forEach(element=>element.classList.add('steel-surface'));
const steelTitles=document.querySelectorAll('.hero h1 span,.services h2,.story h2,.fleet-feature h2,.application-aside h2,.application-step h2,.prose h3,.prose h4');
steelTitles.forEach(element=>element.classList.add('steel-text'));
const motionPreference=matchMedia('(prefers-reduced-motion: reduce)');
const glintElements=[...steelSurfaces,...steelTitles];
const inView=new WeakSet();
const observer=new IntersectionObserver(entries=>entries.forEach(entry=>entry.isIntersecting?inView.add(entry.target):inView.delete(entry.target)));
glintElements.forEach(element=>{
  observer.observe(element);
  function nextPass(){
    setTimeout(()=>{
      if(!motionPreference.matches&&!document.hidden&&inView.has(element)){
        element.style.setProperty('--steel-duration',`${1.8+Math.random()*2.1}s`);
        element.classList.remove('steel-glint');
        void element.offsetWidth;
        element.classList.add('steel-glint');
      }
      nextPass();
    },4500+Math.random()*13000);
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
