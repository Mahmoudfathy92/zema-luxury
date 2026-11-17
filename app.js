'use strict';
let CATALOG = window.ZEMA_CATALOG || [];
let config = structuredClone(window.ZEMA_CONFIG);
let apiOnline = false, csrf = '', admin = null, adminTab = 'orders';
const readStore = (key, fallback) => { try { return JSON.parse(localStorage.getItem('zema.'+key)) ?? fallback; } catch { return fallback; } };
const writeStore = (key,value) => { try { localStorage.setItem('zema.'+key,JSON.stringify(value)); } catch { toast('Browser storage is unavailable. Keep your order reference.'); } };
const state = {lang:'en',currentView:'home',currentCategory:'all',selectedProductId:null,heroIdx:0,cart:readStore('cart',[]),wishlist:readStore('wishlist',[]),recent:readStore('recent',[]),variant:'default',sort:'featured',query:'',checkoutGov:'',orders:readStore('orders',[])};
const e = value => String(value ?? '').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const money = n => Number(n).toLocaleString('en-EG')+' EGP';
const byId = id => CATALOG.find(p=>p.id===id);
const variants = p => p.variants?.length ? p.variants : [{id:'default',color:p.color,hex:p.hex,image:p.image,detail:p.detail,stock:p.stock}];
const variantFor = (p,id='default') => variants(p).find(v=>v.id===id) || variants(p)[0];
const asset = file => { const s=String(file||''); if (/^https:\/\//i.test(s)) return s; if (/^[\w./-]+$/.test(s) && !s.includes('..')) return s.startsWith('media/') || s==='zema-logo.png' ? s : 'media/'+s; return 'media/studio-classic-shoulder.webp'; };
const mediaPath = asset;
const MEDIA_ASSETS = {'hero-01-ivory.webp':'media/hero-01-ivory.webp','hero-02-chocolate.webp':'media/hero-02-chocolate.webp'};
function toast(message) { const box=document.getElementById('toast');box.textContent=message;box.classList.add('show');clearTimeout(toast.timer);toast.timer=setTimeout(()=>box.classList.remove('show'),4500); }
function persist(){writeStore('cart',state.cart);writeStore('wishlist',state.wishlist);writeStore('recent',state.recent);const wb=document.getElementById('wishBadge');if(wb)wb.textContent=state.wishlist.length;}
function cleanCart(){state.cart=Array.isArray(state.cart)?state.cart.filter(x=>x&&typeof x==='object'&&byId(x.id)&&variants(byId(x.id)).some(v=>v.id===(x.variant||'default'))&&Number.isInteger(x.qty)&&x.qty>0).map(x=>({...x,variant:x.variant||'default',qty:Math.min(x.qty,variantFor(byId(x.id),x.variant).stock)})).filter(x=>x.qty>0):[];state.wishlist=Array.isArray(state.wishlist)?state.wishlist.filter(id=>byId(id)):[];state.recent=Array.isArray(state.recent)?state.recent.filter(id=>byId(id)).slice(0,8):[];persist();}
const subtotal = () => state.cart.reduce((s,x)=>s+byId(x.id).price*x.qty,0);
function quote(govId,amount=subtotal()){const g=config.governorates.find(g=>g.id===govId);if(!g||!g.enabled)return {fee:null,text:'Select your governorate',pending:true};if(config.freeShippingThreshold!==null&&amount>config.freeShippingThreshold)return {fee:0,text:'FREE',pending:false};return g.fee===null?{fee:null,text:'To be confirmed',pending:true}:{fee:g.fee,text:money(g.fee),pending:false};}
async function api(path,method='GET',data){const response=await fetch(path,{method,signal:AbortSignal.timeout(15000),headers:{'Content-Type':'application/json',...(csrf?{'X-CSRF-Token':csrf}:{})},...(data?{body:JSON.stringify(data)}:{})});const body=await response.json();if(!response.ok)throw new Error(body.error||'Unable to complete this action.');return body;}
function navigate(view,cat='all',prodId=null){let route=view==='shop'?'shop/'+(cat||'all'):view==='product'?'product/'+prodId:view; if(location.hash==='#'+route)routeView();else location.hash=route;}
function routeView(){if(location.hash==='#appView'){document.getElementById('appView').focus();return;}let route;try{route=decodeURIComponent(location.hash.slice(1));}catch{route='not-found';}const parts=route.split('/');state.currentView=parts[0]||'home';state.currentCategory=parts[1]||'all';if(state.currentView==='product'){state.selectedProductId=parts[1];state.variant='default';if(byId(parts[1])){state.recent=[parts[1],...state.recent.filter(x=>x!==parts[1])].slice(0,8);persist();}}toggleMenu(false);renderView();window.scrollTo({top:0,behavior:'instant'});}
let focusReturn=null;
function setModal(open,element){if(open){focusReturn=document.activeElement;element.removeAttribute('inert');element.setAttribute('aria-hidden','false');document.body.style.overflow='hidden';setTimeout(()=>element.querySelector('button,input,a')?.focus(),0);}else{element.setAttribute('aria-hidden','true');element.setAttribute('inert','');document.body.style.overflow='';focusReturn?.focus();}}
function toggleMenu(force){const menu=document.getElementById('mobileMenu');const open=typeof force==='boolean'?force:menu.hidden;menu.hidden=!open;document.querySelector('.menu-toggle').setAttribute('aria-expanded',String(open));}
function toggleCart(open){const el=document.getElementById('cartDrawer');document.body.classList.toggle('cart-open',open);el.classList.toggle('active',open);document.getElementById('cartBackdrop').classList.toggle('active',open);setModal(open,el);renderCart();}
function addToCart(id,variant=state.currentView==='product'?state.variant:'default',qty=1,open=true){const p=byId(id);if(!p)return false;const v=variantFor(p,variant);const item=state.cart.find(x=>x.id===id&&x.variant===v.id);if((item?.qty||0)+qty>v.stock){toast('Only '+v.stock+' available in '+v.color+'.');return false;}if(item)item.qty+=qty;else state.cart.push({id,variant:v.id,qty});persist();renderCart();if(open)toggleCart(true);return true;}
function updateCartQty(id,variant,delta){const item=state.cart.find(x=>x.id===id&&x.variant===variant);if(!item)return;if(item.qty+delta>variantFor(byId(id),variant).stock){toast('Available stock limit reached.');return;}item.qty+=delta;state.cart=state.cart.filter(x=>x.qty>0);persist();renderCart();if(state.currentView==='checkout')renderView();}
function addFullLook(){const ids=['classic-shoulder','zip-wallet','bag-charm'];if(!ids.every(id=>{const p=byId(id);return p&&variantFor(p).stock>(state.cart.find(x=>x.id===id&&x.variant===variantFor(p).id)?.qty||0);})){toast('One of these pieces is unavailable. Please choose pieces individually.');return;}ids.forEach(id=>addToCart(id,variants(byId(id))[0].id,1,false));toggleCart(true);}
function renderCart(){document.getElementById('cartBadge').textContent=state.cart.reduce((s,x)=>s+x.qty,0);document.getElementById('cartCountHeader').textContent=state.cart.reduce((s,x)=>s+x.qty,0);document.getElementById('cartSubtotalText').textContent=money(subtotal());document.getElementById('cartItemList').innerHTML=state.cart.length?state.cart.map(x=>{const p=byId(x.id),v=variantFor(p,x.variant);return `<div class="cart-item"><img src="${e(asset(v.image))}" alt="${e(p.name)}"><div><h4>${e(p.name)}</h4><p>${e(v.color)} · ${money(p.price)}</p><div class="qty"><button onclick="updateCartQty('${p.id}','${v.id}',-1)" aria-label="Decrease ${e(p.name)} quantity">−</button><span>${x.qty}</span><button onclick="updateCartQty('${p.id}','${v.id}',1)" aria-label="Increase ${e(p.name)} quantity">+</button></div></div><button aria-label="Remove ${e(p.name)}" onclick="updateCartQty('${p.id}','${v.id}',-999)">✕</button></div>`;}).join(''):'<div class="empty-state"><p>Your shopping bag is empty.</p><a href="#shop" class="btn" onclick="toggleCart(false)">Explore the Collection</a></div>';renderCartUpsell();document.getElementById('freeShippingNotice').textContent=config.freeShippingThreshold!==null?subtotal()>config.freeShippingThreshold?'Free shipping threshold reached.':`Free shipping on orders over ${money(config.freeShippingThreshold)}.`:'Shipping is confirmed before your order is finalized.';document.querySelector('.drawer-footer .btn').disabled=!state.cart.length;}
function renderCartUpsell(){const box=document.getElementById('cartUpsellSection');if(!box)return;if(!state.cart.length){box.innerHTML='';return;}const inCart=new Set(state.cart.map(x=>x.id));const candidates=CATALOG.filter(p=>!inCart.has(p.id)&&(p.cat==='accessories'||p.cat==='wallets')).slice(0,2);if(!candidates.length){box.innerHTML='';return;}box.innerHTML=`<div class="zm-cart-upsell"><span class="zm-upsell-title">COMPLETE THE LOOK</span><div class="zm-upsell-list">${candidates.map(u=>{const uv=variants(u)[0];return `<div class="zm-upsell-item"><img src="${e(asset(uv.image))}" alt="${e(u.name)}"><div class="zm-upsell-meta"><strong>${e(u.name)}</strong><span>${money(u.price)}</span></div><button type="button" class="zm-upsell-btn" onclick="addToCart('${u.id}','${uv.id}',1,false);renderCart();toast('${e(u.name)} added to your bag');" title="Add to bag">+ Add</button></div>`;}).join('')}</div></div>`;}
function toggleWishlist(id){state.wishlist=state.wishlist.includes(id)?state.wishlist.filter(x=>x!==id):[...state.wishlist,id];persist();renderView();}
function openSearchModal(){const modal=document.getElementById('searchModal');modal.style.display='flex';setModal(true,modal);document.getElementById('searchInput').focus();}
function closeSearchModal(){const modal=document.getElementById('searchModal');modal.style.display='none';setModal(false,modal);}
function runSearch(query){const q=query.trim().toLowerCase(),box=document.getElementById('searchResults');if(!q){box.innerHTML='';return;}const items=CATALOG.filter(p=>[p.name,p.name_ar,p.desc,...variants(p).map(v=>v.color)].join(' ').toLowerCase().includes(q));box.innerHTML=items.length?items.map(p=>`<a class="search-result" href="#product/${p.id}" onclick="closeSearchModal()"><img src="${e(asset(p.image))}" alt=""><span>${e(p.name)}<br>${money(p.price)}</span></a>`).join(''):`<p>No pieces matching “${e(query)}”.</p>`;}
function renderAboutView() {
  const isAr = state.lang === 'ar';
  if (isAr) {
    return `<div class="zm-story-page shell section-py">
      <nav class="zm-breadcrumb" aria-label="Breadcrumb"><a href="#home">الرئيسية</a><span>/</span>قصتنا</nav>
      <header class="zm-story-header">
        <span class="micro-label">دار زيما · ZEMA MAISON</span>
        <h1 class="zm-story-h1">ZEMA | فخامة التفاصيل، صُممت لترافقكِ كل يوم.</h1>
        <p class="zm-story-lead">علامة تجارية مصرية متخصصة في تصميم وتصنيع الشنط النسائية، المحافظ، وإكسسوارات الشنط، برؤية تجمع بين الذوق الرفيع والعملية اليومية.</p>
      </header>
      <div class="zm-story-hero-media">
        <img src="media/campaign-taupe-v2.webp" alt="حملة دار زيما" loading="lazy">
      </div>
      <div class="zm-story-grid">
        <article class="zm-story-card">
          <div class="zm-story-card-icon">🏛️</div>
          <h2>البداية والفكرة</h2>
          <p>بدأت رحلة ZEMA من شغف مشترك ورؤية واضحة بين شركاء يؤمنون بأن الأناقة الحقيقية لا تحتاج إلى تكلف، وأن المنتج المحلي قادر على المنافسة بأعلى معايير الجودة العالمية. ومن هنا، انطلقنا لنقدم علامة تجارية مصرية متخصصة في تصميم وتصنيع الشنط النسائية، المحافظ، وإكسسوارات الشنط، برؤية تجمع بين الذوق الرفيع والعملية اليومية.</p>
        </article>
        <article class="zm-story-card">
          <div class="zm-story-card-icon">✂️</div>
          <h2>فلسفتنا في التصميم</h2>
          <p>في ZEMA، نؤمن أن الشنطة ليست مجرد قطعة مكملة للمظهر، بل هي رفيقكِ اليومي الذي يحمل تفاصيل يومكِ. لذلك، نركز في كل تصميم على تحقيق التوازن المثالي بين الأناقة الكلاسيكية الهادئة (Minimalist Luxury) والتقسيم الداخلي الذكي الذي يلبي احتياجات المرأة العصرية، مع اختيار أجود الخامات والتشطيبات الدقيقة.</p>
        </article>
        <article class="zm-story-card">
          <div class="zm-story-card-icon">🎁</div>
          <h2>تجربة متكاملة</h2>
          <p>اهتمامنا لا يتوقف عند جودة المنتج فحسب، بل يمتد ليشمل رحلتكِ الكاملة معنا؛ بدايةً من اختيار القطعة وحتى لحظة فتح الصندوق (Unboxing)، لنضمن لكِ تجربة تليق بكِ وبأسلوب حياتكِ.</p>
        </article>
      </div>
      <div class="zm-story-cta">
        <a class="btn" href="#shop">تسوّقي المجموعة الآن ←</a>
      </div>
    </div>`;
  }
  return `<div class="zm-story-page shell section-py">
    <nav class="zm-breadcrumb" aria-label="Breadcrumb"><a href="#home">Home</a><span>/</span>Our Story</nav>
    <header class="zm-story-header">
      <span class="micro-label">MAISON ZEMA ATELIER</span>
      <h1 class="zm-story-h1">ZEMA | Crafted in the Details, Designed for Your Everyday.</h1>
      <p class="zm-story-lead">Specializing in women’s handbags, wallets, and bag charms, we set out to offer pieces that blend timeless elegance with accessible luxury.</p>
    </header>
    <div class="zm-story-hero-media">
      <img src="media/campaign-taupe-v2.webp" alt="ZEMA Campaign" loading="lazy">
    </div>
    <div class="zm-story-grid">
      <article class="zm-story-card">
        <div class="zm-story-card-icon">🏛️</div>
        <h2>Our Beginning</h2>
        <p>ZEMA was born out of a shared passion and a clear vision: to create a local Egyptian brand that rivals international standards in quality, design, and craftsmanship. Specializing in women’s handbags, wallets, and bag charms, we set out to offer pieces that blend timeless elegance with accessible luxury.</p>
      </article>
      <article class="zm-story-card">
        <div class="zm-story-card-icon">✂️</div>
        <h2>Design Philosophy</h2>
        <p>We believe a handbag is more than just an accessory—it is an everyday companion that carries your world. Every ZEMA piece is thoughtfully designed to balance quiet, minimalist luxury with practical, smart interior organization tailored for the modern woman, using carefully selected materials and refined finishes.</p>
      </article>
      <article class="zm-story-card">
        <div class="zm-story-card-icon">🎁</div>
        <h2>The ZEMA Experience</h2>
        <p>Our commitment goes beyond the product itself. From the moment you browse our collection to the unboxing experience at your doorstep, every detail is curated to deliver sophistication and lasting value.</p>
      </article>
    </div>
    <div class="zm-story-cta">
      <a class="btn" href="#shop">Explore the Collection →</a>
    </div>
  </div>`;
}

function recentlyViewed(exclude){const items=state.recent.filter(id=>id!==exclude).map(byId).filter(Boolean).slice(0,4);return items.length?`<section class="shell section-py"><div class="section-header"><h2 class="section-title">Recently Viewed</h2></div><div class="product-grid">${items.map(renderProductCard).join('')}</div></section>`:'';}
function renderShopView(){const cat=state.currentCategory;let items=CATALOG.filter(p=>cat==='all'||cat==='best-sellers'&&p.featured||cat==='new-arrivals'&&p.newArrival||cat==='sale'&&p.compare>p.price||p.cat===cat||bagStyle(p)===cat);const titles={all:'All Collections',bags:'All Bags',shoulder:'Shoulder Bags',handbag:'Handbags',crossbody:'Crossbody Bags',wallets:'Wallets',accessories:'Accessories','best-sellers':'Best Sellers','new-arrivals':'New Arrivals',sale:'Sale'};if(state.query)items=items.filter(p=>(p.name+' '+p.color+' '+p.desc).toLowerCase().includes(state.query.toLowerCase()));if(state.sort==='low')items.sort((a,b)=>a.price-b.price);if(state.sort==='high')items.sort((a,b)=>b.price-a.price);if(state.sort==='name')items.sort((a,b)=>a.name.localeCompare(b.name));return `<section class="shell section-py"><div class="collection-title"><span class="micro-label">ZEMA COLLECTION</span><h1>${titles[cat]||'Collection'}</h1><p>${items.length} considered pieces</p></div><div class="collection-tools"><nav aria-label="Collection categories">${Object.entries(titles).filter(([id])=>id!=='new-arrivals').map(([id,t])=>`<a class="filter ${cat===id?'selected':''}" href="#shop/${id}">${t}</a>`).join('')}</nav><label>Sort by <select onchange="state.sort=this.value;renderView()"><option value="featured" ${state.sort==='featured'?'selected':''}>Featured</option><option value="low" ${state.sort==='low'?'selected':''}>Price: low to high</option><option value="high" ${state.sort==='high'?'selected':''}>Price: high to low</option><option value="name" ${state.sort==='name'?'selected':''}>Name</option></select></label></div><div class="product-grid">${items.map(renderProductCard).join('')}</div>${!items.length?'<p class="empty-state">No pieces in this selection yet. <a href="#shop">View all collections</a>.</p>':''}</section>`;}
function selectVariant(id){state.variant=id;renderView();}
function galleryImage(url,index){const image=document.getElementById('mainProductImage');image.src=url;document.querySelectorAll('.gallery-thumb').forEach((b,i)=>{b.classList.toggle('selected',i===index);b.setAttribute('aria-pressed',String(i===index));});}
function openZoom(){const img=document.getElementById('mainProductImage'),modal=document.getElementById('zoomModal');document.getElementById('zoomImage').src=img.src;document.getElementById('zoomImage').alt=img.alt;document.getElementById('zoomImage').classList.remove('enlarged');modal.hidden=false;setModal(true,modal);}
function closeZoom(){const modal=document.getElementById('zoomModal');modal.hidden=true;setModal(false,modal);}
function emptyView(title,text){return `<section class="shell section-py empty-state"><h1>${e(title)}</h1><p>${e(text)}</p><a class="btn" href="#shop">Explore the Collection</a></section>`;}
function renderWishlistView(){const items=state.wishlist.map(byId).filter(Boolean);return `<section class="shell section-py"><h1>Your Wishlist</h1><p>${items.length} saved pieces</p>${items.length?`<div class="product-grid">${items.map(renderProductCard).join('')}</div>`:'<div class="empty-state">Save your favorite pieces with the heart icon. <a href="#shop">Explore the collection →</a></div>'}</section>`;}
function checkoutSummary(){const q=quote(state.checkoutGov);return `<h2>Order Summary</h2>${state.cart.map(x=>{const p=byId(x.id),v=variantFor(p,x.variant);return `<div class="summary-line"><img src="${e(asset(v.image))}" alt=""><span>${e(p.name)}<small>${e(v.color)} · Qty ${x.qty}</small></span><strong>${money(p.price*x.qty)}</strong></div>`;}).join('')}<div class="summary-total"><span>Items</span><span>${money(subtotal())}</span></div><div class="summary-total"><span>Shipping</span><span>${q.text}</span></div><div class="summary-total grand"><span>${q.pending?'Items total':'Total'}</span><span>${money(subtotal()+(q.fee||0))}</span></div>${q.pending?'<p class="shipping-disclosure">Shipping is not included yet. ZEMA will confirm the delivery charge and final total with you before your order is finalized or dispatched.</p>':''}`;}
function renderCheckoutView(){if(!state.cart.length)return emptyView('Your bag is empty','Choose your pieces before checking out.');const options=config.governorates.filter(g=>g.enabled);if(!options.some(g=>g.id===state.checkoutGov))state.checkoutGov='';return `<section class="shell section-py"><a href="#shop" class="back-link">← Continue Shopping</a><h1>Complete Your Order</h1><div class="checkout-layout"><form id="checkoutForm" onsubmit="event.preventDefault();submitOrder(this)"><div class="form-grid"><label>Full Name<input name="name" id="cName" required minlength="2" maxlength="100" autocomplete="name"></label><label>Mobile Phone<input name="phone" id="cPhone" type="tel" required pattern="(?:\\+?20|0)1[0125][0-9]{8}" title="Enter a valid Egyptian mobile number" placeholder="01xxxxxxxxx" autocomplete="tel"></label></div><label>Email address (optional)<input name="email" type="email" maxlength="254" autocomplete="email" dir="ltr"><small>For order receipts and delivery updates only.</small></label><label>Governorate<select name="governorate" id="cGov" required onchange="state.checkoutGov=this.value;document.getElementById('checkoutSummary').innerHTML=checkoutSummary()"><option value="">Select your governorate</option>${options.map(g=>`<option value="${g.id}" ${state.checkoutGov===g.id?'selected':''}>${e(g.name)} — ${g.fee===null?'Shipping to be confirmed':money(g.fee)}</option>`).join('')}</select></label><label>Detailed Address<textarea id="cAddress" name="address" required minlength="10" maxlength="500" rows="3" autocomplete="street-address" placeholder="Street, building, floor, apartment and landmark"></textarea></label><label>Order Notes (optional)<textarea name="notes" maxlength="500" rows="2"></textarea></label><div class="delivery-note"><strong>Cash on Delivery</strong><p>We will contact you to confirm availability, delivery and the final total before dispatch.</p></div><label class="consent"><input type="checkbox" required> <span>I agree to the <a href="#privacy" target="_blank">privacy information</a> and understand that unpriced shipping will be confirmed before my order is finalized.</span></label><p id="checkoutError" class="form-error" role="alert"></p><button class="btn" id="placeOrder" type="submit">${apiOnline?'Send Order Request':/^\d{10,15}$/.test(config.whatsapp)?'Prepare WhatsApp Order':'Save Order Draft'} →</button>${!apiOnline&&!/^\d{10,15}$/.test(config.whatsapp)?'<p class="shipping-disclosure">Online ordering is being prepared. You can save your order draft; direct sending becomes available when ZEMA adds its contact number.</p>':''}</form><aside id="checkoutSummary">${checkoutSummary()}</aside></div></section>`;}
let pendingOrderKey=null;
function requestId(){if(typeof crypto.randomUUID==='function')return crypto.randomUUID();return Array.from(crypto.getRandomValues(new Uint8Array(24)),b=>b.toString(16).padStart(2,'0')).join('');}
async function submitOrder(form){if(!form.reportValidity())return;const btn=document.getElementById('placeOrder');btn.disabled=true;const fields=Object.fromEntries(new FormData(form));fields.phone=fields.phone.replace(/\s/g,'');const payload={...fields,language:state.lang,items:structuredClone(state.cart),requestId:pendingOrderKey||(pendingOrderKey=requestId())};try{let order;if(apiOnline){order=await api('api/orders','POST',payload);for(const item of order.items){const p=byId(item.id);if(p){const v=variantFor(p,item.variant);v.stock=Math.max(0,v.stock-item.qty);}}pendingOrderKey=null;state.cart=[];persist();renderCart();}else{const q=quote(fields.governorate);order={id:'DRAFT-'+Date.now().toString(36).toUpperCase(),customer:fields.name,phone:fields.phone,address:fields.address,notes:fields.notes,governorate:config.governorates.find(g=>g.id===fields.governorate)?.name,items:state.cart.map(x=>({name:byId(x.id).name,color:variantFor(byId(x.id),x.variant).color,price:byId(x.id).price,qty:x.qty})),subtotal:subtotal(),shipping:q.fee,total:q.pending?null:subtotal()+q.fee,status:'Draft — not sent',createdAt:new Date().toISOString()};pendingOrderKey=null;}state.orders=[order,...state.orders.filter(o=>o.id!==order.id)].slice(0,30);writeStore('orders',state.orders.filter(o=>!o.customerId));location.hash='order/'+order.id;}catch(error){document.getElementById('checkoutError').textContent=error.message;btn.disabled=false;}}
function whatsappUrl(order){if(!/^\d{10,15}$/.test(config.whatsapp))return null;const message=`مرحبًا ZEMA، طلب ${order.id}\n${order.items.map(x=>`${x.name} — ${x.color} × ${x.qty}: ${money(x.price*x.qty)}`).join('\n')}\nقيمة المنتجات: ${money(order.subtotal)}\nالشحن: ${order.shipping===null?'يتم تأكيده قبل اعتماد الطلب':money(order.shipping)}\n${order.total===null?'الإجمالي النهائي بعد تأكيد الشحن':'الإجمالي: '+money(order.total)}\nالاسم: ${order.customer}\nالهاتف: ${order.phone}\nالعنوان: ${order.governorate} — ${order.address}\nملاحظات: ${order.notes||''}`;return 'https://wa.me/'+config.whatsapp+'?text='+encodeURIComponent(message);}
function renderReceipt(order){const url=whatsappUrl(order);return `<section class="shell section-py receipt"><span class="micro-label">${order.status.startsWith('Draft')?'ORDER DRAFT':'ORDER REQUEST RECEIVED'}</span><h1>${order.status.startsWith('Draft')?'Your order draft is ready':'Thank you for your request'}</h1><p>Reference: <strong>${e(order.id)}</strong></p><p>${order.status.startsWith('Draft')?(url?'This draft has not been sent. Send it through WhatsApp to request confirmation.':'This draft has not been sent. Direct sending becomes available once ZEMA adds its contact number.'):'Your request is saved. We will confirm availability, delivery costs and your final total before dispatch.'}</p><div class="receipt-status">${e(order.status)}</div><div class="receipt-details"><p>${e(order.customer)}<br>${e(order.phone)}<br>${e(order.governorate)} · ${e(order.address)}</p>${order.items.map(x=>`<div class="summary-total"><span>${e(x.name)} · ${e(x.color)} × ${x.qty}</span><span>${money(x.price*x.qty)}</span></div>`).join('')}<div class="summary-total"><strong>Items</strong><strong>${money(order.subtotal)}</strong></div><div class="summary-total"><span>Shipping</span><span>${order.shipping===null?'To be confirmed':money(order.shipping)}</span></div><div class="summary-total grand"><strong>${order.total===null?'Final total':'Total'}</strong><strong>${order.total===null?'Awaiting shipping confirmation':money(order.total)}</strong></div></div><div class="receipt-actions">${url?`<a href="${e(url)}" target="_blank" rel="noopener" class="btn">${order.status.startsWith('Draft')?'Send Order via WhatsApp':'Contact ZEMA via WhatsApp'} →</a>`:''}<button class="btn-outline" onclick="window.print()">Print / Save PDF</button><a href="#shop" class="btn-outline">Continue Shopping</a></div></section>`;}
function renderDeviceOrders(){return `<section class="shell section-py"><h1>Your Orders</h1><p>Orders and drafts saved in this browser. Keep your reference if you change devices or clear browser data.</p><div class="order-list">${state.orders.length?state.orders.map(o=>`<article><h2>${e(o.id)}</h2><p>${e(o.status)}</p><p>${new Date(o.createdAt).toLocaleDateString('en-GB')} · ${money(o.subtotal)}${o.shipping===null?' + shipping':''}</p><a class="btn-outline" href="#order/${e(o.id)}">View Order</a>${apiOnline&&o.token?` <button class="btn-outline" onclick="refreshOrder('${e(o.id)}')">Refresh Status</button>`:''}</article>`).join(''):'<div class="empty-state">No orders saved on this device yet. <a href="#shop">Explore the collection →</a></div>'}</div></section>`;}
async function refreshOrder(id){const o=state.orders.find(x=>x.id===id);try{const r=await fetch('api/orders/'+encodeURIComponent(id),{headers:{Authorization:'Bearer '+o.token}});const data=await r.json();if(!r.ok)throw new Error(data.error);Object.assign(o,data);writeStore('orders',state.orders);renderView();toast('Order status updated.');}catch(error){toast(error.message);}}
function renderPolicy(view){const texts={shipping:['Shipping & Delivery',`<p>We deliver across Egypt, subject to service coverage for your address.</p><p>${e(config.deliveryEstimate)}</p><p>When a delivery price is available, checkout calculates it for your governorate. Otherwise you will see “To be confirmed”. That does not mean free shipping. We confirm the charge and final total before your order is finalized or dispatched.</p>${config.freeShippingThreshold!==null?`<p>Free shipping is available for item totals over ${money(config.freeShippingThreshold)}.</p>`:''}<div class="shipping-rates">${config.governorates.filter(g=>g.enabled&&g.fee!==null).map(g=>`<div><span>${e(g.name)}</span><span>${g.fee===null?'To be confirmed':money(g.fee)}</span></div>`).join('')}</div>`],returns:['Returns & Exchanges',`<p>${e(config.returnsText)}</p><p>Please retain your order reference and the original packaging where possible. Contact us before sending an item back.</p>`],privacy:['Privacy',`<p>We use your name, phone number, delivery address and order details to process your order and arrange delivery. If you provide an email address, we also use it for order receipts and status updates through our email provider. Marketing emails require your separate optional signup.</p><p>Your bag, favorites, recently viewed pieces and order receipts are saved in this browser. Clearing browser storage removes these local copies. When you submit an order to our store server, it is also retained in the store database for fulfillment.</p><p>If you choose WhatsApp, your order details are shared with WhatsApp and the store when you send the message. Opening WhatsApp alone does not send your order.</p><p>You can request access to or deletion of your order data by contacting ZEMA with your order reference. This site does not collect payment-card details.</p><button class="btn-outline" onclick="clearLocalData()">Clear this browser's saved store data</button>`],faq:['Frequently Asked Questions',`<details open><summary>How do I place an order?</summary><p>Add your pieces to the bag and complete your delivery details. The confirmation screen clearly shows whether the request was received by our server or is an unsent WhatsApp draft.</p></details><details><summary>How much is shipping?</summary><p>Choose your governorate at checkout. If its price is pending, ZEMA confirms the charge before the order is finalized.</p></details><details><summary>How can I pay?</summary><p>Cash on delivery. Delivery details are confirmed before dispatch.</p></details><details><summary>Where is my order?</summary><p>Open Your Orders on the same browser used to order. Keep your reference for any inquiry.</p></details><details><summary>Are other colors available?</summary><p>Each product page lists its currently configured colors. Only colors with matching product images are offered.</p></details>`]};const t=texts[view];return `<section class="shell section-py policy"><span class="micro-label">CUSTOMER CARE</span><h1>${t[0]}</h1>${t[1]}</section>`;}
function clearLocalData(){if(!confirm('Clear your saved bag, wishlist, recently viewed items and order receipts from this browser? Orders already sent to the store are not deleted.'))return;['cart','wishlist','recent','orders'].forEach(k=>{try{localStorage.removeItem('zema.'+k);}catch{}});state.cart=[];state.wishlist=[];state.recent=[];state.orders=[];persist();renderCart();toast('Saved data cleared from this browser.');}
function renderAdminView(){if(!apiOnline)return `<section class="shell section-py policy"><h1>Store Management</h1><p>Management requires the included store server. GitHub Pages can display the storefront but cannot run the database or password-protected administration.</p><a href="#home" class="btn">Return to Store</a></section>`;if(!admin)return `<section class="shell section-py policy"><h1>Store Management</h1><form onsubmit="event.preventDefault();adminLogin(this)"><label>Admin Password<input type="password" name="password" required autocomplete="current-password" minlength="12"></label><p id="adminError" role="alert" class="form-error"></p><button class="btn">Sign In</button></form></section>`;return `<section class="shell section-py"><div class="admin-heading"><h1>Store Management</h1><button class="btn-outline" onclick="adminLogout()">Sign Out</button></div><nav class="admin-nav-tabs" aria-label="Management">${['orders','products','shipping','store'].map(t=>`<button class="admin-tab ${adminTab===t?'active':''}" onclick="adminTab='${t}';renderView()">${t}</button>`).join('')}</nav>${adminTab==='orders'?adminOrdersView():adminTab==='products'?adminProductsView():adminTab==='shipping'?adminShippingView():adminStoreView()}<p id="adminNotice" role="status"></p></section>`;}
async function adminLogin(form){try{const data=await api('api/admin/login','POST',{password:new FormData(form).get('password')});csrf=data.csrf;await loadAdmin();}catch(error){document.getElementById('adminError').textContent=error.message;}}
async function loadAdmin(){try{admin=await api('api/admin/data');csrf=admin.csrf;renderView();}catch{admin=null;csrf='';renderView();}}
async function adminLogout(){try{await api('api/admin/logout','POST',{});admin=null;csrf='';renderView();}catch(error){toast(error.message);}}
const statuses=['Awaiting confirmation','Confirmed','Processing','Shipped','Delivered','Cancelled'];
function adminOrdersView(){return `<h2>Orders (${admin.orders.length})</h2><p>Confirm shipping and stock with the customer before finalizing. Cancelling restores reserved stock.</p><div class="order-list">${admin.orders.map(o=>`<article><h3>${e(o.id)} · ${e(o.customer)}</h3><p>${e(o.phone)} · ${e(o.governorate)} · ${e(o.address)}</p><p>${e(o.notes)}</p><p>${o.items.map(x=>`${e(x.name)} / ${e(x.color)} × ${x.qty}`).join(' · ')}</p><form class="admin-order-form" onsubmit="event.preventDefault();saveAdminOrder('${o.id}',this)"><label>Shipping (EGP)<input name="shipping" type="number" min="0" max="10000" step="1" value="${o.shipping===null?'':o.shipping}" placeholder="Pending"></label><label>Status<select name="status">${statuses.map(s=>`<option ${o.status===s?'selected':''}>${s}</option>`).join('')}</select></label><p>Items: ${money(o.subtotal)} · Total: ${o.total===null?'Pending':money(o.total)}</p><button class="btn">Save Order</button></form></article>`).join('')||'<p>No orders yet.</p>'}</div>`;}
async function saveAdminOrder(id,form){const values=Object.fromEntries(new FormData(form));values.shipping=values.shipping===''?null:Number(values.shipping);try{await api('api/admin/orders/'+id,'PATCH',values);await loadAdmin();toast('Order saved.');}catch(error){toast(error.message);}}
function adminShippingView(){return `<h2>Shipping prices</h2><p>Leave a price blank until the shipping company confirms it. Enter 0 only for genuinely free delivery. Existing order quotes stay unchanged.</p><form onsubmit="event.preventDefault();saveShipping(this)"><label>Free shipping from item total (EGP, optional)<input name="freeShippingThreshold" type="number" min="0" max="1000000" value="${config.freeShippingThreshold??''}" placeholder="Disabled until set"></label><p><a href="shipping-template.csv" download>Download the shipping price template</a></p><label>Import prices from CSV<input type="file" accept=".csv,text/csv" onchange="importShippingCsv(this)"></label><div class="shipping-editor">${config.governorates.map(g=>`<label><span>${e(g.name)}</span><input name="fee_${g.id}" aria-label="Shipping price for ${e(g.name)}" type="number" min="0" max="10000" step="1" placeholder="To be confirmed" value="${g.fee??''}"><span><input name="enabled_${g.id}" type="checkbox" ${g.enabled?'checked':''}> Delivery available</span></label>`).join('')}</div><button class="btn">Save Shipping Prices</button></form>`;}
async function saveShipping(form){const data=new FormData(form);const next=structuredClone(config);next.freeShippingThreshold=data.get('freeShippingThreshold')===''?null:Number(data.get('freeShippingThreshold'));next.governorates=next.governorates.map(g=>({...g,fee:data.get('fee_'+g.id)===''?null:Number(data.get('fee_'+g.id)),enabled:data.has('enabled_'+g.id)}));await saveSettings(next);}
function adminStoreView(){return `<h2>Store settings</h2><form onsubmit="event.preventDefault();saveStoreSettings(this)"><label>WhatsApp number (country code, digits only)<input name="whatsapp" pattern="[0-9]{10,15}|" value="${e(config.whatsapp)}" placeholder="Enter the actual ZEMA number"></label><label>Delivery information<textarea name="deliveryEstimate" maxlength="500" required>${e(config.deliveryEstimate)}</textarea></label><label>Returns & exchanges information<textarea name="returnsText" rows="5" maxlength="3000" required>${e(config.returnsText)}</textarea></label><button class="btn">Save Store Settings</button></form><p class="shipping-disclosure">Server settings apply to this server. To update a separate static GitHub Pages deployment, export configuration below and replace store-config.js.</p><button class="btn-outline" onclick="downloadConfig()">Export Static Configuration</button>`;}
async function saveStoreSettings(form){const f=Object.fromEntries(new FormData(form));await saveSettings({...config,...f});}
async function saveSettings(next){try{const data=await api('api/admin/settings','PUT',next);config=data;await loadAdmin();renderCart();toast('Settings saved.');}catch(error){toast(error.message);}}
function downloadConfig(){const blob=new Blob(['window.ZEMA_CONFIG = '+JSON.stringify(config,null,2)+';\n'],{type:'text/javascript'});const url=URL.createObjectURL(blob),a=document.createElement('a');a.href=url;a.download='store-config.js';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
function adminProductsView(){return `<h2>Products & Inventory</h2><p>Add real colors with their matching images. Images can be an existing media filename or an HTTPS image URL.</p><button class="btn-outline" onclick="editProduct('')">Add Product</button><div class="table-container"><table><thead><tr><th>Product</th><th>Price</th><th>Stock</th><th>Action</th></tr></thead><tbody>${CATALOG.map(p=>`<tr><td>${e(p.name)}</td><td>${money(p.price)}</td><td>${variants(p).reduce((a,v)=>a+v.stock,0)}</td><td><button class="btn-outline" onclick="editProduct('${p.id}')">Edit</button></td></tr>`).join('')}</tbody></table></div><div id="productEditor"></div>`;}
function editProduct(id){const p=byId(id)||{id:'',name:'',cat:'bags',price:0,compare:null,desc:'',featured:false,newArrival:false,variants:[{id:'default',color:'',hex:'#b7a08a',image:'',detail:'',stock:0}]};document.getElementById('productEditor').innerHTML=`<form class="product-editor" onsubmit="event.preventDefault();saveProduct(this)"><h2>${id?'Edit':'Add'} Product</h2><div class="form-grid"><label>Product ID<input name="id" required pattern="[a-z0-9-]+" maxlength="80" value="${e(p.id)}" ${id?'readonly':''}></label><label>Product Name<input name="name" required maxlength="150" value="${e(p.name)}"></label><label>Category<select name="cat">${['bags','wallets','accessories'].map(c=>`<option ${c===p.cat?'selected':''}>${c}</option>`).join('')}</select></label><label>Price EGP<input name="price" type="number" min="1" max="1000000" step="1" required value="${p.price}"></label><label>Previous price (optional)<input name="compare" type="number" min="1" max="1000000" value="${p.compare??''}"></label></div><label>Description<textarea name="desc" required maxlength="2000">${e(p.desc)}</textarea></label><label class="consent"><input name="featured" type="checkbox" ${p.featured?'checked':''}> Best seller</label><label class="consent"><input name="newArrival" type="checkbox" ${p.newArrival?'checked':''}> New arrival</label><label>Colors, images and stock (JSON)<textarea name="variants" rows="12" required spellcheck="false">${e(JSON.stringify(variants(p),null,2))}</textarea></label><p>Each color needs a unique id, color, hex, image, detail and stock. Keep stock at 0 to mark a color sold out.</p><button class="btn">Save Product</button></form>`;document.getElementById('productEditor').scrollIntoView({behavior:'smooth'});}
async function saveProduct(form){try{const f=new FormData(form),v=JSON.parse(f.get('variants'));const p={id:f.get('id'),name:f.get('name'),name_ar:'',cat:f.get('cat'),price:Number(f.get('price')),compare:f.get('compare')===''?null:Number(f.get('compare')),desc:f.get('desc'),featured:f.has('featured'),newArrival:f.has('newArrival'),variants:v};await api('api/admin/products/'+p.id,'PUT',p);const data=await api('api/bootstrap');CATALOG=data.catalog;cleanCart();renderCart();await loadAdmin();toast('Product saved.');}catch(error){toast(error.message);}}
function renderView(){const view=state.currentView;let html;if(view==='home')html=renderHomeView()+recentlyViewed();else if(view==='shop')html=renderShopView();else if(view==='product')html=renderProductView();else if(view==='checkout')html=renderCheckoutView();else if(view==='about'||view==='story')html=renderAboutView();else if(view==='wishlist')html=renderWishlistView();else if(['account','login','register','forgot','reset'].includes(view))html=window.renderCustomerView?renderCustomerView(view):'';else if(view==='tracking')html=renderDeviceOrders();else if(view==='admin')html=renderAdminView();else if(['shipping','returns','privacy','faq','payment'].includes(view))html=renderPolicy(view);else if(view==='order'){const id=decodeURIComponent(location.hash).split('/')[1];const order=state.orders.find(x=>x.id===id);html=order?renderReceipt(order):emptyView('Order not found on this device','Use the browser where you created your order, or contact ZEMA with your reference.');}else html=emptyView('Page not found','Explore our current collection.');document.getElementById('appView').innerHTML=html;document.title=(view==='product'?byId(state.selectedProductId)?.name||'Product':({home:'Bags, Wallets & Accessories',shop:'Shop',checkout:'Checkout',about:'Our Story',story:'Our Story',admin:'Management',account:'My Account',login:'Sign In',register:'Create Account',forgot:'Reset Password',reset:'New Password',tracking:'Track an Order',wishlist:'Wishlist',order:'Order',shipping:'Shipping',returns:'Returns',privacy:'Privacy',faq:'FAQs'}[view]||'ZEMA'))+' | ZEMA Maison';document.querySelectorAll('.header-nav a,#mobileMenu a').forEach(a=>{a.removeAttribute('aria-current');if(a.hash==='#'+view||a.hash==='#'+view+'/'+state.currentCategory)a.setAttribute('aria-current','page');});document.querySelectorAll('.gallery-thumb').forEach(b=>b.addEventListener('click',()=>galleryImage(b.dataset.image,Number(b.dataset.index))));updateMetadata();setupPurchaseBar();window.setupBrandCampaign?.();document.querySelectorAll('.zm-details details').forEach(d=>d.addEventListener('toggle',()=>d.querySelector('summary span').textContent=d.open?'−':'+'));document.querySelectorAll('.category-card').forEach(el=>{el.tabIndex=0;el.setAttribute('role','link');el.onkeydown=event=>{if(event.key==='Enter'||event.key===' '){event.preventDefault();el.click();}};});}
document.addEventListener('keydown',event=>{if(event.key==='Escape'){if(!document.getElementById('zoomModal').hidden)closeZoom();else if(document.getElementById('searchModal').style.display==='flex')closeSearchModal();else if(document.getElementById('cartDrawer').classList.contains('active'))toggleCart(false);toggleMenu(false);}if(event.key==='Tab'){const modal=!document.getElementById('zoomModal').hidden?document.getElementById('zoomModal'):document.getElementById('searchModal').style.display==='flex'?document.getElementById('searchModal'):document.getElementById('cartDrawer').classList.contains('active')?document.getElementById('cartDrawer'):null;if(modal){const els=[...modal.querySelectorAll('button:not(:disabled),a,input,select,textarea,[tabindex="0"]')].filter(x=>x.getClientRects().length);const first=els[0],last=els.at(-1);if(event.shiftKey&&document.activeElement===first){event.preventDefault();last?.focus();}else if(!event.shiftKey&&document.activeElement===last){event.preventDefault();first?.focus();}}}});
const _ob=document.querySelector('[aria-label="Orders on this device"]');if(_ob)_ob.onclick=()=>navigate('account');
const _wb=document.querySelector('.header-actions [aria-label="Wishlist"]');if(_wb)_wb.onclick=()=>navigate('wishlist');
document.getElementById('zoomImage').ondblclick=event=>event.currentTarget.classList.toggle('enlarged');
document.getElementById('searchModal').addEventListener('click',event=>{if(event.target.id==='searchModal')closeSearchModal();});
window.addEventListener('hashchange',routeView);
function renderProductCard(p) {
  const v=variants(p)[0], saved=state.wishlist.includes(p.id);
  const isAr=state.lang==='ar';
  const isSoldOut=v.stock<=0;
  const qaLabel=isAr?'+ إضافة':'+ ADD';
  const soldBadge=isAr?'نفد من المخزون':'SOLD OUT';
  return `<article class="product-card zm-card ${isSoldOut?'zh-sold-out':''}">
    <div class="zm-card-image">
      ${isSoldOut?`<span class="zh-sold-badge">${soldBadge}</span>`:(p.compare>p.price?'<span class="zm-sale-tag">SALE</span>':'')}
      <a class="zm-open-product" href="#product/${p.id}" aria-label="View ${e(p.name)}"><img src="${e(asset(v.image))}" alt="${e(p.name)} — ${e(v.color)}" width="600" height="750" loading="lazy"></a>
      <button class="zm-card-heart" onclick="toggleWishlist('${p.id}')" aria-label="${saved?'Remove from':'Add to'} wishlist" aria-pressed="${saved}"><svg width="17" height="17" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M20.8 4.7a5.6 5.6 0 0 0-7.9 0L12 5.6l-.9-.9a5.6 5.6 0 0 0-7.9 7.9L12 21l8.8-8.4a5.6 5.6 0 0 0 0-7.9Z"/></svg></button>
      ${isSoldOut?'':`<button class="zh-quick-add-pill" type="button" onclick="event.stopPropagation();addToCart('${p.id}','${v.id}',1,true)" aria-label="${qaLabel}: ${e(p.name)}"><svg class="zh-qap-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path stroke-linecap="round" stroke-linejoin="round" d="M16 11V7a4 4 0 0 0-8 0v4M5 9h14l1 12H4L5 9Z"/></svg><span class="zh-qap-text">${qaLabel}</span></button>`}
    </div>
    <div class="zm-card-caption"><a href="#product/${p.id}">${e(p.name)}</a><span>${money(p.price)} ${p.compare>p.price?`<s>${money(p.compare)}</s>`:''}</span></div>
    <div class="zm-card-color"><span class="zm-swatch" style="background:${/^#[0-9a-f]{6}$/i.test(v.hex)?v.hex:'#b7a08a'}"></span>${e(v.color)}${variants(p).length>1?' · '+variants(p).length+' colors':''}</div>
  </article>`;
}
const HOME_SLIDES=[
  {full:true,img:'media/home/hero-main.webp',alt:'Woman in a dark blazer carrying a tan leather shoulder bag beside a sunlit stone wall',eyebrow:'TIMELESS DETAILS',title:'Bags for<br><em>Every Story</em>',text:'Modern designs, everyday elegance.',cta:'Shop Now',cat:'bags'},
  {img:'media/campaign-taupe-v2.webp',alt:'Warm taupe handbag worn with an ivory linen suit beside sunlit limestone architecture',eyebrow:'THE ZEMA CAMPAIGN',title:'A quiet statement.<br><em>Everywhere you go.</em>',text:'Distinctive pieces. Effortless style.',cta:'Discover the Collection',cat:'all'},
  {img:'media/campaign-chocolate-v2.webp',alt:'Chocolate shoulder bag carried by a seated model in a warm architectural interior',eyebrow:'THE EVERYDAY MUSE',title:'Elegance,<br><em>in your element.</em>',text:'Considered shapes. Distinctive details.',cta:'Shop the Collection',cat:'bags'}
];
const HOME_TILES=[
  {img:'media/home/cat-bags.webp',label:'Bags',sub:'Shop Collection',cat:'bags'},
  {img:'media/home/cat-wallets.webp',label:'Wallets',sub:'Shop Collection',cat:'wallets'},
  {img:'media/home/cat-charms.webp',label:'Charms',sub:'Shop Collection',cat:'accessories'}
];
/* Home rows: product ids from the catalog (New Arrivals / Best Sellers). */
const HOME_NEW=["noir-hobo", "sable-shoulder", "noir-bar-wallet", "bordeaux-top-handle", "sand-wallet"];
const HOME_BEST=["onyx-handbag", "cognac-saddle", "noir-quilted-wallet", "ivory-flap-handbag", "noir-card-wallet"];
function homeCard(id,variant){
  const p=byId(id);if(!p)return '';
  const v=variants(p)[0],saved=state.wishlist.includes(p.id);
  const isAr=state.lang==='ar';
  const isSoldOut=v.stock<=0;
  const qaLabel=isAr?'+ إضافة':'+ ADD';
  const soldBadge=isAr?'نفد من المخزون':'SOLD OUT';
  return `<article class="zh-card ${isSoldOut?'zh-sold-out':''}">
    <div class="zh-media">
      <a class="zh-card-img zh-card-img-${variant}" href="#product/${p.id}" aria-label="${e(p.name)} — ${money(p.price)}"><img src="${e(asset(v.image))}" alt="${e(p.name)} — ${e(v.color)}" width="525" height="${variant==='new'?507:405}" loading="lazy"></a>
      ${isSoldOut?`<span class="zh-sold-badge">${soldBadge}</span>`:''}
      <button type="button" class="zh-heart" onclick="toggleWishlist('${p.id}')" aria-pressed="${saved}" aria-label="${saved?'Remove from':'Add to'} wishlist"><svg width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M20.8 4.7a5.6 5.6 0 0 0-7.9 0L12 5.6l-.9-.9a5.6 5.6 0 0 0-7.9 7.9L12 21l8.8-8.4a5.6 5.6 0 0 0 0-7.9Z"/></svg></button>
      ${isSoldOut?'':`<button type="button" class="zh-quick-add-pill" onclick="event.stopPropagation();addToCart('${p.id}','${v.id}',1,true)" aria-label="${qaLabel}: ${e(p.name)}"><svg class="zh-qap-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path stroke-linecap="round" stroke-linejoin="round" d="M16 11V7a4 4 0 0 0-8 0v4M5 9h14l1 12H4L5 9Z"/></svg><span class="zh-qap-text">${qaLabel}</span></button>`}
    </div>
    <div class="zh-card-info"><a class="zh-name" href="#product/${p.id}">${e(p.name)}</a><span class="zh-price">${money(p.price)}${p.compare>p.price?` <s>${money(p.compare)}</s>`:''}</span><span class="zh-dots"><i style="background:${/^#[0-9a-f]{6}$/i.test(v.hex)?v.hex:'#b7a08a'}"></i><em>${e(v.color)}</em></span></div>
  </article>`;
}
function renderHomeMarquee(){
  const isAr=state.lang==='ar';
  const text=isAr
    ?'✦ دار زيما · ZEMA MAISON &nbsp;·&nbsp; فن التفاصيل والأناقة الخالدة &nbsp;·&nbsp; جلود طبيعية فاخرة بحرفية متقنة &nbsp;·&nbsp; سحر البساطة والفخامة الهادئة &nbsp;·&nbsp; تصاميم استثنائية لكل لحظة &nbsp;·&nbsp; رقيّ يدوم معكِ دائماً &nbsp;'
    :'✦ MAISON ZEMA &nbsp;·&nbsp; THE ART OF TIMELESS ELEGANCE &nbsp;·&nbsp; SCULPTED IN FINE LEATHER &nbsp;·&nbsp; ARCHITECTURAL SILHOUETTES &nbsp;·&nbsp; CRAFTED WITH QUIET LUXURY &nbsp;·&nbsp; BEAUTY IN EVERY SILHOUETTE &nbsp;';
  return `<div class="zm-ticker-wrap" aria-label="Maison ZEMA Highlights">
    <div class="zm-ticker">
      <div class="zm-ticker-item">${text}</div>
      <div class="zm-ticker-item">${text}</div>
    </div>
  </div>`;
}
function renderHomeView(){const free=config.freeShippingThreshold;const arrow='<span class="zh-arr" aria-hidden="true">→</span>';return `<div class="zh-home">
  <section class="zh-hero" aria-roledescription="carousel" aria-label="Featured collections">
    ${HOME_SLIDES.map((s,i)=>`<div class="zh-slide${s.full?' zh-slide-full':''}${i===0?' is-active':''}" role="group" aria-roledescription="slide" aria-label="${i+1} / ${HOME_SLIDES.length}"><img class="zh-slide-img" src="${s.img}" alt="${e(s.alt)}" ${i===0?'fetchpriority="high"':'loading="lazy"'}><div class="zh-slide-copy"><p class="zh-eyebrow">${s.eyebrow}</p><h1>${s.title}</h1><p class="zh-slide-text">${s.text}</p><a class="zh-btn" href="#shop/${s.cat}"><span>${s.cta}</span>${arrow}</a></div></div>`).join('')}
    <div class="zh-hero-ui"><div class="zh-indicators" role="group" aria-label="Choose slide">${HOME_SLIDES.map((s,i)=>`<button type="button" data-zh-go="${i}" class="${i===0?'is-active':''}" aria-label="Slide ${i+1}"><span>0${i+1}</span><i></i></button>`).join('')}</div><div class="zh-arrows"><button type="button" data-zh-prev aria-label="Previous slide">←</button><button type="button" data-zh-next aria-label="Next slide">→</button></div></div>
  </section>
  <section class="zh-tiles" aria-label="Shop by category">${HOME_TILES.map(t=>`<a class="zh-tile" href="#shop/${t.cat}"><img src="${t.img}" alt="" loading="lazy"><span class="zh-tile-copy"><strong>${t.label}</strong><small><span>${t.sub}</span>${arrow}</small></span></a>`).join('')}</section>
  ${renderHomeMarquee()}
  <section class="zh-section" id="zh-new"><div class="zh-head"><div><p class="zh-eyebrow">DISCOVER</p><h2>New Arrivals</h2></div><a class="zh-viewall" href="#shop/new-arrivals"><span>View All</span>${arrow}</a></div><div class="zh-grid">${HOME_NEW.map(id=>homeCard(id,'new')).join('')}</div></section>
  <section class="zh-banner" aria-label="A touch of everyday luxury"><img src="media/home/banner.webp" alt="Black leather handbag with a silk scarf and sunglasses on a marble café table" loading="lazy"><div class="zh-banner-copy"><p class="zh-eyebrow">MORE THAN A BAG</p><h2>A Touch<br><em>of Everyday Luxury</em></h2><p>Thoughtful details for a more beautiful you.</p><a class="zh-btn zh-btn-ghost" href="#shop/accessories"><span>Explore Now</span>${arrow}</a></div></section>
  <section class="zh-section" id="zh-best"><div class="zh-head"><div><p class="zh-eyebrow">CUSTOMER FAVORITES</p><h2>Best Sellers</h2></div><a class="zh-viewall" href="#shop/best-sellers"><span>View All</span>${arrow}</a></div><div class="zh-grid">${HOME_BEST.map(id=>homeCard(id,'best')).join('')}</div></section>
  <section class="zh-perks" aria-label="Store benefits">
    <div><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M3 8h17v14H3zM20 12h6l3 4v6h-9"/><circle cx="9" cy="23" r="2.4"/><circle cx="24" cy="23" r="2.4"/></svg><p><strong>Free Shipping</strong><span>${free!==null?`On orders over ${money(free)}`:'Delivery across Egypt'}</span></p></div>
    <div><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M16 3 28 9v14l-12 6L4 23V9zM4 9l12 6 12-6M16 15v14"/></svg><p><strong>Easy Returns</strong><span>Hassle-free within 14 days</span></p></div>
    <div><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.3"><rect x="3" y="8" width="26" height="16" rx="2"/><circle cx="16" cy="16" r="3.5"/><path d="M7 12v.1M25 20v.1"/></svg><p><strong>Cash on Delivery</strong><span>Pay when your order arrives</span></p></div>
  </section>
</div>`; }
function renderProductView() {
  const p=byId(state.selectedProductId);
  if(!p)return emptyView('Piece not found','Explore our current collection.');
  const v=variantFor(p,state.variant);state.variant=v.id;
  const images=[v.image,v.detail].filter((im,i,arr)=>im&&arr.indexOf(im)===i);
  const title=p.id==='classic-shoulder'?'The Classic<br>Shoulder Bag':e(p.name);
  return `<div class="zm-product-page">
    <nav class="zm-breadcrumb" aria-label="Breadcrumb"><a href="#home">Home</a><span>/</span><a href="#shop/${p.cat}">${e(p.cat.charAt(0).toUpperCase()+p.cat.slice(1))}</a><span>/</span>${e(p.name)}</nav>
    <div class="zm-pdp-layout"><div class="zm-gallery"><div class="zm-main-photo"><img id="mainProductImage" src="${e(asset(v.image))}" alt="${e(p.name)} — ${e(v.color)}"><button class="zm-enlarge" onclick="openZoom()" aria-label="Enlarge product image"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M8 3H3v5m13-5h5v5M3 16v5h5m13-5v5h-5"/></svg></button></div>
      <div class="zm-thumbnails">${images.map((im,i)=>`<button class="gallery-thumb zm-thumb ${i===0?'selected':''}" aria-label="View image ${i+1}" aria-pressed="${i===0}" data-image="${e(asset(im))}" data-index="${i}"><img src="${e(asset(im))}" alt="${e(p.name)} view ${i+1}"></button>`).join('')}</div></div>
      <div class="zm-pdp-info"><p class="zm-eyebrow">THE ZEMA COLLECTION</p><h1>${title}</h1><p class="zm-pdp-price">${money(p.price)} ${p.compare>p.price?`<s>${money(p.compare)}</s>`:''}</p><p class="zm-description">${e(p.desc)}</p>
        <div class="zm-color-choice"><span>COLOR — ${e(v.color.toUpperCase())}</span><div class="zm-color-buttons">${variants(p).map(x=>`<button aria-label="${e(x.color)}" aria-pressed="${x.id===v.id}" onclick="selectVariant('${x.id}')"><span class="zm-swatch" style="background:${/^#[0-9a-f]{6}$/i.test(x.hex)?x.hex:'#b7a08a'}"></span>${e(x.color)}</button>`).join('')}</div></div>
        ${v.stock<=0?`<p class="stock-note zm-sold-out-note">${state.lang==='ar'?'نفد من المخزون حالياً':'Currently sold out'}</p>`:''}
        <div class="zm-original-actions" id="originalPurchaseActions">
          <button class="zm-add-cart-pdp" ${v.stock>0?'':'disabled'} onclick="addToCart('${p.id}','${v.id}')">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path stroke-linecap="round" stroke-linejoin="round" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/></svg>
            <span>${v.stock>0 ? (state.lang==='ar'?'إضافة للسلة':'Add to Cart') : (state.lang==='ar'?'نفد من المخزون':'Sold Out')}</span>
          </button>
          <button class="zm-buy-now-pdp" ${v.stock>0?'':'disabled'} onclick="if(addToCart('${p.id}','${v.id}',1,false))navigate('checkout')">
            <span>${state.lang==='ar'?'شراء فوري':'Buy It Now'}</span>
          </button>
        </div>
        <div class="zm-delivery"><svg width="20" height="20" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 5h12v12H3zM15 9h3l3 4v4h-6"/><circle cx="7" cy="18" r="2"/><circle cx="18" cy="18" r="2"/></svg><span>Delivery across Egypt<br><small>Shipping confirmed before dispatch.</small></span></div>
        <div class="zm-details"><details><summary>Dimensions & Fit <span>+</span></summary><p>${p.dimensions?e(p.dimensions):'Contact ZEMA for exact measurements and fit before ordering.'}</p></details><details><summary>Materials & Details <span>+</span></summary><p>${e(p.materials||p.desc)}</p></details><details><summary>Care Guide <span>+</span></summary><p>${p.care?e(p.care):'Contact ZEMA for care advice specific to this piece.'}</p></details><details><summary>Delivery & Returns <span>+</span></summary><p>${e(config.deliveryEstimate)}</p><p>${e(config.returnsText)}</p><a href="#shipping">Shipping information ↗</a></details></div>
      </div></div>
    ${renderFrequentlyBought(p)}
    ${renderYouMayAlsoLike(p)}
    <aside id="mobilePurchaseBar" class="zm-mobile-purchase" aria-label="Quick purchase" hidden><div><span>${e(p.name)}</span><strong>${money(p.price)}</strong></div><button class="zm-primary" ${v.stock>0?'':'disabled'} onclick="addToCart('${p.id}','${v.id}')">${v.stock>0 ? (state.lang==='ar'?'إضافة للسلة':'Add to Bag') : (state.lang==='ar'?'نفد من المخزون':'Sold Out')} <span>+</span></button></aside>
  </div>${recentlyViewed(p.id)}`;
}

function renderFrequentlyBought(currentProduct) {
  if (!currentProduct) return '';
  let comp1 = null, comp2 = null;
  const colorStr = (currentProduct.color || '').toLowerCase();
  const isDark = colorStr.includes('black') || currentProduct.id.includes('noir') || currentProduct.id.includes('onyx');
  const isWarm = colorStr.includes('brown') || colorStr.includes('taupe') || colorStr.includes('cognac') || colorStr.includes('camel');

  if (currentProduct.cat === 'bags') {
    if (isDark) {
      comp1 = byId('noir-bar-wallet') || byId('noir-quilted-wallet') || CATALOG.find(x => x.cat === 'wallets');
    } else if (isWarm) {
      comp1 = byId('zip-wallet') || byId('sand-wallet') || CATALOG.find(x => x.cat === 'wallets');
    } else {
      comp1 = byId('sand-wallet') || byId('zip-wallet') || CATALOG.find(x => x.cat === 'wallets');
    }
    comp2 = byId('bag-charm') || CATALOG.find(x => x.cat === 'accessories');
  } else if (currentProduct.cat === 'wallets') {
    if (isDark) {
      comp1 = byId('noir-hobo') || byId('onyx-handbag') || CATALOG.find(x => x.cat === 'bags');
    } else if (isWarm) {
      comp1 = byId('cognac-saddle') || byId('classic-shoulder') || CATALOG.find(x => x.cat === 'bags');
    } else {
      comp1 = byId('classic-shoulder') || byId('ivory-flap-handbag') || CATALOG.find(x => x.cat === 'bags');
    }
    comp2 = byId('bag-charm') || CATALOG.find(x => x.cat === 'accessories');
  } else {
    comp1 = byId('classic-shoulder') || CATALOG.find(x => x.cat === 'bags');
    comp2 = byId('zip-wallet') || CATALOG.find(x => x.cat === 'wallets');
  }
  const items = [currentProduct, comp1, comp2].filter(Boolean);
  if (items.length < 2) return '';
  const totalPrice = items.reduce((sum, item) => sum + item.price, 0);
  const idsStr = items.map(x => x.id).join(',');

  return `<section class="zm-frequently-bought">
    <div class="zm-fb-head">
      <span class="zm-fb-eyebrow">CURATED COMBINATION</span>
      <h3>Pair It With</h3>
      <p>Complete the look with harmoniously matched pieces.</p>
    </div>
    <div class="zm-fb-grid">
      ${items.map((item, idx) => {
        const v = variants(item)[0];
        return `<div class="zm-fb-item">
          <div class="zm-fb-thumb"><img src="${e(asset(v.image))}" alt="${e(item.name)}"></div>
          <div class="zm-fb-details">
            <span class="zm-fb-tag">${idx === 0 ? 'This Item' : 'Matching Piece'}</span>
            <strong>${e(item.name)}</strong>
            <span class="zm-fb-price">${money(item.price)}</span>
          </div>
        </div>${idx < items.length - 1 ? '<span class="zm-fb-plus">+</span>' : ''}`;
      }).join('')}
    </div>
    <div class="zm-fb-action">
      <div class="zm-fb-total">
        <span>Bundle Total (${items.length} pieces):</span>
        <strong>${money(totalPrice)}</strong>
      </div>
      <button type="button" class="btn zm-fb-btn" onclick="addBundle('${idsStr}')">
        Add All ${items.length} to Bag →
      </button>
    </div>
  </section>`;
}

function renderYouMayAlsoLike(currentProduct) {
  if (!currentProduct) return '';
  let related = CATALOG.filter(x => x.id !== currentProduct.id && x.cat === currentProduct.cat);
  if (related.length < 4) {
    const extra = CATALOG.filter(x => x.id !== currentProduct.id && !related.some(r => r.id === x.id));
    related = [...related, ...extra];
  }
  related = related.slice(0, 4);
  if (!related.length) return '';
  return `<section class="shell section-py zm-pdp-related" style="margin-top: 36px; padding-top: 32px; border-top: 1px solid rgba(0,0,0,0.06);">
    <div class="section-header" style="text-align: left; margin-bottom: 22px;">
      <span class="micro-label" style="font-size: 10px; letter-spacing: 0.14em; color: #8c7a6b; font-weight: 700; text-transform: uppercase;">CURATED SELECTION</span>
      <h3 class="serif" style="font-size: 32px; font-weight: 400; margin: 4px 0 6px; color: #1a1714;">You May Also Like</h3>
      <p style="font-size: 13px; color: #766a5e; margin: 0;">Similar pieces to consider for your collection.</p>
    </div>
    <div class="product-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 20px;">
      ${related.map(renderProductCard).join('')}
    </div>
  </section>`;
}

function addBundle(idsStr) {
  const ids = String(idsStr).split(',').filter(Boolean);
  let count = 0;
  ids.forEach(id => {
    const p = byId(id);
    if (p) {
      const v = variants(p)[0];
      addToCart(id, v.id, 1, false);
      count++;
    }
  });
  renderCart();
  toggleCart(true);
  toast(count + ' curated pieces added to your shopping bag.');
}

let purchaseObserver=null;
function setupPurchaseBar(){
  purchaseObserver?.disconnect();document.body.classList.remove('has-purchase-bar');
  const bar=document.getElementById('mobilePurchaseBar'),actions=document.getElementById('originalPurchaseActions');
  if(!bar||!actions)return;
  bar.hidden=true;
  if(!matchMedia('(max-width:768px)').matches||!('IntersectionObserver' in window))return;
  purchaseObserver=new IntersectionObserver(entries=>{const entry=entries[0];const show=!entry.isIntersecting&&entry.boundingClientRect.bottom<0&&state.currentView==='product';bar.hidden=!show;document.body.classList.toggle('has-purchase-bar',show);},{threshold:0});
  purchaseObserver.observe(actions);
}
function syncResponsive(){document.body.classList.toggle('zm-phone',matchMedia('(max-width:768px)').matches);setupPurchaseBar();}

async function initialize(){if(!Array.isArray(state.orders))state.orders=[];state.orders=state.orders.filter(o=>o&&!o.customerId&&typeof o.id==='string'&&typeof o.status==='string'&&Array.isArray(o.items));cleanCart();renderCart();routeView();try{const response=await fetch('api/bootstrap',{signal:AbortSignal.timeout(4000)});if(!response.ok||!response.headers.get('content-type')?.includes('application/json'))return;const data=await response.json();if(!data.catalog||!data.config)return;CATALOG=data.catalog;config=data.config;apiOnline=true;cleanCart();renderCart();renderView();if(state.currentView==='admin')await loadAdmin();}catch{/* static hosting intentionally uses the bundled catalog and honest WhatsApp drafts */}}
syncResponsive();window.addEventListener('resize',syncResponsive);initialize();

function updateMetadata(){const p=state.currentView==='product'?byId(state.selectedProductId):null;document.querySelector('meta[name="description"]').content=p?p.desc:'Explore ZEMA handbags, wallets and accessories. Timeless style and modern everyday elegance.';document.querySelector('meta[property="og:title"]').content=document.title;document.querySelector('meta[property="og:description"]').content=document.querySelector('meta[name="description"]').content;let schema=document.getElementById('productSchema');if(!p){schema?.remove();return;}if(!schema){schema=document.createElement('script');schema.type='application/ld+json';schema.id='productSchema';document.head.append(schema);}schema.textContent=JSON.stringify({'@context':'https://schema.org','@type':'Product',name:p.name,description:p.desc,image:new URL(asset(p.image),location.href).href,sku:p.id,brand:{'@type':'Brand',name:'ZEMA'},offers:{'@type':'Offer',priceCurrency:'EGP',price:p.price,availability:variants(p).some(v=>v.stock>0)?'https://schema.org/InStock':'https://schema.org/OutOfStock',url:location.href}});}

async function importShippingCsv(input){const file=input.files[0];if(!file)return;try{const lines=(await file.text()).replace(/^\uFEFF/,'').trim().split(/\r?\n/);if(lines.shift().trim()!=='governorate_id,fee,enabled')throw new Error('Use the provided CSV template headers.');const seen=new Set();const changes=lines.filter(l=>l.trim()).map(line=>{const [id,fee,enabled,...extra]=line.split(',').map(s=>s.trim());if(extra.length||!config.governorates.some(g=>g.id===id)||seen.has(id)||fee!==''&&!/^\d{1,5}$/.test(fee)||Number(fee)>10000||!['true','false'].includes(enabled))throw new Error('Invalid or duplicate row: '+id);seen.add(id);return {id,fee,enabled};});const form=input.closest('form');for(const row of changes){form.elements['fee_'+row.id].value=row.fee;form.elements['enabled_'+row.id].checked=row.enabled==='true';}toast(changes.length+' governorates loaded. Review them, then Save Shipping Prices.');}catch(error){toast(error.message);}input.value='';}

function bagStyle(p){return p.bagStyle||({"classic-shoulder":"shoulder","chocolate-shoulder":"shoulder","top-handle":"handbag","mini-crossbody":"crossbody"}[p.id]||"");}
