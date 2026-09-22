import{u as i,r as d,j as e,L as x,a as p,i as N,f as v,e as m}from"./index-uamL4pK8.js";
import{S as w,a as y,F as k,X as S}from"./SiteChrome-vAcelVMJ.js";
import{P as u}from"./ProductCard-Di7jG7K4.js";

// 1. VIP Newsletter Section
function E(){
  const{t:s,dir:t,lang:l}=i(),isAr=l==="ar",[r,setR]=d.useState(""),[n,setC]=d.useState("idle");
  const h=o=>{o.preventDefault();if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(r)){setC("err");return}setC("ok");setR("")};
  return e.jsx("section",{className:"border-t hairline bg-[#161616] text-[#eae7e0] select-none",dir:t,children:
    e.jsxs("div",{className:"mx-auto max-w-3xl px-5 lg:px-12 py-16 lg:py-20 text-center",children:[
      e.jsx("p",{className:"text-[10px] tracking-[0.3em] uppercase text-accent font-semibold mb-3",children:isAr?"نادي زِيما للأناقة العملية":"ZEMA PRIVÉ CIRCLE"}),
      e.jsx("h2",{className:"display-serif text-3xl md:text-4xl font-bold tracking-tight",children:isAr?"انضمي لمجتمع زِيما الحصري":"Join the ZEMA Circle"}),
      e.jsx("p",{className:"mt-3 text-xs md:text-sm text-stone-400 leading-relaxed max-w-lg mx-auto",children:isAr?"احصلي على كود خصم فوري 10% (ZEMA10) على أول طلب وإشعار مسبق بالإصدارات المحدودة.":"Receive an instant 10% privilege code (ZEMA10) on your first purchase and early access to limited editions."}),
      e.jsxs("form",{onSubmit:h,className:"mt-8 flex max-w-md mx-auto gap-2",children:[
        e.jsx("input",{type:"email",placeholder:isAr?"بريدك الإلكتروني":"Your email address",value:r,onChange:o=>setR(o.target.value),required:!0,className:"flex-1 bg-white/5 border border-white/10 px-4 py-3 text-xs focus:outline-none focus:border-accent text-white placeholder:text-stone-500 rounded-lg"}),
        e.jsx("button",{type:"submit",className:"bg-accent text-accent-foreground px-6 py-3 text-xs font-bold uppercase tracking-wider rounded-lg hover:opacity-90 transition-opacity whitespace-nowrap cursor-pointer",children:isAr?"انضمام":"JOIN"})
      ]}),
      n==="ok"&&e.jsx("p",{className:"mt-3 text-xs text-emerald-400 font-medium",children:isAr?"تم اشتراكك بنجاح! استخدمي كود ZEMA10 عند إتمام الطلب.":"Welcome! Use code ZEMA10 at checkout."}),
      n==="err"&&e.jsx("p",{className:"mt-3 text-xs text-rose-400 font-medium",children:isAr?"يرجى إدخال بريد إلكتروني صحيح":"Please enter a valid email"})
    ]})
  })
}

// 2. Main Page Component (D)

// Testimonials Component (T)
function T(){
  const{lang}=i(),isAr=lang==="ar";
  const reviews = [
    {
      id: 1,
      name: isAr ? "مريم القاضي" : "Mariam El-Kady",
      city: isAr ? "القاهرة" : "Cairo",
      product: isAr ? "حقيبة كلاسيك جلد طبيعي" : "Classic Leather Bag",
      date: isAr ? "منذ أسبوعين" : "2 weeks ago",
      text: isAr ? "جودة الحقيبة والجلد فاقت توقعاتي تماماً، والتقفيل متقن لأدق التفاصيل. تجربة المعاينة مع المندوب قبل الدفع أعطتني راحة وثقة كبيرة." : "The leather quality and finishing exceeded my expectations. Inspecting the order with the courier before paying gave me huge confidence."
    },
    {
      id: 2,
      name: isAr ? "أحمد الشناوي" : "Ahmed El-Shennawy",
      city: isAr ? "الإسكندرية" : "Alexandria",
      product: isAr ? "ساعة أوتوماتيك فاخرة" : "Automatic Luxury Watch",
      date: isAr ? "منذ 3 أسابيع" : "3 weeks ago",
      text: isAr ? "الساعة وصلت في علبة مخملية فاخرة جداً تنفع هدية راقية. الوزن والاهتمام بالتفاصيل يضاهي الماركات السويسرية، وسرعة التوصيل ممتازة." : "The watch arrived in signature luxury velvet packaging. The weight and craftsmanship rival Swiss brands, and delivery was exceptionally fast."
    },
    {
      id: 3,
      name: isAr ? "نور المهدي" : "Nour El-Mahdy",
      city: isAr ? "الشيخ زايد" : "Sheikh Zayed",
      product: isAr ? "نظارة شمسية هافانا" : "Havana Sunglasses",
      date: isAr ? "منذ 4 أيام" : "4 days ago",
      text: isAr ? "النظارة خفيفة جداً ومريحة للعين وخاماتها صلبة وأنيقة. خدمة العملاء على الواتساب راقية ومتعاونة لأقصى درجة حتى استلام الشحنة." : "The sunglasses are lightweight, comfortable, and stylish. Customer support on WhatsApp was extremely helpful throughout delivery."
    }
  ];

  return e.jsx("section",{id:"testimonials",className:"border-b hairline bg-background py-16 lg:py-24 select-none",children:
    e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12",children:[
      e.jsxs("div",{className:"text-center mb-12 md:mb-16 space-y-2",children:[
        e.jsx("p",{className:"text-[10px] tracking-[0.3em] uppercase text-accent font-semibold",children:isAr?"آراء العملاء":"CLIENT VOICES"}),
        e.jsx("h2",{className:"display-serif text-2xl sm:text-3xl md:text-4xl font-bold tracking-tight",children:isAr?"ثقة تميزت بها ZEMA":"Experiences That Define Us"}),
        e.jsx("p",{className:"text-xs sm:text-sm text-muted-foreground max-w-xl mx-auto font-light",children:isAr?"انطباعات حقيقية من عملائنا بعد تجربة المعاينة واستلام القطع الفاخرة":"Authentic reflections from clients across Egypt after inspecting and receiving their curated pieces."})
      ]}),
      e.jsx("div",{className:"grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8",children:
        reviews.map(r=>e.jsxs("div",{key:r.id,className:"rounded-2xl border hairline bg-card/40 p-6 md:p-8 flex flex-col justify-between hover:border-accent/40 transition-colors shadow-sm",children:[
          e.jsxs("div",{className:"space-y-4",children:[
            e.jsxs("div",{className:"flex items-center justify-between",children:[
              e.jsx("div",{className:"flex gap-1 text-accent text-sm tracking-widest",children:"★★★★★"}),
              e.jsx("span",{className:"text-[10px] text-muted-foreground ltr-num",children:r.date})
            ]}),
            e.jsxs("p",{className:"text-xs sm:text-sm leading-relaxed text-foreground/85 font-light italic",children:["“",r.text,"”"]})
          ]}),
          e.jsxs("div",{className:"mt-6 pt-4 border-t hairline flex items-center justify-between",children:[
            e.jsxs("div",{children:[
              e.jsx("h4",{className:"text-xs font-bold text-foreground",children:r.name}),
              e.jsxs("p",{className:"text-[10px] text-muted-foreground",children:[r.city," · ",r.product]})
            ]}),
            e.jsxs("span",{className:"inline-flex items-center gap-1 text-[10px] text-emerald-400 font-medium bg-emerald-500/10 border border-emerald-500/20 px-2 py-0.5 rounded-full",children:[
              "✓ ",isAr?"شراء مؤكد":"Verified"
            ]})
          ]})
        ]}))
      })
    ]})
  })
}

function D(){
  const{dir:s,lang:t}=i();
  return e.jsxs("div",{className:"min-h-screen bg-background text-foreground",dir:s,lang:t,children:[
    e.jsx(w,{}),
    e.jsx(M,{}),
    e.jsx(C,{}),
    e.jsx(R,{}),
    e.jsx(L,{}),
    e.jsx(q,{}),
    e.jsx(I,{}),
    e.jsx(z,{}),
    e.jsx(T,{}),
    e.jsx(E,{}),
    e.jsx(y,{}),
    e.jsx(k,{})
  ]})
}

// 3. Brand Ticker Marquee (C)
function C(){
  const s=["MAISON ZEMA","EVERYDAY ELEGANCE","HANDCRAFTED LEATHER","INSPECT BEFORE PAYMENT","FREE SHIPPING OVER 1500 EGP","LIMITED EDITIONS"],t=[...s,...s,...s,...s];
  return e.jsx("div",{className:"border-y hairline bg-[#111111] text-[#dcd7cb] overflow-hidden py-3.5 select-none","aria-hidden":!0,dir:"ltr",children:
    e.jsx("div",{className:"flex w-max animate-marquee",children:[0,1].map(r=>
      e.jsx("div",{className:"flex shrink-0 items-center",children:t.map((l,n)=>
        e.jsxs("span",{className:"flex items-center",children:[
          e.jsx("span",{className:"text-[10px] md:text-[11px] tracking-[0.25em] uppercase font-semibold px-6",children:l}),
          e.jsx("span",{className:"text-accent text-[8px]",children:"◆"})
        ]},`${r}-${n}`)
      )},r)
    )})
  })
}

// 4. Hero Campaign (M) - Untouched visual layout & image, CTA updated
function M(){
  const{t:s,lang:l}=i(),isAr=l==="ar";
  return e.jsx("section",{className:"relative w-full overflow-hidden select-none","aria-label":"ZEMA Campaign",children:
    e.jsxs("div",{className:"relative h-[70svh] min-h-[460px] max-h-[660px] md:h-[80svh] md:min-h-[540px] md:max-h-[780px] lg:h-[94svh] lg:min-h-[600px] lg:max-h-[980px] w-full",children:[
      e.jsx("img",{src:"/zema-luxury/hero/zema-hero-wide.jpg",alt:"ZEMA Everyday Elegance Campaign",loading:"eager",fetchPriority:"high",className:"h-full w-full object-cover object-center transform scale-[1.01]"}),
      e.jsx("div",{className:"absolute inset-0 bg-gradient-to-t from-black/85 via-black/40 to-black/25"}),
      e.jsx("div",{className:"absolute inset-0 flex items-end justify-center pb-12 sm:pb-16 md:pb-24 lg:pb-28 text-center text-white px-5 sm:px-8",children:
        e.jsxs("div",{className:"max-w-3xl space-y-4 md:space-y-6",children:[
          e.jsx("p",{className:"text-[10px] sm:text-xs tracking-[0.35em] uppercase font-semibold text-accent",children:isAr?"الأناقة العملية لطالبات الجامعة والمرأة العاملة":"EVERYDAY ELEGANCE • AFFORDABLE LUXURY"}),
          e.jsx("h1",{className:"display-serif text-3xl sm:text-4xl md:text-6xl lg:text-7xl font-bold leading-[1.1] tracking-tight drop-shadow-sm",children:isAr?"فخامة تلائم تفاصيل يومك":"Designed for Your Daily Rhythm"}),
          e.jsx("p",{className:"text-xs sm:text-sm md:text-base text-stone-200 leading-relaxed max-w-xl mx-auto drop-shadow-sm font-light",children:isAr?"زِيما — مجموعة مختارة من حقائب اليد الفاخرة، المحافظ، وإكسسوارات الشنط، صُنعت لمن يدرك تفاصيل الأناقة العملية.":"ZEMA — A curated collection of luxury handbags, wallets, and bag accessories, crafted for those who appreciate functional elegance."}),
          e.jsx("div",{className:"pt-2 sm:pt-4",children:
            e.jsx(x,{to:"/shop",search:{category:"bags"},className:"inline-flex items-center justify-center px-8 py-3.5 text-xs sm:text-sm font-bold tracking-[0.16em] uppercase bg-accent text-accent-foreground rounded-full hover:bg-white hover:text-black transition-all duration-300 shadow-xl cursor-pointer",children:isAr?"تسوقي المجموعة الحصرية":"SHOP THE COLLECTION"})
          })
        ]})
      })
    ]})
  })
}

// 5. Limited Edition (L) - Scarcity Section directly below Hero (Top 4 Handbags)
function L(){
  const s=p(),{t,lang}=i(),isAr=lang==="ar";
  const bags = s.filter(x=>x.category==="bags").slice(0,4);
  return e.jsx("section",{id:"limited-edition",className:"border-b hairline bg-background select-none",children:
    e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12 py-16 lg:py-24",children:[
      e.jsxs("div",{className:"flex items-end justify-between mb-10 gap-4 flex-wrap",children:[
        e.jsxs("div",{children:[
          e.jsx("div",{className:"inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-accent/10 border border-accent/20 text-[10px] text-accent font-bold tracking-wider uppercase mb-2.5",children:isAr?"✨ كميات محدودة جداً":"LIMITED EDITION"}),
          e.jsx("h2",{className:"display-serif text-3xl md:text-5xl font-bold tracking-tight",children:isAr?"الإصدار المحدود":"Limited Edition"})
        ]}),
        e.jsxs(x,{to:"/shop",search:{category:"bags"},className:"text-[11px] tracking-[0.2em] uppercase font-bold text-accent hover:underline flex items-center gap-1",children:[isAr?"عرض كل الحقائب":"Explore All Bags"," →"]})
      ]}),
      e.jsx("div",{className:"grid grid-cols-2 md:grid-cols-4 gap-4 lg:gap-6",children:
        bags.map(item=>e.jsx(u,{p:item},item.id))
      })
    ]})
  })
}

// 6. Shop the Look (q) - Editorial Styling Showcase
function q(){
  const{lang}=i(),isAr=lang==="ar";
  return e.jsx("section",{id:"shop-the-look",className:"border-b hairline bg-[#111111] text-[#eae7e0] select-none",children:
    e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12 py-16 lg:py-24 grid grid-cols-1 lg:grid-cols-2 gap-10 lg:gap-14 items-center",children:[
      e.jsxs("div",{className:"relative aspect-[4/5] rounded-2xl overflow-hidden border border-white/10 group shadow-2xl",children:[
        e.jsx("img",{src:"/zema-luxury/hero/zema-editorial.jpg",alt:"Shop The Look Coordination",className:"w-full h-full object-cover transition-transform duration-700 group-hover:scale-[1.03]"}),
        e.jsx("div",{className:"absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-black/20"}),
        e.jsxs("div",{className:"absolute bottom-6 start-6 end-6 text-white",children:[
          e.jsx("span",{className:"text-[10px] tracking-[0.25em] uppercase text-accent font-bold",children:isAr?"تنسيق الموسم الحصري":"SEASONAL CURATION"}),
          e.jsx("h3",{className:"text-lg md:text-xl font-bold mt-1",children:isAr?"طقم الأناقة المتكامل (شنطة + محفظة + دلاية)":"The Everyday Luxe Ensemble"})
        ]})
      ]}),
      e.jsxs("div",{className:"space-y-6",children:[
        e.jsx("p",{className:"text-[10px] tracking-[0.3em] uppercase text-accent font-semibold",children:isAr?"نسقي إطلالتك الكاملة":"SHOP THE LOOK"}),
        e.jsx("h2",{className:"display-serif text-3xl md:text-5xl font-bold leading-tight",children:isAr?"تناغم فاخر يجمع مستلزماتك في طقم واحد":"Flawless Coordination for Everyday Elegance"}),
        e.jsx("p",{className:"text-xs md:text-sm text-stone-400 leading-relaxed",children:isAr?"صممنا لكِ أطقماً متكاملة تجمع بين حقائب اليد ذات السعة العملية، والمحافظ الجلدية المنظمة، وميداليات الشنط الفاخرة، لتمنحك إطلالة متناسقة وتوفيراً يصل إلى 900 جنيه.":"Elevate your everyday presence with meticulously paired handbags, precision-organized wallets, and handcrafted charms designed to complement each other seamlessly."}),
        e.jsxs("div",{className:"grid grid-cols-2 gap-4 pt-2",children:[
          e.jsxs("div",{className:"p-4 rounded-xl bg-white/5 border border-white/10 space-y-1",children:[
            e.jsx("p",{className:"text-xs font-bold text-white",children:isAr?"توفير فوري":"Instant Savings"}),
            e.jsx("p",{className:"text-[11px] text-stone-400",children:isAr?"خصومات خاصة على كافة الأطقم":"Bundle discounts on all sets"})
          ]}),
          e.jsxs("div",{className:"p-4 rounded-xl bg-white/5 border border-white/10 space-y-1",children:[
            e.jsx("p",{className:"text-xs font-bold text-white",children:isAr?"علبة هدايا فاخرة":"Luxury Gift Box"}),
            e.jsx("p",{className:"text-[11px] text-stone-400",children:isAr?"تغليف مخملي أنيق مجاني":"Complimentary signature velvet box"})
          ]})
        ]}),
        e.jsx("div",{className:"pt-4",children:
          e.jsx(x,{to:"/shop",search:{category:"bundles"},className:"inline-flex items-center gap-2 px-8 py-3.5 bg-accent text-accent-foreground font-bold text-xs uppercase tracking-wider rounded-full hover:bg-white hover:text-black transition-all duration-300 shadow-lg cursor-pointer",children:isAr?"تسوقي الأطقم المتكاملة (عروض التوفير)":"SHOP BUNDLES & SETS"})
        })
      ]})
    ]})
  })
}

// 7. 3 Key Value Pillars (I) - خامات متينة، تقسيمات ذكية، معاينة قبل الاستلام
function I(){
  const{lang}=i(),isAr=lang==="ar";
  const pillars = [
    {
      icon: "💎",
      title: isAr ? "خامات عملية ومتينة" : "Durable Practical Materials",
      desc: isAr ? "جلود معالجة فائقة التحمل ومقاومة للماء والخدوش، مصممة لتحمل جدولك اليومي المكثف في الجامعة والعمل لسنوات." : "Treated high-durability vegan leather engineered to endure daily commutes, campus, and work routines effortlessly."
    },
    {
      icon: "🗂️",
      title: isAr ? "تقسيمات داخلية ذكية" : "Smart Interior Organization",
      desc: isAr ? "سعة مدروسة بعناية تتسع للابتوب والمفكرة والهاتف ومستحضراتك الشخصية بجيوب مخصصة تحافظ على ترتيبك التام." : "Purposefully engineered compartments for laptops, smartphones, cards, and daily essentials with zero clutter."
    },
    {
      icon: "📦",
      title: isAr ? "معاينة قبل الاستلام" : "Inspection Before Payment",
      desc: isAr ? "افحصي حقيبتك وتأكدي من جودة الخامات والتفاصيل بنفسك مع مندوب الشحن قبل دفع أي مليم، مع ضمان استبدال ميسر." : "Open, inspect, and verify the quality in front of the courier before paying, with an easy 14-day exchange policy."
    }
  ];
  return e.jsx("section",{id:"brand-pillars",className:"border-b hairline bg-sand/30 select-none",children:
    e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12 py-16 lg:py-20",children:[
      e.jsxs("div",{className:"text-center mb-12",children:[
        e.jsx("p",{className:"text-[10px] tracking-[0.3em] uppercase text-accent font-semibold mb-2",children:isAr?"لماذا تختارين زِيما؟":"THE ZEMA PROMISE"}),
        e.jsx("h2",{className:"display-serif text-3xl md:text-4xl font-bold tracking-tight",children:isAr?"معايير الأناقة العملية الثلاثة":"3 Pillars of Everyday Elegance"})
      ]}),
      e.jsx("div",{className:"grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8",children:
        pillars.map((item,idx)=>e.jsxs("div",{className:"p-6 lg:p-8 rounded-2xl bg-card border hairline hover:border-accent/40 transition-all duration-300 space-y-4 shadow-sm",children:[
          e.jsx("div",{className:"h-12 w-12 rounded-xl bg-accent/10 border border-accent/20 flex items-center justify-center text-2xl",children:item.icon}),
          e.jsx("h3",{className:"text-base lg:text-lg font-bold text-foreground",children:item.title}),
          e.jsx("p",{className:"text-xs lg:text-sm text-muted-foreground leading-relaxed",children:item.desc})
        ]},idx))
      })
    ]})
  })
}

// 8. 4 Core Categories Grid (R) - Bags, Wallets, Charms, Bundles
function R(){
  const{lang}=i(),isAr=lang==="ar",
  cats=[
    {id:"cat-bags",cat:"bags",label:isAr?"حقائب نسائية":"Women Bags",en:"WOMEN BAGS",img:"/zema-luxury/hero/cat-bags.jpg"},
    {id:"cat-wallets",cat:"wallets",label:isAr?"محافظ":"Wallets",en:"WALLETS",img:"/zema-luxury/hero/cat-wallets.jpg"},
    {id:"cat-charms",cat:"charms",label:isAr?"إكسسوارات شنط":"Bag Accessories",en:"BAG ACCESSORIES",img:"/zema-luxury/hero/cat-charms.jpg"},
    {id:"cat-bundles",cat:"bundles",label:isAr?"بوكس زيما":"ZEMA Box",en:"ZEMA BOX",img:"/zema-luxury/hero/cat-box.jpg"}
  ];
  return e.jsx("section",{id:"categories",className:"border-b hairline bg-background select-none",children:
    e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12 py-16 lg:py-24",children:[
      e.jsxs("div",{className:"text-center mb-12",children:[
        e.jsx("p",{className:"text-[10px] tracking-[0.3em] uppercase text-accent font-semibold mb-2.5",children:isAr?"تسوق حسب الفئة":"SHOP BY CATEGORY"}),
        e.jsx("h2",{className:"display-serif text-3xl md:text-5xl font-bold tracking-tight",children:isAr?"التصنيفات الرئيسية":"The Categories"})
      ]}),
      e.jsx("div",{className:"grid grid-cols-2 lg:grid-cols-4 gap-4 lg:gap-6",children:
        cats.map(item=>e.jsxs(x,{to:"/shop",search:{category:item.cat},className:"group block overflow-hidden cursor-pointer",children:[
          e.jsx("div",{className:"aspect-[3/4] overflow-hidden rounded-xl bg-card/40 border hairline relative",children:
            e.jsx("img",{src:item.img,alt:item.label,loading:"lazy",className:"w-full h-full object-cover transition-transform duration-700 ease-out group-hover:scale-[1.04]"})
          }),
          e.jsxs("div",{className:"pt-4 text-center",children:[
            e.jsx("p",{className:"text-sm sm:text-base font-bold group-hover:text-accent transition-colors",children:item.label}),
            e.jsx("p",{className:"text-[9px] tracking-[0.2em] uppercase text-muted-foreground mt-1 font-semibold",children:item.en})
          ]})
        ]},item.id))
      })
    ]})
  })
}

// 9. Bundles & Complete Sets Showcase (z)
function z(){
  const s=p(),{lang}=i(),isAr=lang==="ar",
  bundles=s.filter(l=>l.category==="bundles"||l.bestseller).slice(0,6),
  scrollRef=d.useRef(null),
  scrollBy=(amt)=>{if(scrollRef.current)scrollRef.current.scrollBy({left:amt,behavior:"smooth"})};
  
  return e.jsx("section",{id:"bundles-showcase",className:"border-b hairline bg-sand/20 overflow-hidden select-none",children:
    e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12 py-16 lg:py-24",children:[
      e.jsxs("div",{className:"flex items-end justify-between mb-8 gap-4 flex-wrap",children:[
        e.jsxs("div",{children:[
          e.jsx("p",{className:"text-[10px] tracking-[0.3em] uppercase text-accent font-semibold mb-2.5",children:isAr?"عروض التوفير الذكية":"AFFORDABLE LUXURY"}),
          e.jsx("h2",{className:"display-serif text-3xl md:text-5xl font-bold tracking-tight",children:isAr?"أطقم الأناقة المتكاملة":"Bundles & Complete Sets"})
        ]}),
        e.jsxs("div",{className:"flex items-center gap-2",children:[
          e.jsx("button",{onClick:()=>scrollBy(-320),"aria-label":"Previous",className:"h-9 w-9 rounded-full border hairline bg-background/80 hover:bg-foreground hover:text-background flex items-center justify-center text-sm transition-colors cursor-pointer shadow-sm",children:"←"}),
          e.jsx("button",{onClick:()=>scrollBy(320),"aria-label":"Next",className:"h-9 w-9 rounded-full border hairline bg-background/80 hover:bg-foreground hover:text-background flex items-center justify-center text-sm transition-colors cursor-pointer shadow-sm",children:"→"}),
          e.jsxs(x,{to:"/shop",search:{category:"bundles"},className:"ms-3 text-[11px] tracking-[0.2em] uppercase font-bold text-accent hover:underline",children:[isAr?"تصفح الأطقم":"View All Sets"," →"]})
        ]})
      ]}),
      e.jsx("div",{ref:scrollRef,className:"flex gap-4 md:gap-6 overflow-x-auto pb-6 scrollbar-none snap-x snap-mandatory -mx-5 px-5 lg:-mx-12 lg:px-12",children:
        bundles.map(l=>e.jsx("div",{className:"w-[240px] sm:w-[270px] md:w-[290px] shrink-0 snap-start",children:e.jsx(u,{p:l})},l.id))
      })
    ]})
  })
}

export{D as component};
