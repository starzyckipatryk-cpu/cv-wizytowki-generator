(function(){'use strict';
if(!('scrollBehavior' in document.documentElement.style)){
  document.querySelectorAll('a[href^="#"]').forEach(function(a){
    a.addEventListener('click',function(e){
      var id=this.getAttribute('href');if(id==='#')return;
      var t=document.querySelector(id);if(t){e.preventDefault();t.scrollIntoView({behavior:'smooth',block:'start'});t.focus({preventScroll:true})}
    })
  })
}
if(!window.matchMedia('(prefers-reduced-motion: reduce)').matches){
  var obs=new IntersectionObserver(function(entries){
    entries.forEach(function(en){if(en.isIntersecting){en.target.classList.add('is-visible');obs.unobserve(en.target)}})
  },{rootMargin:'0px 0px -50px 0px',threshold:.1});
  document.querySelectorAll('[data-animate]').forEach(function(el){obs.observe(el)})
}else{document.querySelectorAll('[data-animate]').forEach(function(el){el.style.opacity='1';el.style.transform='none'})}
var qrImgs=document.querySelectorAll('img[data-qr-src]');
if(qrImgs.length){
  var qrObs=new IntersectionObserver(function(entries){
    entries.forEach(function(en){if(en.isIntersecting){var img=en.target;img.src=img.dataset.qrSrc;img.removeAttribute('data-qr-src');qrObs.unobserve(img)}})
  },{rootMargin:'100px'});
  qrImgs.forEach(function(img){qrObs.observe(img)})
}
document.querySelectorAll('.contact__item').forEach(function(item){
  item.addEventListener('click',function(e){
    if(e.target.closest('a'))return;
    var txt=this.querySelector('span')?.textContent?.trim();if(!txt)return;
    navigator.clipboard.writeText(txt).then(function(){showToast('Skopiowano: '+txt)}).catch(function(){
      var ta=document.createElement('textarea');ta.value=txt;document.body.appendChild(ta);ta.select();document.execCommand('copy');document.body.removeChild(ta);showToast('Skopiowano: '+txt)
    })
  });
  item.style.cursor='copy';item.title='Kliknij, aby skopiować'
})
function showToast(msg){
  var ex=document.querySelector('.toast');if(ex)ex.remove();
  var t=document.createElement('div');t.className='toast';t.textContent=msg;t.setAttribute('role','status');t.setAttribute('aria-live','polite');document.body.appendChild(t);
  requestAnimationFrame(function(){t.classList.add('toast--show')});
  setTimeout(function(){t.classList.remove('toast--show');setTimeout(function(){t.remove()},300)},2500)
}
var y=document.querySelector('[data-current-year]');if(y)y.textContent=new Date().getFullYear();
document.body.classList.add('js-loaded')
})();
(function(){var s=document.createElement('style');s.textContent='.toast{position:fixed;bottom:1.5rem;left:50%;transform:translateX(-50%) translateY(100px);padding:.75rem 1.5rem;background:#1a1a2e;color:#fafafa;border-radius:.5rem;box-shadow:0 10px 25px -5px rgba(0,0,0,.2);font-size:.875rem;font-weight:500;z-index:1000;opacity:0;transition:transform .3s ease,opacity .3s ease}.toast--show{transform:translateX(-50%) translateY(0);opacity:1}[data-animate]{opacity:0;transform:translateY(20px);transition:opacity .6s ease,transform .6s ease}[data-animate].is-visible{opacity:1;transform:translateY(0)}.js-loaded [data-animate]{opacity:0}';document.head.appendChild(s)})();
