/* ZEMA home: hero carousel + favorite hearts + Arabic strings */
(()=>{
window.ZEMA_HOME_AR={"The Noir Hobo Bag": "حقيبة هوبو نوار", "Black": "أسود", "The Sable Shoulder Bag": "حقيبة كتف سيبل", "Taupe": "توب", "The Noir Bar Wallet": "محفظة نوار بقطعة ذهبية", "The Bordeaux Top-Handle Bag": "حقيبة يد بوردو", "Burgundy": "عنابي", "The Sand Wallet": "محفظة ساند", "Beige": "بيج", "The Onyx Structured Handbag": "حقيبة يد أونيكس", "The Cognac Saddle Crossbody": "حقيبة كروس كونياك", "Cognac": "كونياك", "The Noir Quilted Wallet": "محفظة نوار مبطنة", "The Ivory Flap Handbag": "حقيبة يد ايفوري", "Cream": "كريمي", "The Noir Button Wallet": "محفظة نوار بزر ذهبي",'TIMELESS DETAILS':'تفاصيل خالدة','Bags for':'حقائب لكل','Every Story':'حكاية','A Touch':'لمسة','of Everyday Luxury':'من الفخامة اليومية','Modern designs, everyday elegance.':'تصاميم عصرية وأناقة لكل يوم.','Shop Now':'تسوّقي الآن','Discover the Collection':'اكتشفي المجموعة','Shop the Collection':'تسوّقي المجموعة','THE ZEMA CAMPAIGN':'حملة زيما','THE EVERYDAY MUSE':'إلهام كل يوم','Distinctive pieces. Effortless style.':'قطع مميزة. أناقة بلا عناء.','Considered shapes. Distinctive details.':'أشكال مدروسة. تفاصيل مميزة.','Search for bags, wallets, charms...':'ابحثي عن حقائب، محافظ، إكسسوارات…','Bags':'الحقائب','Wallets':'المحافظ','Charms':'الإكسسوارات','Box ZEMA':'بوكس زيما','Shop Collection':'تسوّقي المجموعة','Gift Ready':'جاهز للإهداء','DISCOVER':'اكتشفي','New Arrivals':'وصل حديثًا','View All':'عرض الكل','MORE THAN A BAG':'أكثر من مجرد حقيبة','Thoughtful details for a more beautiful you.':'تفاصيل مدروسة لإطلالة أجمل.','Explore Now':'اكتشفي الآن','CUSTOMER FAVORITES':'المفضلة لدى العميلات','Best Sellers':'الأكثر مبيعًا','Free Shipping':'شحن مجاني','Delivery across Egypt':'توصيل لكل أنحاء مصر','Easy Returns':'إرجاع سهل','Hassle-free within 14 days':'بدون تعقيد خلال ١٤ يومًا','Cash on Delivery':'الدفع عند الاستلام','Pay when your order arrives':'ادفعي عند وصول طلبكِ'};
let timer;
document.addEventListener('visibilitychange',()=>{if(document.hidden)clearTimeout(timer);else window.setupZemaHome?.();});
window.setupZemaHome=()=>{
  clearTimeout(timer);
  const hero=document.querySelector('.zh-hero');if(!hero)return;
  const slides=[...hero.querySelectorAll('.zh-slide')],dots=[...hero.querySelectorAll('[data-zh-go]')];
  const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  let i=Math.max(0,slides.findIndex(s=>s.classList.contains('is-active')));
  const show=n=>{i=(n+slides.length)%slides.length;slides.forEach((s,k)=>{const on=k===i;s.classList.toggle('is-active',on);s.setAttribute('aria-hidden',String(!on));s.querySelectorAll('a').forEach(a=>a.tabIndex=on?0:-1);});dots.forEach((d,k)=>{d.classList.toggle('is-active',k===i);d.setAttribute('aria-current',String(k===i));});};
  const schedule=()=>{clearTimeout(timer);if(!reduce&&!document.hidden)timer=setTimeout(()=>{show(i+1);schedule();},6500);};
  dots.forEach(d=>d.addEventListener('click',()=>{show(Number(d.dataset.zhGo));schedule();}));
  hero.querySelector('[data-zh-prev]').addEventListener('click',()=>{show(i-1);schedule();});
  hero.querySelector('[data-zh-next]').addEventListener('click',()=>{show(i+1);schedule();});
  hero.addEventListener('mouseenter',()=>clearTimeout(timer));hero.addEventListener('mouseleave',schedule);
  hero.addEventListener('focusin',()=>clearTimeout(timer));hero.addEventListener('focusout',schedule);
  let x0=null;hero.addEventListener('touchstart',e=>{x0=e.touches[0].clientX;},{passive:true});
  hero.addEventListener('touchend',e=>{if(x0===null)return;const dx=e.changedTouches[0].clientX-x0;x0=null;if(Math.abs(dx)>45){show(i+(dx<0?1:-1));schedule();}});
  show(i);schedule();
};
})();
