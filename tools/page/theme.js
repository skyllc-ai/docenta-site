// SPDX-License-Identifier: LicenseRef-Docenta-Proprietary
// Copyright (c) 2026 SKY, LLC.
// The theme switch shared by every page docenta writes: system by
// default, a choice stamped on the root and remembered per browser.
// Runs before paint so a remembered choice never flashes the other.
(function(){
  var KEY='docenta-theme',root=document.documentElement;
  function saved(){try{return localStorage.getItem(KEY)||'';}catch(e){return '';}}
  function apply(v){if(v==='light'||v==='dark'){root.setAttribute('data-theme',v);}else{root.removeAttribute('data-theme');}}
  apply(saved());
  document.addEventListener('DOMContentLoaded',function(){
    var b=document.getElementById('theme');if(!b)return;
    var order=['','light','dark'],names={'':'System','light':'Light','dark':'Dark'};
    function label(){var v=saved();b.setAttribute('aria-label','Theme: '+names[v]+'. Click to change');b.dataset.mode=v||'system';}
    label();
    b.addEventListener('click',function(){
      var v=saved(),next=order[(order.indexOf(v)+1)%order.length];
      try{if(next){localStorage.setItem(KEY,next);}else{localStorage.removeItem(KEY);}}catch(e){}
      apply(next);label();
    });
  });
})();
