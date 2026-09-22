import{r as i,j as e,p as S,h as z,u as M,a as P,i as L,q as $,t as E,e as k,L as C,d as j}from"./index-uamL4pK8.js";import{S as R,a as Y,F as I}from"./SiteChrome-vAcelVMJ.js";function X({images:s,startIndex:N=0,alt:l,onClose:b}){const[y,p]=i.useState(N),[d,c]=i.useState(1),[x,u]=i.useState({x:0,y:0}),n=i.useRef(null),m=i.useRef(null);i.useEffect(()=>{const t=o=>{o.key==="Escape"&&b(),o.key==="ArrowRight"&&h(),o.key==="ArrowLeft"&&a()};return document.addEventListener("keydown",t),document.body.style.overflow="hidden",()=>{document.removeEventListener("keydown",t),document.body.style.overflow=""}},[]);const g=()=>{c(1),u({x:0,y:0})},h=()=>{p(t=>(t+1)%s.length),g()},a=()=>{p(t=>(t-1+s.length)%s.length),g()},f=()=>{c(t=>t>1?1:2.2),u({x:0,y:0})},v=t=>{t.preventDefault();const o=-t.deltaY*.0015;c(w=>Math.min(4,Math.max(1,w+o)))},r=(t,o)=>Math.hypot(t.clientX-o.clientX,t.clientY-o.clientY);return e.jsxs("div",{className:"fixed inset-0 z-[100] bg-black/95 flex items-center justify-center",onClick:b,children:[e.jsx("button",{onClick:t=>{t.stopPropagation(),b()},"aria-label":"Close",className:"absolute top-4 right-4 z-10 h-11 w-11 rounded-full bg-white/10 hover:bg-white/20 text-white flex items-center justify-center text-2xl",children:"×"}),s.length>1&&e.jsxs(e.Fragment,{children:[e.jsx("button",{onClick:t=>{t.stopPropagation(),a()},"aria-label":"Previous",className:"absolute left-3 md:left-6 z-10 h-12 w-12 rounded-full bg-white/10 hover:bg-white/20 text-white flex items-center justify-center text-2xl",children:"‹"}),e.jsx("button",{onClick:t=>{t.stopPropagation(),h()},"aria-label":"Next",className:"absolute right-3 md:right-6 z-10 h-12 w-12 rounded-full bg-white/10 hover:bg-white/20 text-white flex items-center justify-center text-2xl",children:"›"})]}),e.jsxs("div",{className:"absolute bottom-20 left-1/2 -translate-x-1/2 z-10 flex items-center gap-2 bg-white/10 backdrop-blur rounded-full px-2 py-1.5",onClick:t=>t.stopPropagation(),children:[e.jsx("button",{onClick:()=>c(t=>Math.max(1,t-.4)),"aria-label":"Zoom out",className:"h-8 w-8 rounded-full hover:bg-white/10 text-white text-lg flex items-center justify-center",children:"−"}),e.jsxs("span",{className:"text-white/80 text-xs ltr-num w-10 text-center",children:[Math.round(d*100),"%"]}),e.jsx("button",{onClick:()=>c(t=>Math.min(4,t+.4)),"aria-label":"Zoom in",className:"h-8 w-8 rounded-full hover:bg-white/10 text-white text-lg flex items-center justify-center",children:"+"}),e.jsx("button",{onClick:g,"aria-label":"Reset",className:"h-8 px-3 rounded-full hover:bg-white/10 text-white text-[11px] uppercase tracking-wider",children:"Reset"})]}),e.jsx("div",{className:"w-full h-full flex items-center justify-center p-6 overflow-hidden touch-none select-none",onClick:t=>t.stopPropagation(),onDoubleClick:f,onWheel:v,onMouseDown:t=>{d>1&&(n.current={x:t.clientX-x.x,y:t.clientY-x.y})},onMouseMove:t=>{n.current&&u({x:t.clientX-n.current.x,y:t.clientY-n.current.y})},onMouseUp:()=>{n.current=null},onMouseLeave:()=>{n.current=null},onTouchStart:t=>{t.touches.length===2?m.current={dist:r(t.touches[0],t.touches[1]),zoom:d}:t.touches.length===1&&d>1&&(n.current={x:t.touches[0].clientX-x.x,y:t.touches[0].clientY-x.y})},onTouchMove:t=>{if(t.touches.length===2&&m.current){const o=r(t.touches[0],t.touches[1]),w=m.current.zoom*(o/m.current.dist);c(Math.min(4,Math.max(1,w)))}else t.touches.length===1&&n.current&&u({x:t.touches[0].clientX-n.current.x,y:t.touches[0].clientY-n.current.y})},onTouchEnd:t=>{t.touches.length===0&&(n.current=null,m.current=null)},children:e.jsx("img",{src:s[y],alt:l,draggable:!1,className:"max-h-full max-w-full",style:{transform:`translate(${x.x}px, ${x.y}px) scale(${d})`,transition:n.current||m.current?"none":"transform 0.25s cubic-bezier(0.22, 1, 0.36, 1)",cursor:d>1?n.current?"grabbing":"grab":"zoom-in",willChange:"transform"},onClick:f})}),e.jsxs("div",{className:"absolute bottom-4 left-1/2 -translate-x-1/2 text-white/60 text-[11px] tracking-wide",children:[y+1," / ",s.length," — Double-tap / pinch to zoom"]})]})}function O(){
  const{product:s}=S.useLoaderData(),{add:N}=z(),{t:l,dir:b,lang:y}=M(),isAr=y==="ar",
  [p,d]=i.useState(0),[c,x]=i.useState(0),[u,n]=i.useState(null),
  allProds=P(),
  crossSellItems=allProds.filter(r=>s.crossSellIds?s.crossSellIds.includes(r.id):(r.id!==s.id&&r.category!==s.category)).slice(0,3),
  h=L(s),a=$(s),f=E(s),v=k(s);

  return e.jsxs("div",{className:"min-h-screen bg-background text-foreground select-none",dir:b,lang:y,children:[
    e.jsx(R,{}),
    e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12 py-5 text-xs text-muted-foreground flex items-center justify-between border-b hairline",children:[
      e.jsxs("div",{className:"flex items-center gap-2",children:[
        e.jsx(C,{to:"/",className:"hover:text-accent",children:isAr?"الرئيسية":"Home"}),
        e.jsx("span",{className:"opacity-40",children:"/"}),
        e.jsx(C,{to:"/shop",search:{category:s.category},className:"hover:text-accent font-medium",children:s.categoryLabel||(isAr?"المجموعة":"Collection")}),
        e.jsx("span",{className:"opacity-40",children:"/"}),
        e.jsx("span",{className:"text-foreground font-semibold truncate max-w-[140px] sm:max-w-none",children:isAr?(s.nameAr||s.name):s.name})
      ]}),
      e.jsx(C,{to:"/shop",className:"text-accent hover:underline font-bold text-xs",children:isAr?"← تصفح كل التشكيلة":"← All Collections"})
    ]}),
    e.jsxs("section",{className:"mx-auto max-w-7xl px-5 lg:px-12 py-10 lg:py-16 grid lg:grid-cols-2 gap-10 lg:gap-14",children:[
      e.jsxs("div",{className:"space-y-4",children:[
        e.jsxs("button",{onClick:()=>n(p),className:"block aspect-[4/5] sm:aspect-square w-full overflow-hidden rounded-2xl border hairline bg-card cursor-zoom-in relative group shadow-sm","aria-label":"zoom",children:[
          e.jsx("img",{src:s.gallery[p]||s.image,alt:s.name,fetchPriority:"high",decoding:"async",className:`w-full h-full object-cover transition-transform duration-500 group-hover:scale-[1.03] ${a?"":"opacity-50"}`}),
          h&&e.jsxs("span",{className:"absolute top-4 start-4 bg-destructive text-destructive-foreground text-xs font-bold px-3 py-1.5 rounded-full ltr-num shadow",children:["-",f,"% ",isAr?"خصم":"OFF"]}),
          s.limited&&e.jsx("span",{className:"absolute top-4 end-4 bg-accent text-accent-foreground text-[10px] font-bold px-3 py-1 rounded-full uppercase tracking-wider shadow",children:isAr?"إصدار محدود":"LIMITED"})
        ]}),
        s.gallery.length>1&&e.jsx("div",{className:"grid grid-cols-4 gap-3",children:
          s.gallery.map((r,t)=>e.jsx("button",{key:t,onClick:()=>d(t),className:`aspect-square rounded-xl overflow-hidden border transition-all ${t===p?"border-accent ring-2 ring-accent/30":"hairline opacity-75 hover:opacity-100"}`,children:e.jsx("img",{src:r,alt:"",loading:"lazy",className:"w-full h-full object-cover"})}))
        })
      ]}),
      e.jsxs("div",{className:"space-y-6",children:[
        e.jsxs("div",{className:"flex items-center justify-between",children:[
          e.jsx("span",{className:"text-[10px] tracking-[0.25em] uppercase text-accent font-bold",children:s.sku||"ZEMA LUXE"}),
          e.jsx("span",{className:`text-xs font-bold px-2.5 py-1 rounded-full ${a?"bg-emerald-500/10 text-emerald-500 border border-emerald-500/20":"bg-rose-500/10 text-rose-500"}`,children:a?(isAr?"✓ متوفر بالمخزون":"✓ In Stock"):(isAr?"نفذت الكمية":"Out of Stock")})
        ]}),
        e.jsx("h1",{className:"display-serif text-3xl sm:text-4xl md:text-5xl font-bold leading-tight tracking-tight",children:isAr?(s.nameAr||s.name):s.name}),
        e.jsx("p",{className:"text-xs sm:text-sm text-stone-300 leading-relaxed font-light",children:s.short}),
        e.jsxs("div",{className:"flex items-baseline gap-3 py-2 border-y hairline",children:[
          e.jsxs("span",{className:"text-3xl sm:text-4xl font-bold text-foreground",children:[e.jsx("span",{className:"ltr-num",children:j(v)})," ",e.jsx("span",{className:"text-sm font-semibold text-muted-foreground",children:isAr?"ج.م":"EGP"})]}),
          h&&e.jsxs(e.Fragment,{children:[
            e.jsx("span",{className:"text-base text-muted-foreground line-through ltr-num",children:j(s.price)}),
            e.jsxs("span",{className:"bg-destructive/15 text-destructive border border-destructive/30 text-xs font-bold px-2 py-0.5 rounded ltr-num",children:["-",f,"%"]})
          ]})
        ]}),
        e.jsx("p",{className:"text-xs sm:text-sm leading-relaxed text-foreground/85",children:s.description}),
        e.jsxs("div",{className:"flex gap-3 pt-2",children:[
          e.jsx("button",{onClick:()=>N(s.id),disabled:!a,className:"flex-1 bg-accent text-accent-foreground py-4 text-xs font-bold tracking-[0.2em] uppercase rounded-xl hover:opacity-90 transition-opacity shadow-lg disabled:opacity-40 disabled:cursor-not-allowed cursor-pointer",children:a?(isAr?"أضيفي للحقيبة":"ADD TO BAG"):(isAr?"غير متوفر":"OUT OF STOCK")})
        ]}),
        a&&e.jsxs("div",{className:"flex items-center justify-center gap-2 py-2 px-3 rounded-lg bg-amber-500/10 border border-amber-500/20 text-xs font-medium text-amber-400 select-none",children:[
          e.jsx("span",{className:"inline-block w-2 h-2 rounded-full bg-amber-400 animate-pulse"}),
          e.jsx("span",{children:isAr?`باقي ${((s.id.split('').reduce((acc,ch)=>acc+ch.charCodeAt(0),0)%4)+2)} قطع فقط في المخزن`:`Only ${((s.id.split('').reduce((acc,ch)=>acc+ch.charCodeAt(0),0)%4)+2)} pieces left in stock`})
        ]}),
        e.jsxs("div",{className:"rounded-2xl border hairline bg-card/60 p-5 space-y-3.5 text-xs text-muted-foreground",children:[
          e.jsx("h4",{className:"text-xs font-bold tracking-wider uppercase text-foreground mb-1",children:isAr?"📋 المواصفات الفاخرة للقطعة":"Product Specifications"}),
          s.dimensions&&e.jsxs("div",{className:"flex items-start justify-between py-1.5 border-b hairline",children:[
            e.jsx("span",{className:"text-foreground font-semibold",children:isAr?"الأبعاد والمقاس:":"Dimensions:"}),
            e.jsx("span",{className:"text-end font-medium text-foreground",children:s.dimensions})
          ]}),
          s.interior&&e.jsxs("div",{className:"flex items-start justify-between py-1.5 border-b hairline",children:[
            e.jsx("span",{className:"text-foreground font-semibold shrink-0 me-3",children:isAr?"التقسيم الداخلي:":"Interior:"}),
            e.jsx("span",{className:"text-end font-medium text-foreground",children:s.interior})
          ]}),
          s.material&&e.jsxs("div",{className:"flex items-start justify-between py-1.5 border-b hairline",children:[
            e.jsx("span",{className:"text-foreground font-semibold",children:isAr?"نوع الخامة:":"Material:"}),
            e.jsx("span",{className:"text-end font-medium text-foreground",children:s.material})
          ]}),
          s.hardware&&e.jsxs("div",{className:"flex items-start justify-between py-1.5",children:[
            e.jsx("span",{className:"text-foreground font-semibold",children:isAr?"لون المعادن:":"Hardware:"}),
            e.jsx("span",{className:"text-end font-medium text-foreground",children:s.hardware})
          ]})
        ]}),
        e.jsxs("div",{className:"rounded-2xl border border-emerald-500/20 bg-emerald-500/5 p-4 space-y-2 text-xs text-emerald-300 font-medium",children:[
          e.jsx("p",{children:isAr?"✨ متاح فتح الشحنة ومعاينتها بالكامل مع المندوب قبل دفع أي مبلغ.":"✨ Full package inspection with the courier before paying."}),
          e.jsx("p",{children:isAr?"🚚 شحن مجاني لكافة الطلبات فوق 1,500 ج.م + ضمان استبدال ميسر 14 يوماً.":"🚚 Free shipping over 1,500 EGP + 14-day hassle-free exchange."})
        ]})
      ]})
    ]}),
    crossSellItems.length>0&&e.jsx("section",{id:"cross-selling",className:"border-t hairline bg-sand/20 py-16",children:
      e.jsxs("div",{className:"mx-auto max-w-7xl px-5 lg:px-12",children:[
        e.jsxs("div",{className:"text-center mb-10",children:[
          e.jsx("p",{className:"text-[10px] tracking-[0.3em] uppercase text-accent font-semibold mb-2",children:isAr?"أكملي أناقتك":"COMPLETE THE LOOK"}),
          e.jsx("h2",{className:"display-serif text-2xl sm:text-4xl font-bold tracking-tight",children:isAr?"قطع متناسقة تكمل إطلالتك":"Curated Pairings & Accessories"})
        ]}),
        e.jsx("div",{className:"grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6",children:
          crossSellItems.map(item=>e.jsxs("div",{key:item.id,className:"rounded-2xl bg-card border hairline p-4 space-y-3 group shadow-sm",children:[
            e.jsxs(C,{to:`/products/${item.id}`,className:"block aspect-[4/5] rounded-xl overflow-hidden bg-background relative",children:[
              e.jsx("img",{src:item.image,alt:item.name,className:"w-full h-full object-cover transition-transform duration-500 group-hover:scale-[1.04]"}),
              e.jsx("span",{className:"absolute top-3 start-3 px-2.5 py-1 rounded-full bg-black/70 text-white text-[10px] font-bold",children:item.categoryLabel})
            ]}),
            e.jsxs("div",{className:"space-y-1",children:[
              e.jsx(C,{to:`/products/${item.id}`,className:"block text-sm font-bold hover:text-accent transition-colors truncate",children:isAr?(item.nameAr||item.name):item.name}),
              e.jsxs("p",{className:"text-xs font-semibold text-accent",children:[j(item.price)," ",isAr?"ج.م":"EGP"]})
            ]}),
            e.jsx("button",{onClick:()=>N(item.id),className:"w-full py-2.5 rounded-lg bg-foreground text-background hover:bg-accent hover:text-accent-foreground text-xs font-bold transition-colors cursor-pointer",children:isAr?"+ أضيفي للحقيبة":"+ Quick Add"})
          ]}))
        })
      ]})
    }),
    e.jsx(Y,{}),
    e.jsx(I,{})
  ]})
}

export{O as component};
