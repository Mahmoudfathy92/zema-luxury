import{b as i,c as l,r as x,j as e,L as a,O as d}from"./index-uamL4pK8.js";
function o(){
  const{user:s,signOut:n}=i();
  const[auth,setAuth]=x.useState(()=>localStorage.getItem("zema_admin_key")==="zema2026");
  const[pass,setPass]=x.useState("");
  const[err,setErr]=x.useState(false);

  const handleLogin=(ev)=>{
    ev.preventDefault();
    if(pass.trim()==="zema2026"||pass.trim()==="2026"||pass.trim()==="admin"){
      localStorage.setItem("zema_admin_key","zema2026");
      setAuth(true);
      setErr(false);
    }else{
      setErr(true);
    }
  };

  const handleLogout=()=>{
    localStorage.removeItem("zema_admin_key");
    setAuth(false);
    n();
  };

  if(!auth){
    return e.jsx("div",{dir:"rtl",className:"min-h-screen bg-[#0d0d0d] text-[#e5e5e5] flex items-center justify-center px-5 font-sans",children:
      e.jsxs("div",{className:"max-w-sm w-full bg-[#161616] border border-[#2a2a2a] p-8 shadow-2xl text-center rounded-xl",children:[
        e.jsx("div",{className:"w-12 h-12 mx-auto mb-4 rounded-full bg-accent/10 border border-accent/30 flex items-center justify-center text-accent text-xl",children:"🔒"}),
        e.jsx("h2",{className:"text-xl font-bold tracking-tight mb-1 text-white",children:"لوحة إدارة دار زِيما"}),
        e.jsx("p",{className:"text-xs text-muted-foreground mb-6",children:"الوصول مقتصر فقط على مالك المتجر المصرح له"}),
        e.jsxs("form",{onSubmit:handleLogin,className:"space-y-4",children:[
          e.jsx("input",{
            type:"password",
            required:true,
            autoFocus:true,
            placeholder:"أدخل كلمة مرور الإدارة...",
            value:pass,
            onChange:t=>{setPass(t.target.value);setErr(false);},
            className:"w-full bg-[#0a0a0a] border border-[#333] focus:border-accent px-4 py-3 text-sm text-center tracking-widest text-white outline-none rounded transition-all"
          }),
          err&&e.jsx("p",{className:"text-xs text-rose-500 font-semibold",children:"كلمة المرور غير صحيحة، حاول مجدداً"}),
          e.jsx("button",{
            type:"submit",
            className:"w-full bg-accent text-accent-foreground hover:opacity-95 font-bold py-3 text-sm rounded shadow-lg transition-all active:scale-[0.98] cursor-pointer",
            children:"دخول إلى لوحة التحكم ←"
          })
        ]}),
        e.jsx(a,{to:"/",className:"inline-block mt-6 text-xs text-muted-foreground hover:text-white transition-colors",children:"العودة إلى المتجر الرئيسي"})
      ]})
    });
  }

  return e.jsxs("div",{dir:"rtl",className:"min-h-screen bg-background text-foreground",children:[
    e.jsx("header",{className:"border-b hairline bg-card/60 backdrop-blur-md sticky top-0 z-30",children:
      e.jsxs("div",{className:"max-w-7xl mx-auto px-5 py-4 flex items-center justify-between",children:[
        e.jsxs("div",{className:"flex items-center gap-6",children:[
          e.jsx(a,{to:"/",className:"font-bold text-accent text-lg tracking-wider",children:"ZEMA"}),
          e.jsxs("nav",{className:"flex items-center gap-2 text-sm font-semibold",children:[
            e.jsx(a,{to:"/admin/orders",className:"hover:text-accent px-3 py-1.5 rounded hover:bg-card transition-colors",activeProps:{className:"text-accent font-bold bg-card border hairline"},children:"📋 الطلبات"}),
            e.jsx(a,{to:"/admin/shipping",className:"hover:text-accent px-3 py-1.5 rounded hover:bg-card transition-colors",activeProps:{className:"text-accent font-bold bg-card border hairline"},children:"🚚 الشحن"})
          ]})
        ]}),
        e.jsxs("div",{className:"flex items-center gap-4",children:[
          e.jsx("span",{className:"text-xs text-accent font-bold bg-accent/10 px-3 py-1 rounded border border-accent/20 hidden sm:inline",children:"مدير المتجر (Admin) 🛡️"}),
          e.jsx("button",{onClick:handleLogout,className:"text-xs bg-card hover:bg-destructive hover:text-white border hairline px-3 py-1.5 rounded font-semibold transition-colors cursor-pointer",children:"قفل اللوحة 🔒"})
        ]})
      ]})
    }),
    e.jsx("main",{className:"max-w-7xl mx-auto px-5 py-8",children:e.jsx(d,{})})
  ]});
}
export{o as component};
