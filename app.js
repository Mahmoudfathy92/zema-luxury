'use strict';
// ZEMA Premium Luxury Storefront & Order Management System
const M = 'media/';
const PRODUCTS = ZEMA_CATALOG;

// Bilingual UI Dictionary
const DICT = {
  en: {
    topbarFreeShipping: 'Free shipping on orders over 2,500 EGP',
    topbarReturns: 'Easy 14-day exchange & returns',
    topbarLuxury: 'Premium handcrafted presentation',
    langToggle: 'العربية',
    searchPlaceholder: 'Search for bags, wallets, accessories...',
    noSearchResults: 'No matching products found.',
    navBags: 'Bags',
    navWallets: 'Wallets',
    navAccessories: 'Accessories',
    navBestSellers: 'Best Sellers',
    navNewArrivals: 'New Arrivals',
    navSale: 'Sale',
    shopBestSellers: 'Shop Best Sellers',
    exploreBags: 'Explore Bags',
    viewAll: 'View All →',
    bestSellersTitle: 'Best Sellers',
    newArrivalsTitle: 'New Arrivals',
    youMayAlsoLikeTitle: 'You May Also Like',
    completeTheLookTitle: 'Complete the Look',
    recentlyViewedTitle: 'Recently Viewed',
    clearAll: 'Clear All',
    ourStoryBadge: 'OUR STORY',
    ourStoryTitle: 'The Essence of ZEMA',
    ourStoryDesc: 'A thoughtfully curated collection of luxury bags, wallets, and accessories created for timeless everyday style.',
    ourStoryLink: 'Discover Our Story →',
    newsletterBadge: 'JOIN OUR CIRCLE',
    newsletterTitle: 'Be the First to Know',
    newsletterDesc: 'Subscribe for exclusive previews, new arrivals, and private collections.',
    newsletterPlaceholder: 'Enter your email address',
    newsletterBtn: 'Subscribe →',
    newsletterToast: 'Thank you for subscribing to ZEMA private circle.',
    footerBrandDesc: 'Timeless Style, Modern Luxury',
    footerBrandCol: 'Our Brand',
    footerCustomerCol: 'Customer Care',
    footerStory: 'Our Story',
    footerFaq: 'FAQ',
    footerShipping: 'Shipping & Returns',
    footerPrivacy: 'Privacy Policy',
    copyright: '© 2026 ZEMA Maison — All Rights Reserved · Egypt',
    shippingNoticeFoot: 'Cash on Delivery & Secure Courier Across Egypt',
    addToCart: 'Add to Bag',
    buyNow: 'Buy Now →',
    color: 'Color',
    quantity: 'Quantity',
    detailsHeading: 'Product Details',
    materialsHeading: 'Materials & Craftsmanship',
    shippingHeading: 'Shipping & Delivery',
    deliveryFast: 'Fast Delivery',
    deliveryNote: 'Within 2-4 business days',
    codBadge: 'Cash on Delivery',
    codNote: 'Pay upon parcel inspection',
    qualityBadge: 'Authentic Quality',
    qualityNote: 'Selected premium materials',
    pairBadge: 'THE ZEMA EDIT · CURATED PAIRINGS',
    pairTitle: 'Pair It With',
    pairDesc: 'Complement your bag with matching pieces. Choose your preferred colors, then add everything together.',
    pairIncluded: '✓ Main Selection',
    pairSelectionTitle: 'Your Curated Set',
    pairSelectionMeta: 'Piece(s) selected',
    pairAddBtn: 'Add Set to Bag',
    shoppingBagTitle: 'Shopping Bag',
    emptyBagTitle: 'Your shopping bag is empty',
    emptyBagDesc: 'Discover our collection and find pieces you love.',
    continueShopping: 'Continue Shopping',
    subtotal: 'Subtotal',
    shippingCalc: 'Calculated at checkout',
    reviewCheckout: 'Proceed to Checkout →',
    emptyWishlistTitle: 'Your Wishlist is Empty',
    emptyWishlistDesc: 'Save your favorite items by tapping the heart icon.',
    browseCollection: 'Browse Collection',
    checkoutTitle: 'Checkout',
    crumbsHome: 'Home',
    crumbsCheckout: 'Checkout',
    contactLegend: 'Contact Information',
    fullNameLabel: 'Full Name',
    fullNamePlaceholder: 'Enter your full name',
    phoneLabel: 'Mobile Phone Number',
    phonePlaceholder: '01xxxxxxxxx',
    deliveryLegend: 'Delivery Address in Egypt',
    governorateLabel: 'Governorate',
    selectGov: 'Select your governorate',
    areaLabel: 'Area / City / District',
    areaPlaceholder: 'e.g., New Cairo, Maadi, Dokki, Smouha...',
    addressLabel: 'Detailed Street Address',
    addressPlaceholder: 'Building number, street name, floor, apartment number...',
    notesLabel: 'Delivery Notes (Optional)',
    notesPlaceholder: 'Any landmark or special delivery instructions...',
    paymentLegend: 'Payment Method',
    codTitle: 'Cash on Delivery (COD)',
    codDescription: 'Pay in cash directly to the courier upon receiving and inspecting your order.',
    orderSummary: 'Order Summary',
    deliveryFeeLabel: 'Shipping',
    freeShippingText: 'FREE',
    finalTotalLabel: 'Total',
    confirmOrderBtn: 'Place Order (Cash on Delivery) →',
    orderSuccessBadge: 'ORDER CONFIRMED',
    orderSuccessTitle: 'Thank You for Your Order!',
    orderSuccessSubtitle: 'Your order has been received and is being prepared with care.',
    orderNumberLabel: 'Order Number',
    orderDateLabel: 'Date',
    orderCustomerLabel: 'Customer Name',
    orderPhoneLabel: 'Phone Number',
    orderAddressLabel: 'Delivery Address',
    orderPaymentMethodLabel: 'Payment Method',
    orderStatusCod: 'Cash on Delivery upon arrival',
    sendWhatsAppBtn: 'Confirm & Send Order via WhatsApp',
    printInvoiceBtn: 'Print Invoice',
    filterColor: 'Color',
    allColors: 'All Colors',
    filterPrice: 'Price',
    anyPrice: 'Any Price',
    sortBy: 'Sort',
    sortFeatured: 'Featured',
    sortLow: 'Price: Low to High',
    sortHigh: 'Price: High to Low',
    sortName: 'Name: A–Z',
    itemsCount: 'items'
  },
  ar: {
    topbarFreeShipping: 'شحن مجاني للطلبات بقيمة 2,500 ج.م وأكثر',
    topbarReturns: 'إمكانية الاستبدال والاسترجاع خلال 14 يوماً',
    topbarLuxury: 'تغليف راقٍ وتصميم عصري فاخر',
    langToggle: 'English',
    searchPlaceholder: 'ابحثِ عن الحقائب، المحافظ، الإكسسوارات...',
    noSearchResults: 'لم يتم العثور على منتجات مطابقة.',
    navBags: 'الحقائب',
    navWallets: 'المحافظ',
    navAccessories: 'الإكسسوارات',
    navBestSellers: 'الأكثر مبيعاً',
    navNewArrivals: 'وصل حديثاً',
    navSale: 'التخفيضات',
    shopBestSellers: 'تسوق الأكثر مبيعاً',
    exploreBags: 'استكشف الحقائب',
    viewAll: 'عرض الكل ←',
    bestSellersTitle: 'الأكثر مبيعاً',
    newArrivalsTitle: 'وصل حديثاً',
    youMayAlsoLikeTitle: 'قد يعجبك أيضاً',
    completeTheLookTitle: 'أكملي إطلالتك',
    recentlyViewedTitle: 'شوهدت مؤخراً',
    clearAll: 'مسح الكل',
    ourStoryBadge: 'قصة زيما',
    ourStoryTitle: 'جوهر وأناقة ZEMA',
    ourStoryDesc: 'مجموعة مختارة بعناية من الحقائب والمحافظ والإكسسوارات الفاخرة، صُممت لترافق يومك بأناقة لا تتأثر بمرور الزمن.',
    ourStoryLink: 'اكتشفي قصتنا بالتفصيل ←',
    newsletterBadge: 'انضمي لعالم زيما',
    newsletterTitle: 'كوني أول من يعلم',
    newsletterDesc: 'اشتركي لمعرفة أحدث المجموعات والعروض والقطع الحصرية فور وصولها.',
    newsletterPlaceholder: 'أدخلي بريدك الإلكتروني',
    newsletterBtn: 'اشتراك ←',
    newsletterToast: 'شكراً لانضمامك إلى مجتمع زيما الراقي.',
    footerBrandDesc: 'أناقة خالدة، وفخامة عصرية تناسب كل يوم',
    footerBrandCol: 'عن العلامة',
    footerCustomerCol: 'خدمة العملاء',
    footerStory: 'قصتنا',
    footerFaq: 'الأسئلة الشائعة',
    footerShipping: 'الشحن والاسترجاع',
    footerPrivacy: 'سياسة الخصوصية',
    copyright: '© 2026 ZEMA Maison — جميع الحقوق محفوظة · جمهورية مصر العربية',
    shippingNoticeFoot: 'الدفع عند الاستلام وشحن سريع لجميع محافظات مصر',
    addToCart: 'أضف إلى السلة',
    buyNow: 'شراء الآن ←',
    color: 'اللون',
    quantity: 'الكمية',
    detailsHeading: 'تفاصيل المنتج',
    materialsHeading: 'الخامات والصناعة',
    shippingHeading: 'الشحن والتوصيل',
    deliveryFast: 'توصيل سريع',
    deliveryNote: 'خلال 2-4 أيام عمل لعنوانك',
    codBadge: 'الدفع عند الاستلام',
    codNote: 'ادفعي نقداً عند استلام ومعاينة الطلب',
    qualityBadge: 'جودة استثنائية',
    qualityNote: 'خامات ومصنعية ممتازة ومختارة',
    pairBadge: 'تنسيقات زيما الحصرية · THE ZEMA EDIT',
    pairTitle: 'نسّقي معها (Pair It With)',
    pairDesc: 'أكملي أناقة حقيبتك بالقطع المتناسقة معها. اختاري ألوانك المفضلة وأضيفيها معاً بضغطة زر واحدة.',
    pairIncluded: '✓ القطعة الأساسية',
    pairSelectionTitle: 'مجموعتك المنسقة',
    pairSelectionMeta: 'قطع مختارة مع الحقيبة',
    pairAddBtn: 'إضافة المجموعة كاملة للسلة',
    shoppingBagTitle: 'سلة المشتريات',
    emptyBagTitle: 'سلة المشتريات فارغة',
    emptyBagDesc: 'استكشفي تشكيلتنا الفاخرة واختاري ما يناسب ذوقك.',
    continueShopping: 'متابعة التسوق',
    subtotal: 'المجموع الفرعي',
    shippingCalc: 'يُحسب عند إتمام الطلب',
    reviewCheckout: 'متابعة إتمام الطلب ←',
    emptyWishlistTitle: 'قائمة الرغبات فارغة',
    emptyWishlistDesc: 'يمكنك حفظ منتجاتك المفضلة بالضغط على علامة القلب.',
    browseCollection: 'تصفح المجموعة',
    checkoutTitle: 'إتمام الطلب',
    crumbsHome: 'الرئيسية',
    crumbsCheckout: 'إتمام الطلب',
    contactLegend: 'بيانات التواصل',
    fullNameLabel: 'الاسم بالكامل',
    fullNamePlaceholder: 'اكتبي اسمك بالكامل',
    phoneLabel: 'رقم الهاتف المحمول',
    phonePlaceholder: '01xxxxxxxxx',
    deliveryLegend: 'عنوان التوصيل في مصر',
    governorateLabel: 'المحافظة',
    selectGov: 'اختر المحافظة للتوصيل',
    areaLabel: 'المدينة / المنطقة / الحي',
    areaPlaceholder: 'مثال: التجمع الخامس، المعادي، الدقي، سموحة...',
    addressLabel: 'العنوان بالتفصيل',
    addressPlaceholder: 'اسم الشارع، رقم العمارة، رقم الشقة أو علامة مميزة...',
    notesLabel: 'ملاحظات إضافية للتوصيل (اختياري)',
    notesPlaceholder: 'أي تفاصيل تود إضافتها لمندوب الشحن...',
    paymentLegend: 'طريقة الدفع',
    codTitle: 'الدفع نقدًا عند الاستلام (Cash on Delivery)',
    codDescription: 'ادفعي نقدًا عند وصول مندوب التوصيل ومعاينة الطرد لراحة وأمان تام.',
    orderSummary: 'ملخص الطلب',
    deliveryFeeLabel: 'الشحن والتوصيل',
    freeShippingText: 'مجاناً',
    finalTotalLabel: 'الإجمالي النهائي',
    confirmOrderBtn: 'تأكيد الطلب (الدفع عند الاستلام) ←',
    orderSuccessBadge: 'تم تأكيد الطلب بنجاح',
    orderSuccessTitle: 'شكراً لثقتك واختيارك لـ ZEMA!',
    orderSuccessSubtitle: 'تم تسجيل طلبك وسيقوم فريقنا بتجهيزه وشحنه لعنوانك في أسرع وقت.',
    orderNumberLabel: 'رقم الطلب',
    orderDateLabel: 'تاريخ الطلب',
    orderCustomerLabel: 'اسم العميل',
    orderPhoneLabel: 'رقم الهاتف',
    orderAddressLabel: 'عنوان التوصيل',
    orderPaymentMethodLabel: 'طريقة الدفع',
    orderStatusCod: 'الدفع نقداً عند استلام ومعاينة الطلب',
    sendWhatsAppBtn: 'تأكيد وإرسال تفاصيل الطلب عبر واتساب',
    printInvoiceBtn: 'طباعة الفاتورة',
    filterColor: 'اللون',
    allColors: 'كل الألوان',
    filterPrice: 'السعر',
    anyPrice: 'أي سعر',
    sortBy: 'الترتيب',
    sortFeatured: 'المميز أولاً',
    sortLow: 'السعر: من الأقل للأعلى',
    sortHigh: 'السعر: من الأعلى للأقل',
    sortName: 'الاسم: أ–ي',
    itemsCount: 'منتج'
  }
};

const HERO_SLIDES = [
  {
    tagEn: 'TIMELESS STYLE',
    tagAr: 'أناقة خالدة',
    titleEn: 'Modern<br><em>Luxury</em>',
    titleAr: 'فخامة<br><em>عصرية</em>',
    descEn: 'Refined bags and accessories curated for everyday moments and beyond.',
    descAr: 'حقائب وإكسسوارات راقية صُممت لترافق تفاصيل يومك وأجمل لحظاتك.',
    btnEn: 'Shop Best Sellers',
    btnAr: 'تسوق الأكثر مبيعاً',
    category: 'best-sellers',
    image: 'hero-01-ivory.webp',
    mobile: 'hero-01-ivory-mobile.webp'
  },
  {
    tagEn: 'THE EVERYDAY EDIT',
    tagAr: 'مجموعة كل يوم',
    titleEn: 'Quiet<br><em>Elegance</em>',
    titleAr: 'أناقة هادئة<br><em>تشبهك</em>',
    descEn: 'Beautifully considered leather pieces for effortless everyday grace.',
    descAr: 'تصميمات متوازنة بلمسات جلدية فاخرة تعكس أسلوبك الراقي ببساطة.',
    btnEn: 'Explore Bags',
    btnAr: 'استكشف الحقائب',
    category: 'bags',
    image: 'hero-02-chocolate.webp',
    mobile: 'hero-02-chocolate-mobile.webp'
  }
];

function stored(k, def) {
  try {
    const v = localStorage.getItem(k);
    return v ? JSON.parse(v) : def;
  } catch {
    return def;
  }
}

function persist(k, v) {
  try {
    localStorage.setItem(k, JSON.stringify(v));
  } catch {}
}

const state = {
  lang: stored('zema_lang', 'ar'), // default Arabic for local market
  cart: stored('zema_sample_cart', []).filter(x => PRODUCTS.some(p => p.id === x.id)),
  wish: stored('zema_sample_wish', []),
  recent: stored('zema_sample_recent', []),
  drawer: '',
  zoom: null,
  search: false,
  searchQuery: '',
  hero: 0,
  qty: 1,
  chosenColor: null,
  activePhoto: 0,
  sort: 'featured',
  filterColor: 'all',
  filterMax: 'all',
  selectedGov: '',
  lastOrder: stored('zema_last_order', null),
  pairSelected: {},
  pairColors: {}
};

const root = document.getElementById('app');

function t(key) {
  const dict = DICT[state.lang] || DICT.en;
  return dict[key] || DICT.en[key] || key;
}

const byId = id => PRODUCTS.find(p => p.id === id);

function getGov(idOrEn) {
  return EGYPT_GOVERNORATES.find(g => g.id === idOrEn || g.en === idOrEn || g.ar === idOrEn);
}

function currency(n) {
  const num = Number(n).toLocaleString(state.lang === 'ar' ? 'ar-EG' : 'en-US');
  const sym = state.lang === 'ar' ? STORE_CONFIG.currencyAr : STORE_CONFIG.currencyEn;
  return `${num} ${sym}`;
}

const media = f => M + f;

const safe = s => String(s ?? '')
  .replaceAll('&', '&amp;')
  .replaceAll('<', '&lt;')
  .replaceAll('>', '&gt;')
  .replaceAll('"', '&quot;')
  .replaceAll("'", '&#39;');

const icons = {
  search: '<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/>',
  user: '<circle cx="12" cy="8" r="3.5"/><path d="M4 21v-2a8 8 0 0 1 16 0v2"/>',
  heart: '<path d="M20.8 4.7a5.6 5.6 0 0 0-7.9 0L12 5.6l-.9-.9a5.6 5.6 0 0 0-7.9 7.9L12 21l8.8-8.4a5.6 5.6 0 0 0 0-7.9Z"/>',
  bag: '<path d="M5 8h14l1 13H4L5 8Z"/><path d="M9 9V6a3 3 0 1 1 6 0v3"/>',
  menu: '<path d="M3 6h18M3 12h18M3 18h18"/>',
  close: '<path d="M5 5l14 14M19 5 5 19"/>',
  trash: '<path d="M4 7h16M10 4h4m4 3-1 14H7L6 7M10 11v6M14 11v6"/>',
  truck: '<path d="M1 5h12v11H1zM13 9h5l4 4v3h-9z"/><circle cx="6" cy="18" r="2"/><circle cx="18" cy="18" r="2"/>',
  shield: '<path d="m12 2 9 4v6c0 6-4.5 8.5-9 10-4.5-1.5-9-4-9-10V6l9-4Z"/><path d="m8 12 3 3 5-6"/>',
  box: '<path d="m12 2 9 5v10l-9 5-9-5V7l9-5Z"/><path d="m3 7 9 5 9-5M12 12v10"/>',
  check: '<path d="M20 6 9 17l-5-5"/>',
  zoom: '<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4M8 11h6M11 8v6"/>',
  arrow: '<path d="M4 12h16m-6-6 6 6-6 6"/>',
  whatsapp: '<path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/>',
  print: '<polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/>'
};

const ico = name => `<svg width="19" height="19" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round">${icons[name]||''}</svg>`;

const params = () => new URLSearchParams(location.protocol === 'file:' && location.hash.startsWith('#?') ? location.hash.slice(2) : location.search);
const currentView = () => params().get('view') || 'home';
const currentProduct = () => params().get('product');
const collection = () => params().get('collection');
const linkProduct = p => `?product=${encodeURIComponent(p.id)}`;
const linkCollection = c => `?collection=${encodeURIComponent(c)}`;

function goto(url) {
  if (location.protocol === 'file:') {
    location.hash = '#' + url;
  } else {
    history.pushState({}, '', url);
  }
  state.drawer = '';
  state.search = false;
  state.qty = 1;
  state.activePhoto = 0;
  state.chosenColor = null;
  render();
  window.scrollTo(0, 0);
}

function toast(msg) {
  const n = document.getElementById('announcement');
  n.textContent = msg;
  n.classList.add('show');
  clearTimeout(window.toastTimer);
  window.toastTimer = setTimeout(() => n.classList.remove('show'), 3000);
}

function getProdName(p) {
  return state.lang === 'ar' ? (p.name_ar || p.name) : p.name;
}

function getProdDesc(p) {
  return state.lang === 'ar' ? (p.description_ar || p.description) : p.description;
}

function getProdMaterials(p) {
  return state.lang === 'ar' ? (p.materials_ar || p.materials) : p.materials;
}

function getProdColor(p, colName) {
  const c = p.colors.find(x => x[0] === colName) || p.colors[0];
  if (state.lang === 'ar' && c[3]) return c[3];
  return c[0];
}

function setDocumentLang() {
  document.documentElement.lang = state.lang;
  document.documentElement.dir = state.lang === 'ar' ? 'rtl' : 'ltr';
  document.body.dir = state.lang === 'ar' ? 'rtl' : 'ltr';
}

function toggleLanguage() {
  state.lang = state.lang === 'ar' ? 'en' : 'ar';
  persist('zema_lang', state.lang);
  setDocumentLang();
  render();
}

function header() {
  return `<div class="topbar">
    <span>${ico('truck')} ${t('topbarFreeShipping')}</span>
    <span>${ico('box')} ${t('topbarReturns')}</span>
    <span>${ico('heart')} ${t('topbarLuxury')}</span>
  </div>
  <header class="site-header">
    <div class="shell header-main">
      <div class="header-left">
        <button class="icon-btn mobile-only" data-act="menu" aria-label="Open menu">${ico('menu')}</button>
        <button class="lang-pill" data-act="toggle-lang" aria-label="Switch Language">${t('langToggle')}</button>
        <div class="site-search desktop-only">
          <span>${ico('search')}</span>
          <input type="search" id="desktop-search" placeholder="${t('searchPlaceholder')}" aria-label="Search products" value="${safe(state.searchQuery)}" />
        </div>
      </div>
      <a href="?" data-nav="?" class="brand" aria-label="ZEMA homepage"><img src="zema-logo.png" alt="ZEMA" /></a>
      <div class="header-right">
        <button class="icon-btn mobile-only" data-act="search" aria-label="Search">${ico('search')}</button>
        <button class="icon-btn desktop-only" data-nav="?view=wishlist" aria-label="Wishlist">${ico('heart')}</button>
        <button class="icon-btn cart-btn" data-act="cart" aria-label="Open shopping bag">
          ${ico('bag')}
          ${cartCount() ? `<span class="bag-count">${cartCount()}</span>` : ''}
        </button>
      </div>
    </div>
    <nav class="header-nav" aria-label="Main navigation">
      <a href="${linkCollection('bags')}" data-nav="${linkCollection('bags')}">${t('navBags')}</a>
      <a href="${linkCollection('wallets')}" data-nav="${linkCollection('wallets')}">${t('navWallets')}</a>
      <a href="${linkCollection('accessories')}" data-nav="${linkCollection('accessories')}">${t('navAccessories')}</a>
      <a href="${linkCollection('best-sellers')}" data-nav="${linkCollection('best-sellers')}">${t('navBestSellers')}</a>
      <a href="${linkCollection('new-arrivals')}" data-nav="${linkCollection('new-arrivals')}">${t('navNewArrivals')}</a>
      <a class="sale-link" href="${linkCollection('sale')}" data-nav="${linkCollection('sale')}">${t('navSale')}</a>
    </nav>
    ${state.search ? `<div class="search-panel"><div class="shell"><input id="mobile-search-input" style="width:100%;padding:12px;border:1px solid #ddd3c8;margin-bottom:14px;border-radius:3px" placeholder="${t('searchPlaceholder')}" aria-label="Search products" value="${safe(state.searchQuery)}"><div id="search-results" class="search-results">${searchMatches()}</div></div></div>` : ''}
  </header>`;
}

function searchMatches() {
  const q = state.searchQuery.toLowerCase().trim();
  const list = q 
    ? PRODUCTS.filter(p => p.name.toLowerCase().includes(q) || (p.name_ar && p.name_ar.includes(q)))
    : PRODUCTS.slice(0, 5);
  return list.slice(0, 8).map(p => `
    <a href="${linkProduct(p)}" data-nav="${linkProduct(p)}" class="search-result">
      <img src="${media(p.image)}" alt="">
      <div>
        <strong>${safe(getProdName(p))}</strong>
        <small>${currency(p.price)}</small>
      </div>
    </a>
  `).join('') || `<p style="padding:15px;color:#7a6d63">${t('noSearchResults')}</p>`;
}

function footer() {
  return `<section class="newsletter">
    <div class="shell newsletter-inner">
      <div>
        <span class="micro">${t('newsletterBadge')}</span>
        <h2>${t('newsletterTitle')}</h2>
        <p>${t('newsletterDesc')}</p>
      </div>
      <form class="subscribe" id="newsletter-form">
        <input required type="email" aria-label="Email address" placeholder="${t('newsletterPlaceholder')}">
        <button type="submit">${t('newsletterBtn')}</button>
      </form>
    </div>
  </section>
  <footer class="site-footer">
    <div class="shell">
      <div class="footer-inner">
        <div class="footer-brand">
          <a href="?" data-nav="?" aria-label="ZEMA homepage"><img src="zema-logo.png" alt="ZEMA" /></a>
          <p>${t('footerBrandDesc')}</p>
        </div>
        <div class="footer-group">
          <h3>${t('footerBrandCol')}</h3>
          <div class="footer-links">
            <a href="about.html">${t('footerStory')}</a>
            <a href="?view=info&topic=faq" data-nav="?view=info&topic=faq">${t('footerFaq')}</a>
          </div>
        </div>
        <div class="footer-group">
          <h3>${t('footerCustomerCol')}</h3>
          <div class="footer-links">
            <a href="?view=info&topic=shipping" data-nav="?view=info&topic=shipping">${t('footerShipping')}</a>
            <a href="?view=info&topic=privacy" data-nav="?view=info&topic=privacy">${t('footerPrivacy')}</a>
          </div>
        </div>
      </div>
      <div class="copyright">
        <span>${t('copyright')}</span>
        <span>${t('shippingNoticeFoot')}</span>
      </div>
    </div>
  </footer>`;
}

function home() {
  const curHero = HERO_SLIDES[state.hero];
  const tag = state.lang === 'ar' ? curHero.tagAr : curHero.tagEn;
  const title = state.lang === 'ar' ? curHero.titleAr : curHero.titleEn;
  const desc = state.lang === 'ar' ? curHero.descAr : curHero.descEn;
  const btn = state.lang === 'ar' ? curHero.btnAr : curHero.btnEn;

  return `<main>
    <section class="hero hero-two-slide" style="--hero-desktop:url('${media(curHero.image)}');--hero-mobile:url('${media(curHero.mobile)}')" aria-label="Featured collections">
      <div class="shell hero-inner">
        <div class="hero-copy">
          <span class="micro">${tag}</span>
          <h1>${title}</h1>
          <p>${desc}</p>
          <a class="btn" href="${linkCollection(curHero.category)}" data-nav="${linkCollection(curHero.category)}">${btn} ${ico('arrow')}</a>
        </div>
      </div>
      <div class="hero-dots" role="group" aria-label="Choose featured slide">
        ${HERO_SLIDES.map((slide, i) => `
          <button type="button" data-act="slide" data-index="${i}" class="${state.hero === i ? 'active' : ''}" aria-label="Show slide ${i + 1}" aria-pressed="${state.hero === i}"></button>
        `).join('')}
      </div>
    </section>

    <div class="shell">
      <section class="categories" aria-label="Shop by category">
        <a class="category" href="${linkCollection('bags')}" data-nav="${linkCollection('bags')}">
          <img src="${media('studio-classic-shoulder.webp')}" alt="Bags">
          <div class="category-label"><strong>${t('navBags')}</strong><small>${t('viewAll')}</small></div>
        </a>
        <a class="category" href="${linkCollection('wallets')}" data-nav="${linkCollection('wallets')}">
          <img src="${media('studio-zip-wallet.webp')}" alt="Wallets">
          <div class="category-label"><strong>${t('navWallets')}</strong><small>${t('viewAll')}</small></div>
        </a>
        <a class="category" href="${linkCollection('accessories')}" data-nav="${linkCollection('accessories')}">
          <img src="${media('studio-bag-charm.webp')}" alt="Accessories">
          <div class="category-label"><strong>${t('navAccessories')}</strong><small>${t('viewAll')}</small></div>
        </a>
        <a class="category sale-cat" href="${linkCollection('sale')}" data-nav="${linkCollection('sale')}">
          <div class="sale-art" aria-hidden="true"><span class="sale-tag">SALE</span></div>
          <div class="category-label"><strong>${t('navSale')}</strong><small>${t('viewAll')}</small></div>
        </a>
      </section>

      <section class="products-area" id="best-sellers">
        <div class="section-heading">
          <h2>${t('bestSellersTitle')}</h2>
          <a href="${linkCollection('best-sellers')}" data-nav="${linkCollection('best-sellers')}">${t('viewAll')}</a>
        </div>
        <div class="product-grid">
          ${PRODUCTS.filter(p => p.featured).slice(0, 5).map(card).join('')}
        </div>
      </section>

      <section class="products-area new-arrivals" id="new-arrivals">
        <div class="section-heading">
          <h2>${t('newArrivalsTitle')}</h2>
          <a href="${linkCollection('new-arrivals')}" data-nav="${linkCollection('new-arrivals')}">${t('viewAll')}</a>
        </div>
        <div class="product-grid">
          ${PRODUCTS.filter(p => p.newArrival).slice(0, 5).map(card).join('')}
        </div>
      </section>

      <section class="products-area suggestions-home" id="you-may-also-like">
        <div class="section-heading">
          <h2>${t('youMayAlsoLikeTitle')}</h2>
          <a href="${linkCollection('accessories')}" data-nav="${linkCollection('accessories')}">${t('viewAll')}</a>
        </div>
        <div class="product-grid">
          ${[...PRODUCTS.filter(p => p.cat === 'wallets'), ...PRODUCTS.filter(p => p.cat === 'accessories'), ...PRODUCTS.filter(p => p.cat === 'bags')].slice(0, 5).map(card).join('')}
        </div>
      </section>
    </div>

    <section class="story-band">
      <div class="story-photo" role="img" aria-label="ZEMA Editorial"></div>
      <div class="story-copy">
        <span class="micro">${t('ourStoryBadge')}</span>
        <h2>${t('ourStoryTitle')}</h2>
        <p>${t('ourStoryDesc')}</p>
        <a href="about.html">${t('ourStoryLink')}</a>
      </div>
    </section>

    ${recentSection()}
  </main>`;
}

function card(p) {
  const saved = state.wish.includes(p.id);
  const name = safe(getProdName(p));
  return `<article class="product-card">
    <a class="product-image" href="${linkProduct(p)}" data-nav="${linkProduct(p)}">
      <img src="${media(p.image)}" alt="${name}" loading="lazy">
    </a>
    <button class="heart ${saved ? 'saved' : ''}" data-act="wish" data-id="${p.id}" aria-label="${saved ? 'Remove from' : 'Add to'} wishlist" aria-pressed="${saved}">
      ${ico('heart')}
    </button>
    <div class="product-info">
      <div class="product-meta">
        <a href="${linkProduct(p)}" data-nav="${linkProduct(p)}" class="product-name">${name}</a>
        <div class="product-price">${currency(p.price)}</div>
        <div class="swatches">
          ${p.colors.map(c => `
            <a href="${linkProduct(p)}" data-nav="${linkProduct(p)}" style="background:${c[1]}" title="${safe(state.lang === 'ar' && c[3] ? c[3] : c[0])}"></a>
          `).join('')}
        </div>
      </div>
      <button class="quick-add" data-act="quick" data-id="${p.id}" aria-label="Add ${name} to bag">
        ${ico('bag')}
      </button>
    </div>
  </article>`;
}

function pairingFor(p) {
  const preferred = (p.pairWith || []).map(byId).filter(q => q && q.id !== p.id);
  const fallback = PRODUCTS.filter(q => q.id !== p.id && !preferred.some(x => x.id === q.id))
    .sort((a, b) => ((a.cat === p.cat) ? 1 : 0) - ((b.cat === p.cat) ? 1 : 0));
  return [...preferred, ...fallback].slice(0, 2);
}

function pairKey(p, q) { return p.id + ':' + q.id; }
function pairEnabled(p, q) { return state.pairSelected[pairKey(p, q)] !== false; }
function selectedPairColor(q) {
  return q.colors.find(c => c[0] === state.pairColors[q.id]) || q.colors[0];
}

function pairBlock(p, mainColor) {
  const matches = pairingFor(p);
  if (!matches.length) return '';
  const chosen = matches.filter(q => pairEnabled(p, q));
  const total = p.price * state.qty + chosen.reduce((sum, q) => sum + q.price, 0);

  const item = q => {
    const col = selectedPairColor(q);
    const enabled = pairEnabled(p, q);
    const qName = safe(getProdName(q));
    const colName = safe(state.lang === 'ar' && col[3] ? col[3] : col[0]);
    return `<div class="pair-piece ${enabled ? '' : 'pair-piece-off'}">
      <div class="pair-piece-photo"><img src="${media(col[2])}" alt="${qName}" loading="lazy"></div>
      <div class="pair-piece-copy">
        <button class="pair-toggle" type="button" data-act="pair-toggle" data-id="${q.id}" aria-pressed="${enabled}" aria-label="${enabled ? 'Remove' : 'Include'} ${qName}">
          <span aria-hidden="true">${enabled ? '✓' : '+'}</span>
        </button>
        <a href="${linkProduct(q)}" data-nav="${linkProduct(q)}">${qName}</a>
        <div class="pair-price">${currency(q.price)}</div>
        <div class="pair-colors" aria-label="Colors for ${qName}">
          ${q.colors.map(c => `
            <button type="button" class="pair-swatch ${col[0] === c[0] ? 'on' : ''}" style="--swatch:${c[1]}" title="${safe(state.lang === 'ar' && c[3] ? c[3] : c[0])}" data-act="pair-color" data-id="${q.id}" data-color="${safe(c[0])}"></button>
          `).join('')}
          <small>${colName}</small>
        </div>
      </div>
    </div>`;
  };

  const pName = safe(getProdName(p));
  const mainColName = safe(state.lang === 'ar' && mainColor[3] ? mainColor[3] : mainColor[0]);

  return `<section class="pair-it-with" id="pair-it-with" aria-labelledby="pair-title">
    <div class="pair-heading">
      <div>
        <span class="micro">${t('pairBadge')}</span>
        <h2 id="pair-title">${t('pairTitle')}</h2>
        <p>${t('pairDesc')}</p>
      </div>
      <span class="pair-count">${1 + chosen.length} ${t('pairSelectionMeta')}</span>
    </div>
    <div class="pair-body">
      <div class="pair-products">
        <div class="pair-main">
          <div class="pair-piece-photo"><img src="${media(mainColor[2])}" alt="${pName}" loading="lazy"></div>
          <div class="pair-main-name">
            <span class="pair-included">${t('pairIncluded')}</span>
            <strong>${pName}</strong>
            <small>${mainColName} · ${t('quantity')}: ${state.qty}</small>
            <b>${currency(p.price * state.qty)}</b>
          </div>
        </div>
        ${matches.map(q => `<span class="pair-plus" aria-hidden="true">+</span>${item(q)}`).join('')}
      </div>
      <aside class="pair-summary">
        <span class="micro">${t('pairSelectionTitle')}</span>
        <div class="pair-summary-title">Together, Beautifully</div>
        <div class="pair-summary-meta">${1 + chosen.length} ${t('pairSelectionMeta')}</div>
        <div class="pair-total">
          <span>${t('finalTotalLabel')}</span>
          <strong>${currency(total)}</strong>
        </div>
        <button type="button" class="btn full" data-act="pair-add" data-id="${p.id}" data-color="${safe(mainColor[0])}">
          ${ico('bag')} ${t('pairAddBtn')}
        </button>
      </aside>
    </div>
  </section>`;
}

function productPage(id) {
  const p = byId(id);
  if (!p) {
    return `<main class="shell"><div class="empty-state"><h2>Product not found</h2><a href="?" data-nav="?" class="btn">${t('continueShopping')}</a></div></main>`;
  }

  if (!state.recent.includes(id)) {
    state.recent = [id, ...state.recent].slice(0, 8);
    persist('zema_sample_recent', state.recent);
  } else {
    state.recent = [id, ...state.recent.filter(x => x !== id)].slice(0, 8);
    persist('zema_sample_recent', state.recent);
  }

  const color = p.colors.find(c => c[0] === state.chosenColor) || p.colors[0];
  const gal = state.chosenColor && state.chosenColor !== p.color ? [color[2]] : p.gallery;
  const photo = gal[Math.min(state.activePhoto, gal.length - 1)] || gal[0];
  const related = [...PRODUCTS.filter(q => q.id !== id && q.cat === p.cat), ...PRODUCTS.filter(q => q.id !== id && q.cat !== p.cat)].slice(0, 4);
  const suggestion = PRODUCTS.filter(q => q.id !== id && (p.cat === 'bags' ? q.cat !== 'bags' : q.cat === 'bags')).slice(0, 3);

  const pName = safe(getProdName(p));
  const pDesc = safe(getProdDesc(p));
  const pMaterials = safe(getProdMaterials(p));
  const colorName = safe(state.lang === 'ar' && color[3] ? color[3] : color[0]);
  const catLabel = ({ 'bags': t('navBags'), 'wallets': t('navWallets'), 'accessories': t('navAccessories') }[p.cat] || p.cat);

  return `<main class="shell">
    <div class="crumbs">
      <a href="?" data-nav="?">${t('crumbsHome')}</a>
      <span>›</span>
      <a href="${linkCollection(p.cat)}" data-nav="${linkCollection(p.cat)}">${catLabel}</a>
      <span>›</span>
      <span>${pName}</span>
    </div>
    <section class="detail">
      <div class="gallery">
        <div class="thumbs">
          ${gal.map((im, i) => `
            <button data-act="photo" data-index="${i}" class="${i === state.activePhoto ? 'selected' : ''}" aria-label="Angle ${i + 1}">
              <img src="${media(im)}" alt="${pName}">
            </button>
          `).join('')}
        </div>
        <div class="main-photo" data-act="zoom" data-image="${photo}">
          <img src="${media(photo)}" alt="${pName}">
          <button class="zoom" data-act="zoom" data-image="${photo}" aria-label="Zoom image">+</button>
        </div>
      </div>
      <div class="detail-info">
        <span class="detail-topline">THE ZEMA EDIT</span>
        <h1>${pName}</h1>
        <div class="detail-price">${currency(p.price)}</div>
        <p class="detail-description">${pDesc}</p>
        <div class="variant-label">${t('color')}: <strong>${colorName}</strong></div>
        <div class="variant-options">
          ${p.colors.map(c => `
            <button class="variant-btn ${c[0] === color[0] ? 'selected' : ''}" style="background:${c[1]}" data-act="color" data-color="${safe(c[0])}" aria-label="Select ${safe(c[0])}" title="${safe(state.lang === 'ar' && c[3] ? c[3] : c[0])}"></button>
          `).join('')}
        </div>
        <div class="purchase-bar">
          <div class="qty">
            <button data-act="product-qty" data-delta="-1" aria-label="Decrease quantity">−</button>
            <span>${state.qty}</span>
            <button data-act="product-qty" data-delta="1" aria-label="Increase quantity">+</button>
          </div>
          <button class="btn" data-act="add" data-id="${p.id}" data-color="${safe(color[0])}">
            ${ico('bag')} ${t('addToCart')}
          </button>
          <button class="wishlist-pdp ${state.wish.includes(p.id) ? 'saved' : ''}" data-act="wish" data-id="${p.id}" aria-label="Toggle wishlist">
            ${ico('heart')}
          </button>
        </div>
        <button class="btn outline full" data-act="buy" data-id="${p.id}" data-color="${safe(color[0])}">
          ${t('buyNow')}
        </button>
        <div class="service-row">
          <div>${ico('truck')}<span>${t('deliveryFast')}<small>${t('deliveryNote')}</small></span></div>
          <div>${ico('box')}<span>${t('codBadge')}<small>${t('codNote')}</small></span></div>
          <div>${ico('shield')}<span>${t('qualityBadge')}<small>${t('qualityNote')}</small></span></div>
        </div>
        <div class="accordion">
          <details open>
            <summary>${t('detailsHeading')}</summary>
            <p>${pDesc}</p>
          </details>
          <details>
            <summary>${t('materialsHeading')}</summary>
            <p>${pMaterials}</p>
          </details>
          <details>
            <summary>${t('shippingHeading')}</summary>
            <p>${state.lang === 'ar' ? 'التوصيل متاح لجميع محافظات مصر عبر شركة شحن سريعة مع إمكانية المعاينة قبل الدفع نقدًا عند الاستلام. الاستبدال والاسترجاع متاح خلال 14 يومًا وفق الشروط.' : 'Fast delivery across all Egyptian governorates with cash on delivery and full inspection before payment. 14-day exchange & return policy.'}</p>
          </details>
        </div>
      </div>
    </section>

    ${pairBlock(p, color)}

    <section class="related-section">
      <div class="section-heading"><h2>${t('completeTheLookTitle')}</h2></div>
      <div class="related-grid">${suggestion.map(card).join('')}</div>
    </section>

    <section class="related-section">
      <div class="section-heading"><h2>${t('youMayAlsoLikeTitle')}</h2></div>
      <div class="related-grid">${(related.length ? related : PRODUCTS.filter(q => q.id !== p.id).slice(0, 4)).map(card).join('')}</div>
    </section>

    ${recentSection(id)}
  </main>`;
}

function recentSection(exclude = '') {
  const recent = state.recent.filter(id => id !== exclude).map(byId).filter(Boolean).slice(0, 4);
  if (!recent.length) return '';
  return `<section class="shell recent-section">
    <div class="section-heading">
      <h2>${t('recentlyViewedTitle')}</h2>
      <button data-act="clear-recent" style="border:0;background:none;color:#74675c;font-size:12px">${t('clearAll')}</button>
    </div>
    <div class="related-grid">${recent.map(card).join('')}</div>
  </section>`;
}

function collectionPage(cat) {
  let list = PRODUCTS.filter(p => ['bags', 'wallets', 'accessories'].includes(cat) ? p.cat === cat : true);
  if (cat === 'best-sellers') list = PRODUCTS.filter(p => p.featured);
  if (cat === 'new-arrivals') list = PRODUCTS.filter(p => p.newArrival);
  if (cat === 'sale') list = PRODUCTS.filter(p => p.salePrice && p.salePrice < p.price);

  if (state.filterColor !== 'all') {
    list = list.filter(p => p.colors.some(c => c[0] === state.filterColor || (c[3] && c[3] === state.filterColor)));
  }
  if (state.filterMax !== 'all') {
    list = list.filter(p => p.price <= Number(state.filterMax));
  }

  if (state.sort === 'low') list = [...list].sort((a, b) => a.price - b.price);
  if (state.sort === 'high') list = [...list].sort((a, b) => b.price - a.price);
  if (state.sort === 'name') list = [...list].sort((a, b) => getProdName(a).localeCompare(getProdName(b)));

  const label = ({
    'bags': t('navBags'),
    'wallets': t('navWallets'),
    'accessories': t('navAccessories'),
    'best-sellers': t('navBestSellers'),
    'new-arrivals': t('navNewArrivals'),
    'sale': t('navSale')
  }[cat] || t('navBags'));

  const colors = [...new Set(PRODUCTS.flatMap(p => p.colors.map(c => state.lang === 'ar' && c[3] ? c[3] : c[0])))].sort();

  return `<main class="shell small-section collection-view">
    <div class="crumbs">
      <a data-nav="?" href="?">${t('crumbsHome')}</a>
      <span>›</span>
      ${label}
    </div>
    <div class="collection-top">
      <span class="micro">THE ZEMA EDIT</span>
      <h1>${label}</h1>
      <p>${t('ourStoryDesc')}</p>
    </div>
    <div class="listing-bar">
      <span>${list.length} ${t('itemsCount')}</span>
      <div class="filter-controls">
        <label>${t('filterColor')}
          <select id="color-filter">
            <option value="all">${t('allColors')}</option>
            ${colors.map(c => `<option value="${safe(c)}" ${state.filterColor === c ? 'selected' : ''}>${safe(c)}</option>`).join('')}
          </select>
        </label>
        <label>${t('filterPrice')}
          <select id="price-filter">
            <option value="all">${t('anyPrice')}</option>
            ${[500, 1000, 2000, 2500].map(v => `<option value="${v}" ${state.filterMax === String(v) ? 'selected' : ''}>${currency(v)}</option>`).join('')}
          </select>
        </label>
        <label>${t('sortBy')}
          <select id="sort-select">
            <option value="featured" ${state.sort === 'featured' ? 'selected' : ''}>${t('sortFeatured')}</option>
            <option value="low" ${state.sort === 'low' ? 'selected' : ''}>${t('sortLow')}</option>
            <option value="high" ${state.sort === 'high' ? 'selected' : ''}>${t('sortHigh')}</option>
            <option value="name" ${state.sort === 'name' ? 'selected' : ''}>${t('sortName')}</option>
          </select>
        </label>
      </div>
    </div>
    ${list.length ? `
      <div class="product-grid collection-grid">${list.map(card).join('')}</div>
    ` : `
      <div class="empty-state">
        <h2>${t('noSearchResults')}</h2>
        <button class="btn outline" data-act="reset-filters">${t('clearAll')}</button>
      </div>
    `}
  </main>`;
}

function wishlistPage() {
  const list = state.wish.map(byId).filter(Boolean);
  return `<main class="shell small-section">
    <div class="listing-bar">
      <h1>${state.lang === 'ar' ? 'قائمة الرغبات والمفضلة' : 'Your Wishlist'}</h1>
    </div>
    ${list.length ? `
      <div class="product-grid">${list.map(card).join('')}</div>
    ` : `
      <div class="empty-state">
        <h2>${t('emptyWishlistTitle')}</h2>
        <p>${t('emptyWishlistDesc')}</p>
        <a class="btn" data-nav="?" href="?">${t('browseCollection')}</a>
      </div>
    `}
  </main>`;
}

function infoPage() {
  const topic = params().get('topic') || 'faq';
  const labelsEn = { shipping: 'Shipping & Returns', privacy: 'Privacy Policy', faq: 'Frequently Asked Questions' };
  const labelsAr = { shipping: 'الشحن والاسترجاع', privacy: 'سياسة الخصوصية', faq: 'الأسئلة الشائعة' };
  const title = (state.lang === 'ar' ? labelsAr[topic] : labelsEn[topic]) || labelsAr.faq;

  return `<main class="shell small-section info-page">
    <div class="crumbs"><a data-nav="?" href="?">${t('crumbsHome')}</a> › ${title}</div>
    <span class="micro">HELP CENTER</span>
    <h1>${title}</h1>
    ${topic === 'faq' ? `
      <div class="accordion">
        <details open>
          <summary>${state.lang === 'ar' ? 'ما هي خيارات ومصاريف الشحن داخل مصر؟' : 'What are the shipping options and fees in Egypt?'}</summary>
          <p>${state.lang === 'ar' ? 'نوفر توصيلاً سريعاً لجميع المحافظات خلال 2 إلى 4 أيام عمل. الشحن مجاني لجميع الطلبات بقيمة 2,500 ج.م وأكثر، ورسوم التوصيل العادية تبدأ من 50 ج.م للقاهرة والجيزة و65 ج.م للإسكندرية والمحافظات الأخرى.' : 'We provide fast express delivery across all Egyptian governorates in 2-4 business days. Free shipping on orders over 2,500 EGP. Standard delivery starts from 50 EGP for Cairo & Giza, and 65 EGP for other governorates.'}</p>
        </details>
        <details>
          <summary>${state.lang === 'ar' ? 'كيف يمكنني سداد قيمة الطلب؟' : 'How do I pay for my order?'}</summary>
          <p>${state.lang === 'ar' ? 'ندعم حالياً الدفع نقدًا عند الاستلام (Cash on Delivery). يمكنك استلام طردك، معاينته، والتأكد من مطابقة المنتج ثم سداد قيمته لمندوب التوصيل.' : 'We currently support Cash on Delivery (COD). You can receive your parcel, inspect it, and pay in cash directly to the courier.'}</p>
        </details>
        <details>
          <summary>${state.lang === 'ar' ? 'ما هي سياسة الاستبدال والاسترجاع؟' : 'What is your exchange and return policy?'}</summary>
          <p>${state.lang === 'ar' ? 'يحق لكِ استبدال أو استرجاع أي منتج خلال 14 يوماً من الاستلام بشرط أن يكون بحالته الأصلية، داخل تغليفه ولم يُستخدم.' : 'You have the right to exchange or return any product within 14 days of receipt, provided the item is unused and in its original luxury packaging.'}</p>
        </details>
      </div>
    ` : `
      <div class="policy-page">
        <p>${state.lang === 'ar' ? 'نحن في ZEMA ملتزمون بتقديم تجربة تسوق راقية وشفافة تحمي خصوصية بيانات عملائنا وتضمن أعلى معايير الجودة والتوصيل السريع.' : 'At ZEMA Maison, we are committed to delivering an exceptional shopping experience with transparent policies, fast delivery, and premium care.'}</p>
      </div>
    `}
  </main>`;
}

function cartCount() {
  return state.cart.reduce((n, x) => n + x.qty, 0);
}

function cartSubtotal() {
  return state.cart.reduce((n, x) => n + (byId(x.id)?.price || 0) * x.qty, 0);
}

function calcShipping(subtotal, govId) {
  if (subtotal >= STORE_CONFIG.freeShippingThreshold) return 0;
  const gov = getGov(govId);
  return gov ? gov.fee : STORE_CONFIG.defaultShippingFee;
}

function checkoutPage() {
  if (!state.cart.length) {
    return `<main class="shell">
      <div class="empty-state">
        <h2>${t('emptyBagTitle')}</h2>
        <p>${t('emptyBagDesc')}</p>
        <a class="btn" href="?" data-nav="?">${t('continueShopping')}</a>
      </div>
    </main>`;
  }

  const sub = cartSubtotal();
  const shippingFee = calcShipping(sub, state.selectedGov);
  const total = sub + shippingFee;
  const isFree = sub >= STORE_CONFIG.freeShippingThreshold;

  return `<main class="shell checkout">
    <section>
      <div class="crumbs"><a href="?" data-nav="?">${t('crumbsHome')}</a> › ${t('shoppingBagTitle')} › ${t('crumbsCheckout')}</div>
      <p class="detail-topline">ZEMA MAISON · DIRECT ORDER</p>
      <h1>${t('checkoutTitle')}</h1>

      <form id="checkout-form" class="checkout-form">
        <fieldset>
          <legend>${t('contactLegend')}</legend>
          <label for="cust-name">${t('fullNameLabel')} *</label>
          <input id="cust-name" required autocomplete="name" maxlength="100" placeholder="${t('fullNamePlaceholder')}">

          <label for="cust-phone">${t('phoneLabel')} *</label>
          <input id="cust-phone" required type="tel" inputmode="tel" autocomplete="tel" placeholder="${t('phonePlaceholder')}" pattern="[0-9+ ]{10,15}">
        </fieldset>

        <fieldset>
          <legend>${t('deliveryLegend')}</legend>
          <label for="cust-gov">${t('governorateLabel')} *</label>
          <select id="cust-gov" required>
            <option value="">-- ${t('selectGov')} --</option>
            ${EGYPT_GOVERNORATES.map(g => `
              <option value="${g.id}" ${state.selectedGov === g.id ? 'selected' : ''}>
                ${state.lang === 'ar' ? g.ar : g.en} (${g.fee} ${STORE_CONFIG.currencyAr})
              </option>
            `).join('')}
          </select>

          <label for="cust-area">${t('areaLabel')} *</label>
          <input id="cust-area" required maxlength="120" placeholder="${t('areaPlaceholder')}">

          <label for="cust-address">${t('addressLabel')} *</label>
          <textarea id="cust-address" required maxlength="400" rows="3" placeholder="${t('addressPlaceholder')}"></textarea>

          <label for="cust-notes">${t('notesLabel')}</label>
          <textarea id="cust-notes" maxlength="300" rows="2" placeholder="${t('notesPlaceholder')}"></textarea>
        </fieldset>

        <fieldset>
          <legend>${t('paymentLegend')}</legend>
          <div class="payment-card active">
            <div class="payment-card-head">
              <input type="radio" checked id="cod-radio" name="payment-method">
              <label for="cod-radio"><strong>${t('codTitle')}</strong></label>
            </div>
            <p>${t('codDescription')}</p>
          </div>
        </fieldset>

        <button class="btn full checkout-submit-btn" type="submit">
          ${t('confirmOrderBtn')}
        </button>
      </form>
    </section>

    <aside class="checkout-card">
      <h2>${t('orderSummary')}</h2>
      ${state.cart.map(item => {
        const p = byId(item.id);
        if (!p) return '';
        const col = p.colors.find(c => c[0] === item.color) || p.colors[0];
        const pName = safe(getProdName(p));
        const colName = safe(state.lang === 'ar' && col[3] ? col[3] : col[0]);
        return `
          <div class="checkout-line">
            <img src="${media(col[2])}" alt="${pName}">
            <span>
              <strong>${pName}</strong>
              <small>${colName} · ${t('quantity')}: ${item.qty}</small>
            </span>
            <b>${currency(p.price * item.qty)}</b>
          </div>
        `;
      }).join('')}

      <div class="subtotal">
        <span>${t('subtotal')}</span>
        <span>${currency(sub)}</span>
      </div>

      <div class="checkout-cost">
        <span>${t('deliveryFeeLabel')}</span>
        <b>${isFree ? `<span class="free-pill">${t('freeShippingText')}</span>` : (state.selectedGov ? currency(shippingFee) : t('shippingCalc'))}</b>
      </div>

      <div class="checkout-cost checkout-final-total">
        <span>${t('finalTotalLabel')}</span>
        <strong>${currency(total)}</strong>
      </div>

      ${isFree ? `<p class="cart-hint" style="color:#2f6e3c;font-weight:600">🎉 ${t('topbarFreeShipping')}</p>` : ''}
    </aside>
  </main>`;
}

function orderSuccessPage() {
  const order = state.lastOrder;
  if (!order) {
    return `<main class="shell"><div class="empty-state"><h2>No recent order found</h2><a href="?" data-nav="?" class="btn">${t('continueShopping')}</a></div></main>`;
  }

  // Generate pre-filled WhatsApp message
  const itemsText = order.items.map(it => `• ${it.name} (${it.color}) × ${it.qty} = ${it.price * it.qty} EGP`).join('\n');
  const waMsg = state.lang === 'ar'
    ? `مرحباً ZEMA Maison ✨\nأود تأكيد طلبي رقم: #${order.id}\n\n📋 تفاصيل الفاتورة:\n${itemsText}\n\nالمجموع الفرعي: ${order.subtotal} ج.م\nالشحن: ${order.shippingFee ? order.shippingFee + ' ج.م' : 'مجاني'}\nالإجمالي المطلوب: ${order.total} ج.م\nطريقة السداد: الدفع نقدًا عند الاستلام (COD)\n\n📍 بيانات التوصيل:\nالاسم: ${order.customer.name}\nالهاتف: ${order.customer.phone}\nالمحافظة: ${order.customer.gov}\nالعنوان: ${order.customer.area}، ${order.customer.address}${order.customer.notes ? '\nملاحظات: ' + order.customer.notes : ''}\n\nشكراً لكم!`
    : `Hello ZEMA Maison ✨\nI would like to confirm my order: #${order.id}\n\n📋 Order Items:\n${itemsText}\n\nSubtotal: ${order.subtotal} EGP\nShipping: ${order.shippingFee ? order.shippingFee + ' EGP' : 'Free'}\nTotal: ${order.total} EGP\nPayment: Cash on Delivery\n\n📍 Delivery Details:\nName: ${order.customer.name}\nPhone: ${order.customer.phone}\nGovernorate: ${order.customer.gov}\nAddress: ${order.customer.area}, ${order.customer.address}\n\nThank you!`;

  const waUrl = `https://wa.me/${STORE_CONFIG.whatsappNumber.replace(/[^0-9]/g, '')}?text=${encodeURIComponent(waMsg)}`;

  return `<main class="shell order-success-page">
    <div class="success-banner">
      <div class="success-badge">${ico('check')}</div>
      <span class="micro">${t('orderSuccessBadge')}</span>
      <h1>${t('orderSuccessTitle')}</h1>
      <p>${t('orderSuccessSubtitle')}</p>
    </div>

    <div class="invoice-box">
      <div class="invoice-header">
        <div>
          <h2>#${order.id}</h2>
          <small>${t('orderDateLabel')}: ${new Date(order.date).toLocaleDateString(state.lang === 'ar' ? 'ar-EG' : 'en-US', { year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit' })}</small>
        </div>
        <div class="invoice-logo">
          <img src="zema-logo.png" alt="ZEMA">
        </div>
      </div>

      <div class="invoice-details-grid">
        <div>
          <span class="micro">${t('orderCustomerLabel')}</span>
          <strong>${safe(order.customer.name)}</strong>
          <div>${safe(order.customer.phone)}</div>
        </div>
        <div>
          <span class="micro">${t('orderAddressLabel')}</span>
          <strong>${safe(order.customer.gov)}</strong>
          <div>${safe(order.customer.area)}</div>
          <div>${safe(order.customer.address)}</div>
        </div>
        <div>
          <span class="micro">${t('orderPaymentMethodLabel')}</span>
          <strong>${t('codTitle')}</strong>
          <small style="color:#6d5f53">${t('orderStatusCod')}</small>
        </div>
      </div>

      <div class="invoice-items">
        ${order.items.map(item => `
          <div class="invoice-item-row">
            <img src="${media(item.image)}" alt="">
            <div class="invoice-item-info">
              <strong>${safe(item.name)}</strong>
              <small>${safe(item.color)} × ${item.qty}</small>
            </div>
            <b>${currency(item.price * item.qty)}</b>
          </div>
        `).join('')}
      </div>

      <div class="invoice-totals">
        <div class="line"><span>${t('subtotal')}</span><span>${currency(order.subtotal)}</span></div>
        <div class="line"><span>${t('deliveryFeeLabel')}</span><span>${order.shippingFee ? currency(order.shippingFee) : t('freeShippingText')}</span></div>
        <div class="line final"><span>${t('finalTotalLabel')}</span><strong>${currency(order.total)}</strong></div>
      </div>
    </div>

    <div class="order-actions">
      <a class="btn whatsapp-btn" href="${waUrl}" target="_blank" rel="noopener">
        ${ico('whatsapp')} ${t('sendWhatsAppBtn')}
      </a>
      <button class="btn outline" onclick="window.print()">
        ${ico('print')} ${t('printInvoiceBtn')}
      </button>
      <a class="btn outline" href="?" data-nav="?">
        ${t('continueShopping')}
      </a>
    </div>
  </main>`;
}

function cartDrawer() {
  const suggested = PRODUCTS.find(p => p.cat === 'accessories' && !state.cart.some(x => x.id === p.id));
  return `<div class="backdrop" data-act="close"></div>
  <aside class="drawer wide" role="dialog" aria-modal="true" aria-label="Shopping bag">
    <div class="drawer-head">
      <h2>${t('shoppingBagTitle')} (${cartCount()})</h2>
      <button class="icon-btn" data-act="close" aria-label="Close">${ico('close')}</button>
    </div>
    <div class="drawer-body">
      ${state.cart.length ? state.cart.map(item => {
        const p = byId(item.id);
        const col = p.colors.find(c => c[0] === item.color) || p.colors[0];
        const pName = safe(getProdName(p));
        const colName = safe(state.lang === 'ar' && col[3] ? col[3] : col[0]);
        return `
          <div class="drawer-row">
            <img src="${media(col[2])}" alt="${pName}">
            <div>
              <a data-nav="${linkProduct(p)}" href="${linkProduct(p)}" class="drawer-title">${pName}</a>
              <div class="drawer-sub">${t('color')}: ${colName}</div>
              <div class="drawer-price">${currency(p.price)}</div>
              <div class="qty">
                <button data-act="cart-qty" data-id="${p.id}" data-color="${safe(item.color)}" data-delta="-1">−</button>
                <span>${item.qty}</span>
                <button data-act="cart-qty" data-id="${p.id}" data-color="${safe(item.color)}" data-delta="1">+</button>
              </div>
            </div>
            <button class="remove-btn" data-act="remove" data-id="${p.id}" data-color="${safe(item.color)}" aria-label="Remove item">${ico('trash')}</button>
          </div>
        `;
      }).join('') : `
        <div class="empty-state">
          <h2>${t('emptyBagTitle')}</h2>
          <p>${t('emptyBagDesc')}</p>
        </div>
      `}
      ${state.cart.length && suggested ? `
        <div class="mini-suggestion">
          <h3>${t('completeTheLookTitle')}</h3>
          <div class="suggest-row">
            <img src="${media(suggested.image)}" alt="${safe(getProdName(suggested))}">
            <div>
              <div class="drawer-title">${safe(getProdName(suggested))}</div>
              <div class="drawer-price">${currency(suggested.price)}</div>
            </div>
            <button data-act="quick" data-id="${suggested.id}" class="btn">${t('addToCart')} +</button>
          </div>
        </div>
      ` : ''}
    </div>
    <div class="drawer-footer">
      <div class="subtotal">
        <span>${t('subtotal')}</span>
        <span>${currency(cartSubtotal())}</span>
      </div>
      <p class="cart-hint">${t('topbarFreeShipping')}</p>
      <button class="btn outline full" data-act="close">${t('continueShopping')}</button>
      <button class="btn full" data-nav="?view=checkout">${t('reviewCheckout')}</button>
    </div>
  </aside>`;
}

function menuDrawer() {
  return `<div class="backdrop" data-act="close"></div>
  <aside class="drawer" role="dialog" aria-modal="true" aria-label="Menu">
    <div class="drawer-body">
      <div class="menu-head">
        <a class="menu-logo" href="?" data-nav="?"><img src="zema-logo.png" alt="ZEMA"></a>
        <button class="icon-btn" data-act="close" aria-label="Close menu">${ico('close')}</button>
      </div>
      <div style="margin-bottom:15px">
        <button class="lang-pill" data-act="toggle-lang" style="width:100%;text-align:center;padding:8px">${t('langToggle')}</button>
      </div>
      <nav class="menu-links">
        <a data-nav="?" href="?">${t('crumbsHome')}</a>
        <a data-nav="${linkCollection('bags')}" href="${linkCollection('bags')}">${t('navBags')}　›</a>
        <a data-nav="${linkCollection('wallets')}" href="${linkCollection('wallets')}">${t('navWallets')}　›</a>
        <a data-nav="${linkCollection('accessories')}" href="${linkCollection('accessories')}">${t('navAccessories')}　›</a>
        <a data-nav="${linkCollection('best-sellers')}" href="${linkCollection('best-sellers')}">${t('navBestSellers')}</a>
        <a data-nav="${linkCollection('new-arrivals')}" href="${linkCollection('new-arrivals')}">${t('navNewArrivals')}</a>
        <a class="sale-link" data-nav="${linkCollection('sale')}" href="${linkCollection('sale')}">${t('navSale')}</a>
        <div class="separator"></div>
        <a data-nav="?view=wishlist" href="?view=wishlist">${state.lang === 'ar' ? 'قائمة الرغبات' : 'Wishlist'}</a>
        <a data-act="cart" href="#cart">${t('shoppingBagTitle')} (${cartCount()})</a>
      </nav>
      <nav class="menu-links menu-secondary">
        <a href="about.html">${t('footerStory')}</a>
        <a data-nav="?view=info&topic=faq" href="?view=info&topic=faq">${t('footerFaq')}</a>
        <a data-nav="?view=info&topic=shipping" href="?view=info&topic=shipping">${t('footerShipping')}</a>
      </nav>
    </div>
  </aside>`;
}

function render() {
  setDocumentLang();
  const v = currentView();
  const id = currentProduct();

  root.innerHTML = header() + (
    id ? productPage(id) :
    collection() ? collectionPage(collection()) :
    v === 'wishlist' ? wishlistPage() :
    v === 'checkout' ? checkoutPage() :
    v === 'order-success' ? orderSuccessPage() :
    v === 'info' ? infoPage() :
    home()
  ) + footer() + (
    state.drawer === 'cart' ? cartDrawer() :
    state.drawer === 'menu' ? menuDrawer() : ''
  ) + (
    state.zoom ? `
      <div class="zoom-modal" data-act="close-zoom">
        <img src="${media(state.zoom)}" alt="Zoomed product">
        <button class="zoom-close" data-act="close-zoom" aria-label="Close zoom">×</button>
      </div>
    ` : ''
  );

  document.body.classList.toggle('no-scroll', Boolean(state.drawer || state.zoom));

  // Search input listeners
  const searchInput = document.getElementById('desktop-search');
  if (searchInput) {
    searchInput.addEventListener('focus', () => {
      if (state.search) return;
      state.search = true;
      const pos = searchInput.selectionStart;
      render();
      const i = document.getElementById('desktop-search');
      if (i) {
        i.focus();
        i.setSelectionRange(pos, pos);
      }
    });
    searchInput.addEventListener('input', e => {
      state.searchQuery = e.target.value;
      const matches = document.getElementById('search-results');
      if (matches) matches.innerHTML = searchMatches();
    });
  }

  const mobInput = document.getElementById('mobile-search-input');
  if (mobInput) {
    mobInput.addEventListener('input', e => {
      state.searchQuery = e.target.value;
      const matches = document.getElementById('search-results');
      if (matches) matches.innerHTML = searchMatches();
    });
  }

  // Filters listeners
  const sort = document.getElementById('sort-select');
  if (sort) sort.addEventListener('change', e => { state.sort = e.target.value; render(); });

  for (const [eid, k] of [['color-filter', 'filterColor'], ['price-filter', 'filterMax']]) {
    const el = document.getElementById(eid);
    if (el) el.addEventListener('change', e => { state[k] = e.target.value; render(); });
  }

  // Governorate selection live shipping listener
  const govSelect = document.getElementById('cust-gov');
  if (govSelect) {
    govSelect.addEventListener('change', e => {
      state.selectedGov = e.target.value;
      render();
    });
  }

  // Newsletter form
  const news = document.getElementById('newsletter-form');
  if (news) {
    news.addEventListener('submit', e => {
      e.preventDefault();
      toast(t('newsletterToast'));
      news.reset();
    });
  }

  // Checkout form submit listener (Complete functional checkout)
  const checkout = document.getElementById('checkout-form');
  if (checkout) {
    checkout.addEventListener('submit', e => {
      e.preventDefault();
      const name = document.getElementById('cust-name').value.trim();
      const phone = document.getElementById('cust-phone').value.trim();
      const govId = document.getElementById('cust-gov').value;
      const area = document.getElementById('cust-area').value.trim();
      const address = document.getElementById('cust-address').value.trim();
      const notes = document.getElementById('cust-notes').value.trim();

      if (!name || !phone || !govId || !area || !address) {
        alert(state.lang === 'ar' ? 'يرجى استكمال جميع بيانات التوصيل المطلوبة.' : 'Please fill all required delivery details.');
        return;
      }

      const govObj = getGov(govId);
      const govName = govObj ? (state.lang === 'ar' ? govObj.ar : govObj.en) : govId;
      const sub = cartSubtotal();
      const shippingFee = calcShipping(sub, govId);
      const total = sub + shippingFee;
      const orderId = 'ZM-' + Math.floor(100000 + Math.random() * 900000);

      const orderData = {
        id: orderId,
        date: new Date().toISOString(),
        customer: {
          name,
          phone,
          gov: govName,
          area,
          address,
          notes
        },
        items: state.cart.map(item => {
          const p = byId(item.id);
          const col = p.colors.find(c => c[0] === item.color) || p.colors[0];
          return {
            id: p.id,
            name: getProdName(p),
            color: state.lang === 'ar' && col[3] ? col[3] : col[0],
            qty: item.qty,
            price: p.price,
            image: col[2]
          };
        }),
        subtotal: sub,
        shippingFee,
        total,
        paymentMethod: 'Cash on Delivery (COD)'
      };

      // Store in state & storage
      state.lastOrder = orderData;
      persist('zema_last_order', orderData);

      // Save to orders history
      const history = stored('zema_orders_history', []);
      history.unshift(orderData);
      persist('zema_orders_history', history);

      // Empty cart
      state.cart = [];
      persist('zema_sample_cart', []);

      // Navigate to order-success view
      goto('?view=order-success&id=' + orderId);
    });
  }
}

function pushCartItem(id, color, qty = 1) {
  const p = byId(id);
  if (!p) return;
  const valid = p.colors.find(c => c[0] === color) || p.colors[0];
  const n = Math.max(1, Math.min(99, Number(qty) || 1));
  const existing = state.cart.find(x => x.id === id && x.color === valid[0]);
  if (existing) existing.qty = Math.min(99, existing.qty + n);
  else state.cart.push({ id, color: valid[0], qty: n });
}

function addItem(id, color, qty = 1) {
  pushCartItem(id, color, qty);
  persist('zema_sample_cart', state.cart);
  state.drawer = 'cart';
  render();
}

function addPairedSet(id, color) {
  const p = byId(id);
  if (!p) return;
  pushCartItem(id, color, state.qty);
  for (const q of pairingFor(p)) {
    if (pairEnabled(p, q)) {
      pushCartItem(q.id, selectedPairColor(q)[0], 1);
    }
  }
  persist('zema_sample_cart', state.cart);
  state.drawer = 'cart';
  render();
}

document.addEventListener('click', e => {
  const btn = e.target.closest('[data-act],[data-nav]');
  if (!btn) {
    if (state.search && !e.target.closest('.site-header')) {
      state.search = false;
      render();
    }
    return;
  }

  const nav = btn.dataset.nav;
  const act = btn.dataset.act;

  if (nav) {
    e.preventDefault();
    goto(nav);
    return;
  }

  if (act === 'toggle-lang') {
    toggleLanguage();
  } else if (act === 'reset-filters') {
    state.filterColor = 'all';
    state.filterMax = 'all';
    state.sort = 'featured';
    render();
  } else if (act === 'menu') {
    state.drawer = 'menu';
    render();
  } else if (act === 'search') {
    state.search = !state.search;
    render();
    document.getElementById('mobile-search-input')?.focus();
  } else if (act === 'cart') {
    e.preventDefault();
    state.drawer = 'cart';
    render();
  } else if (act === 'close') {
    state.drawer = '';
    state.search = false;
    render();
  } else if (act === 'wish') {
    const id = btn.dataset.id;
    state.wish = state.wish.includes(id) ? state.wish.filter(x => x !== id) : [...state.wish, id];
    persist('zema_sample_wish', state.wish);
    render();
  } else if (act === 'pair-toggle') {
    const p = byId(currentProduct());
    const q = byId(btn.dataset.id);
    if (p && q) {
      const k = pairKey(p, q);
      state.pairSelected[k] = !pairEnabled(p, q);
      render();
    }
  } else if (act === 'pair-color') {
    const q = byId(btn.dataset.id);
    if (q && q.colors.some(c => c[0] === btn.dataset.color)) {
      state.pairColors[q.id] = btn.dataset.color;
      render();
    }
  } else if (act === 'pair-add') {
    addPairedSet(btn.dataset.id, btn.dataset.color);
  } else if (act === 'quick') {
    addItem(btn.dataset.id, byId(btn.dataset.id)?.color);
  } else if (act === 'add') {
    addItem(btn.dataset.id, btn.dataset.color, state.qty);
  } else if (act === 'buy') {
    addItem(btn.dataset.id, btn.dataset.color, state.qty);
    state.drawer = '';
    goto('?view=checkout');
  } else if (act === 'product-qty') {
    state.qty = Math.max(1, Math.min(99, state.qty + Number(btn.dataset.delta)));
    render();
  } else if (act === 'cart-qty') {
    const x = state.cart.find(x => x.id === btn.dataset.id && x.color === btn.dataset.color);
    if (x) {
      x.qty += Number(btn.dataset.delta);
      if (x.qty <= 0) state.cart = state.cart.filter(y => y !== x);
      persist('zema_sample_cart', state.cart);
      render();
    }
  } else if (act === 'remove') {
    state.cart = state.cart.filter(x => !(x.id === btn.dataset.id && x.color === btn.dataset.color));
    persist('zema_sample_cart', state.cart);
    render();
  } else if (act === 'photo') {
    state.activePhoto = Number(btn.dataset.index);
    render();
  } else if (act === 'color') {
    state.chosenColor = btn.dataset.color;
    state.activePhoto = 0;
    render();
  } else if (act === 'zoom') {
    state.zoom = btn.dataset.image;
    render();
  } else if (act === 'close-zoom') {
    state.zoom = null;
    render();
  } else if (act === 'clear-recent') {
    state.recent = [];
    persist('zema_sample_recent', []);
    render();
  } else if (act === 'slide') {
    state.hero = Number(btn.dataset.index);
    render();
  }
});

window.addEventListener('popstate', () => {
  state.drawer = '';
  state.zoom = null;
  render();
});

window.addEventListener('hashchange', () => {
  if (location.protocol === 'file:') {
    state.drawer = '';
    state.zoom = null;
    render();
  }
});

window.addEventListener('keydown', e => {
  if (e.key === 'Escape' && (state.drawer || state.search || state.zoom)) {
    state.drawer = '';
    state.search = false;
    state.zoom = null;
    render();
  }
});

render();
