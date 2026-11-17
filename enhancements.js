(()=>{const root=document.documentElement,store=document.body;let sceneTimer;window.setupBrandCampaign=()=>{clearTimeout(sceneTimer);root.querySelectorAll('.zm-bag-menu').forEach(m=>m.open=false);window.setupZemaHome?.();  const campaign=root.querySelector('.zm-hero');if(!campaign)return;
  const motionButton=root.querySelector('.zm-motion-control');
  const reduceMotion=matchMedia('(prefers-reduced-motion: reduce)').matches;
  let scene=0,playing=!reduceMotion;
  function showScene(next){scene=next;campaign.dataset.scene=scene?'detail':'lifestyle';root.querySelector('.zm-hero-copy .zm-primary').onclick=()=>navigate('shop','all');root.querySelector('.zm-hero h1').innerHTML=scene?'Small in scale.<br><em>Distinctive by nature.</em>':'A quiet statement.<br><em>Everywhere you go.</em>';root.querySelector('.zm-hero-copy .zm-description').textContent=scene?'':'Distinctive pieces. Effortless style.';root.querySelector('.zm-hero-copy .zm-eyebrow').textContent=scene?'THE ZEMA COLLECTION':'THE DAYLIGHT MOOD';root.querySelector('.zm-hero-copy .zm-primary').innerHTML=scene?'Explore the Collection <span>↗</span>':'Discover the Collection <span>↗</span>';root.querySelectorAll('[data-scene-choice]').forEach(button=>button.setAttribute('aria-pressed',String(Number(button.dataset.sceneChoice)===scene)));}
  function scheduleScene(){clearTimeout(sceneTimer);if(playing&&!document.hidden)sceneTimer=setTimeout(()=>{showScene(1-scene);scheduleScene();},6000);}
  root.querySelectorAll('[data-scene-choice]').forEach(button=>button.addEventListener('click',()=>{showScene(Number(button.dataset.sceneChoice));scheduleScene();}));
  motionButton.addEventListener('click',()=>{playing=!playing;motionButton.textContent=playing?'Ⅱ':'▶';motionButton.setAttribute('aria-label',playing?'Pause slideshow':'Play slideshow');scheduleScene();});
  
  root.querySelector('.zm-ribbon-toggle').addEventListener('click',event=>{const paused=root.querySelector('.zm-brand-ribbon').classList.toggle('is-paused');event.currentTarget.textContent=paused?'▶':'Ⅱ';event.currentTarget.setAttribute('aria-label',paused?'Play moving brand message':'Pause moving brand message');});
  showScene(0);scheduleScene();
};window.setupBrandCampaign();
  let language=readStore('language','en');state.lang=language;
  const dictionary={...(window.ZEMA_HOME_AR||{}),'Skip to content':'انتقلي للمحتوى','Shopping Bag':'حقيبة التسوق','Proceed to Checkout':'إتمام الطلب','PROCEED TO CHECKOUT':'إتمام الطلب','Enter a valid Egyptian mobile number':'أدخلي رقم موبايل مصري صحيح','Search for your next everyday piece...':'ابحثي عن قطعتكِ القادمة…','Privacy Policy':'سياسة الخصوصية',"We will confirm the estimated delivery date for your address before dispatch. Shipping charges will be confirmed with you before your order is finalized.":"سنؤكد لكِ موعد التوصيل المتوقع لعنوانكِ قبل الشحن. وتُؤكد تكلفة الشحن معكِ قبل إتمام الطلب.",'Shop the Collection ↗':'تسوّقي المجموعة ↖','FREE SHIPPING OVER 2,500 EGP':'شحن مجاني للطلبات فوق ٢٬٥٠٠ جنيه','Account':'الحساب',"Items":"المنتجات","Items total":"إجمالي المنتجات","Total":"الإجمالي","Final total":"الإجمالي النهائي","Send Order Request":"إرسال طلب الشراء","Shipping to be confirmed":"الشحن يُؤكد لاحقًا","Awaiting shipping confirmation":"بانتظار تأكيد الشحن","Awaiting confirmation":"بانتظار التأكيد","To be confirmed":"يُؤكد لاحقًا","ORDER REQUEST RECEIVED":"تم استلام طلبكِ","Thank you for your request":"شكرًا لاختياركِ زيما","Reference:":"رقم الطلب:","Print / Save PDF":"طباعة / حفظ PDF","Continue Shopping":"متابعة التسوق","Your request is saved. We will confirm availability, delivery costs and your final total before dispatch.":"تم حفظ طلبكِ. سنؤكد التوفر وتكلفة الشحن والإجمالي النهائي قبل الإرسال.","Shipping is not included yet. ZEMA will confirm the delivery charge and final total with you before your order is finalized or dispatched.":"سعر الشحن غير مضاف بعد. ستؤكد زيما معكِ تكلفة التوصيل والإجمالي قبل إتمام الطلب وشحنه.",
'Email address (optional)':'البريد الإلكتروني (اختياري)','For order receipts and delivery updates only.':'لإشعارات الطلب والتوصيل فقط.','Cash on Delivery':'الدفع عند الاستلام',
'Sign up for email updates on new collections and restocks.':'اشتركي ليصلكِ جديد المجموعات والقطع المتاحة مجددًا.','Subscribe →':'اشتراك ←','Timeless style.':'أناقة لا يحدّها وقت.','Made for your everyday.':'صُممت لترافقكِ كل يوم.','Timeless style.<br>Made for your everyday.':'أناقة لا يحدّها وقت.<br>صُممت لترافقكِ كل يوم.','SOLD OUT':'نفد من المخزون','Currently sold out':'نفد من المخزون حالياً','Privacy':'الخصوصية',
  'COMPLETE THE LOOK': 'أكملي إطلالتكِ',
  'Add to Cart': 'إضافة للسلة',
  'Buy It Now': 'شراء فوري',
  'ADD TO CART': 'إضافة للسلة',
  'BUY IT NOW': 'شراء فوري',
  'About Us': 'عن زيما',
  'ABOUT US': 'عن زيما',
  'About': 'عن زيما',
  'Our Story': 'قصتنا',
  'OUR STORY': 'قصتنا',
  'Story': 'قصتنا',
  'Read Our Story': 'اقرئي قصتنا',
  'Our Beginning': 'البداية والفكرة',
  'Design Philosophy': 'فلسفتنا في التصميم',
  'The ZEMA Experience': 'تجربة متكاملة',
  'The Experience': 'تجربة متكاملة',
  '+ ADD': '+ إضافة',
  'ADD': 'إضافة',
  '+ Add': '+ إضافة',
  'Add': 'إضافة',
  '+ QUICK ADD': '+ إضافة سريعة',
  'QUICK ADD': 'إضافة سريعة',
  '+ Quick Add': '+ إضافة سريعة',
  'Quick Add': 'إضافة سريعة',
  'Brand Highlights': 'أبرز مزايا دار زيما',
  'You May Also Like': 'قد يعجبكِ أيضاً',
  'CURATED SELECTION': 'مختارات مميزة',
  'Similar pieces to consider for your collection.': 'قطع منتقاة بعناية تكمّل مجموعتكِ.',
  'YOU MAY ALSO LIKE': 'قد يعجبكِ أيضاً',
  'CURATED COMBINATION': 'تنسيق متناسق وموصى به',
  'Pair It With': 'نسّقيها مع',
  'Frequently Bought Together': 'غالباً ما يُشترى معاً',
  'Complete the look with harmoniously matched pieces.': 'أكملي إطلالتك بتنسيق القطع الأكثر انسجاماً معاً.',
  'This Item': 'هذه القطعة',
  'Matching Piece': 'قطعة مكملة',
  '+ Add': '+ إضافة',
  'The Complete Look ✦': 'الإطلالة المتكاملة ✦',
  'The Complete Look on Model ✦': 'الإطلالة المتكاملة على العارضة ✦',
  'Daylight Taupe': 'أناقة النهار (توب)',
  'Parisian Noir': 'الأسود الباريسي (نوار)',
  'Bordeaux Elegance': 'فخامة البوردو',
  'LOOK 01 · CASUAL REFINEMENT': 'إطلالة ٠١ · أناقة نهارية هادئة',
  'LOOK 02 · ARCHITECTURAL NOIR': 'إطلالة ٠٢ · سحر المساء الكلاسيكي',
  'LOOK 03 · MODERN MINIMALIST': 'إطلالة ٠٣ · فخامة عصرية متقنة',
  'Select at least one piece': 'اختاري قطعة واحدة على الأقل',
  'The Complete Look': 'الإطلالة المتكاملة',
  'See The Complete Look on Model ↗': 'شاهدي الإطلالة كاملة على العارضة ↖',
  'EDITORIAL STYLING': 'تنسيق أزياء حصري',
  'ON MODEL · THE COMPLETE LOOK': 'على العارضة · الإطلالة المتكاملة',
  'Harmoniously curated pieces designed to elevate your everyday silhouette.': 'قطع منسجمة بعناية لتبرز أناقة إطلالتكِ اليومية.',
  'Full Ensemble:': 'إجمالي الإطلالة:',
  'Add Complete Look to Bag →': 'إضافة الإطلالة كاملة إلى السلة ←',
  'CURATED SIGNATURE SET': 'طقم حصري متناسق',
  'Harmoniously paired essentials for the modern woman.': 'قطع أساسية منسجمة بعناية للمرأة العصرية.',
  'Add Full Look to Bag →': 'إضافة الإطلالة كاملة إلى السلة ←',
  'Add All 3 to Bag →': 'إضافة الطقم كاملاً إلى السلة ←',
  'Home':'الرئيسية','Shop':'تسوق','Bags':'الشنط','All Bags':'كل الشنط','Wallets':'المحافظ','Best Sellers':'الأكثر مبيعًا','Sale':'التخفيضات','All Pieces':'كل القطع','Shoulder Bags':'شنط كتف','Handbags':'شنط يد','Crossbody Bags':'شنط كروس','The Collection':'المجموعة','The Sale Edit':'مختارات التخفيضات','THE DAYLIGHT MOOD':'أناقة النهار','THE ZEMA COLLECTION':'مجموعة زيما','THE ZEMA CAMPAIGN':'عالم زيما','A quiet statement.':'حضور هادئ.','Everywhere you go.':'أينما ذهبتِ.','Small in scale.':'حجم صغير.','Distinctive by nature.':'حضور لا يُنسى.','Distinctive pieces. Effortless style.':'قطع مميزة. أناقة ببساطة.','Discover the Collection':'اكتشفي المجموعة','Explore the Collection':'اكتشفي المجموعة','THE EVERYDAY EDIT':'أناقة كل يوم','CONSIDERED. DISTINCTIVE. ZEMA.':'تفاصيل مدروسة. حضور مميز. زيما.','Explore All Pieces ↗':'اكتشفي كل القطع ↖','The Classic Shoulder Bag':'شنطة الكتف كلاسيك','The Aria Structured Bag':'شنطة اليد آريا','The Mira Mini Crossbody':'شنطة ميرا ميني كروس','The Naya Zip Wallet':'محفظة نايا بسحّاب','Warm Taupe':'تاوب دافئ','Camel':'جملي','Ivory':'عاجي','Dark Brown':'بني داكن','SALE':'تخفيض','THE EVERYDAY MUSE':'إلهام كل يوم','Elegance,':'أناقة،','in your element.':'على طبيعتكِ.','Considered shapes.':'تصاميم مدروسة.','Distinctive details. Entirely yours.':'تفاصيل مميزة. تعبر عنكِ.','Explore the Edit ↗':'اكتشفي المختارات ↖','Everyday ease ↗':'راحة كل يوم ↖','Structured elegance ↗':'أناقة متقنة ↖','Freedom in motion ↗':'حرية الحركة ↖','Explore':'اكتشفي','Client Services':'خدمة العملاء','Customer Care':'خدمة العملاء','About ZEMA':'عن زيما','Shipping & Delivery':'الشحن والتوصيل','Returns & Exchanges':'الاستبدال والاسترجاع','FAQs':'الأسئلة الشائعة','Join the ZEMA Circle':'كوني أقرب إلى زيما','Your email address':'بريدك الإلكتروني','Enter your email':'أدخلي بريدك الإلكتروني','Collection updates, thoughtfully selected.':'مختارات بعناية من جديد مجموعاتنا.','FREE SHIPPING ON ORDERS OVER 2,500 EGP':'شحن مجاني للطلبات فوق ٢٬٥٠٠ جنيه','THE ZEMA COLLECTION':'مجموعة زيما','The Classic':'كلاسيك','Shoulder Bag':'شنطة كتف','COLOR — WARM TAUPE':'اللون — تاوب دافئ','Add to Shopping Bag':'أضيفي إلى حقيبة التسوق','Buy Now ↗':'اشتري الآن ↖','Delivery across Egypt':'توصيل لجميع أنحاء مصر','Free shipping on orders over 2,500 EGP.':'شحن مجاني للطلبات فوق ٢٬٥٠٠ جنيه.','Dimensions & Fit':'المقاسات والسعة','Materials & Details':'الخامات والتفاصيل','Care Guide':'دليل العناية','Delivery & Returns':'التوصيل والاسترجاع','Confirmed product measurements will appear here.':'ستظهر هنا مقاسات المنتج بعد تأكيدها.','Warm taupe finish · Gold-tone hardware.':'لون تاوب دافئ · تفاصيل معدنية ذهبية.','Full material information will be added with the product specifications.':'ستُضاف تفاصيل الخامات مع مواصفات المنتج.','Care instructions will match the confirmed material of this piece.':'ستُضاف إرشادات العناية المناسبة لخامة هذه القطعة.','Add to Bag':'أضيفي للحقيبة','Close ×':'إغلاق ×','A softly curved silhouette with a generous shoulder strap, warm taupe finish and gold-tone details. Considered for your everyday.':'تصميم بانحناءات ناعمة وحزام كتف مريح، بلون تاوب دافئ وتفاصيل ذهبية. يناسب يومكِ.','Orders over 2,500 EGP receive free shipping. For other orders, delivery charges are confirmed for your governorate before dispatch. Returns information is available before you finalize your order.':'شحن مجاني للطلبات فوق ٢٬٥٠٠ جنيه. لباقي الطلبات، تُؤكّد تكلفة التوصيل لمحافظتكِ قبل الشحن، وتتوفر سياسة الاسترجاع قبل تأكيد الطلب.','Preview only — no email has been submitted.':'هذه معاينة فقط — لم يُرسل البريد الإلكتروني.','© 2026 ZEMA Maison — Timeless Style, Modern Luxury':'© ٢٠٢٦ زيما ميزون — أناقة خالدة، فخامة عصرية'};
  Object.assign(dictionary,{"Your shopping bag is empty.": "حقيبة التسوق فارغة.", "Explore the Collection": "اكتشفي المجموعة", "Complete Your Order": "أكملي طلبكِ", "Full Name": "الاسم بالكامل", "Mobile Phone": "رقم الموبايل", "Governorate": "المحافظة", "Select your governorate": "اختاري المحافظة", "Detailed Address": "العنوان بالتفصيل", "Order Notes (optional)": "ملاحظات الطلب (اختياري)", "Cash on Delivery": "الدفع عند الاستلام", "We will contact you to confirm availability, delivery and the final total before dispatch.": "سنتواصل معكِ لتأكيد التوفر والتوصيل والإجمالي النهائي قبل الشحن.", "Send Order Request": "إرسال طلب الشراء", "Save Order Draft": "حفظ مسودة الطلب", "Prepare WhatsApp Order": "تجهيز طلب واتساب", "Subtotal": "الإجمالي الفرعي", "Shipping": "الشحن", "Total": "الإجمالي", "Free shipping threshold reached.": "طلبكِ مؤهل للشحن المجاني.", "Your Bag": "حقيبة التسوق", "Checkout": "إتمام الطلب", "Continue Shopping": "متابعة التسوق", "← Continue Shopping": "متابعة التسوق ←", "Privacy": "الخصوصية", "Your Orders": "طلباتكِ", "Accessories": "الإكسسوارات", "Shipping to be confirmed": "يُؤكد سعر الشحن لاحقًا", "Recently Viewed": "شاهدتِ مؤخرًا", "Subscribe": "اشتركي", "Sold Out": "نفد المخزون", "Wishlist": "المفضلة", "Remove": "إزالة", "Order Summary": "ملخص الطلب", "I agree to the": "أوافق على", "privacy information": "بيان الخصوصية", "and understand that unpriced shipping will be confirmed before my order is finalized.": "وأفهم أن تكلفة الشحن غير المحددة ستُؤكد قبل إتمام طلبي."});
Object.assign(dictionary,{"New Arrivals": "وصل حديثًا", "All Collections": "كل المجموعات", "Collection": "المجموعة", "Featured": "مختارات زيما", "Sort by": "ترتيب حسب", "Price: low to high": "السعر من الأقل للأعلى", "Price: high to low": "السعر من الأعلى للأقل", "Name": "الاسم", "Your Wishlist": "المفضلة", "Save your favorite pieces with the heart icon.": "احفظي قطعكِ المفضلة بالضغط على القلب.", "Explore the collection →": "اكتشفي المجموعة ←", "No pieces in this selection yet.": "لا توجد قطع في هذا القسم حاليًا.", "View all collections": "عرض كل المجموعات", "Currently sold out": "نفدت الكمية حاليًا", "Shipping confirmed before dispatch.": "نؤكد تفاصيل الشحن قبل إرسال الطلب.", "Shipping information ↗": "معلومات الشحن ↖", "Contact ZEMA for exact measurements and fit before ordering.": "تواصلي مع زيما لمعرفة المقاسات الدقيقة قبل الطلب.", "Contact ZEMA for care advice specific to this piece.": "تواصلي مع زيما لمعرفة إرشادات العناية بهذه القطعة.", "Your bag is empty": "حقيبة التسوق فارغة", "Choose your pieces before checking out.": "اختاري قطعكِ قبل إتمام الطلب.", "View Order": "عرض الطلب", "Refresh Status": "تحديث حالة الطلب", "No orders saved on this device yet.": "لا توجد طلبات محفوظة على هذا الجهاز.", "Orders and drafts saved in this browser. Keep your reference if you change devices or clear browser data.": "طلبات ومسودات محفوظة في هذا المتصفح. احتفظي برقم الطلب عند تغيير الجهاز أو مسح البيانات.", "Delivery available": "التوصيل متاح", "CUSTOMER CARE": "خدمة العملاء", "ZEMA COLLECTION": "مجموعة زيما", "THE ZEMA STORY": "حكاية زيما", "A More Thoughtful Approach to Everyday Luxury": "فخامة يومية باختيارات مدروسة", "Proudly curated in Egypt with an international luxury aesthetic.": "مختارات من مصر بروح أناقة عالمية.", "ZEMA was born from a simple conviction: an everyday handbag is more than an accessory. It is a companion to your day, carrying what matters with quiet grace and effortless balance.": "بدأت زيما بفكرة بسيطة، حقيبة كل يوم رفيقة ليومكِ، تحمل ما تحتاجينه بأناقة وراحة.", "In a world of fast trends and overwhelming choices, we curate timeless, architectural leather pieces crafted to stand apart. We balance beautiful proportions, rich neutral tones, and accessible prices for modern women.": "وسط الصيحات المتغيرة والاختيارات الكثيرة، نختار قطعًا بتصاميم مميزة وألوان محايدة تجمع الأناقة والعملية والأسعار المناسبة.", "We deliver across Egypt, subject to service coverage for your address.": "نوصل لجميع أنحاء مصر حسب نطاق خدمة التوصيل لعنوانكِ.", "When a delivery price is available, checkout calculates it for your governorate. Otherwise you will see “To be confirmed”. That does not mean free shipping. We confirm the charge and final total before your order is finalized or dispatched.": "عندما يتحدد سعر الشحن، يظهر حسب محافظتكِ عند إتمام الطلب. وإذا لم يتحدد بعد، نؤكد معكِ التكلفة والإجمالي قبل إتمام الطلب وإرساله.", "Clear this browser's saved store data": "مسح بيانات المتجر المحفوظة في هذا المتصفح", "Frequently Asked Questions": "الأسئلة الشائعة", "How do I place an order?": "كيف أطلب؟", "How much is shipping?": "ما تكلفة الشحن؟", "How can I pay?": "كيف أدفع؟", "Where is my order?": "أين طلبي؟", "Are other colors available?": "هل توجد ألوان أخرى؟", "Cash on delivery. Delivery details are confirmed before dispatch.": "الدفع عند الاستلام. نؤكد تفاصيل التوصيل قبل الشحن.", "Choose your governorate at checkout. If its price is pending, ZEMA confirms the charge before the order is finalized.": "اختاري المحافظة عند إتمام الطلب. إذا لم يتحدد سعر الشحن بعد، ستؤكده زيما معكِ قبل إتمام الطلب.", "Each product page lists its currently configured colors. Only colors with matching product images are offered.": "تعرض صفحة كل منتج ألوانه المتاحة بصورها المطابقة.", "Open Your Orders on the same browser used to order. Keep your reference for any inquiry.": "افتحي الطلبات من المتصفح الذي استخدمتِه للشراء، واحتفظي برقم الطلب للاستفسارات.", "Add your pieces to the bag and complete your delivery details. The confirmation screen clearly shows whether the request was received by our server or is an unsent WhatsApp draft.": "أضيفي القطع إلى الحقيبة وأكملي بيانات التوصيل. ستوضح النتيجة هل استلمنا طلبكِ أم أنه مسودة واتساب لم تُرسل.", "Online ordering is being prepared. You can save your order draft; direct sending becomes available when ZEMA adds its contact number.": "يجري تجهيز الطلب عبر الموقع. يمكنكِ حفظ مسودة الطلب لحين إتاحة إرسالها.", "Search": "بحث", "Search products...": "ابحثي عن المنتجات…", "Search products": "ابحثي عن المنتجات", "Search by name or color...": "ابحثي بالاسم أو اللون…", "Available stock limit reached.": "وصلتِ للكمية المتاحة.", "Order status updated.": "تم تحديث حالة الطلب.", "FREE": "مجاني", "Confirmed": "تم التأكيد", "Processing": "جارٍ التجهيز", "Shipped": "تم الشحن", "Delivered": "تم التسليم", "Cancelled": "تم الإلغاء", "Cairo": "القاهرة", "Giza": "الجيزة", "Alexandria": "الإسكندرية", "Qalyubia": "القليوبية", "Dakahlia": "الدقهلية", "Sharqia": "الشرقية", "Gharbia": "الغربية", "Monufia": "المنوفية", "Beheira": "البحيرة", "Kafr El Sheikh": "كفر الشيخ", "Damietta": "دمياط", "Port Said": "بورسعيد", "Ismailia": "الإسماعيلية", "Suez": "السويس", "Fayoum": "الفيوم", "Beni Suef": "بني سويف", "Minya": "المنيا", "Assiut": "أسيوط", "Sohag": "سوهاج", "Qena": "قنا", "Luxor": "الأقصر", "Aswan": "أسوان", "Red Sea": "البحر الأحمر", "New Valley": "الوادي الجديد", "Matrouh": "مطروح", "North Sinai": "شمال سيناء", "South Sinai": "جنوب سيناء", "The Classic Shoulder Bag": "حقيبة كتف كلاسيكية", "A softly curved shoulder silhouette crafted from supple pebble-grain leather with gold-tone hardware.": "تصميم كتف بانحناءات ناعمة وجلد محبب وتفاصيل معدنية ذهبية.", "Warm Taupe": "توب دافئ", "The Aria Structured Bag": "حقيبة يد كلاسيكية مهندمة", "A timeless architectural top-handle silhouette with reinforced corners and detachable strap.": "تصميم شنطة يد بخطوط هندسية وزوايا مدعمة وحزام قابل للفصل.", "Camel": "جملي", "The Noa Everyday Hobo": "حقيبة هوبو انسيابية", "A relaxed silhouette with a fluid drape, ergonomic carry handle, and magnetic top closure.": "تصميم مرن بانسدال ناعم ومقبض مريح وإغلاق مغناطيسي.", "Chocolate": "شوكولاتة", "The Mira Mini Crossbody": "حقيبة كروس صغيرة", "Compact everyday essentials bag with adjustable cross-body strap and polished brass zipper.": "شنطة صغيرة للأساسيات اليومية بحزام كروس قابل للتعديل وسحّاب معدني.", "Ivory": "عاجي", "The Sienna City Tote": "حقيبة تسوق سيتي توت", "Generous everyday work tote designed to hold a 13-inch laptop, planner, and daily essentials.": "شنطة عمل واسعة تتسع للابتوب 13 بوصة والمفكرة والأساسيات اليومية.", "Cognac": "كونياك", "The Liora Shoulder Bag": "حقيبة كتف عنابي فاخرة", "Rich deep burgundy glazed shoulder silhouette that brings an editorial statement to any outfit.": "شنطة كتف بلون نبيتي غني ولمسة لامعة تضيف حضورًا مميزًا لإطلالتكِ.", "Burgundy": "بورغندي", "The Naya Zip Wallet": "محفظة بسحاب دائري", "Compact zip-around wallet with eight card slots, full billfold sleeve, and central coin pocket.": "محفظة بسحّاب محيطي وثماني فتحات للبطاقات ومساحة للنقود وجيب للعملات.", "Dark Brown": "بني داكن", "The Pearl Bag Charm": "تعليقة حقيبة لؤلؤية", "Hand-assembled delicate gold-tone lobster charm with simulated organic pearls.": "تعليقة رقيقة بتفاصيل ذهبية وحبات لؤلؤ صناعي.", "Gold": "ذهبي", "We use your name, phone number, delivery address and order details to process your order and arrange delivery. If you provide an email address, we also use it for order receipts and status updates through our email provider. Marketing emails require your separate optional signup.": "نستخدم اسمكِ وهاتفكِ وعنوانكِ وبيانات الطلب لتجهيزه وتوصيله. إذا أدخلتِ بريدكِ، نستخدمه لإشعارات الطلب عبر مزود البريد. رسائل التسويق تتطلب اشتراككِ الاختياري المنفصل.", "Your bag, favorites, recently viewed pieces and order receipts are saved in this browser. Clearing browser storage removes these local copies. When you submit an order to our store server, it is also retained in the store database for fulfillment.": "تُحفظ الحقيبة والمفضلة والقطع التي شاهدتِها وإيصالات الطلب محليًا في المتصفح. مسح بياناته يزيل النسخ المحلية. والطلبات المُرسلة إلى المتجر تُحفظ أيضًا في قاعدة بياناته لتنفيذها.", "If you choose WhatsApp, your order details are shared with WhatsApp and the store when you send the message. Opening WhatsApp alone does not send your order.": "عند إرسال الطلب عبر واتساب، تُشارك بياناته مع واتساب والمتجر. فتح واتساب وحده لا يرسل الطلب.", "You can request access to or deletion of your order data by contacting ZEMA with your order reference. This site does not collect payment-card details.": "يمكنكِ طلب الاطلاع على بيانات طلبكِ أو حذفها بالتواصل مع زيما برقم الطلب. لا يجمع الموقع بيانات البطاقات البنكية.", "Returns or exchanges within 14 days of receipt, subject to legal exceptions. Defective items: replacement or refund within 30 days. ZEMA covers the costs of exercising statutory return rights. See Returns & Exchanges for full details.": "استبدال أو استرجاع خلال 14 يومًا من الاستلام وفق الاستثناءات القانونية. وللقطع المعيبة، استبدال أو استرداد خلال 30 يومًا. تتحمل زيما تكاليف ممارسة الحق القانوني. راجعي سياسة الاستبدال والاسترجاع للتفاصيل."});
const originals=new WeakMap();
  function translated(text) {
    if (dictionary[text]) return dictionary[text];
    if (text.startsWith('COLOR — ')) {
      const color = text.slice(8);
      const key = Object.keys(dictionary).find(key => key.toUpperCase() === color);
      return 'اللون — ' + (dictionary[key] || color);
    }
    if (/^\d+ considered pieces$/.test(text)) return text.replace(' considered pieces', ' قطع مختارة');
    if (/^\d+ saved pieces$/.test(text)) return text.replace(' saved pieces', ' قطع محفوظة');
    if (/^On orders over /.test(text)) return 'للطلبات فوق ' + text.replace('On orders over ', '').replace('EGP', 'جنيه');
    if (/^Free shipping on orders over /.test(text)) return 'شحن مجاني للطلبات فوق ' + text.replace('Free shipping on orders over ', '').replace('EGP', 'جنيه');
    if (text.includes('SCULPTED FOR EVERYDAY')) return 'أناقة لكل يوم · تفاصيل تصنع الاختلاف · زيما ميزون · ';
    for (const separator of [' — ', ' · ']) {
      if (text.includes(separator)) return text.split(separator).map(translated).join(separator);
    }
    if (/^Shopping Bag \(\d+\)$/.test(text)) return text.replace('Shopping Bag', 'حقيبة التسوق');
    if (/^Qty \d+$/.test(text)) return text.replace('Qty', 'الكمية');
    return text.replace(/\bEGP\b/g, 'جنيه');
  }
  const originalAttributes = new WeakMap();
  function localize(){
    observer.disconnect();
    const walker=document.createTreeWalker(store,NodeFilter.SHOW_TEXT);let node;
    while(node=walker.nextNode()){if(node.parentElement.closest('script,style,[data-language],input,textarea,.admin-panel'))continue;const current=node.textContent.trim();if(!current)continue;let original=originals.get(node);if(!original||current!==translated(original)&&current!==original)original=current;originals.set(node,original);const leading=node.textContent.match(/^\s*/)[0],trailing=node.textContent.match(/\s*$/)[0];node.textContent=leading+(language==='ar'?translated(original):original)+trailing;}
    store.querySelectorAll('[placeholder], [title]').forEach(element => {
      let attributes = originalAttributes.get(element);
      if (!attributes) {
        attributes = {};
        for (const name of ['placeholder', 'title']) {
          if (element.hasAttribute(name)) attributes[name] = element.getAttribute(name);
        }
        originalAttributes.set(element, attributes);
      }
      for (const [name, original] of Object.entries(attributes)) {
        element.setAttribute(name, language === 'ar' ? translated(original) : original);
      }
    });
    document.documentElement.dir=language==='ar'?'rtl':'ltr';document.documentElement.lang=language;store.dir=language==='ar'?'rtl':'ltr';store.lang=language;store.classList.toggle('zm-ar',language==='ar');
    root.querySelectorAll('[data-language]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.language===language)));
    root.querySelector('#zm-circle-email').placeholder=language==='ar'?'أدخلي بريدك الإلكتروني':'Enter your email';
    observer.observe(store,{childList:true,subtree:true,characterData:true});
  }
  const observer=new MutationObserver(localize);
  root.querySelectorAll('[data-language]').forEach(button=>button.addEventListener('click',()=>{const values = [...document.querySelectorAll('#appView input, #appView textarea, #appView select')].map(element => ({name:element.name,value:element.value,checked:element.checked}));
      language=button.dataset.language;state.lang=language;writeStore('language',language);
      renderView();renderCart();
      for (const saved of values) {
        const element = [...document.querySelectorAll('#appView input, #appView textarea, #appView select')].find(element => element.name && element.name === saved.name);
        if (element) { element.value=saved.value; element.checked=saved.checked; }
      }
      localize();}));
  localize();

})();

function openSocial(network){const url=config.socialLinks?.[network];if(url&&/^https:\/\//.test(url)){window.open(url,'_blank','noopener,noreferrer');}else toast(state.lang==='ar'?'سيتم إضافة رابط حساب زيما الرسمي قريبًا.':'Official ZEMA profile will be available soon.');}
async function subscribeNewsletter(form){const input=form.querySelector('input[type=email]'),note=form.querySelector('.zm-signup-note'),button=form.querySelector('button');button.disabled=true;try{if(!apiOnline){note.textContent=state.lang==='ar'?'الاشتراك البريدي غير متاح حاليًا. لم يتم إرسال بريدك.':'Email signup is not available yet. Your email was not submitted.';return;}await api('api/newsletter','POST',{email:input.value});note.textContent=state.lang==='ar'?'تم تسجيل بريدك في قائمة زيما.':'You are on the ZEMA list.';form.reset();}catch(error){note.textContent=state.lang==='ar'?'تعذر حفظ اشتراكك. حاولي مرة أخرى.':'Unable to save your subscription. Please try again.';}finally{button.disabled=false;}}
