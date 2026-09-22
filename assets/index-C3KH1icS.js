import{u as i,r as d,j as e,L as x,a as p,i as N,f as v,e as m}from"./index-uamL4pK8.js";
import{S as w,a as y,F as k,X as S}from"./SiteChrome-vAcelVMJ.js";
import{P as u}from"./ProductCard-Di7jG7K4.js";

// ==============================================================================
// 1. EDITORIAL CAMPAIGN HERO (75–90vh)
// ==============================================================================
function HeroSection(){
  const{lang:l}=i(),isAr=l==="ar";
  return e.jsx("section",{
    className:"relative w-full h-[78vh] min-h-[520px] max-h-[850px] md:h-[86vh] overflow-hidden bg-[#111111] select-none",
    "aria-label":"ZEMA Maison Campaign",
    children:e.jsxs("div",{className:"relative w-full h-full",children:[
      e.jsx("img",{
        src:"/zema-luxury/hero/zema-hero-wide.jpg",
        alt:"ZEMA Maison Editorial Campaign",
        width:"1920",
        height:"1088",
        fetchPriority:"high",
        className:"absolute inset-0 w-full h-full object-cover object-[50%_center] opacity-90 scale-[1.01] transition-transform duration-1000"
      }),
      e.jsx("div",{className:"absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-black/40"}),
      e.jsx("div",{className:"relative mx-auto max-w-7xl h-full px-6 lg:px-12 flex flex-col justify-end pb-16 md:pb-24",children:
        e.jsxs("div",{className:"max-w-2xl text-white",children:[
          e.jsx("p",{className:"text-[10px] md:text-[11px] font-semibold tracking-[0.3em] uppercase text-stone-300 mb-3",children:"ZEMA MAISON"}),
          e.jsxs("h1",{className:"display-serif text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-light tracking-tight leading-[1.08] text-[#faf9f7] mb-6",children:[
            "TIMELESS STYLE.",
            e.jsx("br",{}),
            e.jsx("span",{className:"font-normal italic",children:"MODERN LUXURY."})
          ]}),
          e.jsxs("div",{className:"flex flex-wrap items-center gap-4 pt-2",children:[
            e.jsx(x,{
              to:"/shop",
              className:"inline-flex items-center justify-center bg-[#faf9f7] text-[#0e0e0e] hover:bg-white px-8 py-3.5 text-[11px] font-semibold tracking-[0.2em] uppercase transition-all duration-300 shadow-lg cursor-pointer",
              children:isAr?"اكتشف المجموعة":"DISCOVER THE COLLECTION"
            }),
            e.jsx(x,{
              to:"/shop",
              search:{category:"bags"},
              className:"inline-flex items-center justify-center bg-transparent border border-white/60 hover:border-white text-white px-8 py-3.5 text-[11px] font-semibold tracking-[0.2em] uppercase transition-all duration-300 backdrop-blur-xs cursor-pointer",
              children:isAr?"تسوق الحقائب":"SHOP BAGS"
            })
          ]})
        ]})
      })
    ]})
  })
}

// ==============================================================================
// 2. FEATURED CATEGORIES (THE COLLECTION - 2x2 Editorial Grid)
// ==============================================================================
function FeaturedCategories(){
  const{lang:l}=i(),isAr=l==="ar";
  const cats=[
    {
      title:isAr?"حقائب نسائية":"BAGS",
      sub:isAr?"حقائب كتف وتوت ويد فاخرة":"Shoulder, Tote & Structured Handbags",
      img:"/zema-luxury/hero/cat-bags.jpg",
      search:{category:"bags"}
    },
    {
      title:isAr?"محافظ":"WALLETS",
      sub:isAr?"محافظ كلاسيكية وحوافظ بطاقات":"Bifold, Continental & Slim Cardholders",
      img:"/zema-luxury/hero/cat-wallets.jpg",
      search:{category:"wallets"}
    },
    {
      title:isAr?"إكسسوارات شنط":"CHARMS",
      sub:isAr?"دلايات مخملية وميداليات مونوغرام":"Velvet Tassels & Artisan Hardware",
      img:"/zema-luxury/hero/cat-charms.jpg",
      search:{category:"charms"}
    },
    {
      title:isAr?"بوكس زيما":"ZEMA BOX",
      sub:isAr?"أطقم متكاملة وتنسيقات الموسم":"Curated Luxury Sets & Gift Editions",
      img:"/zema-luxury/hero/cat-box.jpg",
      search:{category:"bundles"}
    }
  ];

  return e.jsx("section",{id:"the-collection",className:"border-b hairline bg-[#faf9f7] py-20 lg:py-28 select-none",children:
    e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12",children:[
      e.jsxs("div",{className:"text-center max-w-xl mx-auto mb-14 md:mb-18",children:[
        e.jsx("p",{className:"text-[10px] md:text-[11px] font-semibold tracking-[0.3em] uppercase text-stone-500 mb-2",children:"THE COLLECTION"}),
        e.jsx("h2",{className:"display-serif text-3xl md:text-5xl font-light text-stone-900 tracking-tight",children:isAr?"المجموعة الكاملة":"Discover the ZEMA Maison Collection"}),
        e.jsx("p",{className:"text-xs md:text-sm text-stone-500 font-light mt-3 tracking-wide",children:isAr?"أربع فئات صُممت لمن يبحث عن الأناقة العصرية والقطع الخالدة.":"Four distinct categories crafted with purposeful elegance and artisanal leathercraft."})
      ]}),
      e.jsx("div",{className:"grid grid-cols-1 md:grid-cols-2 gap-6 lg:gap-8",children:
        cats.map(c=>e.jsx(x,{
          key:c.title,
          to:"/shop",
          search:c.search,
          className:"group block relative aspect-[4/3] md:aspect-[16/11] overflow-hidden bg-[#161616]",
          children:e.jsxs(e.Fragment,{children:[
            e.jsx("img",{
              src:c.img,
              alt:c.title,
              loading:"lazy",
              decoding:"async",
              className:"w-full h-full object-cover object-center opacity-85 transition-transform duration-[1000ms] cubic-bezier(0.16, 1, 0.3, 1) group-hover:scale-[1.04] group-hover:opacity-95"
            }),
            e.jsx("div",{className:"absolute inset-0 bg-gradient-to-t from-black/75 via-black/20 to-transparent"}),
            e.jsxs("div",{className:"absolute inset-x-6 bottom-6 md:inset-x-8 md:bottom-8 text-white",children:[
              e.jsx("h3",{className:"text-xl md:text-2xl font-light tracking-[0.16em] uppercase text-white mb-1.5",children:c.title}),
              e.jsx("p",{className:"text-xs text-stone-300 font-light tracking-wide mb-3 line-clamp-1",children:c.sub}),
              e.jsxs("span",{className:"inline-flex items-center text-[10px] tracking-[0.2em] uppercase font-semibold text-white/90 group-hover:text-white transition-colors",children:[
                isAr?"استكشف المجموعة":"Explore Collection",
                e.jsx("span",{className:"ms-2 transition-transform duration-300 group-hover:translate-x-1",children:"→"})
              ]})
            ]})
          ]})
        }))
      })
    ]})
  })
}

// ==============================================================================
// 3. NEW ARRIVALS / THE ZEMA EDIT (Max 4 products)
// ==============================================================================
function TheZemaEdit(){
  const all=p(),{lang:l}=i(),isAr=l==="ar";
  // Curate exactly 4 signature new arrivals
  const curatedIds=["bg-01","bg-02","wl-03","ch-01"];
  const items=curatedIds.map(id=>all.find(p=>p.id===id)).filter(Boolean);

  return e.jsx("section",{id:"the-zema-edit",className:"border-b hairline bg-[#faf9f7] py-20 lg:py-28 select-none",children:
    e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12",children:[
      e.jsxs("div",{className:"flex flex-col md:flex-row md:items-end justify-between mb-12 md:mb-16 gap-4",children:[
        e.jsxs("div",{children:[
          e.jsx("p",{className:"text-[10px] md:text-[11px] font-semibold tracking-[0.3em] uppercase text-stone-500 mb-2",children:"NEW ARRIVALS"}),
          e.jsx("h2",{className:"display-serif text-3xl md:text-5xl font-light text-stone-900 tracking-tight",children:"THE ZEMA EDIT"}),
          e.jsx("p",{className:"text-xs md:text-sm text-stone-500 font-light mt-2 tracking-wide",children:isAr?"مختارات حديثة تجمع بين الحرفية اليدوية والخطوط المعاصرة.":"A curated selection of our latest pieces."})
        ]}),
        e.jsx(x,{
          to:"/shop",
          search:{sort:"newest"},
          className:"text-[11px] font-semibold tracking-[0.2em] uppercase text-stone-900 hover:text-stone-600 transition-colors underline underline-offset-8 self-start md:self-end",
          children:isAr?"عرض الكل ←":"VIEW ALL →"
        })
      ]}),
      e.jsx("div",{className:"grid grid-cols-2 lg:grid-cols-4 gap-5 md:gap-8",children:
        items.map(item=>e.jsx(u,{p:item},item.id))
      })
    ]})
  })
}

// ==============================================================================
// 4. EDITORIAL CAMPAIGN BANNER (MADE FOR THE MOMENT)
// ==============================================================================
function EditorialCampaignBanner(){
  const{lang:l}=i(),isAr=l==="ar";
  return e.jsx("section",{
    className:"relative w-full h-[65vh] min-h-[460px] max-h-[700px] overflow-hidden bg-[#0d0d0d] select-none",
    children:e.jsxs("div",{className:"relative w-full h-full",children:[
      e.jsx("img",{
        src:"/zema-luxury/hero/zema-editorial.jpg",
        alt:"ZEMA Maison Lifestyle",
        loading:"lazy",
        decoding:"async",
        className:"absolute inset-0 w-full h-full object-cover object-[65%_center] opacity-80"
      }),
      e.jsx("div",{className:"absolute inset-0 bg-gradient-to-r from-black/85 via-black/50 to-black/20"}),
      e.jsx("div",{className:"relative mx-auto max-w-7xl h-full px-6 lg:px-12 flex items-center",children:
        e.jsxs("div",{className:"max-w-lg text-white",children:[
          e.jsx("p",{className:"text-[10px] md:text-[11px] font-semibold tracking-[0.3em] uppercase text-stone-400 mb-3",children:"EDITORIAL CAMPAIGN"}),
          e.jsx("h2",{className:"display-serif text-3xl sm:text-4xl md:text-5xl font-light tracking-tight leading-tight text-[#faf9f7] mb-4",children:"MADE FOR THE MOMENT"}),
          e.jsx("p",{className:"text-xs md:text-sm text-stone-300 font-light tracking-wider leading-relaxed mb-8 max-w-md",children:isAr?"قطع صُممت للأناقة الدائمة والمناسبات الراقية دون تكلف.":"Timeless pieces designed for modern living."}),
          e.jsx(x,{
            to:"/shop",
            className:"inline-flex items-center justify-center bg-[#faf9f7] text-[#0e0e0e] hover:bg-white px-8 py-3.5 text-[11px] font-semibold tracking-[0.2em] uppercase transition-all duration-300 shadow-md cursor-pointer",
            children:isAr?"استكشف زِيما":"EXPLORE ZEMA"
          })
        ]})
      })
    ]})
  })
}

// ==============================================================================
// 5. BEST SELLERS (Max 4 products)
// ==============================================================================
function BestSellersSection(){
  const all=p(),{lang:l}=i(),isAr=l==="ar";
  // Curate exactly 4 signature bestsellers
  const bestIds=["bg-04","wl-02","wl-04","bd-01"];
  const items=bestIds.map(id=>all.find(p=>p.id===id)).filter(Boolean);

  return e.jsx("section",{id:"best-sellers",className:"border-b hairline bg-[#faf9f7] py-20 lg:py-28 select-none",children:
    e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12",children:[
      e.jsxs("div",{className:"flex flex-col md:flex-row md:items-end justify-between mb-12 md:mb-16 gap-4",children:[
        e.jsxs("div",{children:[
          e.jsx("p",{className:"text-[10px] md:text-[11px] font-semibold tracking-[0.3em] uppercase text-stone-500 mb-2",children:"CURATED ICONICS"}),
          e.jsx("h2",{className:"display-serif text-3xl md:text-5xl font-light text-stone-900 tracking-tight",children:"BEST SELLERS"}),
          e.jsx("p",{className:"text-xs md:text-sm text-stone-500 font-light mt-2 tracking-wide",children:isAr?"إبداعات حازت على ثقة واختيار عملائنا في كل مكان.":"Our most coveted signature creations."})
        ]}),
        e.jsx(x,{
          to:"/shop",
          search:{sort:"bestselling"},
          className:"text-[11px] font-semibold tracking-[0.2em] uppercase text-stone-900 hover:text-stone-600 transition-colors underline underline-offset-8 self-start md:self-end",
          children:isAr?"عرض الكل ←":"VIEW ALL →"
        })
      ]}),
      e.jsx("div",{className:"grid grid-cols-2 lg:grid-cols-4 gap-5 md:gap-8",children:
        items.map(item=>e.jsx(u,{p:item},item.id))
      })
    ]})
  })
}

// ==============================================================================
// 6. BRAND STORY SECTION
// ==============================================================================
function BrandStorySection(){
  const{lang:l}=i(),isAr=l==="ar";
  return e.jsx("section",{className:"border-b hairline bg-[#f4f2ee] py-20 lg:py-28 select-none",children:
    e.jsx("div",{className:"mx-auto max-w-5xl px-6 lg:px-12 text-center",children:
      e.jsxs("div",{className:"space-y-6",children:[
        e.jsx("p",{className:"text-[10px] md:text-[11px] font-semibold tracking-[0.35em] uppercase text-stone-500",children:"ZEMA MAISON"}),
        e.jsx("h2",{className:"display-serif text-3xl md:text-5xl lg:text-6xl font-light text-stone-900 tracking-tight leading-tight",children:"TIMELESS STYLE, MODERN LUXURY."}),
        e.jsx("div",{className:"w-12 h-px bg-stone-400 mx-auto my-6"}),
        e.jsx("p",{
          className:"text-xs md:text-sm text-stone-600 font-light leading-relaxed max-w-2xl mx-auto tracking-wide",
          children:isAr?
            "تأسست دار زِيما ميزون برؤية ترتكز على ابتكار إكسسوارات جلدية فاخرة تجمع بين البساطة الراقية والعملية الفائقة. نختار جلودنا بعناية حرفية تامة ونولي اهتماماً فائقاً لأدق التفاصيل الهندسية لترافق إطلالتك اليومية بثقة وأناقة تدوم.":
            "ZEMA Maison was founded on the belief that modern luxury lies in architectural simplicity and uncompromising craftsmanship. We craft fine leather goods and functional accessories designed to accompany your daily life with quiet confidence and enduring refinement."
        }),
        e.jsx("div",{className:"pt-6",children:
          e.jsx(x,{
            to:"/about",
            className:"text-[11px] font-semibold tracking-[0.2em] uppercase text-stone-900 hover:text-stone-600 transition-colors underline underline-offset-8",
            children:isAr?"اكتشف قصة الدار ←":"DISCOVER OUR STORY →"
          })
        })
      ]})
    })
  })
}

// ==============================================================================
// 7. SUBTLE SERVICE STRIP (Micro-type, No oversized icons)
// ==============================================================================
function SubtleServiceStrip(){
  return e.jsx("div",{className:"border-b hairline bg-[#faf9f7] py-6 select-none text-center",children:
    e.jsx("div",{className:"mx-auto max-w-7xl px-5 text-[10px] md:text-[11px] tracking-[0.22em] uppercase text-stone-500 font-medium flex flex-wrap items-center justify-center gap-x-8 gap-y-2",children:[
      e.jsx("span",{},"CASH ON DELIVERY"),
      e.jsx("span",{className:"text-stone-300 hidden sm:inline"},"•"),
      e.jsx("span",{},"FAST DELIVERY ACROSS EGYPT"),
      e.jsx("span",{className:"text-stone-300 hidden sm:inline"},"•"),
      e.jsx("span",{},"14-DAY RETURNS"),
      e.jsx("span",{className:"text-stone-300 hidden sm:inline"},"•"),
      e.jsx("span",{},"SECURE CHECKOUT")
    ]})
  })
}

// ==============================================================================
// 8. MINIMAL LUXURY NEWSLETTER (JOIN OUR CIRCLE)
// ==============================================================================
function LuxuryNewsletter(){
  const{lang:l}=i(),isAr=l==="ar",[r,setR]=d.useState(""),[status,setStatus]=d.useState("idle");
  const onSubmit=ev=>{
    ev.preventDefault();
    if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(r)){setStatus("err");return}
    setStatus("ok");
    setR("");
  };

  return e.jsx("section",{className:"border-b hairline bg-[#faf9f7] py-20 lg:py-24 select-none",children:
    e.jsxs("div",{className:"mx-auto max-w-2xl px-6 text-center",children:[
      e.jsx("p",{className:"text-[10px] md:text-[11px] font-semibold tracking-[0.3em] uppercase text-stone-500 mb-2",children:"NEWSLETTER"}),
      e.jsx("h2",{className:"display-serif text-3xl md:text-4xl font-light text-stone-900 tracking-tight mb-3",children:"JOIN OUR CIRCLE"}),
      e.jsx("p",{className:"text-xs md:text-sm text-stone-500 font-light mb-8 tracking-wide",children:isAr?"كوني أول من يكتشف التشكيلات الحصرية والإصدارات الخاصة.":"Be the first to discover new arrivals, exclusive offers, and premium collections."}),
      e.jsxs("form",{onSubmit:onSubmit,className:"flex flex-col sm:flex-row items-center gap-3 max-w-md mx-auto",children:[
        e.jsx("input",{
          type:"email",
          value:r,
          onChange:ev=>setR(ev.target.value),
          placeholder:isAr?"عنوان بريدك الإلكتروني":"Your email address",
          className:"w-full flex-1 bg-transparent border border-stone-300 px-4 py-3 text-xs tracking-wider text-stone-900 placeholder:text-stone-400 focus:outline-none focus:border-stone-900 transition-colors"
        }),
        e.jsx("button",{
          type:"submit",
          className:"w-full sm:w-auto bg-[#0e0e0e] hover:bg-[#222222] text-[#faf9f7] px-7 py-3 text-[11px] font-semibold tracking-[0.2em] uppercase transition-colors shrink-0 cursor-pointer",
          children:isAr?"انضمام":"JOIN"
        })
      ]}),
      status==="ok"&&e.jsx("p",{className:"text-xs text-stone-800 font-medium mt-4",children:isAr?"شكراً لانضمامك إلى زِيما ميزون.":"Thank you for joining ZEMA Maison."}),
      status==="err"&&e.jsx("p",{className:"text-xs text-stone-500 font-medium mt-4",children:isAr?"يرجى إدخال بريد إلكتروني صحيح.":"Please enter a valid email address."})
    ]})
  })
}

// ==============================================================================
// MAIN HOMEPAGE COMPONENT
// ==============================================================================
function D(){
  const{dir:s,lang:t}=i();
  return e.jsxs("div",{className:"min-h-screen bg-[#faf9f7] text-[#0e0e0e] selection:bg-stone-200",dir:s,lang:t,children:[
    e.jsx(w,{}),
    e.jsx(HeroSection,{}),
    e.jsx(FeaturedCategories,{}),
    e.jsx(TheZemaEdit,{}),
    e.jsx(EditorialCampaignBanner,{}),
    e.jsx(BestSellersSection,{}),
    e.jsx(BrandStorySection,{}),
    e.jsx(SubtleServiceStrip,{}),
    e.jsx(LuxuryNewsletter,{}),
    e.jsx(k,{})
  ]})
}

export{D as component};
