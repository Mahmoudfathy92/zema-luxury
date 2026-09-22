import{r as i,j as e,W as N,u as m,a as y,L as c,b as w,C}from"./index-uamL4pK8.js";

const g=(...s)=>s.filter((t,o,n)=>!!t&&t.trim()!==""&&n.indexOf(t)===o).join(" ").trim();
const L=s=>s.replace(/([a-z0-9])([A-Z])/g,"$1-$2").toLowerCase();
const _=s=>s.replace(/^([A-Z])|[\s-_]+(\w)/g,(t,o,n)=>n?n.toUpperCase():o.toLowerCase());
const p=s=>{const t=_(s);return t.charAt(0).toUpperCase()+t.slice(1)};

var z={xmlns:"http://www.w3.org/2000/svg",width:24,height:24,viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:1.5,strokeLinecap:"round",strokeLinejoin:"round"};

const A=s=>{for(const t in s)if(t.startsWith("aria-")||t==="role"||t==="title")return!0;return!1};
const M=i.forwardRef(({color:s="currentColor",size:t=22,strokeWidth:o=1.5,absoluteStrokeWidth:n,className:r="",children:l,iconNode:a,...h},d)=>i.createElement("svg",{ref:d,...z,width:t,height:t,stroke:s,strokeWidth:n?Number(o)*24/Number(t):o,className:g("lucide",r),...!l&&!A(h)&&{"aria-hidden":"true"},...h},[...a.map(([v,k])=>i.createElement(v,k)),...Array.isArray(l)?l:[l]]));
const x=(s,t)=>{const o=i.forwardRef(({className:n,...r},l)=>i.createElement(M,{ref:l,iconNode:t,className:g(`lucide-${L(p(s))}`,`lucide-${s}`,n),...r}));return o.displayName=p(s),o};

const S=[["circle",{cx:"12",cy:"12",r:"10",key:"1mglay"}],["path",{d:"M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20",key:"13o1zl"}],["path",{d:"M2 12h20",key:"9i4pu4"}]],$=x("globe",S);
const E=[["path",{d:"M2 9.5a5.5 5.5 0 0 1 9.591-3.676.56.56 0 0 0 .818 0A5.49 5.49 0 0 1 22 9.5c0 2.29-1.5 4-3 5.5l-5.492 5.313a2 2 0 0 1-3 .019L5 15c-1.5-1.5-3-3.2-3-5.5",key:"mvr1a0"}]],W=x("heart",E);
const B=[["path",{d:"M4 6h16",key:"1tepv9"}],["path",{d:"M4 12h16",key:"1lakjw"}],["path",{d:"M4 18h16",key:"1djgab"}]],F=x("menu",B);
const O=[["path",{d:"M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2",key:"975kel"}],["circle",{cx:"12",cy:"7",r:"4",key:"17ys0d"}]],I=x("user",O);
const P=[["path",{d:"M18 6 6 18",key:"1bl5f8"}],["path",{d:"m6 6 12 12",key:"d8bk6v"}]],H=x("x",P);

const R="/zema-luxury/__l5e/assets-v1/f2909711-2a23-4d0d-9aa1-a574bce16e1f/zema-logo.png",u={url:R};

// WhatsApp Float
function D(){
  const s=`https://wa.me/${N}?text=${encodeURIComponent("مرحباً ZEMA Maison، أرغب بالاستفسار عن المنتجات وتأكيد الطلب")}`;
  return e.jsx("a",{
    href:s,
    target:"_blank",
    rel:"noopener noreferrer",
    "aria-label":"WhatsApp Client Care",
    className:"fixed bottom-6 end-6 z-50 flex h-13 w-13 items-center justify-center rounded-full bg-[#111111] text-[#faf9f7] hover:bg-[#222222] border border-white/10 shadow-2xl transition-all duration-300 hover:scale-105",
    children:e.jsx("svg",{width:"22",height:"22",viewBox:"0 0 24 24",fill:"currentColor","aria-hidden":!0,children:e.jsx("path",{d:"M.057 24l1.687-6.163a11.867 11.867 0 01-1.587-5.946C.16 5.335 5.495 0 12.05 0a11.82 11.82 0 018.413 3.488 11.82 11.82 0 013.48 8.414c-.003 6.555-5.338 11.89-11.893 11.89a11.9 11.9 0 01-5.688-1.448L.057 24zm6.597-3.807c1.676.995 3.276 1.591 5.392 1.592 5.448 0 9.886-4.434 9.889-9.885.002-5.462-4.415-9.89-9.881-9.892-5.452 0-9.887 4.434-9.889 9.884-.001 2.225.651 3.891 1.746 5.634l-.999 3.648 3.742-.981zm11.387-5.464c-.074-.124-.272-.198-.57-.347-.297-.149-1.758-.868-2.031-.967-.272-.099-.47-.149-.669.149-.198.297-.768.967-.941 1.165-.173.198-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.372-.025-.521-.075-.148-.669-1.611-.916-2.206-.242-.579-.487-.501-.669-.51l-.57-.01c-.198 0-.52.074-.792.372s-1.04 1.016-1.04 2.479 1.065 2.876 1.213 3.074c.149.198 2.095 3.2 5.076 4.487.709.306 1.263.489 1.694.626.712.226 1.36.194 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.695.248-1.29.173-1.414z"})})
  })
}

// Micro Announcement Bar
function U(){
  const{lang:l}=m(),isAr=l==="ar";
  return e.jsx("div",{className:"bg-[#0a0a0a] text-[#d6d3cd] text-[10px] tracking-[0.2em] uppercase py-2 border-b border-white/5 select-none text-center",children:
    e.jsx("div",{className:"mx-auto max-w-7xl px-4",children:
      e.jsx("span",{className:"font-medium",children:isAr?"معاينة الشحنة قبل الاستلام • شحن سريع لجميع المحافظات • استبدال خلال 14 يوماً":"CASH ON DELIVERY • FAST DELIVERY ACROSS EGYPT • 14-DAY RETURNS"})
    })
  })
}

// Search Modal
function V({open:s,onClose:t}){
  const o=y(),[n,r]=i.useState(""),{lang:l}=m(),isAr=l==="ar";
  i.useEffect(()=>{s||r("")},[s]);
  const q=n.trim().toLowerCase();
  const res=q?o.filter(a=>a.name.toLowerCase().includes(q)||(a.short&&a.short.toLowerCase().includes(q))||a.category.toLowerCase().includes(q)):o.slice(0,6);
  if(!s)return null;
  return e.jsx("div",{dir:isAr?"rtl":"ltr",className:"fixed inset-0 z-[100] bg-black/70 backdrop-blur-md overflow-y-auto flex items-start justify-center pt-20 px-4",onClick:t,children:
    e.jsxs("div",{className:"bg-[#faf9f7] w-full max-w-2xl p-6 md:p-8 shadow-2xl border border-stone-200",onClick:a=>a.stopPropagation(),children:[
      e.jsxs("div",{className:"flex items-center gap-3 border-b border-stone-300 pb-3",children:[
        e.jsx("input",{
          autoFocus:!0,
          value:n,
          onChange:a=>r(a.target.value),
          placeholder:isAr?"ابحث في مجموعة زِيما ميزون...":"Search ZEMA Maison collection...",
          className:"flex-1 bg-transparent text-lg md:text-xl font-light text-stone-900 focus:outline-none placeholder:text-stone-400"
        }),
        e.jsx("button",{onClick:t,"aria-label":"Close",className:"text-2xl text-stone-500 hover:text-stone-900 px-2 cursor-pointer",children:"×"})
      ]}),
      e.jsx("div",{className:"mt-6 space-y-3 max-h-[60vh] overflow-y-auto",children:
        res.length===0?
          e.jsx("p",{className:"text-stone-400 text-center py-10 text-sm",children:isAr?"لا توجد نتائج بحث مطابقة":"No pieces found."}):
          res.map(a=>e.jsxs(c,{to:"/zema-luxury/products/$id",params:{id:a.id},onClick:t,className:"flex items-center gap-4 p-2.5 hover:bg-stone-100 transition-colors",children:[
            e.jsx("img",{src:a.image,alt:a.name,className:"w-12 h-16 object-cover bg-stone-100"}),
            e.jsxs("div",{className:"flex-1",children:[
              e.jsx("p",{className:"font-medium text-xs tracking-wider uppercase text-stone-900",children:a.name}),
              e.jsx("p",{className:"text-[11px] text-stone-500 font-light",children:a.categoryLabel})
            ]}),
            e.jsxs("p",{className:"text-xs font-semibold text-stone-900",children:[a.priceArabic||a.price," ",isAr?"ج.م":"EGP"]})
          ]},a.id))
      })
    ]})
  })
}

// Language Switcher
function f({className:s=""}){
  const{lang:t,setLang:o}=m(),[n,r]=i.useState(!1);
  return e.jsxs("div",{className:`relative ${s}`,children:[
    e.jsx("button",{
      onClick:()=>r(a=>!a),
      "aria-label":"Language",
      className:"text-[11px] font-semibold tracking-widest text-stone-700 hover:text-stone-900 transition-colors uppercase px-1 py-1 cursor-pointer",
      children:t==="ar"?"EN":"AR"
    })
  ]})
}

// Primary Header
function G(){
  const[s,setS]=i.useState(!1), // search modal
  [o,setO]=i.useState(!1),       // mobile drawer
  [scrolled,setScrolled]=i.useState(!1),
  {t:r,dir:l,lang:t}=m(),
  {user:a}=w(),
  isAr=t==="ar";

  i.useEffect(()=>{
    const handleScroll=()=>setScrolled(window.scrollY>40);
    window.addEventListener("scroll",handleScroll,{passive:!0});
    return()=>window.removeEventListener("scroll",handleScroll);
  },[]);

  i.useEffect(()=>{
    if(typeof document!=="undefined")document.body.style.overflow=o?"hidden":"";
  },[o]);

  const navLinkClass="text-[11px] tracking-[0.18em] uppercase font-medium text-stone-700 hover:text-stone-950 transition-colors py-2 relative";

  return e.jsxs(e.Fragment,{children:[
    e.jsx(U,{}),
    e.jsxs("header",{
      className:`sticky top-0 z-40 transition-all duration-300 ${scrolled?"bg-[#faf9f7]/95 backdrop-blur-md border-b border-stone-200/80 shadow-xs":"bg-[#faf9f7] border-b border-stone-200/40"}`,
      children:[
        e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12 h-18 md:h-22 flex items-center justify-between gap-6",children:[
          // Left: ZEMA MAISON Logo & Mobile Menu Toggle
          e.jsxs("div",{className:"flex items-center gap-4",children:[
            e.jsx("button",{
              className:"lg:hidden p-1.5 text-stone-800 hover:text-stone-950 cursor-pointer",
              "aria-label":"Menu",
              onClick:()=>setO(!0),
              children:e.jsx(F,{size:20})
            }),
            e.jsx(c,{to:"/",className:"shrink-0",children:
              e.jsx("img",{src:u.url,alt:"ZEMA MAISON",className:"h-auto w-full max-w-[125px] md:max-w-[145px] select-none"})
            })
          ]}),

          // Center: Primary Editorial Desktop Navigation
          e.jsxs("nav",{className:"hidden lg:flex items-center justify-center gap-8 xl:gap-10",children:[
            // 1. SHOP Group with clean flyout/direct links
            e.jsxs("div",{className:"relative group",children:[
              e.jsx(c,{to:"/shop",className:navLinkClass,children:isAr?"المتجر":"SHOP"}),
              e.jsxs("div",{className:"absolute start-0 top-full pt-2 opacity-0 pointer-events-none group-hover:opacity-100 group-hover:pointer-events-auto transition-all duration-200",children:[
                e.jsxs("div",{className:"bg-[#faf9f7] border border-stone-200 shadow-xl py-3 px-5 min-w-[180px] space-y-2.5 text-[11px] tracking-[0.16em] uppercase",children:[
                  e.jsx(c,{to:"/shop",search:{category:"wallets"},className:"block text-stone-600 hover:text-stone-950 transition-colors",children:isAr?"محافظ":"Wallets"}),
                  e.jsx(c,{to:"/shop",search:{category:"bags"},className:"block text-stone-600 hover:text-stone-950 transition-colors",children:isAr?"حقائب نسائية":"Bags"}),
                  e.jsx(c,{to:"/shop",search:{category:"charms"},className:"block text-stone-600 hover:text-stone-950 transition-colors",children:isAr?"إكسسوارات شنط":"Charms"}),
                  e.jsx(c,{to:"/shop",search:{category:"bundles"},className:"block text-stone-900 font-semibold hover:text-stone-950 transition-colors pt-1 border-t border-stone-200",children:isAr?"بوكس زيما":"ZEMA Box"})
                ]})
              ]})
            ]}),

            // 2. DISCOVER Group
            e.jsxs("div",{className:"relative group",children:[
              e.jsx(c,{to:"/shop",search:{sort:"newest"},className:navLinkClass,children:isAr?"اكتشف":"DISCOVER"}),
              e.jsxs("div",{className:"absolute start-0 top-full pt-2 opacity-0 pointer-events-none group-hover:opacity-100 group-hover:pointer-events-auto transition-all duration-200",children:[
                e.jsxs("div",{className:"bg-[#faf9f7] border border-stone-200 shadow-xl py-3 px-5 min-w-[190px] space-y-2.5 text-[11px] tracking-[0.16em] uppercase",children:[
                  e.jsx(c,{to:"/shop",search:{sort:"newest"},className:"block text-stone-600 hover:text-stone-950 transition-colors",children:isAr?"وصل حديثاً":"New Arrivals"}),
                  e.jsx(c,{to:"/shop",search:{sort:"bestselling"},className:"block text-stone-600 hover:text-stone-950 transition-colors",children:isAr?"الأكثر مبيعاً":"Best Sellers"}),
                  e.jsx(c,{to:"/shop",search:{offers:1},className:"block text-stone-900 font-semibold hover:text-stone-950 transition-colors pt-1 border-t border-stone-200",children:isAr?"عروض التوفير":"Sale"})
                ]})
              ]})
            ]}),

            // Direct Category Links
            e.jsx(c,{to:"/shop",search:{category:"bags"},className:navLinkClass,children:isAr?"حقائب":"BAGS"}),
            e.jsx(c,{to:"/shop",search:{category:"wallets"},className:navLinkClass,children:isAr?"محافظ":"WALLETS"}),
            e.jsx(c,{to:"/shop",search:{category:"charms"},className:navLinkClass,children:isAr?"إكسسوارات شنط":"CHARMS"}),
            e.jsx(c,{to:"/shop",search:{category:"bundles"},className:navLinkClass,children:isAr?"بوكس زيما":"ZEMA BOX"}),

            // 3. ABOUT Group
            e.jsxs("div",{className:"relative group",children:[
              e.jsx(c,{to:"/about",className:navLinkClass,children:isAr?"عن زِيما":"ABOUT"}),
              e.jsxs("div",{className:"absolute start-0 top-full pt-2 opacity-0 pointer-events-none group-hover:opacity-100 group-hover:pointer-events-auto transition-all duration-200",children:[
                e.jsxs("div",{className:"bg-[#faf9f7] border border-stone-200 shadow-xl py-3 px-5 min-w-[200px] space-y-2.5 text-[11px] tracking-[0.16em] uppercase",children:[
                  e.jsx(c,{to:"/about",className:"block text-stone-600 hover:text-stone-950 transition-colors",children:isAr?"قصة الدار":"Our Story"}),
                  e.jsx(c,{to:"/faq",className:"block text-stone-600 hover:text-stone-950 transition-colors",children:isAr?"الأسئلة الشائعة":"FAQ"}),
                  e.jsx(c,{to:"/return-policy",className:"block text-stone-600 hover:text-stone-950 transition-colors",children:isAr?"المعاينة والاسترجاع":"Shipping & Returns"}),
                  e.jsx(c,{to:"/track",className:"block text-stone-600 hover:text-stone-950 transition-colors",children:isAr?"تتبع شحنتك":"Track Order"})
                ]})
              ]})
            ]})
          ]}),

          // Right Icons (Search, Lang, Wishlist, Cart)
          e.jsxs("div",{className:"flex items-center gap-3 md:gap-5",children:[
            e.jsx("button",{
              onClick:()=>setS(!0),
              "aria-label":"Search",
              className:"text-stone-700 hover:text-stone-950 transition-colors p-1 cursor-pointer",
              children:e.jsxs("svg",{width:"18",height:"18",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"1.5",children:[
                e.jsx("circle",{cx:"11",cy:"11",r:"7"}),
                e.jsx("path",{d:"m20 20-3.5-3.5"})
              ]})
            }),
            e.jsx(f,{}),
            e.jsx(c,{to:"/wishlist","aria-label":"Wishlist",className:"text-stone-700 hover:text-stone-950 transition-colors p-1 hidden sm:block",children:
              e.jsx(W,{size:19,strokeWidth:1.5})
            }),
            e.jsx(C,{})
          ]})
        ]})
      ]
    }),

    // Full-Screen Mobile Drawer
    o&&e.jsxs("div",{className:"fixed inset-0 z-50 lg:hidden",role:"dialog","aria-modal":"true",dir:l,children:[
      e.jsx("div",{className:"absolute inset-0 bg-black/60 backdrop-blur-xs",onClick:()=>setO(!1)}),
      e.jsxs("div",{className:"absolute inset-y-0 start-0 w-[85%] max-w-sm bg-[#faf9f7] border-e border-stone-200 flex flex-col justify-between p-6 shadow-2xl overflow-y-auto",children:[
        e.jsxs("div",{children:[
          e.jsxs("div",{className:"flex items-center justify-between pb-6 border-b border-stone-200",children:[
            e.jsx(c,{to:"/",onClick:()=>setO(!1),children:
              e.jsx("img",{src:u.url,alt:"ZEMA MAISON",className:"h-auto w-full max-w-[115px] select-none"})
            }),
            e.jsx("button",{onClick:()=>setO(!1),"aria-label":"Close",className:"p-1 text-stone-500 hover:text-stone-900",children:e.jsx(H,{size:20})})
          ]}),
          e.jsxs("nav",{className:"py-6 space-y-4 text-xs tracking-[0.18em] uppercase",onClick:()=>setO(!1),children:[
            e.jsx(c,{to:"/shop",search:{category:"bags"},className:"block py-2 text-stone-900 font-semibold border-b border-stone-200/60",children:isAr?"حقائب نسائية":"Bags"}),
            e.jsx(c,{to:"/shop",search:{category:"wallets"},className:"block py-2 text-stone-900 font-semibold border-b border-stone-200/60",children:isAr?"محافظ فاخرة":"Wallets"}),
            e.jsx(c,{to:"/shop",search:{category:"charms"},className:"block py-2 text-stone-900 font-semibold border-b border-stone-200/60",children:isAr?"إكسسوارات شنط":"Charms"}),
            e.jsx(c,{to:"/shop",search:{category:"bundles"},className:"block py-2 text-stone-900 font-semibold border-b border-stone-200/60",children:isAr?"بوكس زيما":"ZEMA Box"}),
            e.jsx(c,{to:"/shop",search:{sort:"newest"},className:"block py-2 text-stone-600 border-b border-stone-200/60",children:isAr?"وصل حديثاً":"New Arrivals"}),
            e.jsx(c,{to:"/shop",search:{sort:"bestselling"},className:"block py-2 text-stone-600 border-b border-stone-200/60",children:isAr?"الأكثر مبيعاً":"Best Sellers"}),
            e.jsx(c,{to:"/about",className:"block py-2 text-stone-600 border-b border-stone-200/60",children:isAr?"عن زِيما":"Our Story"}),
            e.jsx(c,{to:"/faq",className:"block py-2 text-stone-600 border-b border-stone-200/60",children:isAr?"الأسئلة الشائعة":"FAQ"}),
            e.jsx(c,{to:"/track",className:"block py-2 text-stone-600",children:isAr?"تتبع شحنتك":"Track Order"})
          ]})
        ]}),
        e.jsxs("div",{className:"pt-6 border-t border-stone-200 flex items-center justify-between text-xs",children:[
          e.jsx(f,{}),
          e.jsx("span",{className:"text-[10px] tracking-widest text-stone-400 uppercase",children:"ZEMA MAISON © 2026"})
        ]})
      ]})
    ]}),

    e.jsx(V,{open:s,onClose:()=>setS(!1)}),
    e.jsx(D,{})
  ]})
}

// Sophisticated Luxury Footer
function K(){
  const{lang:t,dir:l}=m(),isAr=t==="ar";
  return e.jsx("footer",{className:"bg-[#0c0c0c] text-[#f2efe9] pt-20 pb-12 select-none border-t border-white/5",dir:l,children:
    e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12",children:[
      e.jsxs("div",{className:"grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-10 pb-16 border-b border-white/10",children:[
        // Column 1: Brand & Tagline
        e.jsxs("div",{className:"lg:col-span-2 space-y-4",children:[
          e.jsx(c,{to:"/",className:"inline-block",children:
            e.jsx("img",{src:u.url,alt:"ZEMA MAISON",className:"h-auto w-full max-w-[120px] select-none brightness-0 invert opacity-95"})
          }),
          e.jsx("p",{className:"text-xs text-stone-400 font-light tracking-wide max-w-sm leading-relaxed",children:"Timeless Style, Modern Luxury. A modern luxury accessories brand crafted for discerning individuals."}),
          e.jsx("p",{className:"text-[11px] text-stone-500 tracking-[0.16em] uppercase pt-2",children:"Inspection Before Payment • Cairo, Egypt"})
        ]}),

        // Column 2: SHOP
        e.jsxs("div",{className:"space-y-3.5",children:[
          e.jsx("h4",{className:"text-[11px] font-semibold tracking-[0.22em] uppercase text-white",children:isAr?"المتجر":"SHOP"}),
          e.jsxs("ul",{className:"space-y-2.5 text-xs text-stone-400 font-light tracking-wider",children:[
            e.jsx("li",{children:e.jsx(c,{to:"/shop",search:{category:"wallets"},className:"hover:text-white transition-colors",children:isAr?"محافظ":"Wallets"})}),
            e.jsx("li",{children:e.jsx(c,{to:"/shop",search:{category:"bags"},className:"hover:text-white transition-colors",children:isAr?"حقائب":"Bags"})}),
            e.jsx("li",{children:e.jsx(c,{to:"/shop",search:{category:"charms"},className:"hover:text-white transition-colors",children:isAr?"إكسسوارات شنط":"Charms"})}),
            e.jsx("li",{children:e.jsx(c,{to:"/shop",search:{category:"bundles"},className:"hover:text-white transition-colors",children:isAr?"بوكس زيما":"ZEMA Box"})})
          ]})
        ]}),

        // Column 3: DISCOVER
        e.jsxs("div",{className:"space-y-3.5",children:[
          e.jsx("h4",{className:"text-[11px] font-semibold tracking-[0.22em] uppercase text-white",children:isAr?"اكتشف":"DISCOVER"}),
          e.jsxs("ul",{className:"space-y-2.5 text-xs text-stone-400 font-light tracking-wider",children:[
            e.jsx("li",{children:e.jsx(c,{to:"/shop",search:{sort:"newest"},className:"hover:text-white transition-colors",children:isAr?"وصل حديثاً":"New Arrivals"})}),
            e.jsx("li",{children:e.jsx(c,{to:"/shop",search:{sort:"bestselling"},className:"hover:text-white transition-colors",children:isAr?"الأكثر مبيعاً":"Best Sellers"})}),
            e.jsx("li",{children:e.jsx(c,{to:"/shop",search:{offers:1},className:"hover:text-white transition-colors",children:isAr?"عروض التوفير":"Sale"})})
          ]})
        ]}),

        // Column 4: ABOUT
        e.jsxs("div",{className:"space-y-3.5",children:[
          e.jsx("h4",{className:"text-[11px] font-semibold tracking-[0.22em] uppercase text-white",children:isAr?"عن الدار":"ABOUT"}),
          e.jsxs("ul",{className:"space-y-2.5 text-xs text-stone-400 font-light tracking-wider",children:[
            e.jsx("li",{children:e.jsx(c,{to:"/about",className:"hover:text-white transition-colors",children:isAr?"قصتنا":"Our Story"})}),
            e.jsx("li",{children:e.jsx(c,{to:"/faq",className:"hover:text-white transition-colors",children:isAr?"الأسئلة الشائعة":"FAQ"})}),
            e.jsx("li",{children:e.jsx(c,{to:"/return-policy",className:"hover:text-white transition-colors",children:isAr?"الشحن والاسترجاع":"Shipping & Returns"})}),
            e.jsx("li",{children:e.jsx(c,{to:"/track",className:"hover:text-white transition-colors",children:isAr?"تتبع شحنتك":"Track Order"})})
          ]})
        ]}),

        // Column 5: FOLLOW
        e.jsxs("div",{className:"space-y-3.5",children:[
          e.jsx("h4",{className:"text-[11px] font-semibold tracking-[0.22em] uppercase text-white",children:isAr?"تابعنا":"FOLLOW"}),
          e.jsxs("ul",{className:"space-y-2.5 text-xs text-stone-400 font-light tracking-wider",children:[
            e.jsx("li",{children:e.jsx("a",{href:"https://www.instagram.com/zema.luxury/",target:"_blank",rel:"noopener noreferrer",className:"hover:text-white transition-colors",children:"Instagram"})}),
            e.jsx("li",{children:e.jsx("a",{href:"https://www.facebook.com/zema.luxury/",target:"_blank",rel:"noopener noreferrer",className:"hover:text-white transition-colors",children:"Facebook"})}),
            e.jsx("li",{children:e.jsx("a",{href:"https://www.tiktok.com/",target:"_blank",rel:"noopener noreferrer",className:"hover:text-white transition-colors",children:"TikTok"})})
          ]})
        ]})
      ]}),

      // Bottom Row
      e.jsxs("div",{className:"pt-8 flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-stone-500 font-light tracking-wider",children:[
        e.jsx("p",{children:"© 2026 ZEMA Maison. All Rights Reserved."}),
        e.jsxs("div",{className:"flex items-center gap-6",children:[
          e.jsx(c,{to:"/privacy",className:"hover:text-stone-300 transition-colors",children:isAr?"سياسة الخصوصية":"Privacy Policy"}),
          e.jsx(c,{to:"/return-policy",className:"hover:text-stone-300 transition-colors",children:isAr?"الشروط والأحكام":"Terms of Service"})
        ]})
      ]})
    ]})
  })
}

export{G as S,K as F,D as W,f as a,U as b,V as X};
