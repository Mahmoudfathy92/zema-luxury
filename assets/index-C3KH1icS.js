import{u as i,r as d,j as e,L as x,a as p,i as N,f as v,e as m}from"./index-uamL4pK8.js";
import{S as w,a as y,F as k,X as S}from"./SiteChrome-vAcelVMJ.js";
import{P as u}from"./ProductCard-Di7jG7K4.js";

// 1. VIP Newsletter Section (Polène-Inspired Serene Design)
function E(){
  const{dir:t,lang:l}=i(),isAr=l==="ar",[r,setR]=d.useState(""),[n,setC]=d.useState("idle");
  const h=o=>{o.preventDefault();if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(r)){setC("err");return}setC("ok");setR("")};
  return e.jsx("section",{className:"border-t hairline bg-[#121212] text-[#f5f3ef] select-none",dir:t,children:
    e.jsxs("div",{className:"mx-auto max-w-3xl px-5 lg:px-12 py-20 lg:py-24 text-center",children:[
      e.jsx("p",{className:"text-[10px] tracking-[0.35em] uppercase text-stone-400 font-medium mb-3",children:isAr?"نادي زِيما للأناقة العملية":"ZEMA PRIVÉ CIRCLE"}),
      e.jsx("h2",{className:"display-serif text-3xl md:text-4xl font-light tracking-tight text-white",children:isAr?"انضمي لمجتمع زِيما الحصري":"Join the ZEMA Circle"}),
      e.jsx("p",{className:"mt-3 text-xs md:text-sm text-stone-400 leading-relaxed max-w-md mx-auto font-light",children:isAr?"احصلي على كود خصم 10% (ZEMA10) على أول طلب وإشعار مسبق بالإصدارات المحدودة.":"Receive an instant 10% privilege code (ZEMA10) on your first purchase and early access to limited editions."}),
      e.jsxs("form",{onSubmit:h,className:"mt-8 flex max-w-md mx-auto gap-2.5",children:[
        e.jsx("input",{type:"email",placeholder:isAr?"بريدك الإلكتروني":"Your email address",value:r,onChange:o=>setR(o.target.value),required:!0,className:"flex-1 bg-white/[0.06] border border-white/15 px-4 py-3.5 text-xs focus:outline-none focus:border-white/40 text-white placeholder:text-stone-500 rounded-full"}),
        e.jsx("button",{type:"submit",className:"bg-white text-black px-7 py-3.5 text-[11px] font-semibold uppercase tracking-[0.16em] rounded-full hover:bg-stone-200 transition-colors whitespace-nowrap cursor-pointer",children:isAr?"انضمام":"JOIN"})
      ]}),
      n==="ok"&&e.jsx("p",{className:"mt-3.5 text-xs text-emerald-400 font-medium",children:isAr?"تم اشتراكك بنجاح! استخدمي كود ZEMA10 عند إتمام الطلب.":"Welcome! Use code ZEMA10 at checkout."}),
      n==="err"&&e.jsx("p",{className:"mt-3.5 text-xs text-rose-400 font-medium",children:isAr?"يرجى إدخال بريد إلكتروني صحيح":"Please enter a valid email"})
    ]})
  })
}

// 2. Testimonials Component (T) - Quiet Editorial Reviews
function T(){
  const{lang}=i(),isAr=lang==="ar";
  const reviews = [
    {
      id: 1,
      name: isAr ? "مريم القاضي" : "Mariam El Kady",
      city: isAr ? "القاهرة" : "Cairo",
      product: isAr ? "حقيبة كلاسيك جلد طبيعي" : "Classic Handbag",
      date: isAr ? "منذ أسبوعين" : "2 weeks ago",
      text: isAr ? "جودة الحقيبة والجلد فاقت توقعاتي تماماً، والتقفيل متقن لأدق التفاصيل. تجربة المعاينة مع المندوب قبل الدفع أعطتني راحة وثقة كبيرة." : "The quality of the handbag and leather exceeded my expectations. Inspecting with the courier before payment gave me absolute peace of mind."
    },
    {
      id: 2,
      name: isAr ? "أحمد الشناوي" : "Ahmed El Shenawy",
      city: isAr ? "الإسكندرية" : "Alexandria",
      product: isAr ? "ساعة أوتوماتيك فاخرة" : "Automatic Watch",
      date: isAr ? "منذ 3 أسابيع" : "3 weeks ago",
      text: isAr ? "الساعة وصلت في علبة مخملية فاخرة جداً تنفع هدية راقية. الوزن والاهتمام بالتفاصيل يضاهي الماركات السويسرية، وسرعة التوصيل ممتازة." : "The watch arrived in a stunning luxury box suitable for gifting. The weight and attention to detail reflect true craftsmanship."
    },
    {
      id: 3,
      name: isAr ? "نور المهدي" : "Nour El Mahdy",
      city: isAr ? "الشيخ زايد" : "Sheikh Zayed",
      product: isAr ? "نظارة شمسية هافانا" : "Havana Sunglasses",
      date: isAr ? "منذ 4 أيام" : "4 days ago",
      text: isAr ? "النظارة خفيفة جداً ومريحة للعين وخاماتها صلبة وأنيقة. خدمة العملاء على الواتساب راقية ومتعاونة لأقصى درجة حتى استلام الشحنة." : "The sunglasses are lightweight, comfortable, and stylish. Customer support on WhatsApp was extremely helpful throughout delivery."
    }
  ];

  return e.jsx("section",{id:"testimonials",className:"border-b hairline bg-background py-20 lg:py-28 select-none",children:
    e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12",children:[
      e.jsxs("div",{className:"text-center mb-14 md:mb-20 space-y-2.5",children:[
        e.jsx("p",{className:"text-[10px] tracking-[0.35em] uppercase text-muted-foreground font-medium",children:isAr?"آراء العملاء":"TÉMOIGNAGES • CLIENT EXPERIENCES"}),
        e.jsx("h2",{className:"display-serif text-3xl md:text-5xl font-light tracking-tight text-foreground",children:isAr?"ثقة تميزت بها ZEMA":"Experiences That Define Us"}),
        e.jsx("p",{className:"text-xs sm:text-sm text-muted-foreground max-w-md mx-auto font-light",children:isAr?"انطباعات حقيقية من عملائنا بعد تجربة المعاينة واستلام القطع الفاخرة":"Authentic reflections from clients across Egypt after inspecting and receiving their curated pieces."})
      ]}),
      e.jsx("div",{className:"grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8",children:
        reviews.map(r=>e.jsxs("div",{key:r.id,className:"rounded-2xl border hairline bg-[#f4f2ee]/40 p-7 md:p-9 flex flex-col justify-between hover:border-foreground/30 transition-all duration-300",children:[
          e.jsxs("div",{className:"space-y-4",children:[
            e.jsxs("div",{className:"flex items-center justify-between",children:[
              e.jsx("div",{className:"flex gap-1 text-foreground/80 text-xs tracking-widest",children:"★★★★★"}),
              e.jsx("span",{className:"text-[10px] text-muted-foreground font-light ltr-num",children:r.date})
            ]}),
            e.jsxs("p",{className:"text-xs sm:text-[13px] leading-relaxed text-foreground/85 font-light italic",children:["“",r.text,"”"]})
          ]}),
          e.jsxs("div",{className:"mt-8 pt-4 border-t hairline flex items-center justify-between",children:[
            e.jsxs("div",{children:[
              e.jsx("h4",{className:"font-serif text-sm font-medium text-foreground",children:r.name}),
              e.jsxs("p",{className:"text-[10px] text-muted-foreground font-light mt-0.5",children:[r.city," · ",r.product]})
            ]}),
            e.jsxs("span",{className:"inline-flex items-center gap-1 text-[10px] text-emerald-800 font-medium bg-emerald-50 border border-emerald-200/60 px-2.5 py-0.5 rounded-full",children:[
              "✓ ",isAr?"شراء مؤكد":"Verified"
            ]})
          ]})
        ]}))
      })
    ]})
  })
}

// 3. Brand Ticker Marquee (C) - Polène-Style Subtle Whisper Ribbon
function C(){
  const s=["MAISON ZEMA","EVERYDAY ELEGANCE","ARTISANAL LEATHER","INSPECT BEFORE PAYMENT","FREE DELIVERY OVER 2,500 EGP","LIMITED EDITIONS"],t=[...s,...s,...s,...s];
  return e.jsx("div",{className:"border-y hairline bg-[#faf9f7] text-foreground/80 overflow-hidden py-3.5 select-none","aria-hidden":!0,dir:"ltr",children:
    e.jsx("div",{className:"flex w-max animate-marquee",children:[0,1].map(r=>
      e.jsx("div",{className:"flex shrink-0 items-center",children:t.map((l,n)=>
        e.jsxs("span",{className:"flex items-center",children:[
          e.jsx("span",{className:"text-[10px] md:text-[11px] tracking-[0.28em] uppercase font-medium px-6 text-foreground/75",children:l}),
          e.jsx("span",{className:"h-1 w-1 rounded-full bg-foreground/30",children:""})
        ]},`${r}-${n}`)
      )},r)
    )})
  })
}

// 4. Hero Campaign (M) - 100% UNTOUCHED PER CRITICAL USER REQUIREMENT
function M(){
  const{lang:l}=i(),isAr=l==="ar";
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

// 5. 4 Core Categories Grid (R) - Polène "Les Collections" Gallery
function R(){
  const{lang}=i(),isAr=lang==="ar",
  cats=[
    {id:"cat-bags",cat:"bags",label:isAr?"حقائب نسائية":"Women Bags",en:"SAC PORTÉ ÉPAULE & MAIN",img:"/zema-luxury/hero/cat-bags.jpg"},
    {id:"cat-wallets",cat:"wallets",label:isAr?"محافظ":"Wallets",en:"PETITE MAROQUINERIE",img:"/zema-luxury/hero/cat-wallets.jpg"},
    {id:"cat-charms",cat:"charms",label:isAr?"إكسسوارات شنط":"Bag Accessories",en:"ACCESSOIRES DE SAC",img:"/zema-luxury/hero/cat-charms.jpg"},
    {id:"cat-bundles",cat:"bundles",label:isAr?"بوكس زيما":"ZEMA Box",en:"COFFRETS EXCLUSIFS",img:"/zema-luxury/hero/cat-box.jpg"}
  ];
  return e.jsx("section",{id:"categories",className:"border-b hairline bg-background select-none",children:
    e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12 py-20 lg:py-28",children:[
      e.jsxs("div",{className:"text-center mb-14 md:mb-20 space-y-2.5",children:[
        e.jsx("p",{className:"text-[10px] tracking-[0.35em] uppercase text-muted-foreground font-medium",children:isAr?"التصنيفات الرئيسية":"LES COLLECTIONS • THE CATEGORIES"}),
        e.jsx("h2",{className:"display-serif text-3xl md:text-5xl lg:text-6xl font-light tracking-tight text-foreground",children:isAr?"تسوق حسب الفئة":"Shop by Category"})
      ]}),
      e.jsx("div",{className:"grid grid-cols-2 lg:grid-cols-4 gap-5 lg:gap-7",children:
        cats.map(item=>e.jsxs(x,{to:"/shop",search:{category:item.cat},className:"group block overflow-hidden cursor-pointer",children:[
          e.jsx("div",{className:"aspect-[3/4] overflow-hidden rounded-2xl bg-[#f4f2ee]/60 border hairline relative group-hover:shadow-md transition-all duration-500",children:
            e.jsx("img",{src:item.img,alt:item.label,loading:"lazy",className:"w-full h-full object-cover transition-transform duration-[800ms] ease-out group-hover:scale-[1.04]"})
          }),
          e.jsxs("div",{className:"pt-4 text-center",children:[
            e.jsx("p",{className:"font-serif text-base sm:text-lg font-medium text-foreground group-hover:text-accent transition-colors",children:item.label}),
            e.jsx("p",{className:"text-[9px] tracking-[0.22em] uppercase text-muted-foreground/80 mt-1 font-light",children:item.en})
          ]})
        ]},item.id))
      })
    ]})
  })
}

// 6. Limited Edition (L) - Polène Sculptural New Arrivals
function L(){
  const s=p(),{lang}=i(),isAr=lang==="ar";
  const bags = s.filter(x=>x.category==="bags").slice(0,4);
  return e.jsx("section",{id:"limited-edition",className:"border-b hairline bg-background select-none",children:
    e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12 py-20 lg:py-28",children:[
      e.jsxs("div",{className:"flex items-end justify-between mb-12 md:mb-16 gap-4 flex-wrap",children:[
        e.jsxs("div",{className:"space-y-2",children:[
          e.jsx("p",{className:"text-[10px] tracking-[0.35em] uppercase text-muted-foreground font-medium",children:isAr?"إصدارات الموسم":"NOUVEAUTÉS • NEW ARRIVALS"}),
          e.jsx("h2",{className:"display-serif text-3xl md:text-5xl font-light tracking-tight text-foreground",children:isAr?"وصل حديثاً":"New Arrivals"})
        ]}),
        e.jsxs(x,{to:"/shop",search:{category:"bags"},className:"text-[11px] tracking-[0.2em] uppercase font-semibold text-foreground/80 hover:text-foreground border-b border-foreground/30 hover:border-foreground pb-0.5 transition-all flex items-center gap-1.5",children:[isAr?"عرض كل الحقائب":"Explore All Bags"," →"]})
      ]}),
      e.jsx("div",{className:"grid grid-cols-2 md:grid-cols-4 gap-5 md:gap-7 lg:gap-8",children:
        bags.map(item=>e.jsx(u,{p:item},item.id))
      })
    ]})
  })
}

// 7. Editorial Craftsmanship Diptych (q) - Polène "Savoir-Faire" Heritage
function q(){
  const{lang}=i(),isAr=lang==="ar";
  return e.jsx("section",{id:"savoir-faire",className:"border-b hairline bg-[#faf9f7] select-none",children:
    e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12 py-20 lg:py-28 grid grid-cols-1 lg:grid-cols-2 gap-12 lg:gap-16 items-center",children:[
      e.jsxs("div",{className:"relative aspect-[4/5] rounded-3xl overflow-hidden border hairline group shadow-sm",children:[
        e.jsx("img",{src:"/zema-luxury/hero/zema-editorial.jpg",alt:"ZEMA Savoir-Faire Craftsmanship",className:"w-full h-full object-cover transition-transform duration-[900ms] group-hover:scale-[1.03]"}),
        e.jsx("div",{className:"absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent"}),
        e.jsxs("div",{className:"absolute bottom-7 start-7 end-7 text-white",children:[
          e.jsx("span",{className:"text-[10px] tracking-[0.3em] uppercase text-stone-300 font-medium",children:isAr?"فلسفة التصميم":"LE SAVOIR-FAIRE"}),
          e.jsx("h3",{className:"font-serif text-lg md:text-xl font-medium mt-1 text-white",children:isAr?"حرفية متقنة تليق بيومك":"Crafted with Architectural Precision"})
        ]})
      ]}),
      e.jsxs("div",{className:"space-y-6 lg:pe-6",children:[
        e.jsx("p",{className:"text-[10px] tracking-[0.35em] uppercase text-muted-foreground font-medium",children:isAr?"أناقة هادئة ومستدامة":"QUIET LUXURY • L'ART DE LA MAROQUINERIE"}),
        e.jsx("h2",{className:"display-serif text-3xl sm:text-4xl md:text-5xl font-light text-foreground leading-[1.2] tracking-tight",children:isAr?"حرفية استثنائية وأناقة تلائم تفاصيل يومك":"Architectural Lines, Everyday Purpose"}),
        e.jsx("p",{className:"text-xs sm:text-sm md:text-[14px] text-muted-foreground leading-relaxed font-light",children:isAr?"في دار زِيما، نؤمن بأن الفخامة الحقيقية لا تحتاج إلى مبالغة، بل تتجلى في نقاء الخطوط، وجودة الجلود المعالجة، والتقسيمات الداخلية الذكية التي تلائم متطلباتك اليومية في العمل والجامعة. كل قطعة مصممة لتدوم وترافقك بثقة ورقي.":"At ZEMA Maison, we believe genuine luxury needs no excess. It is articulated through pure architectural contours, meticulously treated leather, and thoughtful compartments designed to harmonise with your daily rhythm."}),
        e.jsxs("div",{className:"grid grid-cols-2 gap-4 pt-3",children:[
          e.jsxs("div",{className:"p-4 rounded-xl bg-card border hairline space-y-1",children:[
            e.jsx("p",{className:"font-serif text-xs font-semibold text-foreground",children:isAr?"جلود معالجة فائقة التحمل":"Resilient Finished Leather"}),
            e.jsx("p",{className:"text-[11px] text-muted-foreground font-light",children:isAr?"مقاومة للماء والخدوش للاستخدام المكثف":"Water and scratch-resistant engineering"})
          ]}),
          e.jsxs("div",{className:"p-4 rounded-xl bg-card border hairline space-y-1",children:[
            e.jsx("p",{className:"font-serif text-xs font-semibold text-foreground",children:isAr?"حق المعاينة قبل الدفع":"Inspect Before Payment"}),
            e.jsx("p",{className:"text-[11px] text-muted-foreground font-light",children:isAr?"افحصي شحنتك مع المندوب باطمئنان":"Verify craftsmanship at your doorstep"})
          ]})
        ]}),
        e.jsx("div",{className:"pt-4",children:
          e.jsx(x,{to:"/shop",search:{category:"bags"},className:"inline-flex items-center gap-2 text-xs font-semibold tracking-[0.18em] uppercase text-foreground border-b border-foreground pb-1 hover:opacity-65 transition-all cursor-pointer",children:isAr?"استكشفي المجموعة الكاملة →":"DISCOVER THE COLLECTION →"})
        })
      ]})
    ]})
  })
}

// 8. 3 Key Value Pillars (I) - Polène Understated Guarantees
function I(){
  const{lang}=i(),isAr=lang==="ar";
  const pillars = [
    {
      num: "01",
      title: isAr ? "خامات عملية ومتينة" : "Enduring Craftsmanship",
      desc: isAr ? "جلود معالجة فائقة التحمل ومقاومة للماء والخدوش، مصممة لتحمل جدولك اليومي المكثف في الجامعة والعمل لسنوات." : "Treated high-durability leather engineered to endure daily commutes and work routines effortlessly."
    },
    {
      num: "02",
      title: isAr ? "تقسيمات داخلية ذكية" : "Thoughtful Compartments",
      desc: isAr ? "سعة مدروسة بعناية تتسع للابتوب والمفكرة والهاتف ومستحضراتك الشخصية بجيوب مخصصة تحافظ على ترتيبك التام." : "Purposefully engineered compartments for laptops, smartphones, and daily essentials with zero clutter."
    },
    {
      num: "03",
      title: isAr ? "معاينة قبل الاستلام" : "Inspection Before Payment",
      desc: isAr ? "افحصي حقيبتك وتأكدي من جودة الخامات والتفاصيل بنفسك مع مندوب الشحن قبل دفع أي مليم، مع ضمان استبدال ميسر." : "Open, inspect, and verify the quality in front of the courier before paying, with an easy exchange policy."
    }
  ];
  return e.jsx("section",{id:"brand-pillars",className:"border-b hairline bg-background select-none",children:
    e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12 py-20 lg:py-24",children:[
      e.jsxs("div",{className:"text-center mb-14 md:mb-16 space-y-2",children:[
        e.jsx("p",{className:"text-[10px] tracking-[0.35em] uppercase text-muted-foreground font-medium",children:isAr?"معايير زِيما للأناقة":"THE ZEMA STANDARDS"}),
        e.jsx("h2",{className:"display-serif text-3xl md:text-4xl font-light tracking-tight text-foreground",children:isAr?"ثلاثة معايير نلتزم بها":"Three Pillars of Everyday Elegance"})
      ]}),
      e.jsx("div",{className:"grid grid-cols-1 md:grid-cols-3 gap-8 lg:gap-12",children:
        pillars.map((item,idx)=>e.jsxs("div",{className:"p-8 rounded-2xl bg-[#f4f2ee]/40 border hairline hover:border-foreground/30 transition-all duration-300 space-y-3.5",children:[
          e.jsx("span",{className:"font-serif text-2xl font-light text-muted-foreground/60 ltr-num block",children:item.num}),
          e.jsx("h3",{className:"font-serif text-base lg:text-lg font-medium text-foreground",children:item.title}),
          e.jsx("p",{className:"text-xs lg:text-[13px] text-muted-foreground leading-relaxed font-light",children:item.desc})
        ]},idx))
      })
    ]})
  })
}

// 9. Bundles & Complete Sets Showcase (z) - Polène Horizontal Rail
function z(){
  const s=p(),{lang}=i(),isAr=lang==="ar",
  bundles=s.filter(l=>l.category==="bundles"||l.bestseller).slice(0,6),
  scrollRef=d.useRef(null),
  scrollBy=(amt)=>{if(scrollRef.current)scrollRef.current.scrollBy({left:amt,behavior:"smooth"})};
  
  return e.jsx("section",{id:"bundles-showcase",className:"border-b hairline bg-[#faf9f7] overflow-hidden select-none",children:
    e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12 py-20 lg:py-28",children:[
      e.jsxs("div",{className:"flex items-end justify-between mb-10 md:mb-14 gap-4 flex-wrap",children:[
        e.jsxs("div",{className:"space-y-2",children:[
          e.jsx("p",{className:"text-[10px] tracking-[0.35em] uppercase text-muted-foreground font-medium",children:isAr?"تنسيقات متناسقة":"COMPOSITIONS • CURATED ENSEMBLES"}),
          e.jsx("h2",{className:"display-serif text-3xl md:text-5xl font-light tracking-tight text-foreground",children:isAr?"أطقم الأناقة المتكاملة":"Curated Sets & Ensembles"})
        ]}),
        e.jsxs("div",{className:"flex items-center gap-2",children:[
          e.jsx("button",{onClick:()=>scrollBy(-320),"aria-label":"Previous",className:"h-10 w-10 rounded-full border hairline bg-background hover:bg-foreground hover:text-background flex items-center justify-center text-sm transition-colors cursor-pointer shadow-sm",children:"←"}),
          e.jsx("button",{onClick:()=>scrollBy(320),"aria-label":"Next",className:"h-10 w-10 rounded-full border hairline bg-background hover:bg-foreground hover:text-background flex items-center justify-center text-sm transition-colors cursor-pointer shadow-sm",children:"→"}),
          e.jsxs(x,{to:"/shop",search:{category:"bundles"},className:"ms-4 text-[11px] tracking-[0.2em] uppercase font-semibold text-foreground/80 hover:text-foreground border-b border-foreground/30 hover:border-foreground pb-0.5 transition-all",children:[isAr?"تصفح الأطقم":"View All Sets"," →"]})
        ]})
      ]}),
      e.jsx("div",{ref:scrollRef,className:"flex gap-5 md:gap-7 overflow-x-auto pb-6 scrollbar-none snap-x snap-mandatory -mx-5 px-5 lg:-mx-12 lg:px-12",children:
        bundles.map(l=>e.jsx("div",{className:"w-[250px] sm:w-[280px] md:w-[300px] shrink-0 snap-start",children:e.jsx(u,{p:l})},l.id))
      })
    ]})
  })
}

// Main Page Layout
function D(){
  const{dir:s,lang:t}=i();
  return e.jsxs("div",{className:"min-h-screen bg-background text-foreground",dir:s,lang:t,children:[
    e.jsx(w,{}),
    e.jsx(M,{}),   // 100% untouched first hero section
    e.jsx(C,{}),   // Polène-inspired quiet marquee
    e.jsx(R,{}),   // Polène-inspired 3:4 category gallery
    e.jsx(L,{}),   // Polène-inspired New Arrivals
    e.jsx(q,{}),   // Polène-inspired Savoir-Faire Diptych
    e.jsx(z,{}),   // Polène-inspired Horizontal Curated Sets
    e.jsx(I,{}),   // Polène-inspired Minimalist 3 Pillars
    e.jsx(T,{}),   // Polène-inspired Editorial Testimonials
    e.jsx(E,{}),   // Polène-inspired VIP Newsletter
    e.jsx(y,{}),   // Footer
    e.jsx(k,{})    // Cart drawer
  ]})
}

export{D as component};
