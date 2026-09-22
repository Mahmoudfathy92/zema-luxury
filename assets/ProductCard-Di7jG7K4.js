import{h as v,u as N,r as i,i as k,q as y,t as S,e as C,j as e,L as u,d as x}from"./index-uamL4pK8.js";

function P({p:t}){
  const{add:f}=v(),{t:o,lang:l}=N(),isAr=l==="ar",[m,a]=i.useState(0),
  gallery=t.gallery&&t.gallery.length>0?t.gallery:[t.image],
  price=C(t);
  
  return e.jsxs("div",{className:"group flex h-full flex-col bg-transparent select-none",children:[
    e.jsxs(u,{
      to:"/zema-luxury/products/$id",
      params:{id:t.id},
      className:"block relative overflow-hidden bg-[#f4f2ee] aspect-[3/4]",
      onMouseEnter:()=>gallery.length>1&&a(1),
      onMouseLeave:()=>a(0),
      children:[
        e.jsx("img",{
          src:gallery[m],
          alt:t.name,
          loading:"lazy",
          decoding:"async",
          className:"w-full h-full object-cover transition-transform duration-[850ms] group-hover:scale-[1.04]"
        }),
        e.jsx("div",{
          className:"absolute inset-x-3 bottom-3 hidden md:flex items-center justify-center opacity-0 translate-y-2 transition-all duration-300 group-hover:opacity-100 group-hover:translate-y-0",
          children:e.jsx("button",{
            onClick:(ev)=>{ev.preventDefault();ev.stopPropagation();f(t.id)},
            className:"w-full bg-[#0e0e0e]/95 hover:bg-[#0e0e0e] text-[#faf9f7] py-3 text-[11px] font-semibold tracking-[0.18em] uppercase transition-colors shadow-lg cursor-pointer",
            children:isAr?"إضافة إلى الحقيبة":"ADD TO BAG"
          })
        })
      ]
    }),
    e.jsxs("div",{className:"pt-3.5 pb-1 flex flex-col flex-1",children:[
      e.jsx(u,{
        to:"/zema-luxury/products/$id",
        params:{id:t.id},
        className:"hover:opacity-75 transition-opacity",
        children:e.jsx("h4",{className:"text-[13px] md:text-[14px] font-semibold tracking-[0.08em] uppercase text-foreground leading-snug line-clamp-1",children:t.name})
      }),
      t.short&&e.jsx("p",{className:"text-[11px] text-stone-500 font-light tracking-wide mt-0.5 line-clamp-1",children:t.short}),
      e.jsxs("div",{className:"flex items-baseline justify-between gap-2 mt-2 pt-1 border-t border-stone-200/50",children:[
        e.jsxs("p",{className:"text-[13px] font-medium text-foreground tracking-wide",children:[
          e.jsx("span",{className:"ltr-num",children:isAr?t.priceArabic||x(price):x(price)}),
          " ",
          e.jsx("span",{className:"text-[11px] font-normal text-stone-400",children:isAr?"ج.م":"EGP"})
        ]}),
        e.jsx("button",{
          onClick:(ev)=>{ev.preventDefault();f(t.id)},
          "aria-label":isAr?"إضافة":"Add",
          className:"md:hidden text-[11px] font-semibold tracking-wider text-stone-900 underline underline-offset-4 hover:opacity-70 cursor-pointer",
          children:isAr?"+ إضافة":"+ ADD"
        })
      ]})
    ]})
  ]})
}
export{P};
