(this.webpackJsonpkrampus2=this.webpackJsonpkrampus2||[]).push([[0],{380:function(o,t,e){"use strict";e.r(t);var n=e(4),r=e.n(n),l=e(82),a=e.n(l),c=(e(93),e(94),e(398)),i=e(83),s=e.n(i),f=e(6),p=e.n(f),x=e(62),d=e(84),u=e(85),F=e(7),b={borderRadius:"50%",borderColor:"#000",borderWidth:"1px",borderStyle:"solid",backgroundColor:"#000",color:"#fff",cursor:"pointer",float:"left",height:"70px",lineHeight:"48px",margin:"5px",padding:"10px",width:"70px"},C={borderColor:"#FFF",transform:"scale(0.98)",boxShadow:"3px 2px 22px 1px rgba(0, 0, 0, 0.24)"},h={width:55,height:55};var g=function(o){var t=Object(d.a)({},b);return t.backgroundColor=o.color,t.color=o.textColor,o.data.icon&&(t.lineHeight="55px",t.padding="0px"),"blank"===o.data.action&&(t.borderColor="#fff",t.cursor="default"),Object(F.jsx)("div",{style:t,activeStyle:C,onClick:function(t){o.onClick&&o.onClick(o.data)},children:Object(F.jsx)(u.Textfit,{mode:"single",children:o.data.icon?Object(F.jsx)(o.data.icon,{style:h}):o.text})})},m=e(391),j=e(392),y=e(393),v=e(394),O=e(395),S={borderColor:"#333",borderStyle:"solid",borderWidth:"3px",borderRadius:"15px",marginBottom:"5px",padding:"10px",width:"350px",boxShadow:"rgba(50, 50, 93, 0.25) 0px 30px 60px -12px, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px"},k=[{color:"#FF0000",textColor:"#FFF",text:"On",icon:null,action:"On"},{color:"#000000",textColor:"#FFF",text:"Off",icon:null,action:"Off"},{color:"#ffffff",textColor:"#fff",text:"",icon:null,action:"blank"},{color:"#ffffff",textColor:"#000",text:"Loop",icon:m.a,action:"Loop"},{color:"#ffffff",textColor:"#000",text:"Delay Up",icon:j.a,action:"DelayUp"},{color:"#ffffff",textColor:"#000",text:"Delay Dn",icon:y.a,action:"DelayDn"},{color:"#ffffff",textColor:"#000",text:"Brightnes Dn",icon:v.a,action:"BrightnessDn"},{color:"#ffffff",textColor:"#000",text:"Brightness Up",icon:O.a,action:"BrightnessUp"},{color:"#FF0000",textColor:"#FFF",text:"R",icon:null,action:"SetTreeColor"},{color:"#00FF00",textColor:"#FFF",text:"G",icon:null,action:"SetTreeColor"},{color:"#0000FF",textColor:"#FFF",text:"B",icon:null,action:"SetTreeColor"},{color:"#FFFFFF",textColor:"#000",text:"W",icon:null,action:"SetTreeColor"},{color:"#ff3333",textColor:"#FFF",text:"",icon:null,action:"SetTreeColor"},{color:"#33ff33",textColor:"#FFF",text:"",icon:null,action:"SetTreeColor"},{color:"#3333ff",textColor:"#FFF",text:"",icon:null,action:"SetTreeColor"},{color:"#FFEE58",textColor:"#FFF",text:"",icon:null,action:"SetTreeColor"},{color:"#ff6666",textColor:"#FFF",text:"",icon:null,action:"SetTreeColor"},{color:"#66ff66",textColor:"#FFF",text:"",icon:null,action:"SetTreeColor"},{color:"#6666ff",textColor:"#FFF",text:"",icon:null,action:"SetTreeColor"},{color:"#ffa500",textColor:"#FFF",text:"",icon:null,action:"SetTreeColor"},{color:"#800080",textColor:"#FFF",text:"",icon:null,action:"SetTreeColor"},{color:"#40E0D0",textColor:"#FFF",text:"",icon:null,action:"SetTreeColor"}],T={On:"/api/start",Off:"/api/stop",Loop:"/api/loop",SetTreeColor:"/api/color/change/",DelayUp:"/api/delayUp",DelayDn:"/api/delayDown",BrightnessUp:"/api/brightnessUp",BrightnessDn:"/api/brightnessDown"};function w(o){return D.apply(this,arguments)}function D(){return(D=Object(x.a)(p.a.mark((function o(t){var e,n;return p.a.wrap((function(o){for(;;)switch(o.prev=o.next){case 0:return o.next=2,fetch(t);case 2:return e=o.sent,o.next=5,e.text();case 5:return n=o.sent,o.abrupt("return",JSON.parse(n));case 7:case"end":return o.stop()}}),o)})))).apply(this,arguments)}var _=function(){var o=function(){var o=Object(x.a)(p.a.mark((function o(t){var e,n;return p.a.wrap((function(o){for(;;)switch(o.prev=o.next){case 0:if(console.log(t.action),e=T[t.action],console.log("ApiUrl: "+e),!e){o.next=9;break}return"SetTreeColor"===t.action&&(console.log("Color "+t.color),e+=encodeURIComponent(t.color)),o.next=7,w(e);case 7:n=o.sent,console.log(n);case 9:case"end":return o.stop()}}),o)})));return function(t){return o.apply(this,arguments)}}();return Object(F.jsxs)("div",{style:S,class:"remote",children:[k.map((function(t){return Object(F.jsx)(g,{color:t.color,data:t,textColor:t.textColor,text:t.text,onClick:o})})),Object(F.jsx)("div",{style:{clear:"both"}})]})};var B=function(){return Object(F.jsx)(F.Fragment,{children:Object(F.jsxs)("div",{className:"App",children:[Object(F.jsx)(s.a,{params:{particles:{number:{value:400,density:{enable:!0,value_area:800}},color:{value:"#fff"},shape:{type:"circle",stroke:{width:0,color:"#000000"},polygon:{nb_sides:5},image:{src:"img/github.svg",width:100,height:100}},opacity:{value:.5,random:!0,anim:{enable:!1,speed:1,opacity_min:.1,sync:!1}},size:{value:10,random:!0,anim:{enable:!1,speed:40,size_min:.1,sync:!1}},line_linked:{enable:!1,distance:500,color:"#ffffff",opacity:.4,width:2},move:{enable:!0,speed:6,direction:"bottom",random:!1,straight:!1,out_mode:"out",bounce:!1,attract:{enable:!1,rotateX:600,rotateY:1200}}},interactivity:{detect_on:"canvas",events:{onhover:{enable:!0,mode:"bubble"},onclick:{enable:!0,mode:"repulse"},resize:!0},modes:{grab:{distance:400,line_linked:{opacity:.5}},bubble:{distance:400,size:4,duration:.3,opacity:1,speed:3},repulse:{distance:200,duration:.4},push:{particles_nb:4},remove:{particles_nb:2}}},retina_detect:!0},className:"App-particles__container"}),Object(F.jsx)(c.a,{}),Object(F.jsx)("div",{style:{position:"absolute",left:"0",right:"0",marginLeft:"auto",marginRight:"auto",marginTop:"80px",width:"370px",padding:"10px",backgroundColor:"#fff"},children:Object(F.jsx)(_,{})})]})})},U=function(o){o&&o instanceof Function&&e.e(3).then(e.bind(null,399)).then((function(t){var e=t.getCLS,n=t.getFID,r=t.getFCP,l=t.getLCP,a=t.getTTFB;e(o),n(o),r(o),l(o),a(o)}))};a.a.render(Object(F.jsx)(r.a.StrictMode,{children:Object(F.jsx)(B,{})}),document.getElementById("root")),U()},93:function(o,t,e){},94:function(o,t,e){}},[[380,1,2]]]);
//# sourceMappingURL=main.2399e1b6.chunk.js.map