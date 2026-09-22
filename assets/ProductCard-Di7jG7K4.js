import{h as v,u as N,r as i,i as k,q as y,t as S,e as C,j as e,L as u,d as x}from"./index-uamL4pK8.js";
function P({p:t}){
  const{add:f}=v(),{t:o}=N(),[m,a]=i.useState(0),[g,b]=i.useState(0),
  l=t.gallery.length>0?t.gallery:[t.image],
  n=k(t),s=y(t),h=S(t),p=C(t);
  
  return e.jsxs("div",{className:"group flex h-full flex-col select-none",children:[
    e.jsxs(u,{to:"/zema-luxury/products/$id",params:{id:t.id},className:"block relative",onMouseEnter:()=>l.length>1&&a(1),onMouseLeave:()=>a(0),children:[
      e.jsx("div",{className:"aspect-[3/4] overflow-hidden rounded-2xl bg-[#f4f2ee]/70 border hairline relative group-hover:shadow-md transition-all duration-500",children:
        e.jsx("img",{src:l[m],alt:t.name,loading:"lazy",decoding:"async",className:`w-full h-full object-cover transition-transform duration-[800ms] ease-out group-hover:scale-[1.04] ${s?"":"opacity-50"}`})
      }),
      n&&e.jsxs("span",{className:"absolute top-3.5 start-3.5 bg-foreground/90 backdrop-blur-sm text-background text-[9px] font-semibold px-2.5 py-1 rounded-full tracking-wider ltr-num shadow-sm",children:["-",h,"%"]}),
      t.bestseller&&!n&&e.jsx("span",{className:"absolute top-3.5 end-3.5 bg-background/90 backdrop-blur-sm text-foreground text-[9px] font-semibold px-2.5 py-1 rounded-full border hairline tracking-wide",children:o("p.bestseller")}),
      !s&&e.jsx("span",{className:"absolute inset-0 flex items-center justify-center bg-background/70 backdrop-blur-[2px] text-foreground text-xs font-semibold uppercase tracking-wider",children:o("p.outOfStock")})
    ]}),
    e.jsxs("div",{className:"pt-4 flex flex-col flex-1",children:[
      e.jsx(u,{to:"/zema-luxury/products/$id",params:{id:t.id},className:"hover:text-foreground/75 transition-colors",children:
        e.jsx("h4",{className:"font-serif text-[15px] sm:text-[16px] font-medium mb-1 leading-snug line-clamp-1 tracking-wide text-foreground",children:t.name})
      }),
      e.jsx("p",{className:"text-[11px] text-muted-foreground/80 mb-2.5 line-clamp-1 leading-relaxed font-light",children:t.short}),
      t.colors&&t.colors.length>0&&e.jsx("div",{className:"flex items-center gap-1.5 mb-3",children:
        t.colors.map((r,d)=>e.jsx("button",{
          onClick:j=>{j.preventDefault();b(d);if(r.image){const c=l.indexOf(r.image);c>=0&&a(c)}},
          "aria-label":r.name,
          title:r.name,
          className:`h-3.5 w-3.5 rounded-full border transition-all ${g===d?"border-foreground ring-2 ring-foreground/20 ring-offset-2 ring-offset-background":"border-border hover:border-foreground/40"}`,
          style:{backgroundColor:r.hex}
        },r.name))
      }),
      e.jsxs("div",{className:"flex items-baseline gap-2 mt-auto mb-3.5",children:[
        e.jsxs("p",{className:"font-medium text-foreground text-[14px] sm:text-[15px]",children:[
          e.jsx("span",{className:"ltr-num",children:x(p)})," ",
          e.jsx("span",{className:"text-[12px] text-muted-foreground font-normal",children:o("cart.egp")})
        ]}),
        n&&e.jsx("span",{className:"text-[11px] text-muted-foreground line-through ltr-num",children:x(t.price)}),
        e.jsx("span",{className:`ms-auto text-[10px] ${s?"text-emerald-700":"text-destructive"} font-light`,children:s?`● ${o("p.inStock")}`:`● ${o("p.outOfStock")}`})
      ]}),
      e.jsx("button",{
        onClick:()=>f(t.id),
        disabled:!s,
        className:"w-full rounded-full border border-foreground/30 bg-transparent text-foreground hover:bg-foreground hover:text-background py-2.5 sm:py-3 text-[11px] font-medium tracking-[0.14em] uppercase transition-all duration-300 shadow-none active:scale-[0.98] disabled:opacity-40 disabled:cursor-not-allowed cursor-pointer",
        children:o(s?"p.addToCart":"p.outOfStock")
      })
    ]})
  ]})
}
export{P};
