# Content from http://www.truth-out.org/goodbye-all-reflections-gop-operative-who-left-cult/1314907779

*Retrieved: 2025-09-15T12:53:59.941370*

---

<!doctype html>
<html class="no-focus-outline no-js" lang="en-US">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge"><script type="text/javascript">(window.NREUM||(NREUM={})).init={privacy:{cookies_enabled:true},ajax:{deny_list:[]},distributed_tracing:{enabled:true}};(window.NREUM||(NREUM={})).loader_config={agentID:"1386156550",accountID:"2045203",trustKey:"2045203",xpid:"VgYDVFRTCxABV1lXAAYCXlMI",licenseKey:"549d3cf919",applicationID:"1385775879"};;/*! For license information please see nr-loader-spa-1.297.0.min.js.LICENSE.txt */
(()=>{var e,t,r={8122:(e,t,r)=>{"use strict";r.d(t,{a:()=>i});var n=r(944);function i(e,t){try{if(!e||"object"!=typeof e)return(0,n.R)(3);if(!t||"object"!=typeof t)return(0,n.R)(4);const r=Object.create(Object.getPrototypeOf(t),Object.getOwnPropertyDescriptors(t)),o=0===Object.keys(r).length?e:r;for(let a in o)if(void 0!==e[a])try{if(null===e[a]){r[a]=null;continue}Array.isArray(e[a])&&Array.isArray(t[a])?r[a]=Array.from(new Set([...e[a],...t[a]])):"object"==typeof e[a]&&"object"==typeof t[a]?r[a]=i(e[a],t[a]):r[a]=e[a]}catch(e){r[a]||(0,n.R)(1,e)}return r}catch(e){(0,n.R)(2,e)}}},2555:(e,t,r)=>{"use strict";r.d(t,{D:()=>s,f:()=>a});var n=r(384),i=r(8122);const o={beacon:n.NT.beacon,errorBeacon:n.NT.errorBeacon,licenseKey:void 0,applicationID:void 0,sa:void 0,queueTime:void 0,applicationTime:void 0,ttGuid:void 0,user:void 0,account:void 0,product:void 0,extra:void 0,jsAttributes:{},userAttributes:void 0,atts:void 0,transactionName:void 0,tNamePlain:void 0};function a(e){try{return!!e.licenseKey&&!!e.errorBeacon&&!!e.applicationID}catch(e){return!1}}const s=e=>(0,i.a)(e,o)},9324:(e,t,r)=>{"use strict";r.d(t,{F3:()=>i,Xs:()=>o,Yq:()=>a,xv:()=>n});const n="1.297.0",i="PROD",o="CDN",a="^2.0.0-alpha.18"},6154:(e,t,r)=>{"use strict";r.d(t,{A4:()=>s,OF:()=>d,RI:()=>i,WN:()=>h,bv:()=>o,gm:()=>a,lR:()=>f,m:()=>u,mw:()=>c,sb:()=>l});var n=r(1863);const i="undefined"!=typeof window&&!!window.document,o="undefined"!=typeof WorkerGlobalScope&&("undefined"!=typeof self&&self instanceof WorkerGlobalScope&&self.navigator instanceof WorkerNavigator||"undefined"!=typeof globalThis&&globalThis instanceof WorkerGlobalScope&&globalThis.navigator instanceof WorkerNavigator),a=i?window:"undefined"!=typeof WorkerGlobalScope&&("undefined"!=typeof self&&self instanceof WorkerGlobalScope&&self||"undefined"!=typeof globalThis&&globalThis instanceof WorkerGlobalScope&&globalThis),s="complete"===a?.document?.readyState,c=Boolean("hidden"===a?.document?.visibilityState),u=""+a?.location,d=/iPad|iPhone|iPod/.test(a.navigator?.userAgent),l=d&&"undefined"==typeof SharedWorker,f=(()=>{const e=a.navigator?.userAgent?.match(/Firefox[/\s](\d+\.\d+)/);return Array.isArray(e)&&e.length>=2?+e[1]:0})(),h=Date.now()-(0,n.t)()},7295:(e,t,r)=>{"use strict";r.d(t,{Xv:()=>a,gX:()=>i,iW:()=>o});var n=[];function i(e){if(!e||o(e))return!1;if(0===n.length)return!0;for(var t=0;t<n.length;t++){var r=n[t];if("*"===r.hostname)return!1;if(s(r.hostname,e.hostname)&&c(r.pathname,e.pathname))return!1}return!0}function o(e){return void 0===e.hostname}function a(e){if(n=[],e&&e.length)for(var t=0;t<e.length;t++){let r=e[t];if(!r)continue;0===r.indexOf("http://")?r=r.substring(7):0===r.indexOf("https://")&&(r=r.substring(8));const i=r.indexOf("/");let o,a;i>0?(o=r.substring(0,i),a=r.substring(i)):(o=r,a="");let[s]=o.split(":");n.push({hostname:s,pathname:a})}}function s(e,t){return!(e.length>t.length)&&t.indexOf(e)===t.length-e.length}function c(e,t){return 0===e.indexOf("/")&&(e=e.substring(1)),0===t.indexOf("/")&&(t=t.substring(1)),""===e||e===t}},3241:(e,t,r)=>{"use strict";r.d(t,{W:()=>o});var n=r(6154);const i="newrelic";function o(e={}){try{n.gm.dispatchEvent(new CustomEvent(i,{detail:e}))}catch(e){}}},1687:(e,t,r)=>{"use strict";r.d(t,{Ak:()=>u,Ze:()=>f,x3:()=>d});var n=r(3241),i=r(7836),o=r(3606),a=r(860),s=r(2646);const c={};function u(e,t){const r={staged:!1,priority:a.P3[t]||0};l(e),c[e].get(t)||c[e].set(t,r)}function d(e,t){e&&c[e]&&(c[e].get(t)&&c[e].delete(t),p(e,t,!1),c[e].size&&h(e))}function l(e){if(!e)throw new Error("agentIdentifier required");c[e]||(c[e]=new Map)}function f(e="",t="feature",r=!1){if(l(e),!e||!c[e].get(t)||r)return p(e,t);c[e].get(t).staged=!0,h(e)}function h(e){const t=Array.from(c[e]);t.every((([e,t])=>t.staged))&&(t.sort(((e,t)=>e[1].priority-t[1].priority)),t.forEach((([t])=>{c[e].delete(t),p(e,t)})))}function p(e,t,r=!0){const a=e?i.ee.get(e):i.ee,c=o.i.handlers;if(!a.aborted&&a.backlog&&c){if((0,n.W)({agentIdentifier:e,type:"lifecycle",name:"drain",feature:t}),r){const e=a.backlog[t],r=c[t];if(r){for(let t=0;e&&t<e.length;++t)g(e[t],r);Object.entries(r).forEach((([e,t])=>{Object.values(t||{}).forEach((t=>{t[0]?.on&&t[0]?.context()instanceof s.y&&t[0].on(e,t[1])}))}))}}a.isolatedBacklog||delete c[t],a.backlog[t]=null,a.emit("drain-"+t,[])}}function g(e,t){var r=e[1];Object.values(t[r]||{}).forEach((t=>{var r=e[0];if(t[0]===r){var n=t[1],i=e[3],o=e[2];n.apply(i,o)}}))}},7836:(e,t,r)=>{"use strict";r.d(t,{P:()=>s,ee:()=>c});var n=r(384),i=r(8990),o=r(2646),a=r(5607);const s="nr@context:".concat(a.W),c=function e(t,r){var n={},a={},d={},l=!1;try{l=16===r.length&&u.initializedAgents?.[r]?.runtime.isolatedBacklog}catch(e){}var f={on:p,addEventListener:p,removeEventListener:function(e,t){var r=n[e];if(!r)return;for(var i=0;i<r.length;i++)r[i]===t&&r.splice(i,1)},emit:function(e,r,n,i,o){!1!==o&&(o=!0);if(c.aborted&&!i)return;t&&o&&t.emit(e,r,n);var s=h(n);g(e).forEach((e=>{e.apply(s,r)}));var u=v()[a[e]];u&&u.push([f,e,r,s]);return s},get:m,listeners:g,context:h,buffer:function(e,t){const r=v();if(t=t||"feature",f.aborted)return;Object.entries(e||{}).forEach((([e,n])=>{a[n]=t,t in r||(r[t]=[])}))},abort:function(){f._aborted=!0,Object.keys(f.backlog).forEach((e=>{delete f.backlog[e]}))},isBuffering:function(e){return!!v()[a[e]]},debugId:r,backlog:l?{}:t&&"object"==typeof t.backlog?t.backlog:{},isolatedBacklog:l};return Object.defineProperty(f,"aborted",{get:()=>{let e=f._aborted||!1;return e||(t&&(e=t.aborted),e)}}),f;function h(e){return e&&e instanceof o.y?e:e?(0,i.I)(e,s,(()=>new o.y(s))):new o.y(s)}function p(e,t){n[e]=g(e).concat(t)}function g(e){return n[e]||[]}function m(t){return d[t]=d[t]||e(f,t)}function v(){return f.backlog}}(void 0,"globalEE"),u=(0,n.Zm)();u.ee||(u.ee=c)},2646:(e,t,r)=>{"use strict";r.d(t,{y:()=>n});class n{constructor(e){this.contextId=e}}},9908:(e,t,r)=>{"use strict";r.d(t,{d:()=>n,p:()=>i});var n=r(7836).ee.get("handle");function i(e,t,r,i,o){o?(o.buffer([e],i),o.emit(e,t,r)):(n.buffer([e],i),n.emit(e,t,r))}},3606:(e,t,r)=>{"use strict";r.d(t,{i:()=>o});var n=r(9908);o.on=a;var i=o.handlers={};function o(e,t,r,o){a(o||n.d,i,e,t,r)}function a(e,t,r,i,o){o||(o="feature"),e||(e=n.d);var a=t[o]=t[o]||{};(a[r]=a[r]||[]).push([e,i])}},3878:(e,t,r)=>{"use strict";function n(e,t){return{capture:e,passive:!1,signal:t}}function i(e,t,r=!1,i){window.addEventListener(e,t,n(r,i))}function o(e,t,r=!1,i){document.addEventListener(e,t,n(r,i))}r.d(t,{DD:()=>o,jT:()=>n,sp:()=>i})},5607:(e,t,r)=>{"use strict";r.d(t,{W:()=>n});const n=(0,r(9566).bz)()},9566:(e,t,r)=>{"use strict";r.d(t,{LA:()=>s,ZF:()=>c,bz:()=>a,el:()=>u});var n=r(6154);const i="xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx";function o(e,t){return e?15&e[t]:16*Math.random()|0}function a(){const e=n.gm?.crypto||n.gm?.msCrypto;let t,r=0;return e&&e.getRandomValues&&(t=e.getRandomValues(new Uint8Array(30))),i.split("").map((e=>"x"===e?o(t,r++).toString(16):"y"===e?(3&o()|8).toString(16):e)).join("")}function s(e){const t=n.gm?.crypto||n.gm?.msCrypto;let r,i=0;t&&t.getRandomValues&&(r=t.getRandomValues(new Uint8Array(e)));const a=[];for(var s=0;s<e;s++)a.push(o(r,i++).toString(16));return a.join("")}function c(){return s(16)}function u(){return s(32)}},2614:(e,t,r)=>{"use strict";r.d(t,{BB:()=>a,H3:()=>n,g:()=>u,iL:()=>c,tS:()=>s,uh:()=>i,wk:()=>o});const n="NRBA",i="SESSION",o=144e5,a=18e5,s={STARTED:"session-started",PAUSE:"session-pause",RESET:"session-reset",RESUME:"session-resume",UPDATE:"session-update"},c={SAME_TAB:"same-tab",CROSS_TAB:"cross-tab"},u={OFF:0,FULL:1,ERROR:2}},1863:(e,t,r)=>{"use strict";function n(){return Math.floor(performance.now())}r.d(t,{t:()=>n})},7485:(e,t,r)=>{"use strict";r.d(t,{D:()=>i});var n=r(6154);function i(e){if(0===(e||"").indexOf("data:"))return{protocol:"data"};try{const t=new URL(e,location.href),r={port:t.port,hostname:t.hostname,pathname:t.pathname,search:t.search,protocol:t.protocol.slice(0,t.protocol.indexOf(":")),sameOrigin:t.protocol===n.gm?.location?.protocol&&t.host===n.gm?.location?.host};return r.port&&""!==r.port||("http:"===t.protocol&&(r.port="80"),"https:"===t.protocol&&(r.port="443")),r.pathname&&""!==r.pathname?r.pathname.startsWith("/")||(r.pathname="/".concat(r.pathname)):r.pathname="/",r}catch(e){return{}}}},944:(e,t,r)=>{"use strict";r.d(t,{R:()=>i});var n=r(3241);function i(e,t){"function"==typeof console.debug&&(console.debug("New Relic Warning: https://github.com/newrelic/newrelic-browser-agent/blob/main/docs/warning-codes.md#".concat(e),t),(0,n.W)({agentIdentifier:null,drained:null,type:"data",name:"warn",feature:"warn",data:{code:e,secondary:t}}))}},5701:(e,t,r)=>{"use strict";r.d(t,{B:()=>o,t:()=>a});var n=r(3241);const i=new Set,o={};function a(e,t){const r=t.agentIdentifier;o[r]??={},e&&"object"==typeof e&&(i.has(r)||(t.ee.emit("rumresp",[e]),o[r]=e,i.add(r),(0,n.W)({agentIdentifier:r,loaded:!0,drained:!0,type:"lifecycle",name:"load",feature:void 0,data:e})))}},8990:(e,t,r)=>{"use strict";r.d(t,{I:()=>i});var n=Object.prototype.hasOwnProperty;function i(e,t,r){if(n.call(e,t))return e[t];var i=r();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,t,{value:i,writable:!0,enumerable:!1}),i}catch(e){}return e[t]=i,i}},6389:(e,t,r)=>{"use strict";function n(e,t=500,r={}){const n=r?.leading||!1;let i;return(...r)=>{n&&void 0===i&&(e.apply(this,r),i=setTimeout((()=>{i=clearTimeout(i)}),t)),n||(clearTimeout(i),i=setTimeout((()=>{e.apply(this,r)}),t))}}function i(e){let t=!1;return(...r)=>{t||(t=!0,e.apply(this,r))}}r.d(t,{J:()=>i,s:()=>n})},1910:(e,t,r)=>{"use strict";r.d(t,{i:()=>o});var n=r(944);const i=new Map;function o(...e){return e.every((e=>{if(i.has(e))return i.get(e);const t="function"==typeof e&&e.toString().includes("[native code]");return t||(0,n.R)(64,e?.name||e?.toString()),i.set(e,t),t}))}},3304:(e,t,r)=>{"use strict";r.d(t,{A:()=>o});var n=r(7836);const i=()=>{const e=new WeakSet;return(t,r)=>{if("object"==typeof r&&null!==r){if(e.has(r))return;e.add(r)}return r}};function o(e){try{return JSON.stringify(e,i())??""}catch(e){try{n.ee.emit("internal-error",[e])}catch(e){}return""}}},3496:(e,t,r)=>{"use strict";function n(e){return!e||!(!e.licenseKey||!e.applicationID)}function i(e,t){return!e||e.licenseKey===t.info.licenseKey&&e.applicationID===t.info.applicationID}r.d(t,{A:()=>i,I:()=>n})},5289:(e,t,r)=>{"use strict";r.d(t,{GG:()=>o,Qr:()=>s,sB:()=>a});var n=r(3878);function i(){return"undefined"==typeof document||"complete"===document.readyState}function o(e,t){if(i())return e();(0,n.sp)("load",e,t)}function a(e){if(i())return e();(0,n.DD)("DOMContentLoaded",e)}function s(e){if(i())return e();(0,n.sp)("popstate",e)}},384:(e,t,r)=>{"use strict";r.d(t,{NT:()=>a,US:()=>d,Zm:()=>s,bQ:()=>u,dV:()=>c,pV:()=>l});var n=r(6154),i=r(1863),o=r(1910);const a={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net"};function s(){return n.gm.NREUM||(n.gm.NREUM={}),void 0===n.gm.newrelic&&(n.gm.newrelic=n.gm.NREUM),n.gm.NREUM}function c(){let e=s();return e.o||(e.o={ST:n.gm.setTimeout,SI:n.gm.setImmediate||n.gm.setInterval,CT:n.gm.clearTimeout,XHR:n.gm.XMLHttpRequest,REQ:n.gm.Request,EV:n.gm.Event,PR:n.gm.Promise,MO:n.gm.MutationObserver,FETCH:n.gm.fetch,WS:n.gm.WebSocket},(0,o.i)(...Object.values(e.o))),e}function u(e,t){let r=s();r.initializedAgents??={},t.initializedAt={ms:(0,i.t)(),date:new Date},r.initializedAgents[e]=t}function d(e,t){s()[e]=t}function l(){return function(){let e=s();const t=e.info||{};e.info={beacon:a.beacon,errorBeacon:a.errorBeacon,...t}}(),function(){let e=s();const t=e.init||{};e.init={...t}}(),c(),function(){let e=s();const t=e.loader_config||{};e.loader_config={...t}}(),s()}},2843:(e,t,r)=>{"use strict";r.d(t,{u:()=>i});var n=r(3878);function i(e,t=!1,r,i){(0,n.DD)("visibilitychange",(function(){if(t)return void("hidden"===document.visibilityState&&e());e(document.visibilityState)}),r,i)}},8139:(e,t,r)=>{"use strict";r.d(t,{u:()=>f});var n=r(7836),i=r(3434),o=r(8990),a=r(6154);const s={},c=a.gm.XMLHttpRequest,u="addEventListener",d="removeEventListener",l="nr@wrapped:".concat(n.P);function f(e){var t=function(e){return(e||n.ee).get("events")}(e);if(s[t.debugId]++)return t;s[t.debugId]=1;var r=(0,i.YM)(t,!0);function f(e){r.inPlace(e,[u,d],"-",p)}function p(e,t){return e[1]}return"getPrototypeOf"in Object&&(a.RI&&h(document,f),c&&h(c.prototype,f),h(a.gm,f)),t.on(u+"-start",(function(e,t){var n=e[1];if(null!==n&&("function"==typeof n||"object"==typeof n)&&"newrelic"!==e[0]){var i=(0,o.I)(n,l,(function(){var e={object:function(){if("function"!=typeof n.handleEvent)return;return n.handleEvent.apply(n,arguments)},function:n}[typeof n];return e?r(e,"fn-",null,e.name||"anonymous"):n}));this.wrapped=e[1]=i}})),t.on(d+"-start",(function(e){e[1]=this.wrapped||e[1]})),t}function h(e,t,...r){let n=e;for(;"object"==typeof n&&!Object.prototype.hasOwnProperty.call(n,u);)n=Object.getPrototypeOf(n);n&&t(n,...r)}},3434:(e,t,r)=>{"use strict";r.d(t,{Jt:()=>o,YM:()=>c});var n=r(7836),i=r(5607);const o="nr@original:".concat(i.W);var a=Object.prototype.hasOwnProperty,s=!1;function c(e,t){return e||(e=n.ee),r.inPlace=function(e,t,n,i,o){n||(n="");const a="-"===n.charAt(0);for(let s=0;s<t.length;s++){const c=t[s],u=e[c];d(u)||(e[c]=r(u,a?c+n:n,i,c,o))}},r.flag=o,r;function r(t,r,n,s,c){return d(t)?t:(r||(r=""),nrWrapper[o]=t,function(e,t,r){if(Object.defineProperty&&Object.keys)try{return Object.keys(e).forEach((function(r){Object.defineProperty(t,r,{get:function(){return e[r]},set:function(t){return e[r]=t,t}})})),t}catch(e){u([e],r)}for(var n in e)a.call(e,n)&&(t[n]=e[n])}(t,nrWrapper,e),nrWrapper);function nrWrapper(){var o,a,d,l;let f;try{a=this,o=[...arguments],d="function"==typeof n?n(o,a):n||{}}catch(t){u([t,"",[o,a,s],d],e)}i(r+"start",[o,a,s],d,c);const h=performance.now();let p=h;try{return l=t.apply(a,o),p=performance.now(),l}catch(e){throw p=performance.now(),i(r+"err",[o,a,e],d,c),f=e,f}finally{const e=p-h,t={duration:e,isLongTask:e>=50,methodName:s,thrownError:f};t.isLongTask&&i("long-task",[t],d,c),i(r+"end",[o,a,l,t],d,c)}}}function i(r,n,i,o){if(!s||t){var a=s;s=!0;try{e.emit(r,n,i,t,o)}catch(t){u([t,r,n,i],e)}s=a}}}function u(e,t){t||(t=n.ee);try{t.emit("internal-error",e)}catch(e){}}function d(e){return!(e&&"function"==typeof e&&e.apply&&!e[o])}},9300:(e,t,r)=>{"use strict";r.d(t,{T:()=>n});const n=r(860).K7.ajax},3333:(e,t,r)=>{"use strict";r.d(t,{$v:()=>u,TZ:()=>n,Zp:()=>i,kd:()=>c,mq:()=>s,nf:()=>a,qN:()=>o});const n=r(860).K7.genericEvents,i=["auxclick","click","copy","keydown","paste","scrollend"],o=["focus","blur"],a=4,s=1e3,c=["PageAction","UserAction","BrowserPerformance"],u={MARKS:"experimental.marks",MEASURES:"experimental.measures",RESOURCES:"experimental.resources"}},6774:(e,t,r)=>{"use strict";r.d(t,{T:()=>n});const n=r(860).K7.jserrors},993:(e,t,r)=>{"use strict";r.d(t,{A$:()=>o,ET:()=>a,TZ:()=>s,p_:()=>i});var n=r(860);const i={ERROR:"ERROR",WARN:"WARN",INFO:"INFO",DEBUG:"DEBUG",TRACE:"TRACE"},o={OFF:0,ERROR:1,WARN:2,INFO:3,DEBUG:4,TRACE:5},a="log",s=n.K7.logging},3785:(e,t,r)=>{"use strict";r.d(t,{R:()=>c,b:()=>u});var n=r(9908),i=r(1863),o=r(860),a=r(8154),s=r(993);function c(e,t,r={},c=s.p_.INFO,u,d=(0,i.t)()){(0,n.p)(a.xV,["API/logging/".concat(c.toLowerCase(),"/called")],void 0,o.K7.metrics,e),(0,n.p)(s.ET,[d,t,r,c,u],void 0,o.K7.logging,e)}function u(e){return"string"==typeof e&&Object.values(s.p_).some((t=>t===e.toUpperCase().trim()))}},8154:(e,t,r)=>{"use strict";r.d(t,{z_:()=>o,XG:()=>s,TZ:()=>n,rs:()=>i,xV:()=>a});r(6154),r(9566),r(384);const n=r(860).K7.metrics,i="sm",o="cm",a="storeSupportabilityMetrics",s="storeEventMetrics"},6630:(e,t,r)=>{"use strict";r.d(t,{T:()=>n});const n=r(860).K7.pageViewEvent},782:(e,t,r)=>{"use strict";r.d(t,{T:()=>n});const n=r(860).K7.pageViewTiming},6344:(e,t,r)=>{"use strict";r.d(t,{BB:()=>d,G4:()=>o,Qb:()=>l,TZ:()=>i,Ug:()=>a,_s:()=>s,bc:()=>u,yP:()=>c});var n=r(2614);const i=r(860).K7.sessionReplay,o={RECORD:"recordReplay",PAUSE:"pauseReplay",ERROR_DURING_REPLAY:"errorDuringReplay"},a=.12,s={DomContentLoaded:0,Load:1,FullSnapshot:2,IncrementalSnapshot:3,Meta:4,Custom:5},c={[n.g.ERROR]:15e3,[n.g.FULL]:3e5,[n.g.OFF]:0},u={RESET:{message:"Session was reset",sm:"Reset"},IMPORT:{message:"Recorder failed to import",sm:"Import"},TOO_MANY:{message:"429: Too Many Requests",sm:"Too-Many"},TOO_BIG:{message:"Payload was too large",sm:"Too-Big"},CROSS_TAB:{message:"Session Entity was set to OFF on another tab",sm:"Cross-Tab"},ENTITLEMENTS:{message:"Session Replay is not allowed and will not be started",sm:"Entitlement"}},d=5e3,l={API:"api"}},5270:(e,t,r)=>{"use strict";r.d(t,{Aw:()=>a,SR:()=>o,rF:()=>s});var n=r(384),i=r(7767);function o(e){return!!(0,n.dV)().o.MO&&(0,i.V)(e)&&!0===e?.session_trace.enabled}function a(e){return!0===e?.session_replay.preload&&o(e)}function s(e,t){try{if("string"==typeof t?.type){if("password"===t.type.toLowerCase())return"*".repeat(e?.length||0);if(void 0!==t?.dataset?.nrUnmask||t?.classList?.contains("nr-unmask"))return e}}catch(e){}return"string"==typeof e?e.replace(/[\S]/g,"*"):"*".repeat(e?.length||0)}},3738:(e,t,r)=>{"use strict";r.d(t,{He:()=>i,Kp:()=>s,Lc:()=>u,Rz:()=>d,TZ:()=>n,bD:()=>o,d3:()=>a,jx:()=>l,sl:()=>f,uP:()=>c});const n=r(860).K7.sessionTrace,i="bstResource",o="resource",a="-start",s="-end",c="fn"+a,u="fn"+s,d="pushState",l=1e3,f=3e4},3962:(e,t,r)=>{"use strict";r.d(t,{AM:()=>o,O2:()=>c,Qu:()=>u,TZ:()=>s,ih:()=>d,pP:()=>a,tC:()=>i});var n=r(860);const i=["click","keydown","submit","popstate"],o="api",a="initialPageLoad",s=n.K7.softNav,c={INITIAL_PAGE_LOAD:"",ROUTE_CHANGE:1,UNSPECIFIED:2},u={INTERACTION:1,AJAX:2,CUSTOM_END:3,CUSTOM_TRACER:4},d={IP:"in progress",FIN:"finished",CAN:"cancelled"}},7378:(e,t,r)=>{"use strict";r.d(t,{$p:()=>x,BR:()=>b,Kp:()=>R,L3:()=>y,Lc:()=>c,NC:()=>o,SG:()=>d,TZ:()=>i,U6:()=>p,UT:()=>m,d3:()=>w,dT:()=>f,e5:()=>A,gx:()=>v,l9:()=>l,oW:()=>h,op:()=>g,rw:()=>u,tH:()=>E,uP:()=>s,wW:()=>T,xq:()=>a});var n=r(384);const i=r(860).K7.spa,o=["click","submit","keypress","keydown","keyup","change"],a=999,s="fn-start",c="fn-end",u="cb-start",d="api-ixn-",l="remaining",f="interaction",h="spaNode",p="jsonpNode",g="fetch-start",m="fetch-done",v="fetch-body-",b="jsonp-end",y=(0,n.dV)().o.ST,w="-start",R="-end",x="-body",T="cb"+R,A="jsTime",E="fetch"},4234:(e,t,r)=>{"use strict";r.d(t,{W:()=>o});var n=r(7836),i=r(1687);class o{constructor(e,t){this.agentIdentifier=e,this.ee=n.ee.get(e),this.featureName=t,this.blocked=!1}deregisterDrain(){(0,i.x3)(this.agentIdentifier,this.featureName)}}},7767:(e,t,r)=>{"use strict";r.d(t,{V:()=>i});var n=r(6154);const i=e=>n.RI&&!0===e?.privacy.cookies_enabled},1741:(e,t,r)=>{"use strict";r.d(t,{W:()=>o});var n=r(944),i=r(4261);class o{#e(e,...t){if(this[e]!==o.prototype[e])return this[e](...t);(0,n.R)(35,e)}addPageAction(e,t){return this.#e(i.hG,e,t)}register(e){return this.#e(i.eY,e)}recordCustomEvent(e,t){return this.#e(i.fF,e,t)}setPageViewName(e,t){return this.#e(i.Fw,e,t)}setCustomAttribute(e,t,r){return this.#e(i.cD,e,t,r)}noticeError(e,t){return this.#e(i.o5,e,t)}setUserId(e){return this.#e(i.Dl,e)}setApplicationVersion(e){return this.#e(i.nb,e)}setErrorHandler(e){return this.#e(i.bt,e)}addRelease(e,t){return this.#e(i.k6,e,t)}log(e,t){return this.#e(i.$9,e,t)}start(){return this.#e(i.d3)}finished(e){return this.#e(i.BL,e)}recordReplay(){return this.#e(i.CH)}pauseReplay(){return this.#e(i.Tb)}addToTrace(e){return this.#e(i.U2,e)}setCurrentRouteName(e){return this.#e(i.PA,e)}interaction(){return this.#e(i.dT)}wrapLogger(e,t,r){return this.#e(i.Wb,e,t,r)}measure(e,t){return this.#e(i.V1,e,t)}}},4261:(e,t,r)=>{"use strict";r.d(t,{$9:()=>d,BL:()=>c,CH:()=>p,Dl:()=>R,Fw:()=>w,PA:()=>v,Pl:()=>n,Tb:()=>f,U2:()=>a,V1:()=>A,Wb:()=>T,bt:()=>y,cD:()=>b,d3:()=>x,dT:()=>u,eY:()=>g,fF:()=>h,hG:()=>o,hw:()=>i,k6:()=>s,nb:()=>m,o5:()=>l});const n="api-",i=n+"ixn-",o="addPageAction",a="addToTrace",s="addRelease",c="finished",u="interaction",d="log",l="noticeError",f="pauseReplay",h="recordCustomEvent",p="recordReplay",g="register",m="setApplicationVersion",v="setCurrentRouteName",b="setCustomAttribute",y="setErrorHandler",w="setPageViewName",R="setUserId",x="start",T="wrapLogger",A="measure"},5205:(e,t,r)=>{"use strict";r.d(t,{j:()=>S});var n=r(384),i=r(1741);var o=r(2555),a=r(3333);const s=e=>{if(!e||"string"!=typeof e)return!1;try{document.createDocumentFragment().querySelector(e)}catch{return!1}return!0};var c=r(2614),u=r(944),d=r(8122);const l="[data-nr-mask]",f=e=>(0,d.a)(e,(()=>{const e={feature_flags:[],experimental:{marks:!1,measures:!1,resources:!1},mask_selector:"*",block_selector:"[data-nr-block]",mask_input_options:{color:!1,date:!1,"datetime-local":!1,email:!1,month:!1,number:!1,range:!1,search:!1,tel:!1,text:!1,time:!1,url:!1,week:!1,textarea:!1,select:!1,password:!0}};return{ajax:{deny_list:void 0,block_internal:!0,enabled:!0,autoStart:!0},api:{allow_registered_children:!0,duplicate_registered_data:!1},distributed_tracing:{enabled:void 0,exclude_newrelic_header:void 0,cors_use_newrelic_header:void 0,cors_use_tracecontext_headers:void 0,allowed_origins:void 0},get feature_flags(){return e.feature_flags},set feature_flags(t){e.feature_flags=t},generic_events:{enabled:!0,autoStart:!0},harvest:{interval:30},jserrors:{enabled:!0,autoStart:!0},logging:{enabled:!0,autoStart:!0},metrics:{enabled:!0,autoStart:!0},obfuscate:void 0,page_action:{enabled:!0},page_view_event:{enabled:!0,autoStart:!0},page_view_timing:{enabled:!0,autoStart:!0},performance:{get capture_marks(){return e.feature_flags.includes(a.$v.MARKS)||e.experimental.marks},set capture_marks(t){e.experimental.marks=t},get capture_measures(){return e.feature_flags.includes(a.$v.MEASURES)||e.experimental.measures},set capture_measures(t){e.experimental.measures=t},capture_detail:!0,resources:{get enabled(){return e.feature_flags.includes(a.$v.RESOURCES)||e.experimental.resources},set enabled(t){e.experimental.resources=t},asset_types:[],first_party_domains:[],ignore_newrelic:!0}},privacy:{cookies_enabled:!0},proxy:{assets:void 0,beacon:void 0},session:{expiresMs:c.wk,inactiveMs:c.BB},session_replay:{autoStart:!0,enabled:!1,preload:!1,sampling_rate:10,error_sampling_rate:100,collect_fonts:!1,inline_images:!1,fix_stylesheets:!0,mask_all_inputs:!0,get mask_text_selector(){return e.mask_selector},set mask_text_selector(t){s(t)?e.mask_selector="".concat(t,",").concat(l):""===t||null===t?e.mask_selector=l:(0,u.R)(5,t)},get block_class(){return"nr-block"},get ignore_class(){return"nr-ignore"},get mask_text_class(){return"nr-mask"},get block_selector(){return e.block_selector},set block_selector(t){s(t)?e.block_selector+=",".concat(t):""!==t&&(0,u.R)(6,t)},get mask_input_options(){return e.mask_input_options},set mask_input_options(t){t&&"object"==typeof t?e.mask_input_options={...t,password:!0}:(0,u.R)(7,t)}},session_trace:{enabled:!0,autoStart:!0},soft_navigations:{enabled:!0,autoStart:!0},spa:{enabled:!0,autoStart:!0},ssl:void 0,user_actions:{enabled:!0,elementAttributes:["id","className","tagName","type"]}}})());var h=r(6154),p=r(9324);let g=0;const m={buildEnv:p.F3,distMethod:p.Xs,version:p.xv,originTime:h.WN},v={appMetadata:{},customTransaction:void 0,denyList:void 0,disabled:!1,entityManager:void 0,harvester:void 0,isolatedBacklog:!1,isRecording:!1,loaderType:void 0,maxBytes:3e4,obfuscator:void 0,onerror:void 0,ptid:void 0,releaseIds:{},session:void 0,timeKeeper:void 0,jsAttributesMetadata:{bytes:0},get harvestCount(){return++g}},b=e=>{const t=(0,d.a)(e,v),r=Object.keys(m).reduce(((e,t)=>(e[t]={value:m[t],writable:!1,configurable:!0,enumerable:!0},e)),{});return Object.defineProperties(t,r)};var y=r(5701);const w=e=>{const t=e.startsWith("http");e+="/",r.p=t?e:"https://"+e};var R=r(7836),x=r(3241);const T={accountID:void 0,trustKey:void 0,agentID:void 0,licenseKey:void 0,applicationID:void 0,xpid:void 0},A=e=>(0,d.a)(e,T),E=new Set;function S(e,t={},r,a){let{init:s,info:c,loader_config:u,runtime:d={},exposed:l=!0}=t;if(!c){const e=(0,n.pV)();s=e.init,c=e.info,u=e.loader_config}e.init=f(s||{}),e.loader_config=A(u||{}),c.jsAttributes??={},h.bv&&(c.jsAttributes.isWorker=!0),e.info=(0,o.D)(c);const p=e.init,g=[c.beacon,c.errorBeacon];E.has(e.agentIdentifier)||(p.proxy.assets&&(w(p.proxy.assets),g.push(p.proxy.assets)),p.proxy.beacon&&g.push(p.proxy.beacon),function(e){const t=(0,n.pV)();Object.getOwnPropertyNames(i.W.prototype).forEach((r=>{const n=i.W.prototype[r];if("function"!=typeof n||"constructor"===n)return;let o=t[r];e[r]&&!1!==e.exposed&&"micro-agent"!==e.runtime?.loaderType&&(t[r]=(...t)=>{const n=e[r](...t);return o?o(...t):n})}))}(e),(0,n.US)("activatedFeatures",y.B),e.runSoftNavOverSpa&&=!0===p.soft_navigations.enabled&&p.feature_flags.includes("soft_nav")),d.denyList=[...p.ajax.deny_list||[],...p.ajax.block_internal?g:[]],d.ptid=e.agentIdentifier,d.loaderType=r,e.runtime=b(d),E.has(e.agentIdentifier)||(e.ee=R.ee.get(e.agentIdentifier),e.exposed=l,(0,x.W)({agentIdentifier:e.agentIdentifier,drained:!!y.B?.[e.agentIdentifier],type:"lifecycle",name:"initialize",feature:void 0,data:e.config})),E.add(e.agentIdentifier)}},8374:(e,t,r)=>{r.nc=(()=>{try{return document?.currentScript?.nonce}catch(e){}return""})()},860:(e,t,r)=>{"use strict";r.d(t,{$J:()=>d,K7:()=>c,P3:()=>u,XX:()=>i,Yy:()=>s,df:()=>o,qY:()=>n,v4:()=>a});const n="events",i="jserrors",o="browser/blobs",a="rum",s="browser/logs",c={ajax:"ajax",genericEvents:"generic_events",jserrors:i,logging:"logging",metrics:"metrics",pageAction:"page_action",pageViewEvent:"page_view_event",pageViewTiming:"page_view_timing",sessionReplay:"session_replay",sessionTrace:"session_trace",softNav:"soft_navigations",spa:"spa"},u={[c.pageViewEvent]:1,[c.pageViewTiming]:2,[c.metrics]:3,[c.jserrors]:4,[c.spa]:5,[c.ajax]:6,[c.sessionTrace]:7,[c.softNav]:8,[c.sessionReplay]:9,[c.logging]:10,[c.genericEvents]:11},d={[c.pageViewEvent]:a,[c.pageViewTiming]:n,[c.ajax]:n,[c.spa]:n,[c.softNav]:n,[c.metrics]:i,[c.jserrors]:i,[c.sessionTrace]:o,[c.sessionReplay]:o,[c.logging]:s,[c.genericEvents]:"ins"}}},n={};function i(e){var t=n[e];if(void 0!==t)return t.exports;var o=n[e]={exports:{}};return r[e](o,o.exports,i),o.exports}i.m=r,i.d=(e,t)=>{for(var r in t)i.o(t,r)&&!i.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})},i.f={},i.e=e=>Promise.all(Object.keys(i.f).reduce(((t,r)=>(i.f[r](e,t),t)),[])),i.u=e=>({212:"nr-spa-compressor",249:"nr-spa-recorder",478:"nr-spa"}[e]+"-1.297.0.min.js"),i.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),e={},t="NRBA-1.297.0.PROD:",i.l=(r,n,o,a)=>{if(e[r])e[r].push(n);else{var s,c;if(void 0!==o)for(var u=document.getElementsByTagName("script"),d=0;d<u.length;d++){var l=u[d];if(l.getAttribute("src")==r||l.getAttribute("data-webpack")==t+o){s=l;break}}if(!s){c=!0;var f={478:"sha512-EisHRLvMvGYshzPigxfc0qFaG5ATndTGVYKkxR7SdfFrMUtgTYyLH0CjxkE6oFqdiSeGiVkx20++Rs52RvEcUQ==",249:"sha512-6yiBtW3LZf+Ub7HGWYbpDLPruOPaQ94yLYSwmEwTuyMYdwlULNtMVmE2Cl4N3h5DuKVuB13ugzr7tDnZM9dUYg==",212:"sha512-BCHlEhaFWmKdUvTSTsoVN3ZB9kOPANfL7Cw9LbvZX8mM8ff1v906TbD5up9SOW2AoqQWZ7K0+vnJD7tn4JXZOg=="};(s=document.createElement("script")).charset="utf-8",s.timeout=120,i.nc&&s.setAttribute("nonce",i.nc),s.setAttribute("data-webpack",t+o),s.src=r,0!==s.src.indexOf(window.location.origin+"/")&&(s.crossOrigin="anonymous"),f[a]&&(s.integrity=f[a])}e[r]=[n];var h=(t,n)=>{s.onerror=s.onload=null,clearTimeout(p);var i=e[r];if(delete e[r],s.parentNode&&s.parentNode.removeChild(s),i&&i.forEach((e=>e(n))),t)return t(n)},p=setTimeout(h.bind(null,void 0,{type:"timeout",target:s}),12e4);s.onerror=h.bind(null,s.onerror),s.onload=h.bind(null,s.onload),c&&document.head.appendChild(s)}},i.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.p="https://js-agent.newrelic.com/",(()=>{var e={38:0,788:0};i.f.j=(t,r)=>{var n=i.o(e,t)?e[t]:void 0;if(0!==n)if(n)r.push(n[2]);else{var o=new Promise(((r,i)=>n=e[t]=[r,i]));r.push(n[2]=o);var a=i.p+i.u(t),s=new Error;i.l(a,(r=>{if(i.o(e,t)&&(0!==(n=e[t])&&(e[t]=void 0),n)){var o=r&&("load"===r.type?"missing":r.type),a=r&&r.target&&r.target.src;s.message="Loading chunk "+t+" failed.\n("+o+": "+a+")",s.name="ChunkLoadError",s.type=o,s.request=a,n[1](s)}}),"chunk-"+t,t)}};var t=(t,r)=>{var n,o,[a,s,c]=r,u=0;if(a.some((t=>0!==e[t]))){for(n in s)i.o(s,n)&&(i.m[n]=s[n]);if(c)c(i)}for(t&&t(r);u<a.length;u++)o=a[u],i.o(e,o)&&e[o]&&e[o][0](),e[o]=0},r=self["webpackChunk:NRBA-1.297.0.PROD"]=self["webpackChunk:NRBA-1.297.0.PROD"]||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))})(),(()=>{"use strict";i(8374);var e=i(9566),t=i(1741);class r extends t.W{agentIdentifier=(0,e.LA)(16)}var n=i(860);const o=Object.values(n.K7);var a=i(5205);var s=i(9908),c=i(1863),u=i(4261),d=i(3241),l=i(944),f=i(5701),h=i(8154);function p(e,t,i,o){const a=o||i;!a||a[e]&&a[e]!==r.prototype[e]||(a[e]=function(){(0,s.p)(h.xV,["API/"+e+"/called"],void 0,n.K7.metrics,i.ee),(0,d.W)({agentIdentifier:i.agentIdentifier,drained:!!f.B?.[i.agentIdentifier],type:"data",name:"api",feature:u.Pl+e,data:{}});try{return t.apply(this,arguments)}catch(e){(0,l.R)(23,e)}})}function g(e,t,r,n,i){const o=e.info;null===r?delete o.jsAttributes[t]:o.jsAttributes[t]=r,(i||null===r)&&(0,s.p)(u.Pl+n,[(0,c.t)(),t,r],void 0,"session",e.ee)}var m=i(1687),v=i(4234),b=i(5289),y=i(6154),w=i(5270),R=i(7767),x=i(6389);class T extends v.W{constructor(e,t){super(e.agentIdentifier,t),this.abortHandler=void 0,this.featAggregate=void 0,this.onAggregateImported=void 0,this.deferred=Promise.resolve(),!1===e.init[this.featureName].autoStart?this.deferred=new Promise(((t,r)=>{this.ee.on("manual-start-all",(0,x.J)((()=>{(0,m.Ak)(e.agentIdentifier,this.featureName),t()})))})):(0,m.Ak)(e.agentIdentifier,t)}importAggregator(e,t,r={}){if(this.featAggregate)return;let o;this.onAggregateImported=new Promise((e=>{o=e}));const a=async()=>{let a;await this.deferred;try{if((0,R.V)(e.init)){const{setupAgentSession:t}=await i.e(478).then(i.bind(i,2955));a=t(e)}}catch(e){(0,l.R)(20,e),this.ee.emit("internal-error",[e]),this.featureName===n.K7.sessionReplay&&this.abortHandler?.()}try{if(!this.#t(this.featureName,a,e.init))return(0,m.Ze)(this.agentIdentifier,this.featureName),void o(!1);const{Aggregate:n}=await t();this.featAggregate=new n(e,r),e.runtime.harvester.initializedAggregates.push(this.featAggregate),o(!0)}catch(e){(0,l.R)(34,e),this.abortHandler?.(),(0,m.Ze)(this.agentIdentifier,this.featureName,!0),o(!1),this.ee&&this.ee.abort()}};y.RI?(0,b.GG)((()=>a()),!0):a()}#t(e,t,r){switch(e){case n.K7.sessionReplay:return(0,w.SR)(r)&&!!t;case n.K7.sessionTrace:return!!t;default:return!0}}}var A=i(6630),E=i(2614);class S extends T{static featureName=A.T;constructor(e){var t;super(e,A.T),this.setupInspectionEvents(e.agentIdentifier),t=e,p(u.Fw,(function(e,r){"string"==typeof e&&("/"!==e.charAt(0)&&(e="/"+e),t.runtime.customTransaction=(r||"http://custom.transaction")+e,(0,s.p)(u.Pl+u.Fw,[(0,c.t)()],void 0,void 0,t.ee))}),t),this.ee.on("api-send-rum",((e,t)=>(0,s.p)("send-rum",[e,t],void 0,this.featureName,this.ee))),this.importAggregator(e,(()=>i.e(478).then(i.bind(i,1983))))}setupInspectionEvents(e){const t=(t,r)=>{t&&(0,d.W)({agentIdentifier:e,timeStamp:t.timeStamp,loaded:"complete"===t.target.readyState,type:"window",name:r,data:t.target.location+""})};(0,b.sB)((e=>{t(e,"DOMContentLoaded")})),(0,b.GG)((e=>{t(e,"load")})),(0,b.Qr)((e=>{t(e,"navigate")})),this.ee.on(E.tS.UPDATE,((t,r)=>{(0,d.W)({agentIdentifier:e,type:"lifecycle",name:"session",data:r})}))}}var _=i(384);var N=i(2843),O=i(3878),I=i(782);class P extends T{static featureName=I.T;constructor(e){super(e,I.T),y.RI&&((0,N.u)((()=>(0,s.p)("docHidden",[(0,c.t)()],void 0,I.T,this.ee)),!0),(0,O.sp)("pagehide",(()=>(0,s.p)("winPagehide",[(0,c.t)()],void 0,I.T,this.ee))),this.importAggregator(e,(()=>i.e(478).then(i.bind(i,9917)))))}}class j extends T{static featureName=h.TZ;constructor(e){super(e,h.TZ),y.RI&&document.addEventListener("securitypolicyviolation",(e=>{(0,s.p)(h.xV,["Generic/CSPViolation/Detected"],void 0,this.featureName,this.ee)})),this.importAggregator(e,(()=>i.e(478).then(i.bind(i,8351))))}}var k=i(6774),C=i(3304);class L{constructor(e,t,r,n,i){this.name="UncaughtError",this.message="string"==typeof e?e:(0,C.A)(e),this.sourceURL=t,this.line=r,this.column=n,this.__newrelic=i}}function M(e){return D(e)?e:new L(void 0!==e?.message?e.message:e,e?.filename||e?.sourceURL,e?.lineno||e?.line,e?.colno||e?.col,e?.__newrelic,e?.cause)}function H(e){const t="Unhandled Promise Rejection: ";if(!e?.reason)return;if(D(e.reason)){try{e.reason.message.startsWith(t)||(e.reason.message=t+e.reason.message)}catch(e){}return M(e.reason)}const r=M(e.reason);return(r.message||"").startsWith(t)||(r.message=t+r.message),r}function K(e){if(e.error instanceof SyntaxError&&!/:\d+$/.test(e.error.stack?.trim())){const t=new L(e.message,e.filename,e.lineno,e.colno,e.error.__newrelic,e.cause);return t.name=SyntaxError.name,t}return D(e.error)?e.error:M(e)}function D(e){return e instanceof Error&&!!e.stack}function U(e,t,r,i,o=(0,c.t)()){"string"==typeof e&&(e=new Error(e)),(0,s.p)("err",[e,o,!1,t,r.runtime.isRecording,void 0,i],void 0,n.K7.jserrors,r.ee)}var F=i(3496),W=i(993),B=i(3785);function G(e,{customAttributes:t={},level:r=W.p_.INFO}={},n,i,o=(0,c.t)()){(0,B.R)(n.ee,e,t,r,i,o)}function V(e,t,r,i,o=(0,c.t)()){(0,s.p)(u.Pl+u.hG,[o,e,t,i],void 0,n.K7.genericEvents,r.ee)}function z(e){p(u.eY,(function(t){return function(e,t){const r={};let i,o;(0,l.R)(54,"newrelic.register"),e.init.api.allow_registered_children||(i=()=>(0,l.R)(55));t&&(0,F.I)(t)||(i=()=>(0,l.R)(48,t));const a={addPageAction:(n,i={})=>{u(V,[n,{...r,...i},e],t)},log:(n,i={})=>{u(G,[n,{...i,customAttributes:{...r,...i.customAttributes||{}}},e],t)},noticeError:(n,i={})=>{u(U,[n,{...r,...i},e],t)},setApplicationVersion:e=>{r["application.version"]=e},setCustomAttribute:(e,t)=>{r[e]=t},setUserId:e=>{r["enduser.id"]=e},metadata:{customAttributes:r,target:t,get connected(){return o||Promise.reject(new Error("Failed to connect"))}}};i?i():o=new Promise(((n,i)=>{try{const o=e.runtime?.entityManager;let s=!!o?.get().entityGuid,c=o?.getEntityGuidFor(t.licenseKey,t.applicationID),u=!!c;if(s&&u)t.entityGuid=c,n(a);else{const d=setTimeout((()=>i(new Error("Failed to connect - Timeout"))),15e3);function l(r){(0,F.A)(r,e)?s||=!0:t.licenseKey===r.licenseKey&&t.applicationID===r.applicationID&&(u=!0,t.entityGuid=r.entityGuid),s&&u&&(clearTimeout(d),e.ee.removeEventListener("entity-added",l),n(a))}e.ee.emit("api-send-rum",[r,t]),e.ee.on("entity-added",l)}}catch(f){i(f)}}));const u=async(t,r,a)=>{if(i)return i();const u=(0,c.t)();(0,s.p)(h.xV,["API/register/".concat(t.name,"/called")],void 0,n.K7.metrics,e.ee);try{await o;const n=e.init.api.duplicate_registered_data;(!0===n||Array.isArray(n)&&n.includes(a.entityGuid))&&t(...r,void 0,u),t(...r,a.entityGuid,u)}catch(e){(0,l.R)(50,e)}};return a}(e,t)}),e)}class Z extends T{static featureName=k.T;constructor(e){var t;super(e,k.T),t=e,p(u.o5,((e,r)=>U(e,r,t)),t),function(e){p(u.bt,(function(t){e.runtime.onerror=t}),e)}(e),function(e){let t=0;p(u.k6,(function(e,r){++t>10||(this.runtime.releaseIds[e.slice(-200)]=(""+r).slice(-200))}),e)}(e),z(e);try{this.removeOnAbort=new AbortController}catch(e){}this.ee.on("internal-error",((t,r)=>{this.abortHandler&&(0,s.p)("ierr",[M(t),(0,c.t)(),!0,{},e.runtime.isRecording,r],void 0,this.featureName,this.ee)})),y.gm.addEventListener("unhandledrejection",(t=>{this.abortHandler&&(0,s.p)("err",[H(t),(0,c.t)(),!1,{unhandledPromiseRejection:1},e.runtime.isRecording],void 0,this.featureName,this.ee)}),(0,O.jT)(!1,this.removeOnAbort?.signal)),y.gm.addEventListener("error",(t=>{this.abortHandler&&(0,s.p)("err",[K(t),(0,c.t)(),!1,{},e.runtime.isRecording],void 0,this.featureName,this.ee)}),(0,O.jT)(!1,this.removeOnAbort?.signal)),this.abortHandler=this.#r,this.importAggregator(e,(()=>i.e(478).then(i.bind(i,2176))))}#r(){this.removeOnAbort?.abort(),this.abortHandler=void 0}}var q=i(8990);let X=1;function Y(e){const t=typeof e;return!e||"object"!==t&&"function"!==t?-1:e===y.gm?0:(0,q.I)(e,"nr@id",(function(){return X++}))}function J(e){if("string"==typeof e&&e.length)return e.length;if("object"==typeof e){if("undefined"!=typeof ArrayBuffer&&e instanceof ArrayBuffer&&e.byteLength)return e.byteLength;if("undefined"!=typeof Blob&&e instanceof Blob&&e.size)return e.size;if(!("undefined"!=typeof FormData&&e instanceof FormData))try{return(0,C.A)(e).length}catch(e){return}}}var Q=i(8139),ee=i(7836),te=i(3434);const re={},ne=["open","send"];function ie(e){var t=e||ee.ee;const r=function(e){return(e||ee.ee).get("xhr")}(t);if(void 0===y.gm.XMLHttpRequest)return r;if(re[r.debugId]++)return r;re[r.debugId]=1,(0,Q.u)(t);var n=(0,te.YM)(r),i=y.gm.XMLHttpRequest,o=y.gm.MutationObserver,a=y.gm.Promise,s=y.gm.setInterval,c="readystatechange",u=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],d=[],f=y.gm.XMLHttpRequest=function(e){const t=new i(e),o=r.context(t);try{r.emit("new-xhr",[t],o),t.addEventListener(c,(a=o,function(){var e=this;e.readyState>3&&!a.resolved&&(a.resolved=!0,r.emit("xhr-resolved",[],e)),n.inPlace(e,u,"fn-",b)}),(0,O.jT)(!1))}catch(e){(0,l.R)(15,e);try{r.emit("internal-error",[e])}catch(e){}}var a;return t};function h(e,t){n.inPlace(t,["onreadystatechange"],"fn-",b)}if(function(e,t){for(var r in e)t[r]=e[r]}(i,f),f.prototype=i.prototype,n.inPlace(f.prototype,ne,"-xhr-",b),r.on("send-xhr-start",(function(e,t){h(e,t),function(e){d.push(e),o&&(p?p.then(v):s?s(v):(g=-g,m.data=g))}(t)})),r.on("open-xhr-start",h),o){var p=a&&a.resolve();if(!s&&!a){var g=1,m=document.createTextNode(g);new o(v).observe(m,{characterData:!0})}}else t.on("fn-end",(function(e){e[0]&&e[0].type===c||v()}));function v(){for(var e=0;e<d.length;e++)h(0,d[e]);d.length&&(d=[])}function b(e,t){return t}return r}var oe="fetch-",ae=oe+"body-",se=["arrayBuffer","blob","json","text","formData"],ce=y.gm.Request,ue=y.gm.Response,de="prototype";const le={};function fe(e){const t=function(e){return(e||ee.ee).get("fetch")}(e);if(!(ce&&ue&&y.gm.fetch))return t;if(le[t.debugId]++)return t;function r(e,r,n){var i=e[r];"function"==typeof i&&(e[r]=function(){var e,r=[...arguments],o={};t.emit(n+"before-start",[r],o),o[ee.P]&&o[ee.P].dt&&(e=o[ee.P].dt);var a=i.apply(this,r);return t.emit(n+"start",[r,e],a),a.then((function(e){return t.emit(n+"end",[null,e],a),e}),(function(e){throw t.emit(n+"end",[e],a),e}))})}return le[t.debugId]=1,se.forEach((e=>{r(ce[de],e,ae),r(ue[de],e,ae)})),r(y.gm,"fetch",oe),t.on(oe+"end",(function(e,r){var n=this;if(r){var i=r.headers.get("content-length");null!==i&&(n.rxSize=i),t.emit(oe+"done",[null,r],n)}else t.emit(oe+"done",[e],n)})),t}var he=i(7485);class pe{constructor(e){this.agentRef=e}generateTracePayload(t){const r=this.agentRef.loader_config;if(!this.shouldGenerateTrace(t)||!r)return null;var n=(r.accountID||"").toString()||null,i=(r.agentID||"").toString()||null,o=(r.trustKey||"").toString()||null;if(!n||!i)return null;var a=(0,e.ZF)(),s=(0,e.el)(),c=Date.now(),u={spanId:a,traceId:s,timestamp:c};return(t.sameOrigin||this.isAllowedOrigin(t)&&this.useTraceContextHeadersForCors())&&(u.traceContextParentHeader=this.generateTraceContextParentHeader(a,s),u.traceContextStateHeader=this.generateTraceContextStateHeader(a,c,n,i,o)),(t.sameOrigin&&!this.excludeNewrelicHeader()||!t.sameOrigin&&this.isAllowedOrigin(t)&&this.useNewrelicHeaderForCors())&&(u.newrelicHeader=this.generateTraceHeader(a,s,c,n,i,o)),u}generateTraceContextParentHeader(e,t){return"00-"+t+"-"+e+"-01"}generateTraceContextStateHeader(e,t,r,n,i){return i+"@nr=0-1-"+r+"-"+n+"-"+e+"----"+t}generateTraceHeader(e,t,r,n,i,o){if(!("function"==typeof y.gm?.btoa))return null;var a={v:[0,1],d:{ty:"Browser",ac:n,ap:i,id:e,tr:t,ti:r}};return o&&n!==o&&(a.d.tk=o),btoa((0,C.A)(a))}shouldGenerateTrace(e){return this.agentRef.init?.distributed_tracing?.enabled&&this.isAllowedOrigin(e)}isAllowedOrigin(e){var t=!1;const r=this.agentRef.init?.distributed_tracing;if(e.sameOrigin)t=!0;else if(r?.allowed_origins instanceof Array)for(var n=0;n<r.allowed_origins.length;n++){var i=(0,he.D)(r.allowed_origins[n]);if(e.hostname===i.hostname&&e.protocol===i.protocol&&e.port===i.port){t=!0;break}}return t}excludeNewrelicHeader(){var e=this.agentRef.init?.distributed_tracing;return!!e&&!!e.exclude_newrelic_header}useNewrelicHeaderForCors(){var e=this.agentRef.init?.distributed_tracing;return!!e&&!1!==e.cors_use_newrelic_header}useTraceContextHeadersForCors(){var e=this.agentRef.init?.distributed_tracing;return!!e&&!!e.cors_use_tracecontext_headers}}var ge=i(9300),me=i(7295),ve=["load","error","abort","timeout"],be=ve.length,ye=(0,_.dV)().o.REQ,we=(0,_.dV)().o.XHR;const Re="X-NewRelic-App-Data";class xe extends T{static featureName=ge.T;constructor(e){super(e,ge.T),this.dt=new pe(e),this.handler=(e,t,r,n)=>(0,s.p)(e,t,r,n,this.ee);try{const e={xmlhttprequest:"xhr",fetch:"fetch",beacon:"beacon"};y.gm?.performance?.getEntriesByType("resource").forEach((t=>{if(t.initiatorType in e&&0!==t.responseStatus){const r={status:t.responseStatus},i={rxSize:t.transferSize,duration:Math.floor(t.duration),cbTime:0};Te(r,t.name),this.handler("xhr",[r,i,t.startTime,t.responseEnd,e[t.initiatorType]],void 0,n.K7.ajax)}}))}catch(e){}fe(this.ee),ie(this.ee),function(e,t,r,i){function o(e){var t=this;t.totalCbs=0,t.called=0,t.cbTime=0,t.end=A,t.ended=!1,t.xhrGuids={},t.lastSize=null,t.loadCaptureCalled=!1,t.params=this.params||{},t.metrics=this.metrics||{},e.addEventListener("load",(function(r){E(t,e)}),(0,O.jT)(!1)),y.lR||e.addEventListener("progress",(function(e){t.lastSize=e.loaded}),(0,O.jT)(!1))}function a(e){this.params={method:e[0]},Te(this,e[1]),this.metrics={}}function u(t,r){e.loader_config.xpid&&this.sameOrigin&&r.setRequestHeader("X-NewRelic-ID",e.loader_config.xpid);var n=i.generateTracePayload(this.parsedOrigin);if(n){var o=!1;n.newrelicHeader&&(r.setRequestHeader("newrelic",n.newrelicHeader),o=!0),n.traceContextParentHeader&&(r.setRequestHeader("traceparent",n.traceContextParentHeader),n.traceContextStateHeader&&r.setRequestHeader("tracestate",n.traceContextStateHeader),o=!0),o&&(this.dt=n)}}function d(e,r){var n=this.metrics,i=e[0],o=this;if(n&&i){var a=J(i);a&&(n.txSize=a)}this.startTime=(0,c.t)(),this.body=i,this.listener=function(e){try{"abort"!==e.type||o.loadCaptureCalled||(o.params.aborted=!0),("load"!==e.type||o.called===o.totalCbs&&(o.onloadCalled||"function"!=typeof r.onload)&&"function"==typeof o.end)&&o.end(r)}catch(e){try{t.emit("internal-error",[e])}catch(e){}}};for(var s=0;s<be;s++)r.addEventListener(ve[s],this.listener,(0,O.jT)(!1))}function l(e,t,r){this.cbTime+=e,t?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof r.onload||"function"!=typeof this.end||this.end(r)}function f(e,t){var r=""+Y(e)+!!t;this.xhrGuids&&!this.xhrGuids[r]&&(this.xhrGuids[r]=!0,this.totalCbs+=1)}function p(e,t){var r=""+Y(e)+!!t;this.xhrGuids&&this.xhrGuids[r]&&(delete this.xhrGuids[r],this.totalCbs-=1)}function g(){this.endTime=(0,c.t)()}function m(e,r){r instanceof we&&"load"===e[0]&&t.emit("xhr-load-added",[e[1],e[2]],r)}function v(e,r){r instanceof we&&"load"===e[0]&&t.emit("xhr-load-removed",[e[1],e[2]],r)}function b(e,t,r){t instanceof we&&("onload"===r&&(this.onload=!0),("load"===(e[0]&&e[0].type)||this.onload)&&(this.xhrCbStart=(0,c.t)()))}function w(e,r){this.xhrCbStart&&t.emit("xhr-cb-time",[(0,c.t)()-this.xhrCbStart,this.onload,r],r)}function R(e){var t,r=e[1]||{};if("string"==typeof e[0]?0===(t=e[0]).length&&y.RI&&(t=""+y.gm.location.href):e[0]&&e[0].url?t=e[0].url:y.gm?.URL&&e[0]&&e[0]instanceof URL?t=e[0].href:"function"==typeof e[0].toString&&(t=e[0].toString()),"string"==typeof t&&0!==t.length){t&&(this.parsedOrigin=(0,he.D)(t),this.sameOrigin=this.parsedOrigin.sameOrigin);var n=i.generateTracePayload(this.parsedOrigin);if(n&&(n.newrelicHeader||n.traceContextParentHeader))if(e[0]&&e[0].headers)s(e[0].headers,n)&&(this.dt=n);else{var o={};for(var a in r)o[a]=r[a];o.headers=new Headers(r.headers||{}),s(o.headers,n)&&(this.dt=n),e.length>1?e[1]=o:e.push(o)}}function s(e,t){var r=!1;return t.newrelicHeader&&(e.set("newrelic",t.newrelicHeader),r=!0),t.traceContextParentHeader&&(e.set("traceparent",t.traceContextParentHeader),t.traceContextStateHeader&&e.set("tracestate",t.traceContextStateHeader),r=!0),r}}function x(e,t){this.params={},this.metrics={},this.startTime=(0,c.t)(),this.dt=t,e.length>=1&&(this.target=e[0]),e.length>=2&&(this.opts=e[1]);var r,n=this.opts||{},i=this.target;"string"==typeof i?r=i:"object"==typeof i&&i instanceof ye?r=i.url:y.gm?.URL&&"object"==typeof i&&i instanceof URL&&(r=i.href),Te(this,r);var o=(""+(i&&i instanceof ye&&i.method||n.method||"GET")).toUpperCase();this.params.method=o,this.body=n.body,this.txSize=J(n.body)||0}function T(e,t){if(this.endTime=(0,c.t)(),this.params||(this.params={}),(0,me.iW)(this.params))return;let i;this.params.status=t?t.status:0,"string"==typeof this.rxSize&&this.rxSize.length>0&&(i=+this.rxSize);const o={txSize:this.txSize,rxSize:i,duration:(0,c.t)()-this.startTime};r("xhr",[this.params,o,this.startTime,this.endTime,"fetch"],this,n.K7.ajax)}function A(e){const t=this.params,i=this.metrics;if(!this.ended){this.ended=!0;for(let t=0;t<be;t++)e.removeEventListener(ve[t],this.listener,!1);t.aborted||(0,me.iW)(t)||(i.duration=(0,c.t)()-this.startTime,this.loadCaptureCalled||4!==e.readyState?null==t.status&&(t.status=0):E(this,e),i.cbTime=this.cbTime,r("xhr",[t,i,this.startTime,this.endTime,"xhr"],this,n.K7.ajax))}}function E(e,r){e.params.status=r.status;var i=function(e,t){var r=e.responseType;return"json"===r&&null!==t?t:"arraybuffer"===r||"blob"===r||"json"===r?J(e.response):"text"===r||""===r||void 0===r?J(e.responseText):void 0}(r,e.lastSize);if(i&&(e.metrics.rxSize=i),e.sameOrigin&&r.getAllResponseHeaders().indexOf(Re)>=0){var o=r.getResponseHeader(Re);o&&((0,s.p)(h.rs,["Ajax/CrossApplicationTracing/Header/Seen"],void 0,n.K7.metrics,t),e.params.cat=o.split(", ").pop())}e.loadCaptureCalled=!0}t.on("new-xhr",o),t.on("open-xhr-start",a),t.on("open-xhr-end",u),t.on("send-xhr-start",d),t.on("xhr-cb-time",l),t.on("xhr-load-added",f),t.on("xhr-load-removed",p),t.on("xhr-resolved",g),t.on("addEventListener-end",m),t.on("removeEventListener-end",v),t.on("fn-end",w),t.on("fetch-before-start",R),t.on("fetch-start",x),t.on("fn-start",b),t.on("fetch-done",T)}(e,this.ee,this.handler,this.dt),this.importAggregator(e,(()=>i.e(478).then(i.bind(i,3845))))}}function Te(e,t){var r=(0,he.D)(t),n=e.params||e;n.hostname=r.hostname,n.port=r.port,n.protocol=r.protocol,n.host=r.hostname+":"+r.port,n.pathname=r.pathname,e.parsedOrigin=r,e.sameOrigin=r.sameOrigin}const Ae={},Ee=["pushState","replaceState"];function Se(e){const t=function(e){return(e||ee.ee).get("history")}(e);return!y.RI||Ae[t.debugId]++||(Ae[t.debugId]=1,(0,te.YM)(t).inPlace(window.history,Ee,"-")),t}var _e=i(3738);function Ne(e){p(u.BL,(function(t=Date.now()){const r=t-y.WN;r<0&&(0,l.R)(62,t),(0,s.p)(h.XG,[u.BL,{time:r}],void 0,n.K7.metrics,e.ee),e.addToTrace({name:u.BL,start:t,origin:"nr"}),(0,s.p)(u.Pl+u.hG,[r,u.BL],void 0,n.K7.genericEvents,e.ee)}),e)}const{He:Oe,bD:Ie,d3:Pe,Kp:je,TZ:ke,Lc:Ce,uP:Le,Rz:Me}=_e;class He extends T{static featureName=ke;constructor(e){var t;super(e,ke),t=e,p(u.U2,(function(e){if(!(e&&"object"==typeof e&&e.name&&e.start))return;const r={n:e.name,s:e.start-y.WN,e:(e.end||e.start)-y.WN,o:e.origin||"",t:"api"};r.s<0||r.e<0||r.e<r.s?(0,l.R)(61,{start:r.s,end:r.e}):(0,s.p)("bstApi",[r],void 0,n.K7.sessionTrace,t.ee)}),t),Ne(e);if(!(0,R.V)(e.init))return void this.deregisterDrain();const r=this.ee;let o;Se(r),this.eventsEE=(0,Q.u)(r),this.eventsEE.on(Le,(function(e,t){this.bstStart=(0,c.t)()})),this.eventsEE.on(Ce,(function(e,t){(0,s.p)("bst",[e[0],t,this.bstStart,(0,c.t)()],void 0,n.K7.sessionTrace,r)})),r.on(Me+Pe,(function(e){this.time=(0,c.t)(),this.startPath=location.pathname+location.hash})),r.on(Me+je,(function(e){(0,s.p)("bstHist",[location.pathname+location.hash,this.startPath,this.time],void 0,n.K7.sessionTrace,r)}));try{o=new PerformanceObserver((e=>{const t=e.getEntries();(0,s.p)(Oe,[t],void 0,n.K7.sessionTrace,r)})),o.observe({type:Ie,buffered:!0})}catch(e){}this.importAggregator(e,(()=>i.e(478).then(i.bind(i,6974))),{resourceObserver:o})}}var Ke=i(6344);class De extends T{static featureName=Ke.TZ;#n;#i;constructor(e){var t;let r;super(e,Ke.TZ),t=e,p(u.CH,(function(){(0,s.p)(u.CH,[],void 0,n.K7.sessionReplay,t.ee)}),t),function(e){p(u.Tb,(function(){(0,s.p)(u.Tb,[],void 0,n.K7.sessionReplay,e.ee)}),e)}(e),this.#i=e;try{r=JSON.parse(localStorage.getItem("".concat(E.H3,"_").concat(E.uh)))}catch(e){}(0,w.SR)(e.init)&&this.ee.on(Ke.G4.RECORD,(()=>this.#o())),this.#a(r)?(this.#n=r?.sessionReplayMode,this.#s()):this.importAggregator(this.#i,(()=>i.e(478).then(i.bind(i,6167)))),this.ee.on("err",(e=>{this.#i.runtime.isRecording&&(this.errorNoticed=!0,(0,s.p)(Ke.G4.ERROR_DURING_REPLAY,[e],void 0,this.featureName,this.ee))}))}#a(e){return e&&(e.sessionReplayMode===E.g.FULL||e.sessionReplayMode===E.g.ERROR)||(0,w.Aw)(this.#i.init)}#c=!1;async#s(e){if(!this.#c){this.#c=!0;try{const{Recorder:t}=await Promise.all([i.e(478),i.e(249)]).then(i.bind(i,8589));this.recorder??=new t({...this,mode:this.#n,agentRef:this.#i,trigger:e,timeKeeper:this.#i.runtime.timeKeeper}),this.recorder.startRecording(),this.abortHandler=this.recorder.stopRecording}catch(e){this.parent.ee.emit("internal-error",[e])}this.importAggregator(this.#i,(()=>i.e(478).then(i.bind(i,6167))),{recorder:this.recorder,errorNoticed:this.errorNoticed})}}#o(){this.featAggregate?this.featAggregate.mode!==E.g.FULL&&this.featAggregate.initializeRecording(E.g.FULL,!0):(this.#n=E.g.FULL,this.#s(Ke.Qb.API),this.recorder&&this.recorder.parent.mode!==E.g.FULL&&(this.recorder.parent.mode=E.g.FULL,this.recorder.stopRecording(),this.recorder.startRecording(),this.abortHandler=this.recorder.stopRecording))}}var Ue=i(3962);function Fe(e){const t=e.ee.get("tracer");function r(){}p(u.dT,(function(e){return(new r).get("object"==typeof e?e:{})}),e);const i=r.prototype={createTracer:function(r,i){var o={},a=this,d="function"==typeof i;return(0,s.p)(h.xV,["API/createTracer/called"],void 0,n.K7.metrics,e.ee),e.runSoftNavOverSpa||(0,s.p)(u.hw+"tracer",[(0,c.t)(),r,o],a,n.K7.spa,e.ee),function(){if(t.emit((d?"":"no-")+"fn-start",[(0,c.t)(),a,d],o),d)try{return i.apply(this,arguments)}catch(e){const r="string"==typeof e?new Error(e):e;throw t.emit("fn-err",[arguments,this,r],o),r}finally{t.emit("fn-end",[(0,c.t)()],o)}}}};["actionText","setName","setAttribute","save","ignore","onEnd","getContext","end","get"].forEach((t=>{p.apply(this,[t,function(){return(0,s.p)(u.hw+t,[(0,c.t)(),...arguments],this,e.runSoftNavOverSpa?n.K7.softNav:n.K7.spa,e.ee),this},e,i])})),p(u.PA,(function(){e.runSoftNavOverSpa?(0,s.p)(u.hw+"routeName",[performance.now(),...arguments],void 0,n.K7.softNav,e.ee):(0,s.p)(u.Pl+"routeName",[(0,c.t)(),...arguments],this,n.K7.spa,e.ee)}),e)}class We extends T{static featureName=Ue.TZ;constructor(e){if(super(e,Ue.TZ),Fe(e),!y.RI||!(0,_.dV)().o.MO)return;const t=Se(this.ee);Ue.tC.forEach((e=>{(0,O.sp)(e,(e=>{a(e)}),!0)}));const r=()=>(0,s.p)("newURL",[(0,c.t)(),""+window.location],void 0,this.featureName,this.ee);t.on("pushState-end",r),t.on("replaceState-end",r);try{this.removeOnAbort=new AbortController}catch(e){}(0,O.sp)("popstate",(e=>(0,s.p)("newURL",[e.timeStamp,""+window.location],void 0,this.featureName,this.ee)),!0,this.removeOnAbort?.signal);let n=!1;const o=new((0,_.dV)().o.MO)(((e,t)=>{n||(n=!0,requestAnimationFrame((()=>{(0,s.p)("newDom",[(0,c.t)()],void 0,this.featureName,this.ee),n=!1})))})),a=(0,x.s)((e=>{(0,s.p)("newUIEvent",[e],void 0,this.featureName,this.ee),o.observe(document.body,{attributes:!0,childList:!0,subtree:!0,characterData:!0})}),100,{leading:!0});this.abortHandler=function(){this.removeOnAbort?.abort(),o.disconnect(),this.abortHandler=void 0},this.importAggregator(e,(()=>i.e(478).then(i.bind(i,4393))),{domObserver:o})}}var Be=i(7378);const Ge={},Ve=["appendChild","insertBefore","replaceChild"];function ze(e){const t=function(e){return(e||ee.ee).get("jsonp")}(e);if(!y.RI||Ge[t.debugId])return t;Ge[t.debugId]=!0;var r=(0,te.YM)(t),n=/[?&](?:callback|cb)=([^&#]+)/,i=/(.*)\.([^.]+)/,o=/^(\w+)(\.|$)(.*)$/;function a(e,t){if(!e)return t;const r=e.match(o),n=r[1];return a(r[3],t[n])}return r.inPlace(Node.prototype,Ve,"dom-"),t.on("dom-start",(function(e){!function(e){if(!e||"string"!=typeof e.nodeName||"script"!==e.nodeName.toLowerCase())return;if("function"!=typeof e.addEventListener)return;var o=(s=e.src,c=s.match(n),c?c[1]:null);var s,c;if(!o)return;var u=function(e){var t=e.match(i);if(t&&t.length>=3)return{key:t[2],parent:a(t[1],window)};return{key:e,parent:window}}(o);if("function"!=typeof u.parent[u.key])return;var d={};function l(){t.emit("jsonp-end",[],d),e.removeEventListener("load",l,(0,O.jT)(!1)),e.removeEventListener("error",f,(0,O.jT)(!1))}function f(){t.emit("jsonp-error",[],d),t.emit("jsonp-end",[],d),e.removeEventListener("load",l,(0,O.jT)(!1)),e.removeEventListener("error",f,(0,O.jT)(!1))}r.inPlace(u.parent,[u.key],"cb-",d),e.addEventListener("load",l,(0,O.jT)(!1)),e.addEventListener("error",f,(0,O.jT)(!1)),t.emit("new-jsonp",[e.src],d)}(e[0])})),t}const Ze={};function qe(e){const t=function(e){return(e||ee.ee).get("promise")}(e);if(Ze[t.debugId])return t;Ze[t.debugId]=!0;var r=t.context,n=(0,te.YM)(t),i=y.gm.Promise;return i&&function(){function e(r){var o=t.context(),a=n(r,"executor-",o,null,!1);const s=Reflect.construct(i,[a],e);return t.context(s).getCtx=function(){return o},s}y.gm.Promise=e,Object.defineProperty(e,"name",{value:"Promise"}),e.toString=function(){return i.toString()},Object.setPrototypeOf(e,i),["all","race"].forEach((function(r){const n=i[r];e[r]=function(e){let i=!1;[...e||[]].forEach((e=>{this.resolve(e).then(a("all"===r),a(!1))}));const o=n.apply(this,arguments);return o;function a(e){return function(){t.emit("propagate",[null,!i],o,!1,!1),i=i||!e}}}})),["resolve","reject"].forEach((function(r){const n=i[r];e[r]=function(e){const r=n.apply(this,arguments);return e!==r&&t.emit("propagate",[e,!0],r,!1,!1),r}})),e.prototype=i.prototype;const o=i.prototype.then;i.prototype.then=function(...e){var i=this,a=r(i);a.promise=i,e[0]=n(e[0],"cb-",a,null,!1),e[1]=n(e[1],"cb-",a,null,!1);const s=o.apply(this,e);return a.nextPromise=s,t.emit("propagate",[i,!0],s,!1,!1),s},i.prototype.then[te.Jt]=o,t.on("executor-start",(function(e){e[0]=n(e[0],"resolve-",this,null,!1),e[1]=n(e[1],"resolve-",this,null,!1)})),t.on("executor-err",(function(e,t,r){e[1](r)})),t.on("cb-end",(function(e,r,n){t.emit("propagate",[n,!0],this.nextPromise,!1,!1)})),t.on("propagate",(function(e,r,n){this.getCtx&&!r||(this.getCtx=function(){if(e instanceof Promise)var r=t.context(e);return r&&r.getCtx?r.getCtx():this})}))}(),t}const Xe={},Ye="setTimeout",$e="setInterval",Je="clearTimeout",Qe="-start",et=[Ye,"setImmediate",$e,Je,"clearImmediate"];function tt(e){const t=function(e){return(e||ee.ee).get("timer")}(e);if(Xe[t.debugId]++)return t;Xe[t.debugId]=1;var r=(0,te.YM)(t);return r.inPlace(y.gm,et.slice(0,2),Ye+"-"),r.inPlace(y.gm,et.slice(2,3),$e+"-"),r.inPlace(y.gm,et.slice(3),Je+"-"),t.on($e+Qe,(function(e,t,n){e[0]=r(e[0],"fn-",null,n)})),t.on(Ye+Qe,(function(e,t,n){this.method=n,this.timerDuration=isNaN(e[1])?0:+e[1],e[0]=r(e[0],"fn-",this,n)})),t}const rt={};function nt(e){const t=function(e){return(e||ee.ee).get("mutation")}(e);if(!y.RI||rt[t.debugId])return t;rt[t.debugId]=!0;var r=(0,te.YM)(t),n=y.gm.MutationObserver;return n&&(window.MutationObserver=function(e){return this instanceof n?new n(r(e,"fn-")):n.apply(this,arguments)},MutationObserver.prototype=n.prototype),t}const{TZ:it,d3:ot,Kp:at,$p:st,wW:ct,e5:ut,tH:dt,uP:lt,rw:ft,Lc:ht}=Be;class pt extends T{static featureName=it;constructor(e){if(super(e,it),Fe(e),!y.RI)return;try{this.removeOnAbort=new AbortController}catch(e){}let t,r=0;const n=this.ee.get("tracer"),o=ze(this.ee),a=qe(this.ee),u=tt(this.ee),d=ie(this.ee),l=this.ee.get("events"),f=fe(this.ee),h=Se(this.ee),p=nt(this.ee);function g(e,t){h.emit("newURL",[""+window.location,t])}function m(){r++,t=window.location.hash,this[lt]=(0,c.t)()}function v(){r--,window.location.hash!==t&&g(0,!0);var e=(0,c.t)();this[ut]=~~this[ut]+e-this[lt],this[ht]=e}function b(e,t){e.on(t,(function(){this[t]=(0,c.t)()}))}this.ee.on(lt,m),a.on(ft,m),o.on(ft,m),this.ee.on(ht,v),a.on(ct,v),o.on(ct,v),this.ee.on("fn-err",((...t)=>{t[2]?.__newrelic?.[e.agentIdentifier]||(0,s.p)("function-err",[...t],void 0,this.featureName,this.ee)})),this.ee.buffer([lt,ht,"xhr-resolved"],this.featureName),l.buffer([lt],this.featureName),u.buffer(["setTimeout"+at,"clearTimeout"+ot,lt],this.featureName),d.buffer([lt,"new-xhr","send-xhr"+ot],this.featureName),f.buffer([dt+ot,dt+"-done",dt+st+ot,dt+st+at],this.featureName),h.buffer(["newURL"],this.featureName),p.buffer([lt],this.featureName),a.buffer(["propagate",ft,ct,"executor-err","resolve"+ot],this.featureName),n.buffer([lt,"no-"+lt],this.featureName),o.buffer(["new-jsonp","cb-start","jsonp-error","jsonp-end"],this.featureName),b(f,dt+ot),b(f,dt+"-done"),b(o,"new-jsonp"),b(o,"jsonp-end"),b(o,"cb-start"),h.on("pushState-end",g),h.on("replaceState-end",g),window.addEventListener("hashchange",g,(0,O.jT)(!0,this.removeOnAbort?.signal)),window.addEventListener("load",g,(0,O.jT)(!0,this.removeOnAbort?.signal)),window.addEventListener("popstate",(function(){g(0,r>1)}),(0,O.jT)(!0,this.removeOnAbort?.signal)),this.abortHandler=this.#r,this.importAggregator(e,(()=>i.e(478).then(i.bind(i,5592))))}#r(){this.removeOnAbort?.abort(),this.abortHandler=void 0}}var gt=i(3333);class mt extends T{static featureName=gt.TZ;constructor(e){super(e,gt.TZ);const t=[e.init.page_action.enabled,e.init.performance.capture_marks,e.init.performance.capture_measures,e.init.user_actions.enabled,e.init.performance.resources.enabled];var r;if(r=e,p(u.hG,((e,t)=>V(e,t,r)),r),function(e){p(u.fF,(function(){(0,s.p)(u.Pl+u.fF,[(0,c.t)(),...arguments],void 0,n.K7.genericEvents,e.ee)}),e)}(e),Ne(e),z(e),function(e){p(u.V1,(function(t,r){const i=(0,c.t)(),{start:o,end:a,customAttributes:d}=r||{},f={customAttributes:d||{}};if("object"!=typeof f.customAttributes||"string"!=typeof t||0===t.length)return void(0,l.R)(57);const h=(e,t)=>null==e?t:"number"==typeof e?e:e instanceof PerformanceMark?e.startTime:Number.NaN;if(f.start=h(o,0),f.end=h(a,i),Number.isNaN(f.start)||Number.isNaN(f.end))(0,l.R)(57);else{if(f.duration=f.end-f.start,!(f.duration<0))return(0,s.p)(u.Pl+u.V1,[f,t],void 0,n.K7.genericEvents,e.ee),f;(0,l.R)(58)}}),e)}(e),y.RI&&(e.init.user_actions.enabled&&(gt.Zp.forEach((e=>(0,O.sp)(e,(e=>(0,s.p)("ua",[e],void 0,this.featureName,this.ee)),!0))),gt.qN.forEach((e=>{const t=(0,x.s)((e=>{(0,s.p)("ua",[e],void 0,this.featureName,this.ee)}),500,{leading:!0});(0,O.sp)(e,t)}))),e.init.performance.resources.enabled&&y.gm.PerformanceObserver?.supportedEntryTypes.includes("resource"))){new PerformanceObserver((e=>{e.getEntries().forEach((e=>{(0,s.p)("browserPerformance.resource",[e],void 0,this.featureName,this.ee)}))})).observe({type:"resource",buffered:!0})}t.some((e=>e))?this.importAggregator(e,(()=>i.e(478).then(i.bind(i,8019)))):this.deregisterDrain()}}var vt=i(2646);const bt=new Map;function yt(e,t,r,n){if("object"!=typeof t||!t||"string"!=typeof r||!r||"function"!=typeof t[r])return(0,l.R)(29);const i=function(e){return(e||ee.ee).get("logger")}(e),o=(0,te.YM)(i),a=new vt.y(ee.P);a.level=n.level,a.customAttributes=n.customAttributes;const s=t[r]?.[te.Jt]||t[r];return bt.set(s,a),o.inPlace(t,[r],"wrap-logger-",(()=>bt.get(s))),i}var wt=i(1910);class Rt extends T{static featureName=W.TZ;constructor(e){var t;super(e,W.TZ),t=e,p(u.$9,((e,r)=>G(e,r,t)),t),function(e){p(u.Wb,((t,r,{customAttributes:n={},level:i=W.p_.INFO}={})=>{yt(e.ee,t,r,{customAttributes:n,level:i})}),e)}(e),z(e);const r=this.ee;["log","error","warn","info","debug","trace"].forEach((e=>{(0,wt.i)(y.gm.console[e]),yt(r,y.gm.console,e,{level:"log"===e?"info":e})})),this.ee.on("wrap-logger-end",(function([e]){const{level:t,customAttributes:n}=this;(0,B.R)(r,e,n,t)})),this.importAggregator(e,(()=>i.e(478).then(i.bind(i,5288))))}}new class extends r{constructor(e){var t;(super(),y.gm)?(this.features={},(0,_.bQ)(this.agentIdentifier,this),this.desiredFeatures=new Set(e.features||[]),this.desiredFeatures.add(S),this.runSoftNavOverSpa=[...this.desiredFeatures].some((e=>e.featureName===n.K7.softNav)),(0,a.j)(this,e,e.loaderType||"agent"),t=this,p(u.cD,(function(e,r,n=!1){if("string"==typeof e){if(["string","number","boolean"].includes(typeof r)||null===r)return g(t,e,r,u.cD,n);(0,l.R)(40,typeof r)}else(0,l.R)(39,typeof e)}),t),function(e){p(u.Dl,(function(t){if("string"==typeof t||null===t)return g(e,"enduser.id",t,u.Dl,!0);(0,l.R)(41,typeof t)}),e)}(this),function(e){p(u.nb,(function(t){if("string"==typeof t||null===t)return g(e,"application.version",t,u.nb,!1);(0,l.R)(42,typeof t)}),e)}(this),function(e){p(u.d3,(function(){e.ee.emit("manual-start-all")}),e)}(this),this.run()):(0,l.R)(21)}get config(){return{info:this.info,init:this.init,loader_config:this.loader_config,runtime:this.runtime}}get api(){return this}run(){try{const e=function(e){const t={};return o.forEach((r=>{t[r]=!!e[r]?.enabled})),t}(this.init),t=[...this.desiredFeatures];t.sort(((e,t)=>n.P3[e.featureName]-n.P3[t.featureName])),t.forEach((t=>{if(!e[t.featureName]&&t.featureName!==n.K7.pageViewEvent)return;if(this.runSoftNavOverSpa&&t.featureName===n.K7.spa)return;if(!this.runSoftNavOverSpa&&t.featureName===n.K7.softNav)return;const r=function(e){switch(e){case n.K7.ajax:return[n.K7.jserrors];case n.K7.sessionTrace:return[n.K7.ajax,n.K7.pageViewEvent];case n.K7.sessionReplay:return[n.K7.sessionTrace];case n.K7.pageViewTiming:return[n.K7.pageViewEvent];default:return[]}}(t.featureName).filter((e=>!(e in this.features)));r.length>0&&(0,l.R)(36,{targetFeature:t.featureName,missingDependencies:r}),this.features[t.featureName]=new t(this)}))}catch(e){(0,l.R)(22,e);for(const e in this.features)this.features[e].abortHandler?.();const t=(0,_.Zm)();delete t.initializedAgents[this.agentIdentifier]?.features,delete this.sharedAggregator;return t.ee.get(this.agentIdentifier).abort(),!1}}}({features:[xe,S,P,He,De,j,Z,mt,Rt,We,pt],loaderType:"spa"})})()})();</script>
<script>
var gform;gform||(document.addEventListener("gform_main_scripts_loaded",function(){gform.scriptsLoaded=!0}),document.addEventListener("gform/theme/scripts_loaded",function(){gform.themeScriptsLoaded=!0}),window.addEventListener("DOMContentLoaded",function(){gform.domLoaded=!0}),gform={domLoaded:!1,scriptsLoaded:!1,themeScriptsLoaded:!1,isFormEditor:()=>"function"==typeof InitializeEditor,callIfLoaded:function(o){return!(!gform.domLoaded||!gform.scriptsLoaded||!gform.themeScriptsLoaded&&!gform.isFormEditor()||(gform.isFormEditor()&&console.warn("The use of gform.initializeOnLoaded() is deprecated in the form editor context and will be removed in Gravity Forms 3.1."),o(),0))},initializeOnLoaded:function(o){gform.callIfLoaded(o)||(document.addEventListener("gform_main_scripts_loaded",()=>{gform.scriptsLoaded=!0,gform.callIfLoaded(o)}),document.addEventListener("gform/theme/scripts_loaded",()=>{gform.themeScriptsLoaded=!0,gform.callIfLoaded(o)}),window.addEventListener("DOMContentLoaded",()=>{gform.domLoaded=!0,gform.callIfLoaded(o)}))},hooks:{action:{},filter:{}},addAction:function(o,r,e,t){gform.addHook("action",o,r,e,t)},addFilter:function(o,r,e,t){gform.addHook("filter",o,r,e,t)},doAction:function(o){gform.doHook("action",o,arguments)},applyFilters:function(o){return gform.doHook("filter",o,arguments)},removeAction:function(o,r){gform.removeHook("action",o,r)},removeFilter:function(o,r,e){gform.removeHook("filter",o,r,e)},addHook:function(o,r,e,t,n){null==gform.hooks[o][r]&&(gform.hooks[o][r]=[]);var d=gform.hooks[o][r];null==n&&(n=r+"_"+d.length),gform.hooks[o][r].push({tag:n,callable:e,priority:t=null==t?10:t})},doHook:function(r,o,e){var t;if(e=Array.prototype.slice.call(e,1),null!=gform.hooks[r][o]&&((o=gform.hooks[r][o]).sort(function(o,r){return o.priority-r.priority}),o.forEach(function(o){"function"!=typeof(t=o.callable)&&(t=window[t]),"action"==r?t.apply(null,e):e[0]=t.apply(null,e)})),"filter"==r)return e[0]},removeHook:function(o,r,t,n){var e;null!=gform.hooks[o][r]&&(e=(e=gform.hooks[o][r]).filter(function(o,r,e){return!!(null!=n&&n!=o.tag||null!=t&&t!=o.priority)}),gform.hooks[o][r]=e)}});
</script>

<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Goodbye to All That: Reflections of a GOP Operative Who Left the Cult | Truthout</title>

<!-- GTM dataLayer - Google Analytics - TO5 -->
        <script>
          window.dataLayer = window.dataLayer || [];
          dataLayer.push({
    "page_event": "to_data_push",
    "page_post_type": "article",
    "page_publish_date": "2011-09-03 15:09:39",
    "page_first_author": "Mike Lofgren",
    "page_description": "(Photo: Carolyn Tiry \/ Flickr) Barbara Stanwyck: &ldquo;We\\'re both rotten!&rdquo; Fred MacMurray: &ldquo;Yeah &ndash; only you\\'re a little more rotten.&rdquo; &#x2d;&rdquo;Double Indemnity&rdquo; (1944)&#8230;",
    "page_source": "Truthout",
    "page_primary_topic": "",
    "page_primary_section": "",
    "page_tags": "",
    "page_word_count": "6148",
    "page_seo_title": "",
    "page_full_title": "Goodbye to All That: Reflections of a GOP Operative Who Left the Cult",
    "page_post_id": "218684",
    "page_category": "News Analysis",
    "page_sections": ""
});
       </script>

<!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-TXMPNN7');</script>
    <!-- End Google Tag Manager -->

<!-- Facebook Pixel Code -->
    <script>
      ! function(f, b, e, v, n, t, s) {
        if (f.fbq) return;
        n = f.fbq = function() {
          n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments)
        };
        if (!f._fbq) f._fbq = n;
        n.push = n;
        n.loaded = !0;
        n.version = '2.0';
        n.queue = [];
        t = b.createElement(e);
        t.async = !0;
        t.src = v;
        s = b.getElementsByTagName(e)[0];
        s.parentNode.insertBefore(t, s)
      }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
      fbq('init', '717290745328772');
      fbq('track', 'PageView');
    </script>
    	<style>img:is([sizes="auto" i], [sizes^="auto," i]) { contain-intrinsic-size: 3000px 1500px }</style>

<!-- The SEO Framework by Sybre Waaijer -->
<meta name="robots" content="max-snippet:-1,max-image-preview:large,max-video-preview:-1" />
<link rel="canonical" href="https://truthout.org/articles/goodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult/" />
<meta name="description" content="(Photo: Carolyn Tiry / Flickr) Barbara Stanwyck: &ldquo;We&#039;re both rotten!&rdquo; Fred MacMurray: &ldquo;Yeah &ndash; only you&#039;re a little more rotten.&rdquo; &#x2d;&rdquo;Double Indemnity&rdquo; (1944)&#8230;" />
<meta name="theme-color" content="#000000" />
<meta property="og:type" content="article" />
<meta property="og:locale" content="en_US" />
<meta property="og:site_name" content="Truthout" />
<meta property="og:title" content="Goodbye to All That: Reflections of a GOP Operative Who Left the Cult" />
<meta property="og:description" content="(Photo: Carolyn Tiry / Flickr) Barbara Stanwyck: &ldquo;We&#039;re both rotten!&rdquo; Fred MacMurray: &ldquo;Yeah &ndash; only you&#039;re a little more rotten.&rdquo; &#x2d;&rdquo;Double Indemnity&rdquo; (1944)&#8230;" />
<meta property="og:url" content="https://truthout.org/articles/goodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult/" />
<meta property="og:image" content="https://truthout.org/app/uploads/2017/12/Goodbye-to-All-That-Reflections-of-a-GOP-Operative-Who-Left-the-Cult.jpg" />
<meta property="og:image:width" content="240" />
<meta property="og:image:height" content="272" />
<meta property="article:published_time" content="2011-09-03T15:09:39+00:00" />
<meta property="article:modified_time" content="2011-09-03T15:09:39+00:00" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Goodbye to All That: Reflections of a GOP Operative Who Left the Cult" />
<meta name="twitter:description" content="(Photo: Carolyn Tiry / Flickr) Barbara Stanwyck: &ldquo;We&#039;re both rotten!&rdquo; Fred MacMurray: &ldquo;Yeah &ndash; only you&#039;re a little more rotten.&rdquo; &#x2d;&rdquo;Double Indemnity&rdquo; (1944)&#8230;" />
<meta name="twitter:image" content="https://truthout.org/app/uploads/2017/12/Goodbye-to-All-That-Reflections-of-a-GOP-Operative-Who-Left-the-Cult.jpg" />
<script type="application/ld+json">{"@context":"https://schema.org","@graph":[{"@type":"WebSite","@id":"https://truthout.org/#/schema/WebSite","url":"https://truthout.org/","name":"Truthout","description":"Fearless Independent Journalism","inLanguage":"en-US","potentialAction":{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://truthout.org/search/{search_term_string}/"},"query-input":"required name=search_term_string"},"publisher":{"@type":"Organization","@id":"https://truthout.org/#/schema/Organization","name":"Truthout","url":"https://truthout.org/","logo":{"@type":"ImageObject","url":"https://truthout.org/app/uploads/2018/03/cropped-Truthout-T-logo-sq-1200x1200-e1521532408148.png","contentUrl":"https://truthout.org/app/uploads/2018/03/cropped-Truthout-T-logo-sq-1200x1200-e1521532408148.png","width":512,"height":512,"inLanguage":"en-US","caption":"Truthout","contentSize":"6938"}}},{"@type":"WebPage","@id":"https://truthout.org/articles/goodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult/","url":"https://truthout.org/articles/goodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult/","name":"Goodbye to All That: Reflections of a GOP Operative Who Left the Cult | Truthout","description":"(Photo: Carolyn Tiry / Flickr) Barbara Stanwyck: &ldquo;We&#039;re both rotten!&rdquo; Fred MacMurray: &ldquo;Yeah &ndash; only you&#039;re a little more rotten.&rdquo; &#x2d;&rdquo;Double Indemnity&rdquo; (1944)&#8230;","inLanguage":"en-US","isPartOf":{"@id":"https://truthout.org/#/schema/WebSite"},"breadcrumb":{"@type":"BreadcrumbList","@id":"https://truthout.org/#/schema/BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"item":"https://truthout.org/","name":"Truthout"},{"@type":"ListItem","position":2,"item":"https://truthout.org/articles/","name":"Articles"},{"@type":"ListItem","position":3,"item":"https://truthout.org/category/news-analysis/","name":"News Analysis"},{"@type":"ListItem","position":4,"name":"Goodbye to All That: Reflections of a GOP Operative Who Left the Cult"}]},"potentialAction":{"@type":"ReadAction","target":"https://truthout.org/articles/goodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult/"},"datePublished":"2011-09-03T15:09:39+00:00","dateModified":"2011-09-03T15:09:39+00:00","author":{"@type":"Person","@id":"https://truthout.org/#/schema/Person/4042c149658b2aea29d7346ac3914b6d","name":"Truthout"}}]}</script>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"AnalysisNewsArticle","mainEntityOfPage":{"@type":"WebPage","@id":"https://truthout.org/articles/goodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult/"},"headline":"Goodbye to All That: Reflections of a GOP Operative Who Left the Cult","image":"https://truthout.org/app/uploads/2017/12/Goodbye-to-All-That-Reflections-of-a-GOP-Operative-Who-Left-the-Cult.jpg","datePublished":"2011-09-03T15:09:39+00:00","dateModified":"2011-09-03T15:09:39+00:00","author":[{"@type":"Person","name":"Mike Lofgren","url":"https://truthout.org/authors/mike-lofgren/"}],"publisher":{"@type":"Organization","name":"Truthout","logo":{"@type":"ImageObject","url":"https://truthout.org/app/uploads/2018/01/cropped-Truthout-Logo-60x60.jpg","width":60,"height":60}},"description":"(Photo: Carolyn Tiry / Flickr) Barbara Stanwyck: &ldquo;We&#039;re both rotten!&rdquo; Fred MacMurray: &ldquo;Yeah &ndash; only you&#039;re a little more rotten.&rdquo; &#x2d;&rdquo;Double Indemnity&rdquo; (1944)&#8230;","sourceOrganization":{"@type":"Organization","name":"Truthout"}}</script>
<!-- / The SEO Framework by Sybre Waaijer | 7.12ms meta | 0.24ms boot -->

<script>
window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/16.0.1\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/16.0.1\/svg\/","svgExt":".svg","source":{"concatemoji":"https:\/\/truthout.org\/wp\/wp-includes\/js\/wp-emoji-release.min.js?ver=6.8.2"}};
/*! This file is auto-generated */
!function(s,n){var o,i,e;function c(e){try{var t={supportTests:e,timestamp:(new Date).valueOf()};sessionStorage.setItem(o,JSON.stringify(t))}catch(e){}}function p(e,t,n){e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(t,0,0);var t=new Uint32Array(e.getImageData(0,0,e.canvas.width,e.canvas.height).data),a=(e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(n,0,0),new Uint32Array(e.getImageData(0,0,e.canvas.width,e.canvas.height).data));return t.every(function(e,t){return e===a[t]})}function u(e,t){e.clearRect(0,0,e.canvas.width,e.canvas.height),e.fillText(t,0,0);for(var n=e.getImageData(16,16,1,1),a=0;a<n.data.length;a++)if(0!==n.data[a])return!1;return!0}function f(e,t,n,a){switch(t){case"flag":return n(e,"\ud83c\udff3\ufe0f\u200d\u26a7\ufe0f","\ud83c\udff3\ufe0f\u200b\u26a7\ufe0f")?!1:!n(e,"\ud83c\udde8\ud83c\uddf6","\ud83c\udde8\u200b\ud83c\uddf6")&&!n(e,"\ud83c\udff4\udb40\udc67\udb40\udc62\udb40\udc65\udb40\udc6e\udb40\udc67\udb40\udc7f","\ud83c\udff4\u200b\udb40\udc67\u200b\udb40\udc62\u200b\udb40\udc65\u200b\udb40\udc6e\u200b\udb40\udc67\u200b\udb40\udc7f");case"emoji":return!a(e,"\ud83e\udedf")}return!1}function g(e,t,n,a){var r="undefined"!=typeof WorkerGlobalScope&&self instanceof WorkerGlobalScope?new OffscreenCanvas(300,150):s.createElement("canvas"),o=r.getContext("2d",{willReadFrequently:!0}),i=(o.textBaseline="top",o.font="600 32px Arial",{});return e.forEach(function(e){i[e]=t(o,e,n,a)}),i}function t(e){var t=s.createElement("script");t.src=e,t.defer=!0,s.head.appendChild(t)}"undefined"!=typeof Promise&&(o="wpEmojiSettingsSupports",i=["flag","emoji"],n.supports={everything:!0,everythingExceptFlag:!0},e=new Promise(function(e){s.addEventListener("DOMContentLoaded",e,{once:!0})}),new Promise(function(t){var n=function(){try{var e=JSON.parse(sessionStorage.getItem(o));if("object"==typeof e&&"number"==typeof e.timestamp&&(new Date).valueOf()<e.timestamp+604800&&"object"==typeof e.supportTests)return e.supportTests}catch(e){}return null}();if(!n){if("undefined"!=typeof Worker&&"undefined"!=typeof OffscreenCanvas&&"undefined"!=typeof URL&&URL.createObjectURL&&"undefined"!=typeof Blob)try{var e="postMessage("+g.toString()+"("+[JSON.stringify(i),f.toString(),p.toString(),u.toString()].join(",")+"));",a=new Blob([e],{type:"text/javascript"}),r=new Worker(URL.createObjectURL(a),{name:"wpTestEmojiSupports"});return void(r.onmessage=function(e){c(n=e.data),r.terminate(),t(n)})}catch(e){}c(n=g(i,f,p,u))}t(n)}).then(function(e){for(var t in e)n.supports[t]=e[t],n.supports.everything=n.supports.everything&&n.supports[t],"flag"!==t&&(n.supports.everythingExceptFlag=n.supports.everythingExceptFlag&&n.supports[t]);n.supports.everythingExceptFlag=n.supports.everythingExceptFlag&&!n.supports.flag,n.DOMReady=!1,n.readyCallback=function(){n.DOMReady=!0}}).then(function(){return e}).then(function(){var e;n.supports.everything||(n.readyCallback(),(e=n.source||{}).concatemoji?t(e.concatemoji):e.wpemoji&&e.twemoji&&(t(e.twemoji),t(e.wpemoji)))}))}((window,document),window._wpemojiSettings);
</script>
<!-- truthout.org is managing ads with Advanced Ads 2.0.9 – https://wpadvancedads.com/ --><script id="truth-ready">
			window.advanced_ads_ready=function(e,a){a=a||"complete";var d=function(e){return"interactive"===a?"loading"!==e:"complete"===e};d(document.readyState)?e():document.addEventListener("readystatechange",(function(a){d(a.target.readyState)&&e()}),{once:"interactive"===a})},window.advanced_ads_ready_queue=window.advanced_ads_ready_queue||[];		</script>
		<style id='wp-emoji-styles-inline-css'>

img.wp-smiley, img.emoji {
		display: inline !important;
		border: none !important;
		box-shadow: none !important;
		height: 1em !important;
		width: 1em !important;
		margin: 0 0.07em !important;
		vertical-align: -0.1em !important;
		background: none !important;
		padding: 0 !important;
	}
</style>
<style id='safe-svg-svg-icon-style-inline-css'>
.safe-svg-cover{text-align:center}.safe-svg-cover .safe-svg-inside{display:inline-block;max-width:100%}.safe-svg-cover svg{fill:currentColor;height:100%;max-height:100%;max-width:100%;width:100%}

</style>
<style id='global-styles-inline-css'>
:root{--wp--preset--aspect-ratio--square: 1;--wp--preset--aspect-ratio--4-3: 4/3;--wp--preset--aspect-ratio--3-4: 3/4;--wp--preset--aspect-ratio--3-2: 3/2;--wp--preset--aspect-ratio--2-3: 2/3;--wp--preset--aspect-ratio--16-9: 16/9;--wp--preset--aspect-ratio--9-16: 9/16;--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--color--red: #9C162C;--wp--preset--color--dark: #292219;--wp--preset--color--lightgray: #F8F8F8;--wp--preset--color--tan: #D5D1C9;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);--wp--preset--shadow--outlined: 6px 6px 0px -3px rgba(255, 255, 255, 1), 6px 6px rgba(0, 0, 0, 1);--wp--preset--shadow--crisp: 6px 6px 0px rgba(0, 0, 0, 1);}:where(body) { margin: 0; }.wp-site-blocks > .alignleft { float: left; margin-right: 2em; }.wp-site-blocks > .alignright { float: right; margin-left: 2em; }.wp-site-blocks > .aligncenter { justify-content: center; margin-left: auto; margin-right: auto; }:where(.is-layout-flex){gap: 0.5em;}:where(.is-layout-grid){gap: 0.5em;}.is-layout-flow > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}.is-layout-flow > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}.is-layout-flow > .aligncenter{margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > .alignleft{float: left;margin-inline-start: 0;margin-inline-end: 2em;}.is-layout-constrained > .alignright{float: right;margin-inline-start: 2em;margin-inline-end: 0;}.is-layout-constrained > .aligncenter{margin-left: auto !important;margin-right: auto !important;}.is-layout-constrained > :where(:not(.alignleft):not(.alignright):not(.alignfull)){margin-left: auto !important;margin-right: auto !important;}body .is-layout-flex{display: flex;}.is-layout-flex{flex-wrap: wrap;align-items: center;}.is-layout-flex > :is(*, div){margin: 0;}body .is-layout-grid{display: grid;}.is-layout-grid > :is(*, div){margin: 0;}body{padding-top: 0px;padding-right: 0px;padding-bottom: 0px;padding-left: 0px;}a:where(:not(.wp-element-button)){text-decoration: underline;}:root :where(.wp-element-button, .wp-block-button__link){background-color: #32373c;border-width: 0;color: #fff;font-family: inherit;font-size: inherit;line-height: inherit;padding: calc(0.667em + 2px) calc(1.333em + 2px);text-decoration: none;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-red-color{color: var(--wp--preset--color--red) !important;}.has-dark-color{color: var(--wp--preset--color--dark) !important;}.has-lightgray-color{color: var(--wp--preset--color--lightgray) !important;}.has-tan-color{color: var(--wp--preset--color--tan) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-red-background-color{background-color: var(--wp--preset--color--red) !important;}.has-dark-background-color{background-color: var(--wp--preset--color--dark) !important;}.has-lightgray-background-color{background-color: var(--wp--preset--color--lightgray) !important;}.has-tan-background-color{background-color: var(--wp--preset--color--tan) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-red-border-color{border-color: var(--wp--preset--color--red) !important;}.has-dark-border-color{border-color: var(--wp--preset--color--dark) !important;}.has-lightgray-border-color{border-color: var(--wp--preset--color--lightgray) !important;}.has-tan-border-color{border-color: var(--wp--preset--color--tan) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
:where(.wp-block-post-template.is-layout-flex){gap: 1.25em;}:where(.wp-block-post-template.is-layout-grid){gap: 1.25em;}
:where(.wp-block-columns.is-layout-flex){gap: 2em;}:where(.wp-block-columns.is-layout-grid){gap: 2em;}
:root :where(.wp-block-pullquote){font-size: 1.5em;line-height: 1.6;}
</style>
<link rel='stylesheet' id='truthout/app.css-css' href='https://truthout.org/app/themes/truthout5/public/styles/app.css?id=20331f90f0c5845458516f4996161966' media='all' />
<script src="https://truthout.org/wp/wp-includes/js/jquery/jquery.min.js?ver=3.7.1" id="jquery-core-js"></script>
<script src="https://truthout.org/wp/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.4.1" id="jquery-migrate-js"></script>
<script id="advanced-ads-advanced-js-js-extra">
var advads_options = {"blog_id":"1","privacy":{"enabled":false,"state":"not_needed"}};
</script>
<script src="https://truthout.org/app/plugins/advanced-ads/public/assets/js/advanced.min.js?ver=2.0.9" id="advanced-ads-advanced-js-js"></script>
<link rel="https://api.w.org/" href="https://truthout.org/wp-json/" /><link rel="alternate" title="JSON" type="application/json" href="https://truthout.org/wp-json/wp/v2/to4_article_post/218684" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://truthout.org/wp/xmlrpc.php?rsd" />
<link rel="alternate" title="oEmbed (JSON)" type="application/json+oembed" href="https://truthout.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ftruthout.org%2Farticles%2Fgoodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult%2F" />
<link rel="alternate" title="oEmbed (XML)" type="text/xml+oembed" href="https://truthout.org/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ftruthout.org%2Farticles%2Fgoodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult%2F&#038;format=xml" />
<script>advads_items = { conditions: {}, display_callbacks: {}, display_effect_callbacks: {}, hide_callbacks: {}, backgrounds: {}, effect_durations: {}, close_functions: {}, showed: [] };</script><style type="text/css" id="truth-layer-custom-css"></style>
<!-- meta author for semrush and other trackers -->
<meta name="author" content="Mike Lofgren">
<!-- Bing Webmaster Tools -->
<meta name="msvalidate.01" content="A8B609490531D97CB12F2800611EEAC3" />
<!-- favicon management -->
<link rel="apple-touch-icon" sizes="180x180" href="https://truthout.org/webicons/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="https://truthout.org/webicons/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="https://truthout.org/webicons/favicon-16x16.png">
<link rel="manifest" href="https://truthout.org/webicons/site.webmanifest">
<link rel="mask-icon" href="https://truthout.org/webicons/safari-pinned-tab.svg" color="#000000">
<link rel="shortcut icon" href="https://truthout.org/webicons/favicon.ico">
<meta name="apple-mobile-web-app-title" content="Truthout">
<meta name="application-name" content="Truthout">
<meta name="msapplication-TileColor" content="#c42b35">
<meta name="msapplication-config" content="https://truthout.org/webicons/browserconfig.xml">
<meta name="theme-color" content="#ffffff">

<link rel="preconnect" href="https://use.typekit.net" crossorigin />
    <link rel="preconnect" href="https://p.typekit.net" crossorigin />
    <link rel="preload" as="style" href="https://use.typekit.net/tcf1vwe.css" />
    <link rel="stylesheet" href="https://use.typekit.net/tcf1vwe.css" media="print" onload="this.media='all'" />

<noscript>
        <link rel="stylesheet" href="https://use.typekit.net/tcf1vwe.css" />
    </noscript>

<!-- Mailchimp -->
        <script id="mcjs">!function(c,h,i,m,p){m=c.createElement(h),p=c.getElementsByTagName(h)[0],m.async=1,m.src=i,p.parentNode.insertBefore(m,p)}(document,"script","https://chimpstatic.com/mcjs-connected/js/users/913e3fb0c16829e59f7694d2a/4726dae6779b3469917d97674.js");</script>
        <!-- End Mailchimp -->

              <script async src="https://cdn.flipboard.com/web/buttons/js/flbuttons.min.js"></script>

<!-- Fundraise Up -->
        <script>(function(w,d,s,n,a){if(!w[n]){var l='call,catch,on,once,set,then,track'
        .split(','),i,o=function(n){return'function'==typeof n?o.l.push([arguments])&&o
        :function(){return o.l.push([n,arguments])&&o}},t=d.getElementsByTagName(s)[0],
        j=d.createElement(s);j.async=!0;j.src='https://cdn.fundraiseup.com/widget/'+a;
        t.parentNode.insertBefore(j,t);o.s=Date.now();o.v=4;o.h=w.location.href;o.l=[];
        for(i=0;i<7;i++)o[l[i]]=o(l[i]);w[n]=o}
        })(window,document,'script','FundraiseUp','ASWCKERB');</script>
        <!-- End Fundraise Up -->
      		<script type="text/javascript">
			var advadsCfpQueue = [];
			var advadsCfpAd = function( adID ) {
				if ( 'undefined' === typeof advadsProCfp ) {
					advadsCfpQueue.push( adID )
				} else {
					advadsProCfp.addElement( adID )
				}
			}
		</script>

<link rel='alternate' type='application/rss+xml' title='RSS 2.0' href='https://truthout.org/articles/goodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult/feed/?withoutcomments=1' />

<link rel="icon" href="https://truthout.org/app/uploads/2018/03/cropped-Truthout-T-logo-sq-1200x1200-e1521532408148-60x60.png" sizes="32x32" />
<link rel="icon" href="https://truthout.org/app/uploads/2018/03/cropped-Truthout-T-logo-sq-1200x1200-e1521532408148-200x200.png" sizes="192x192" />
<link rel="apple-touch-icon" href="https://truthout.org/app/uploads/2018/03/cropped-Truthout-T-logo-sq-1200x1200-e1521532408148-200x200.png" />
<meta name="msapplication-TileImage" content="https://truthout.org/app/uploads/2018/03/cropped-Truthout-T-logo-sq-1200x1200-e1521532408148-400x400.png" />
  </head>

<body class="wp-singular single postid-218684 wp-theme-truthout5 goodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult to3-item ar ar--d ar--dr--p ar--d--v ar--c aa-prefix-truth-">

    <div id="app">
      <a class="visually-hidden-focusable" href="#main">
    Skip to content
  </a>

<a class="visually-hidden-focusable" href="#footer">
    Skip to footer
  </a>

<header class="banner banner--visible bg-lightgray">
  <div class="container-fluid">
    <div class="banner__con d-grid gap-0 justify-content-between align-items-center py-2 pt-md-4 pb-md-1">
      <a class="brand order-1 d-flex justify-content-center ms-4 ms-md-0" href="https://truthout.org/">
        <span class="brand__logo mb-2">
          <svg fill="none" xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 138.2 29"><title>Truthout Logo</title><path d="M94.1,13.2c-2,0-3.9,0.8-5.1,1.8c-1.5,1.2-3,3.2-3,6.3c0,4.3,3.8,7.7,8.2,7.7c1.5,0,3.5-0.6,4.8-1.6c1.3-1,3.2-3.3,3.2-6.4 C102.2,16.6,98.8,13.2,94.1,13.2z M93.5,13.9c3.5,0,5.4,3.7,5.4,7.8c0,3-1,5-1.6,5.5c-0.6,0.6-1.5,1-2.5,1c-1.2,0-2.6-0.7-3.7-2.2 c-1.3-1.7-1.6-4-1.6-5.8C89.4,16.2,91.5,13.9,93.5,13.9z" fill="currentColor"></path> <path d="M113.1,28.8c0.8,0,1.7-0.2,2.5-0.6c0.8-0.3,2-1.2,2.9-2c0.1-0.1,0.1,0.1,0.1,0.2c0,0.3,0,1.2,0,1.7c0,0.4,0,0.6,0.1,0.7 s0.2,0.2,0.5,0c1.2-0.6,4-1.1,4.5-1.1c0.4-0.1,0.8-0.2,0.8-0.4c0-0.2-0.2-0.5-0.5-0.5c-0.3,0-1.3,0.2-1.7,0.3c-0.3,0-0.4,0-0.5-0.4 c-0.1-0.5-0.1-1.1-0.1-2.2c0-4.5,0.1-9,0.3-10.8c0-0.3,0-0.5-0.2-0.5c-0.5,0-1.3,0.3-3,0.3c-0.7,0-1.3,0-1.9,0 c-0.3,0-0.6,0.1-0.6,0.3c0,0.1,0.2,0.3,0.7,0.4c1.3,0.2,1.7,0.5,1.8,1.9c0,1.1,0.1,3.2,0.1,3.8c0,1.4,0,3.1-0.1,4.3 c0,0.9-0.3,1.4-0.7,1.8c-1,0.9-1.9,1.2-3.2,1.2c-0.9,0-1.8-0.3-2.3-1c-0.3-0.3-0.6-0.9-0.6-2.7c0-2,0-7.6,0.1-9.9 c0-0.2-0.1-0.5-0.2-0.5c-0.6,0.2-2.3,0.5-3.9,0.5c-0.5,0-0.7,0.1-0.7,0.2c0,0.1,0.1,0.2,0.5,0.5c0.5,0.3,0.9,0.6,0.9,1.4 c0.1,0.7,0.1,7.7,0.1,9c0,0.9,0.2,1.9,0.8,2.6C110.4,28.5,111.5,28.8,113.1,28.8z" fill="currentColor"></path> <path d="M133.8,28.8c1.2,0,2.5-0.4,3.5-1.1c0.6-0.5,0.9-0.9,0.9-1.1c0-0.2-0.1-0.2-0.5,0c-0.4,0.2-1.1,0.6-2.2,0.6 c-1,0-1.8-0.3-2.5-1.1c-0.3-0.4-0.4-0.9-0.5-2.1c0-1.2,0-7.8,0-8.5c0-0.2,0.1-0.4,0.6-0.4c1.1,0,3,0,4.4,0c0.2,0,0.5-0.2,0.5-1 c0-0.3-0.3-0.6-0.3-0.6c-0.8,0-4.1,0.1-4.9,0.1c-0.2,0-0.3-0.2-0.3-0.4c0-0.5,0-1.8,0.1-2.1c0-0.2-0.3-0.3-0.7,0.2 c-1.1,1.2-2.6,2.4-3.6,2.8c-0.5,0.2-0.6,0.4-0.6,0.5c0,0.2,0.2,0.3,0.5,0.4c0.3,0.1,0.8,0.2,0.9,0.3c0.2,0.1,0.3,0.3,0.3,0.8v8.5 c0,1,0.1,1.9,0.5,2.4C130.7,28.3,132,28.8,133.8,28.8z" fill="currentColor"></path> <path d="M6.1,28.8c1.2,0,2.5-0.4,3.5-1.1c0.6-0.5,0.9-0.9,0.9-1.1c0-0.2-0.1-0.2-0.5,0c-0.4,0.2-1.1,0.6-2.2,0.6 c-1,0-1.9-0.3-2.5-1.1C5,25.8,5,25.3,4.9,24.1c0-1.2,0-7.8,0-8.6c0-0.2,0.1-0.4,0.6-0.4c1.1,0,3,0,4.4,0c0.2,0,0.5-0.2,0.5-1 c0-0.3-0.3-0.6-0.3-0.6c-0.8,0-4.1,0.1-4.9,0.1c-0.2,0-0.3-0.2-0.3-0.4c0-0.5,0-1.8,0.1-2.1c0-0.2-0.3-0.3-0.7,0.2 c-1.1,1.2-2.6,2.4-3.6,2.8C0.1,14.3,0,14.5,0,14.5c0,0.2,0.2,0.3,0.6,0.4c0.3,0.1,0.8,0.2,0.9,0.3c0.2,0.1,0.3,0.3,0.3,0.8v8.6 c0,1,0.1,1.9,0.5,2.4C3,28.3,4.3,28.8,6.1,28.8z" fill="currentColor"></path> <path d="M21.9,15.5c0.5,0,1,0.2,1.5,0.5c0.5,0.3,0.7,0.3,0.8,0.3c0.2,0,0.3,0,0.8-0.4c0.5-0.5,1-1.2,1-1.5c0-0.2-0.1-0.4-0.4-0.7 c-0.4-0.3-0.9-0.5-1.4-0.5c-1.7,0-3.3,1.5-4.5,3c-0.1,0.1-0.2,0-0.2-0.1c0-0.7,0.1-2.2,0.1-2.7c0-0.3-0.1-0.5-0.2-0.5 c-0.1,0-0.3,0-0.6,0.2c-0.7,0.4-2,0.8-3,1.1c-0.3,0.1-0.6,0.3-0.6,0.4c0,0.1,0,0.2,0.3,0.4c0.8,0.7,1.1,0.8,1.1,1.1 c0,0.6,0,1.9,0,4.5c0,2.7,0,5-0.1,5.7c-0.1,1.2-0.5,1.5-1.5,1.7c-0.4,0.1-0.6,0.3-0.6,0.5c0,0.2,0.2,0.2,0.7,0.2 c0.7,0,1.1-0.2,2.8-0.2c1.9,0,3.1,0.2,4,0.2c0.6,0,1-0.1,1-0.3c0-0.2-0.2-0.3-0.8-0.4c-1.6-0.1-2.1-0.4-2.2-1.7 c-0.1-0.9-0.2-2.9-0.2-5.9c0-0.8,0-2.1,0.1-2.7c0-0.5,0.2-0.9,0.6-1.3C20.6,15.8,21.3,15.5,21.9,15.5z" fill="currentColor"></path> <path d="M35.8,28.8c0.8,0,1.7-0.2,2.5-0.6c0.8-0.3,2-1.2,2.9-2c0.1-0.1,0.1,0.1,0.1,0.2c0,0.3,0,1.2,0,1.7c0,0.4,0,0.6,0.1,0.7 c0.1,0.1,0.2,0.2,0.5,0c1.2-0.6,4-1.1,4.5-1.1c0.4-0.1,0.8-0.2,0.8-0.4c0-0.2-0.2-0.5-0.5-0.5c-0.3,0-1.3,0.2-1.7,0.3 c-0.3,0-0.4,0-0.5-0.4c-0.1-0.5-0.1-1.1-0.1-2.2c0-4.5,0.1-9,0.3-10.8c0-0.3,0-0.5-0.2-0.5c-0.5,0-1.3,0.3-3,0.3c-0.7,0-1.4,0-1.9,0 c-0.3,0-0.6,0.1-0.6,0.3c0,0.1,0.2,0.3,0.7,0.4c1.4,0.2,1.7,0.5,1.8,1.9c0,1.1,0.1,3.2,0.1,3.8c0,1.4,0,3.1-0.1,4.3 c0,0.9-0.3,1.4-0.7,1.8c-1,0.9-1.9,1.2-3.3,1.2c-0.9,0-1.8-0.3-2.3-1c-0.3-0.3-0.6-1-0.6-2.7c0-2,0-7.6,0.1-10 c0-0.2-0.1-0.5-0.2-0.5c-0.6,0.2-2.3,0.5-3.9,0.5c-0.5,0-0.7,0.1-0.7,0.2s0.1,0.2,0.5,0.5c0.5,0.3,0.9,0.6,0.9,1.4 c0.1,0.7,0.1,7.7,0.1,9.1c0,0.9,0.2,1.9,0.8,2.6C33.1,28.5,34.2,28.8,35.8,28.8z" fill="currentColor"></path> <path d="M56.6,28.8c1.2,0,2.5-0.4,3.5-1.1c0.6-0.5,0.9-0.9,0.9-1.1c0-0.2-0.1-0.2-0.5,0c-0.4,0.2-1.1,0.6-2.2,0.6 c-1,0-1.9-0.3-2.5-1.1c-0.3-0.4-0.4-0.9-0.5-2.1c0-1.2,0-7.8,0-8.6c0-0.2,0.1-0.4,0.6-0.4c1.1,0,3,0,4.4,0c0.2,0,0.5-0.2,0.5-1 c0-0.3-0.3-0.6-0.3-0.6c-0.8,0-4.1,0.1-4.9,0.1c-0.2,0-0.3-0.2-0.3-0.4c0-0.5,0-1.8,0.1-2.1c0-0.2-0.3-0.3-0.7,0.2 c-1.1,1.2-2.6,2.4-3.6,2.8c-0.5,0.2-0.6,0.4-0.6,0.5c0,0.2,0.2,0.3,0.5,0.4c0.3,0.1,0.8,0.2,0.9,0.3c0.2,0.1,0.3,0.3,0.3,0.8v8.6 c0,1,0.1,1.9,0.5,2.4C53.5,28.3,54.9,28.8,56.6,28.8z" fill="currentColor"></path> <path d="M73.3,14.7c1.4,0,2.3,0.5,2.9,1.5c0.5,0.8,0.6,2.1,0.6,3.1c0,4.1-0.1,6-0.2,6.9c-0.2,1.2-0.3,1.6-1.4,1.8 c-0.4,0.1-0.6,0.2-0.6,0.4c0,0.1,0.2,0.2,0.7,0.2c1.1,0,1.3-0.2,3-0.2c1.2,0,2,0.2,3.1,0.2c0.4,0,0.7-0.1,0.7-0.3 c0-0.2-0.2-0.3-0.7-0.4c-1.2-0.2-1.4-0.5-1.4-1.3c0-1.7,0-4.3,0-7.3c0-2.5-0.5-3.8-1-4.4c-1-1.3-2.5-1.8-3.9-1.8 c-1.1,0-2.1,0.3-2.8,0.7c-0.8,0.4-1.9,1.2-2.5,1.7c-0.1,0-0.2,0-0.2-0.2c0-0.7,0.2-13.5,0.2-14.5c0-0.6-0.1-0.8-0.3-0.8 c-0.1,0-0.2,0-0.4,0.2c-1,0.5-2.1,0.7-3.4,1.1c-0.5,0.1-0.7,0.2-0.7,0.4s0.1,0.2,0.3,0.3c0.9,0.5,1.2,0.6,1.3,1.9 c0.1,1.5,0,4.2,0,10.4c0,6.4,0,10.2-0.1,11.8c-0.1,1.4-0.3,1.7-1.5,1.9c-0.5,0.1-0.7,0.2-0.7,0.4c0,0.2,0.2,0.2,0.7,0.2 c0.9,0,1.5-0.2,2.9-0.2c1.1,0,2.3,0.2,3.5,0.2c0.4,0,0.7-0.1,0.7-0.2c0-0.2-0.3-0.3-0.9-0.4c-0.9-0.2-1.2-0.7-1.4-1.4 c-0.1-0.9-0.3-3.4-0.2-9.1c0-0.8,0.2-1.2,0.4-1.4C70.5,15.4,71.7,14.7,73.3,14.7z" fill="currentColor"></path> </svg>
        </span>
        <span class="brand__ti visually-hidden">Truthout</span>
      </a>

<nav id="topLeftNav" class="nav-top-left d-none d-md-block order-0" aria-label="Top left navigation">
  <ul class="nav text-uppercase font-sans--con">
          <li class="nav-item text-center  current_page_parent ">
        <a id="latestLink" class="nav-link" href="https://truthout.org/latest/">
          Latest
        </a>

</li>
          <li class="nav-item text-center  ">
        <a id="aboutLink" class="nav-link" href="https://truthout.org/about/">
          About
        </a>

</li>
      </ul>
</nav>

<nav id="topRightNav" class="nav-top-right d-none d-md-flex justify-content-end order-2" aria-label="Top right navigation">
  <ul class="nav text-uppercase font-sans--con">
          <li class="nav-item text-center  ">
        <a id="donateLink" class="nav-link" href="https://support.truthout.org/-/XXQLBDSX">
          Donate
        </a>

</li>
      </ul>
</nav>

<button id="menuToggle" class="navbar-toggler d-flex order-last justify-content-end mt-1 mt-md-0 px-0" type="button" data-bs-toggle="offcanvas" data-bs-target="#primaryMenu" aria-controls="primaryMenu" aria-label="Toggle main menu">
        <span class="navbar-toggler-icon d-flex align-middle me-md-1"><i class="fal fa-bars my-auto"></i></span>
      </button>

</div>
  </div>
</header>

<aside id="secondaryMenu" class="trending d-none d-md-block" aria-label="Trending news navigation">
  <section class="menu--trending-top d-flex justify-content-center align-items-center">
    <header class="menu--trending-top__hd">
      <h4 id="trendingTitle" class="visually-hidden">Trending<span class="separator">:</span></h4>
      <svg class="true" width="18" height="12" viewBox="0 0 18 12" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<path fill-rule="evenodd" clip-rule="evenodd" d="M15.2774 0.000469522C15.5014 -0.00884774 15.7079 0.121216 15.7962 0.327284L17.9562 5.36724C18.0737 5.64136 17.9467 5.95881 17.6726 6.07629C17.3985 6.19377 17.081 6.06678 16.9635 5.79267L15.363 2.05817L12.2122 11.5107C12.1415 11.7229 11.9472 11.8695 11.7238 11.8794C11.5003 11.8892 11.2939 11.7603 11.2047 11.5552L8.09841 4.41073L6.0747 9.03636C5.99838 9.21079 5.83585 9.33214 5.64693 9.35575C5.45801 9.37936 5.27062 9.30173 5.15373 9.15145L3.06 6.45951L0.966266 9.15145C0.78317 9.38686 0.443904 9.42927 0.208495 9.24617C-0.0269144 9.06307 -0.0693226 8.72381 0.113774 8.4884L2.63375 5.24843C2.73606 5.11689 2.89336 5.03996 3.06 5.03996C3.22663 5.03996 3.38394 5.11689 3.48624 5.24843L5.44903 7.772L7.60523 2.84353C7.69131 2.64678 7.88581 2.51974 8.10057 2.51998C8.31533 2.52023 8.50953 2.64771 8.59516 2.84467L11.6333 9.83227L14.7876 0.369237C14.8585 0.156546 15.0534 0.00978674 15.2774 0.000469522Z" fill="currentColor" fill-opacity="0.65"/>
</svg>    </header>

<ul class="nav text-uppercase font-sans">
              <li class="nav-item">
          <a id="trending1" href="https://truthout.org/topics/donald-trump/" title="Donald Trump" class="topic donald-trump nav-link">
          Donald Trump
         </a>
       </li>
              <li class="nav-item">
          <a id="trending2" href="https://truthout.org/topics/vaccines/" title="Vaccines" class="topic vaccines nav-link">
          Vaccines
         </a>
       </li>
              <li class="nav-item">
          <a id="trending3" href="https://truthout.org/topics/charlie-kirk/" title="Charlie Kirk" class="topic charlie-kirk nav-link">
          Charlie Kirk
         </a>
       </li>
              <li class="nav-item">
          <a id="trending4" href="https://truthout.org/topics/palestine/" title="Palestine" class="topic palestine nav-link">
          Palestine
         </a>
       </li>
              <li class="nav-item">
          <a id="trending5" href="https://truthout.org/topics/immigration/" title="Immigration" class="topic immigration nav-link">
          Immigration
         </a>
       </li>
          </ul>
  </section>
</aside>

<div class="offcanvas offcanvas-end w-100 pt-2 pb-5" tabindex="-1" id="primaryMenu" aria-labelledby="primaryMenuLabel">

  <div class="offcanvas-header d-grid gap-0 justify-content-between align-items-center pt-2 py-md-3">
    <a class="brand d-none d-md-flex justify-content-center order-1 mb-2 mx-auto ps-0" href="https://truthout.org/">
      <span class="brand__logo">
        <svg fill="none" xmlns="http://www.w3.org/2000/svg" version="1.1" viewBox="0 0 138.2 29"><title>Truthout Logo</title><path d="M94.1,13.2c-2,0-3.9,0.8-5.1,1.8c-1.5,1.2-3,3.2-3,6.3c0,4.3,3.8,7.7,8.2,7.7c1.5,0,3.5-0.6,4.8-1.6c1.3-1,3.2-3.3,3.2-6.4 C102.2,16.6,98.8,13.2,94.1,13.2z M93.5,13.9c3.5,0,5.4,3.7,5.4,7.8c0,3-1,5-1.6,5.5c-0.6,0.6-1.5,1-2.5,1c-1.2,0-2.6-0.7-3.7-2.2 c-1.3-1.7-1.6-4-1.6-5.8C89.4,16.2,91.5,13.9,93.5,13.9z" fill="currentColor"></path> <path d="M113.1,28.8c0.8,0,1.7-0.2,2.5-0.6c0.8-0.3,2-1.2,2.9-2c0.1-0.1,0.1,0.1,0.1,0.2c0,0.3,0,1.2,0,1.7c0,0.4,0,0.6,0.1,0.7 s0.2,0.2,0.5,0c1.2-0.6,4-1.1,4.5-1.1c0.4-0.1,0.8-0.2,0.8-0.4c0-0.2-0.2-0.5-0.5-0.5c-0.3,0-1.3,0.2-1.7,0.3c-0.3,0-0.4,0-0.5-0.4 c-0.1-0.5-0.1-1.1-0.1-2.2c0-4.5,0.1-9,0.3-10.8c0-0.3,0-0.5-0.2-0.5c-0.5,0-1.3,0.3-3,0.3c-0.7,0-1.3,0-1.9,0 c-0.3,0-0.6,0.1-0.6,0.3c0,0.1,0.2,0.3,0.7,0.4c1.3,0.2,1.7,0.5,1.8,1.9c0,1.1,0.1,3.2,0.1,3.8c0,1.4,0,3.1-0.1,4.3 c0,0.9-0.3,1.4-0.7,1.8c-1,0.9-1.9,1.2-3.2,1.2c-0.9,0-1.8-0.3-2.3-1c-0.3-0.3-0.6-0.9-0.6-2.7c0-2,0-7.6,0.1-9.9 c0-0.2-0.1-0.5-0.2-0.5c-0.6,0.2-2.3,0.5-3.9,0.5c-0.5,0-0.7,0.1-0.7,0.2c0,0.1,0.1,0.2,0.5,0.5c0.5,0.3,0.9,0.6,0.9,1.4 c0.1,0.7,0.1,7.7,0.1,9c0,0.9,0.2,1.9,0.8,2.6C110.4,28.5,111.5,28.8,113.1,28.8z" fill="currentColor"></path> <path d="M133.8,28.8c1.2,0,2.5-0.4,3.5-1.1c0.6-0.5,0.9-0.9,0.9-1.1c0-0.2-0.1-0.2-0.5,0c-0.4,0.2-1.1,0.6-2.2,0.6 c-1,0-1.8-0.3-2.5-1.1c-0.3-0.4-0.4-0.9-0.5-2.1c0-1.2,0-7.8,0-8.5c0-0.2,0.1-0.4,0.6-0.4c1.1,0,3,0,4.4,0c0.2,0,0.5-0.2,0.5-1 c0-0.3-0.3-0.6-0.3-0.6c-0.8,0-4.1,0.1-4.9,0.1c-0.2,0-0.3-0.2-0.3-0.4c0-0.5,0-1.8,0.1-2.1c0-0.2-0.3-0.3-0.7,0.2 c-1.1,1.2-2.6,2.4-3.6,2.8c-0.5,0.2-0.6,0.4-0.6,0.5c0,0.2,0.2,0.3,0.5,0.4c0.3,0.1,0.8,0.2,0.9,0.3c0.2,0.1,0.3,0.3,0.3,0.8v8.5 c0,1,0.1,1.9,0.5,2.4C130.7,28.3,132,28.8,133.8,28.8z" fill="currentColor"></path> <path d="M6.1,28.8c1.2,0,2.5-0.4,3.5-1.1c0.6-0.5,0.9-0.9,0.9-1.1c0-0.2-0.1-0.2-0.5,0c-0.4,0.2-1.1,0.6-2.2,0.6 c-1,0-1.9-0.3-2.5-1.1C5,25.8,5,25.3,4.9,24.1c0-1.2,0-7.8,0-8.6c0-0.2,0.1-0.4,0.6-0.4c1.1,0,3,0,4.4,0c0.2,0,0.5-0.2,0.5-1 c0-0.3-0.3-0.6-0.3-0.6c-0.8,0-4.1,0.1-4.9,0.1c-0.2,0-0.3-0.2-0.3-0.4c0-0.5,0-1.8,0.1-2.1c0-0.2-0.3-0.3-0.7,0.2 c-1.1,1.2-2.6,2.4-3.6,2.8C0.1,14.3,0,14.5,0,14.5c0,0.2,0.2,0.3,0.6,0.4c0.3,0.1,0.8,0.2,0.9,0.3c0.2,0.1,0.3,0.3,0.3,0.8v8.6 c0,1,0.1,1.9,0.5,2.4C3,28.3,4.3,28.8,6.1,28.8z" fill="currentColor"></path> <path d="M21.9,15.5c0.5,0,1,0.2,1.5,0.5c0.5,0.3,0.7,0.3,0.8,0.3c0.2,0,0.3,0,0.8-0.4c0.5-0.5,1-1.2,1-1.5c0-0.2-0.1-0.4-0.4-0.7 c-0.4-0.3-0.9-0.5-1.4-0.5c-1.7,0-3.3,1.5-4.5,3c-0.1,0.1-0.2,0-0.2-0.1c0-0.7,0.1-2.2,0.1-2.7c0-0.3-0.1-0.5-0.2-0.5 c-0.1,0-0.3,0-0.6,0.2c-0.7,0.4-2,0.8-3,1.1c-0.3,0.1-0.6,0.3-0.6,0.4c0,0.1,0,0.2,0.3,0.4c0.8,0.7,1.1,0.8,1.1,1.1 c0,0.6,0,1.9,0,4.5c0,2.7,0,5-0.1,5.7c-0.1,1.2-0.5,1.5-1.5,1.7c-0.4,0.1-0.6,0.3-0.6,0.5c0,0.2,0.2,0.2,0.7,0.2 c0.7,0,1.1-0.2,2.8-0.2c1.9,0,3.1,0.2,4,0.2c0.6,0,1-0.1,1-0.3c0-0.2-0.2-0.3-0.8-0.4c-1.6-0.1-2.1-0.4-2.2-1.7 c-0.1-0.9-0.2-2.9-0.2-5.9c0-0.8,0-2.1,0.1-2.7c0-0.5,0.2-0.9,0.6-1.3C20.6,15.8,21.3,15.5,21.9,15.5z" fill="currentColor"></path> <path d="M35.8,28.8c0.8,0,1.7-0.2,2.5-0.6c0.8-0.3,2-1.2,2.9-2c0.1-0.1,0.1,0.1,0.1,0.2c0,0.3,0,1.2,0,1.7c0,0.4,0,0.6,0.1,0.7 c0.1,0.1,0.2,0.2,0.5,0c1.2-0.6,4-1.1,4.5-1.1c0.4-0.1,0.8-0.2,0.8-0.4c0-0.2-0.2-0.5-0.5-0.5c-0.3,0-1.3,0.2-1.7,0.3 c-0.3,0-0.4,0-0.5-0.4c-0.1-0.5-0.1-1.1-0.1-2.2c0-4.5,0.1-9,0.3-10.8c0-0.3,0-0.5-0.2-0.5c-0.5,0-1.3,0.3-3,0.3c-0.7,0-1.4,0-1.9,0 c-0.3,0-0.6,0.1-0.6,0.3c0,0.1,0.2,0.3,0.7,0.4c1.4,0.2,1.7,0.5,1.8,1.9c0,1.1,0.1,3.2,0.1,3.8c0,1.4,0,3.1-0.1,4.3 c0,0.9-0.3,1.4-0.7,1.8c-1,0.9-1.9,1.2-3.3,1.2c-0.9,0-1.8-0.3-2.3-1c-0.3-0.3-0.6-1-0.6-2.7c0-2,0-7.6,0.1-10 c0-0.2-0.1-0.5-0.2-0.5c-0.6,0.2-2.3,0.5-3.9,0.5c-0.5,0-0.7,0.1-0.7,0.2s0.1,0.2,0.5,0.5c0.5,0.3,0.9,0.6,0.9,1.4 c0.1,0.7,0.1,7.7,0.1,9.1c0,0.9,0.2,1.9,0.8,2.6C33.1,28.5,34.2,28.8,35.8,28.8z" fill="currentColor"></path> <path d="M56.6,28.8c1.2,0,2.5-0.4,3.5-1.1c0.6-0.5,0.9-0.9,0.9-1.1c0-0.2-0.1-0.2-0.5,0c-0.4,0.2-1.1,0.6-2.2,0.6 c-1,0-1.9-0.3-2.5-1.1c-0.3-0.4-0.4-0.9-0.5-2.1c0-1.2,0-7.8,0-8.6c0-0.2,0.1-0.4,0.6-0.4c1.1,0,3,0,4.4,0c0.2,0,0.5-0.2,0.5-1 c0-0.3-0.3-0.6-0.3-0.6c-0.8,0-4.1,0.1-4.9,0.1c-0.2,0-0.3-0.2-0.3-0.4c0-0.5,0-1.8,0.1-2.1c0-0.2-0.3-0.3-0.7,0.2 c-1.1,1.2-2.6,2.4-3.6,2.8c-0.5,0.2-0.6,0.4-0.6,0.5c0,0.2,0.2,0.3,0.5,0.4c0.3,0.1,0.8,0.2,0.9,0.3c0.2,0.1,0.3,0.3,0.3,0.8v8.6 c0,1,0.1,1.9,0.5,2.4C53.5,28.3,54.9,28.8,56.6,28.8z" fill="currentColor"></path> <path d="M73.3,14.7c1.4,0,2.3,0.5,2.9,1.5c0.5,0.8,0.6,2.1,0.6,3.1c0,4.1-0.1,6-0.2,6.9c-0.2,1.2-0.3,1.6-1.4,1.8 c-0.4,0.1-0.6,0.2-0.6,0.4c0,0.1,0.2,0.2,0.7,0.2c1.1,0,1.3-0.2,3-0.2c1.2,0,2,0.2,3.1,0.2c0.4,0,0.7-0.1,0.7-0.3 c0-0.2-0.2-0.3-0.7-0.4c-1.2-0.2-1.4-0.5-1.4-1.3c0-1.7,0-4.3,0-7.3c0-2.5-0.5-3.8-1-4.4c-1-1.3-2.5-1.8-3.9-1.8 c-1.1,0-2.1,0.3-2.8,0.7c-0.8,0.4-1.9,1.2-2.5,1.7c-0.1,0-0.2,0-0.2-0.2c0-0.7,0.2-13.5,0.2-14.5c0-0.6-0.1-0.8-0.3-0.8 c-0.1,0-0.2,0-0.4,0.2c-1,0.5-2.1,0.7-3.4,1.1c-0.5,0.1-0.7,0.2-0.7,0.4s0.1,0.2,0.3,0.3c0.9,0.5,1.2,0.6,1.3,1.9 c0.1,1.5,0,4.2,0,10.4c0,6.4,0,10.2-0.1,11.8c-0.1,1.4-0.3,1.7-1.5,1.9c-0.5,0.1-0.7,0.2-0.7,0.4c0,0.2,0.2,0.2,0.7,0.2 c0.9,0,1.5-0.2,2.9-0.2c1.1,0,2.3,0.2,3.5,0.2c0.4,0,0.7-0.1,0.7-0.2c0-0.2-0.3-0.3-0.9-0.4c-0.9-0.2-1.2-0.7-1.4-1.4 c-0.1-0.9-0.3-3.4-0.2-9.1c0-0.8,0.2-1.2,0.4-1.4C70.5,15.4,71.7,14.7,73.3,14.7z" fill="currentColor"></path> </svg>
      </span>
      <span class="brand__ti visually-hidden">Truthout</span>
    </a>

<nav id="offCanvasLeftTop" class="nav-top-left me-auto order-0" aria-label="Offcanvas top left navigation">
  <ul class="nav d-none d-md-flex flex-row text-uppercase font-sans--con">
          <li class="nav-item text-center mb-0  current_page_parent ">
        <a id="latestLink" class="nav-link" href="https://truthout.org/latest/">
          Latest
        </a>

</li>
          <li class="nav-item text-center mb-0  ">
        <a id="aboutLink" class="nav-link" href="https://truthout.org/about/">
          About
        </a>

</li>
      </ul>
</nav>

<nav id="offCanvasRightTop" class="nav-top-right ms-auto order-2" aria-label="Offcanvas top right navigation">
  <ul class="nav d-none d-md-flex flex-row text-uppercase font-sans--con">
          <li class="nav-item text-center mb-0  ">
        <a id="donateLink" class="nav-link" href="https://support.truthout.org/-/XXQLBDSX">
          Donate
        </a>

</li>
      </ul>
</nav>

<h5 id="primaryMenuLabel" class="visually-hidden">Menu</h5>
    <button type="button" class="btn-close order-0 order-md-3 mt-0 mb-0 ms-auto ms-md-4 me-2 text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>

<div class="offcanvas-body px-0 pt-0 pl-4 border-top--gray--md">

<div class="d-flex d-md-none flex-column pb-0">
      <nav id="offCanvasTop" class="nav-top" aria-label="Off canvas mobile menu">
  <ul class="nav d-flex flex-column text-uppercase font-sans--con">
          <li class="nav-item text-center mb-3  current_page_parent ">
        <a id="latestLink" class="nav-link" href="https://truthout.org/latest/">
          Latest
        </a>

</li>
          <li class="nav-item text-center mb-3  ">
        <a id="aboutUsLink" class="nav-link" href="https://truthout.org/about/">
          About Us
        </a>

</li>
          <li class="nav-item text-center mb-3  ">
        <a id="subscribeLink" class="nav-link" href="https://truthout.org/subscribe/">
          Subscribe
        </a>

</li>
          <li class="nav-item text-center mb-3  ">
        <a id="donateLink" class="nav-link" href="#XSDZSCGH">
          Donate
        </a>

</li>
      </ul>
</nav>
    </div>

<div class="d-flex flex-row justify-content-center px-4 px-md-5">
      <!-- begin partials/advanced-search -->
<form id="search" class="search w-100 mt-0 mb-0 mb-md-3" name="searchform" method="get" action="https://truthout.org">

<div class="input-group mt-3 mb-md-3 pb-2 pb-md-3 border-bottom--gray">
    <label for="searchForm" class="form-label visually-hidden">Search</label>
    <input id="searchForm" type="search" class="search__input form-control font-sans" name="s" title="Search Blog" value="" placeholder="Search for&hellip;" />
    <button type="submit" value="submit" class="search__submit button button--outline" id="searchsubmit">Search</button>
  </div>

<fieldset class="search__options d-none d-md-flex justify-content-around justify-content-lg-center pb-3 font-sans border-bottom--gray">
    <legend class="visually-hidden">Filter Search</legend>
    <div class="d-flex px-lg-5">
        <input class="form-check-input me-2 visually-hidden" type="radio" value="all" name="post_type" id="searchOptionsAll" checked> <label class="d-flex align-items-center" for="searchOptionsAll">Search All Content</label>
    </div>
    <div class="d-flex px-lg-5">
      <input class="form-check-input me-2 visually-hidden" type="radio" value="to4_article_post" name="post_type" id="searchOptionsArticles"> <label class="d-flex align-items-center" for="searchOptionsArticles">Articles</label>
    </div>
    <div class="d-flex px-lg-5">
      <input class="form-check-input me-2 visually-hidden" type="radio" value="to4_audio_post" name="post_type" id="searchOptionsAudioPosts"> <label class="d-flex align-items-center" for="searchOptionsAudioPosts">Audio Posts</label>
    </div>
    <div class="d-flex px-lg-5">
      <input class="form-check-input me-2 visually-hidden" type="radio" value="to4_video_post" name="post_type" id="searchOptionsVideoPosts"> <label class="d-flex align-items-center" for="searchOptionsVideoPosts">Video Posts</label>
    </div>
    <div class="d-flex px-lg-5">
      <input class="form-check-input me-2 visually-hidden" type="radio" value="to4_author_post" name="post_type" id="searchOptionsAuthors"> <label class="d-flex align-items-center" for="searchOptionsAuthors">Authors</label>
    </div>
  </fieldset>

</form>

</div>

<div class="row mx-0 px-3 px-md-4">

<div class="col-12 col-md-5">
        <section class="menu--social col-12 mt-4 mb-4 mt-md-0 ps-md-0">
  <header class="menu--social__hd d-flex flex-row mt-2 mt-md-0 mb-4 pb-1 pb-md-3 align-items-center border-bottom--gray">
    <h4 class="menu__ti mb-0 mt-md-2 pb-2 text-uppercase font-sans fw-900">Social Media</h4>
  </header>
  <ul class="nav--social nav">

<li class="nav--social__item menu-item mb-3">
      <a class="me-md-4 social__btn d-flex flex-row align-items-center" href="https://www.facebook.com/truthout" aria-label="Facebook" target="_top" rel="nofollow">
        <span class="visually-hidden">Facebook</span>
        <svg aria-hidden="true" class="social__icon" version="1.1" role="img" focusable="false" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 x="0px" y="0px" viewBox="0 0 403.2 403.2" style="enable-background:new 0 0 403.2 403.2;" xml:space="preserve"><title>Facebook Circle Icon</title>
<path fill="currentColor" d="M201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S312.9,0,201.6,0z M174.8,310.3L174.8,310.3
	V222h-36.5v-41.5h36.5v-31.7c0-36,21.4-55.9,54.3-55.9c15.7,0,32.2,2.8,32.2,2.8v35.3h-18.1c-17.9,0-23.4,11.1-23.4,22.4v27h39.8
	l-6.4,41.5h-33.5v88.2l0,0"/>
</svg>      </a>
    </li>

<li class="nav--social__item menu-item mb-3">
      <a class="me-md-4 social__btn d-flex flex-row align-items-center" href="https://bsky.app/profile/truthout.org" aria-label="Bluesky" target="_top" rel="nofollow">
        <span class="visually-hidden">Bluesky</span>
        <svg aria-hidden="true" class="social__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 403.2 403.2"><title>Bluesky Circle Icon</title><defs><style>.cls-1{stroke-width:0px;}</style></defs><g id="Layer_1" focusable="false"><path fill="currentColor" class="cls-1" d="m201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6,201.6-90.3,201.6-201.6S312.9,0,201.6,0Zm126.12,198.07c-9.35,33.42-43.43,41.94-73.74,36.79,52.99,9.02,66.47,38.89,37.36,68.76-55.29,56.73-79.46-14.23-85.66-32.42-1.14-3.33-1.67-4.89-1.67-3.57,0-1.33-.54.23-1.67,3.57-6.19,18.18-30.37,89.15-85.66,32.42-29.11-29.87-15.63-59.75,37.36-68.76-30.31,5.16-64.39-3.36-73.74-36.79-2.69-9.61-7.28-68.82-7.28-76.82,0-40.06,35.12-27.47,56.79-11.2h0c30.04,22.55,62.35,68.27,74.21,92.81,11.86-24.54,44.17-70.26,74.21-92.81,21.67-16.27,56.79-28.86,56.79,11.2,0,8-4.59,67.21-7.28,76.82Z"/></g></svg>      </a>
    </li>

<li class="nav--social__item menu-item mb-3">
      <a class="me-md-4 social__btn d-flex flex-row align-items-center" href="https://flipboard.com/@Truthout" aria-label="Flipboard" target="_top" rel="nofollow">
        <span class="visually-hidden">Flipboard</span>
        <svg aria-hidden="true" class="social__icon" version="1.1" role="img" focusable="false" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 x="0px" y="0px" viewBox="0 0 403.2 403.2" style="enable-background:new 0 0 403.2 403.2;" xml:space="preserve"><title>Flipboard Circle Icon</title>
<path fill="currentColor" d="M201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S312.9,0,201.6,0z M294.1,180.8h-60.9v60.9
	h-60.9v60.9h-60.9V119.9h182.6V180.8z"/>
</svg>      </a>
    </li>

<li class="nav--social__item menu-item mb-3">
      <a class="me-md-4 social__btn d-flex flex-row align-items-center" href="https://www.instagram.com/truthout/" aria-label="Instagram" target="_top" rel="nofollow">
        <span class="visually-hidden">Instagram</span>
        <svg aria-hidden="true" class="social__icon" role="img" data-name="Instagram Circle Icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 403.2 403.2"><title>Instagram Circle Icon</title><defs><style>.cls-1{stroke:#000;stroke-miterlimit:10;}</style></defs><path fill="currentColor" class="cls-1" d="M201.56,162.78A38.85,38.85,0,1,0,229,174.13,38.84,38.84,0,0,0,201.56,162.78Z"/><path fill="currentColor" d="M292.4,132.93h-.07A39.35,39.35,0,0,0,270.2,110.8c-15.29-6-51.69-4.68-68.65-4.68s-53.32-1.41-68.65,4.68a39.35,39.35,0,0,0-22.13,22.13c-6,15.29-4.68,51.72-4.68,68.67s-1.34,53.33,4.72,68.62a39.27,39.27,0,0,0,22.13,22.13c15.29,6,51.68,4.68,68.65,4.68s53.31,1.41,68.64-4.68a39.32,39.32,0,0,0,22.14-22.13c6.08-15.29,4.68-51.72,4.68-68.67S298.45,148.22,292.4,132.93Zm-35.67,91.5a59.83,59.83,0,1,1,4.52-22.86A59.75,59.75,0,0,1,256.73,224.43Zm19.85-79.72a13.77,13.77,0,0,1-3,4.52,13.82,13.82,0,0,1-9.85,4.08h0A13.84,13.84,0,0,1,256,151a13.94,13.94,0,1,1,21.66-11.59A13.73,13.73,0,0,1,276.58,144.71Z"/><path fill="currentColor" d="M201.6,0C90.3,0,0,90.3,0,201.6S90.3,403.2,201.6,403.2s201.6-90.3,201.6-201.6S312.9,0,201.6,0ZM317.23,249.62c-.94,18.65-5.2,35.18-18.82,48.77s-30.14,17.92-48.77,18.81c-19.22,1.09-76.87,1.09-96.08,0-18.66-.94-35.13-5.2-48.77-18.81S86.86,268.24,86,249.62c-1.09-19.23-1.09-76.87,0-96.09.94-18.65,5.15-35.18,18.82-48.77S135,86.89,153.56,86c19.22-1.09,76.86-1.09,96.08,0,18.66.94,35.18,5.2,48.77,18.81s17.93,30.15,18.82,48.81C318.32,172.75,318.32,230.4,317.23,249.62Z"/></svg>      </a>
    </li>

<li class="nav--social__item menu-item mb-3">
      <a class="me-md-4 social__btn d-flex flex-row align-items-center" href="https://twitter.com/truthout" aria-label="Twitter" target="_top" rel="nofollow">
        <span class="visually-hidden">Twitter</span>
        <svg aria-hidden="true" class="social__icon" version="1.1" role="img" focusable="false" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 x="0px" y="0px" viewBox="0 0 403.2 403.2" style="enable-background:new 0 0 403.2 403.2;" xml:space="preserve"><title>Twitter Circle Icon</title>
<path fill="currentColor" d="M201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S312.9,0,201.6,0z M302,161.5
	c0.1,2,0.1,4.1,0.1,6.1c0,62.5-47.6,134.5-134.5,134.5c-26.8,0-51.7-7.8-72.6-21.2c3.8,0.4,7.5,0.6,11.4,0.6
	c22.1,0,42.5-7.5,58.7-20.2c-20.8-0.4-38.2-14.1-44.2-32.8c7.3,1.1,13.8,1.1,21.3-0.9c-21.6-4.4-37.8-23.4-37.8-46.4v-0.6
	c6.3,3.5,13.6,5.7,21.3,6c-13.2-8.8-21.1-23.5-21.1-39.4c0-8.8,2.3-16.9,6.4-23.9c23.3,28.7,58.3,47.4,97.5,49.5
	c-6.7-32.1,17.3-58.1,46.1-58.1c13.6,0,25.9,5.7,34.5,14.9c10.7-2,20.9-6,30-11.4c-3.5,11-11,20.2-20.8,26c9.5-1,18.7-3.7,27.3-7.4
	C319.3,146.4,311.2,154.8,302,161.5z"/>
</svg>      </a>
    </li>

<li class="nav--social__item menu-item mb-3">
      <a class="me-md-4 social__btn d-flex flex-row align-items-center" href="https://truthout.org/latest/feed/" aria-label="RSS" target="_top" rel="nofollow">
        <span class="visually-hidden">RSS</span>
        <svg aria-hidden="true" class="social__icon" version="1.1" role="img" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 404.2 404.2" style="enable-background:new 0 0 404.2 404.2;" xml:space="preserve"><title>RSS Circle Icon</title>
<path fill="currentColor" d="M202.1,0.5C90.8,0.5,0.5,90.8,0.5,202.1s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S313.4,0.5,202.1,0.5z M151.1,287.6
	c-4,4-9.4,6.3-15.1,6.3c-11.8,0-21.4-9.5-21.4-21.3c0-11.8,9.5-21.4,21.3-21.4c11.8,0,21.4,9.5,21.4,21.3
	C157.4,278.1,155.1,283.6,151.1,287.6z M217.2,293.8c-0.4-0.5-0.7,0.1-1.7,0.1c-8.5,0-15.5-6.6-16-15c-1.8-36.5-33.4-68.1-69.9-70.5
	c-8.8-0.6-15.5-8.2-14.9-17c0,0,0,0,0,0c0.6-8.8,8.3-15.2,17-14.9c51.9,3.4,96.9,48.4,100.3,100.3
	C232.6,285.5,226,293.1,217.2,293.8C217.2,293.8,217.2,293.8,217.2,293.8L217.2,293.8z M280.8,293.2c-0.2,0.6-0.5,0.6-1.3,0.6
	c-8.6,0-15.7-6.8-16-15.4c-2.4-71-62.5-131.2-133.5-134.7c-8.4,0.1-15.2-6.6-15.4-15c0-0.4,0-0.7,0-1.1c0.4-8.8,7.8-15.7,16.6-15.3
	c0,0,0,0,0,0c87.2,3.6,161.1,77.6,164.2,164.2C296.4,286,289.6,293.5,280.8,293.2L280.8,293.2z"/>
</svg>      </a>
    </li>

</ul></section>        <section class="menu--sections col-12 ps-md-0 mb-3">
  <header class="menu--sections__hd d-flex flex-row mb-4 pb-3 align-items-center border-bottom--gray">
    <h4 class="menu__ti w-100 d-flex flex-row align-items-center mb-0 pb-0 text-uppercase font-sans fw-900">Sections
    </h4>
  </header>

<ul class="nav nav--sections row row-cols-2 text-uppercase font-sans fw-600">
              <li class="nav--sections__item col nav-item mb-4 text-left"><a class="nav--sections__item__link text-decoration-none" href=https://truthout.org/section/culture-media/>Culture &amp; Media</a></li>
              <li class="nav--sections__item col nav-item mb-4 text-left"><a class="nav--sections__item__link text-decoration-none" href=https://truthout.org/section/economy-and-labor/>Economy &amp; Labor</a></li>
              <li class="nav--sections__item col nav-item mb-4 text-left"><a class="nav--sections__item__link text-decoration-none" href=https://truthout.org/section/education-and-youth/>Education &amp; Youth</a></li>
              <li class="nav--sections__item col nav-item mb-4 text-left"><a class="nav--sections__item__link text-decoration-none" href=https://truthout.org/section/environment-and-health/>Environment &amp; Health</a></li>
              <li class="nav--sections__item col nav-item mb-4 text-left"><a class="nav--sections__item__link text-decoration-none" href=https://truthout.org/section/humanrights/>Human Rights</a></li>
              <li class="nav--sections__item col nav-item mb-4 text-left"><a class="nav--sections__item__link text-decoration-none" href=https://truthout.org/section/immigration/>Immigration</a></li>
              <li class="nav--sections__item col nav-item mb-4 text-left"><a class="nav--sections__item__link text-decoration-none" href=https://truthout.org/section/lgbtq-rights/>LGBTQ Rights</a></li>
              <li class="nav--sections__item col nav-item mb-4 text-left"><a class="nav--sections__item__link text-decoration-none" href=https://truthout.org/section/politics-and-elections/>Politics &amp; Elections</a></li>
              <li class="nav--sections__item col nav-item mb-4 text-left"><a class="nav--sections__item__link text-decoration-none" href=https://truthout.org/section/prisons-and-policing/>Prisons &amp; Policing</a></li>
              <li class="nav--sections__item col nav-item mb-4 text-left"><a class="nav--sections__item__link text-decoration-none" href=https://truthout.org/section/racial-justice/>Racial Justice</a></li>
              <li class="nav--sections__item col nav-item mb-4 text-left"><a class="nav--sections__item__link text-decoration-none" href=https://truthout.org/section/reproductive-rights/>Reproductive Rights</a></li>
              <li class="nav--sections__item col nav-item mb-4 text-left"><a class="nav--sections__item__link text-decoration-none" href=https://truthout.org/section/war-and-peace/>War &amp; Peace</a></li>
              <li class="nav--sections__item col nav-item mb-4 text-left"><a class="nav--sections__item__link text-decoration-none" href=https://truthout.org/series/>Series &#038; Podcasts</a></li>
          </ul>
  </section>      </div>

<div class="col-12 col-md-7 row">
        <section class="menu--trending col-12 col-md-4 d-flex flex-column mt-4 mt-md-0">
    <header class="menu--trending__hd d-flex flex-row w-100 align-items-center mb-4 pb-3 border-bottom--gray">
      <h4 id="trendingTitle" class="menu--trending__ti menu__ti d-flex flex-row me-2 mb-0 font-sans text-uppercase fw-900 text-left">Trending<span class="separator"></span></h4>
      <svg class="true" width="18" height="12" viewBox="0 0 18 12" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
<path fill-rule="evenodd" clip-rule="evenodd" d="M15.2774 0.000469522C15.5014 -0.00884774 15.7079 0.121216 15.7962 0.327284L17.9562 5.36724C18.0737 5.64136 17.9467 5.95881 17.6726 6.07629C17.3985 6.19377 17.081 6.06678 16.9635 5.79267L15.363 2.05817L12.2122 11.5107C12.1415 11.7229 11.9472 11.8695 11.7238 11.8794C11.5003 11.8892 11.2939 11.7603 11.2047 11.5552L8.09841 4.41073L6.0747 9.03636C5.99838 9.21079 5.83585 9.33214 5.64693 9.35575C5.45801 9.37936 5.27062 9.30173 5.15373 9.15145L3.06 6.45951L0.966266 9.15145C0.78317 9.38686 0.443904 9.42927 0.208495 9.24617C-0.0269144 9.06307 -0.0693226 8.72381 0.113774 8.4884L2.63375 5.24843C2.73606 5.11689 2.89336 5.03996 3.06 5.03996C3.22663 5.03996 3.38394 5.11689 3.48624 5.24843L5.44903 7.772L7.60523 2.84353C7.69131 2.64678 7.88581 2.51974 8.10057 2.51998C8.31533 2.52023 8.50953 2.64771 8.59516 2.84467L11.6333 9.83227L14.7876 0.369237C14.8585 0.156546 15.0534 0.00978674 15.2774 0.000469522Z" fill="currentColor" fill-opacity="0.65"/>
</svg>    </header>

<ul class="nav row row-cols-2 row-cols-md-1 text-uppercase font-sans">
              <li class="nav-item">
          <a id="trending1" href="https://truthout.org/topics/donald-trump/" title="Donald Trump" class="topic donald-trump nav-link">
          Donald Trump
         </a>
       </li>
              <li class="nav-item">
          <a id="trending2" href="https://truthout.org/topics/vaccines/" title="Vaccines" class="topic vaccines nav-link">
          Vaccines
         </a>
       </li>
              <li class="nav-item">
          <a id="trending3" href="https://truthout.org/topics/charlie-kirk/" title="Charlie Kirk" class="topic charlie-kirk nav-link">
          Charlie Kirk
         </a>
       </li>
              <li class="nav-item">
          <a id="trending4" href="https://truthout.org/topics/palestine/" title="Palestine" class="topic palestine nav-link">
          Palestine
         </a>
       </li>
              <li class="nav-item">
          <a id="trending5" href="https://truthout.org/topics/immigration/" title="Immigration" class="topic immigration nav-link">
          Immigration
         </a>
       </li>
          </ul>
  </section>

<section class="menu--latest col-12 col-md-8 mt-4 mt-md-0 pe-md-0">
  <header class="menu--latest__hd d-flex flex-row mb-4 pb-3 align-items-center border-bottom--gray">
    <h4 class="menu__ti w-100 mb-0 pb-0 text-uppercase font-sans fw-900">
      <a class="w-100 d-flex flex-row align-items-center" href="/latest">Latest
        <svg aria-hidden="true" class="mb-0 ms-auto ms-md-2"
  xmlns="http://www.w3.org/2000/svg"
  width="24"
  height="24"
  viewBox="0 0 24 24"
  fill="none"
  stroke="currentColor"
  stroke-width="2"
  stroke-linecap="round"
  stroke-linejoin="round"
>
  <circle cx="12" cy="12" r="10" />
  <polyline points="12 16 16 12 12 8" />
  <line x1="8" y1="12" x2="16" y2="12" />
</svg>      </a>
    </h4>
  </header>

<div class="row row-cols-2 h-100">
              <article class="menu--latest__item mb-4">
                       <div class="menu--latest__section pt-1 mb-2 font-sans text-uppercase">Environment</div>
                    <h5 class="menu--latest__item__ti fw-bold"><a class="menu--latest__item__link text-decoration-none" href="https://truthout.org/articles/this-researcher-studied-how-climate-change-hurts-children-trump-shut-her-down/">This Researcher Studied How Climate Change Hurts Children — Trump Shut Her Down</a></h5>
        </article>
              <article class="menu--latest__item mb-4">
                       <div class="menu--latest__section pt-1 mb-2 font-sans text-uppercase">Trump Administration</div>
                    <h5 class="menu--latest__item__ti fw-bold"><a class="menu--latest__item__link text-decoration-none" href="https://truthout.org/articles/new-bill-would-allow-rubio-to-strip-us-citizens-passports-over-political-speech/">New Bill Would Allow Rubio to Strip US Citizens&#8217; Passports Over Political Speech</a></h5>
        </article>
              <article class="menu--latest__item mb-4">
                       <div class="menu--latest__section pt-1 mb-2 font-sans text-uppercase">Trump Administration</div>
                    <h5 class="menu--latest__item__ti fw-bold"><a class="menu--latest__item__link text-decoration-none" href="https://truthout.org/articles/stephen-miller-vows-to-dismantle-the-left-after-charlie-kirk-assassination/">Stephen Miller Vows to &#8220;Dismantle&#8221; the Left After Charlie Kirk Assassination</a></h5>
        </article>
              <article class="menu--latest__item mb-4">
                       <div class="menu--latest__section pt-1 mb-2 font-sans text-uppercase">Donald Trump</div>
                    <h5 class="menu--latest__item__ti fw-bold"><a class="menu--latest__item__link text-decoration-none" href="https://truthout.org/articles/trumps-health-care-funding-cuts-leave-states-with-impossible-budget-choices/">Trump&#8217;s Health Care Funding Cuts Leave States With Impossible Budget Choices</a></h5>
        </article>
          </div>
  </section>
        <section class="menu--more col-12 mt-5 mt-md-0">
  <header class="menu--more__hd d-flex flex-row mb-3 pb-3 align-items-center border-bottom--gray">
    <h4 class="menu__ti mb-0 pb-0 text-uppercase font-sans fw-900">More</h4>
  </header>

<nav id="menuMore" class="nav nav--more font-sans" aria-label="Additional links">
  <ul class="nav row gr-0 row-cols-2 row-cols-md-3 ">
          <li class="nav-item nav-item text-left ps-0 pb-1  ">
        <a id="aboutLink" class="nav-link" href="https://truthout.org/about/">
          About
        </a>

</li>
          <li class="nav-item nav-item text-left ps-0 pb-1  ">
        <a id="donateLink" class="nav-link" href="/?form=donate">
          Donate
        </a>

</li>
          <li class="nav-item nav-item text-left ps-0 pb-1  ">
        <a id="manageYourDonationLink" class="nav-link" href="https://truthout.org/manage-your-donation/">
          Manage Your Donation
        </a>

</li>
          <li class="nav-item nav-item text-left ps-0 pb-1  ">
        <a id="supportOurWorkLink" class="nav-link" href="https://truthout.org/more-ways-to-give/">
          Support Our Work
        </a>

</li>
          <li class="nav-item nav-item text-left ps-0 pb-1  ">
        <a id="subscribeLink" class="nav-link" href="https://truthout.org/subscribe/">
          Subscribe
        </a>

</li>
          <li class="nav-item nav-item text-left ps-0 pb-1  ">
        <a id="submissionGuidelinesLink" class="nav-link" href="https://truthout.org/submission-guidelines/">
          Submission Guidelines
        </a>

</li>
          <li class="nav-item nav-item text-left ps-0 pb-1  ">
        <a id="financialInformationLink" class="nav-link" href="https://truthout.org/about/#financial">
          Financial Information
        </a>

</li>
          <li class="nav-item nav-item text-left ps-0 pb-1  ">
        <a id="privacyPolicyLink" class="nav-link" href="https://truthout.org/about/#dtpp">
          Privacy Policy
        </a>

</li>
          <li class="nav-item nav-item text-left ps-0 pb-1  ">
        <a id="memorialEssayPrizeLink" class="nav-link" href="https://truthout.org/articles/keeley-schenwar-memorial-essay-prize/">
          Memorial Essay Prize
        </a>

</li>
          <li class="nav-item nav-item text-left ps-0 pb-1  ">
        <a id="truthoutCenterForGrassrootsJournalismLink" class="nav-link" href="https://truthout.org/articles/truthout-center-for-grassroots-journalism/">
          Truthout Center for Grassroots Journalism
        </a>

</li>
          <li class="nav-item nav-item text-left ps-0 pb-1  ">
        <a id="jobOpeningsLink" class="nav-link" href="https://truthout.org/job-openings/">
          Job Openings
        </a>

</li>
          <li class="nav-item nav-item text-left ps-0 pb-1  ">
        <a id="contactUsLink" class="nav-link" href="https://truthout.org/contact-us">
          Contact Us
        </a>

</li>
      </ul>
</nav>
</section>
      </div>
    </div>

<div class="tagline row d-md-none mt-5 text-center">
      <small class="copyright">&copy; 2025 Truthout</small>
    </div>
  </div>

</div>

<main id="main" class="main container-fluid d-flex flex-wrap justify-content-center pb-6 px-0">
             <!--begin content-single -->
  <div class="ar__hd col-12 d-flex flex-column justify-content-center overflow-hidden bg-black text-white  mb-4" aria-hidden="true">

<div class="container row gx-3 gx-md-4 pb-4 pb-md-0 mx-auto">

      <div class="col-lg-6 d-flex flex-column justify-content-center order-1 order-md-0 my-md-6">

  <div class="before-headline mt-2 mt-md-0 mb-md-1 pb-4 d-inline text-uppercase font-sans text-decoration-none black-65">
  <!-- components/category-terms -->
  <div class="categories d-inline">
                  <a href="https://truthout.org/category/news-analysis/" rel='category' class="news-analysis text-decoration-none black-65">News Analysis</a>
            </div>
  <span class="separator px-1">|</span>

  </div>

    <span class="ar__ti d-block" >Goodbye to All That: Reflections of a GOP Operative Who Left the Cult</span>

<div class="ar__meta font-sans mt-2 my-md-3">

<!-- components/authors -->
    <dl class="byline list-inline font-sans d-inline mt-2 mb-0 white-70">
        <dt class="byline__label d-inline me-0">By</dt>
                  <dd class="byline__author author vcard d-inline me-0" itemprop="author" itemscope itemtype="https://schema.org/Person">
            <span class="byline__author__name" itemprop="name">
              <a class="byline__author__link url fn text-decoration-none white-70" href="https://truthout.org/authors/mike-lofgren/" itemprop="url" rel="author">Mike Lofgren</a>
            </span>

<span class="separator">, </span>
                      </dd>

                  <dd class="byline__source source org d-inline" itemprop="sourceOrganization" itemscope itemtype="https://schema.org/Organization"><span class="byline__source__name text-uppercase" itemprop="name"> <a class="byline__source__link text-decoration-none d-inline white-70" href="https://truthout.org" itemprop="url"><span class="byline__source__upper">T</span>ruthout</a></span></dd>
            </dl>

<dl class="dateline list-inline mb-0 fs-8">
    <dt class="dateline__label list-inline-item me-0 visually-hidden">
      Published
    </dt>
    <dd class="list-inline-item me-0">
      <time class="published updated meta-data d-inline mt-2 font-sans black-70"
    datetime="2011-09-03T15:09:39+00:00"
    itemprop="datePublished dateCreated"
    content="2011-09-03T15:09:39+00:00">
    September 3, 2011
  </time>
    </dd>
  </dl>
</div>

</div>

      <figure class="ar__media ar__media--v ar__media--p col-12 col-lg-6 order-0 order-md-1 position-relative d-flex flex-column flex-md-row align-items-center justify-content-center mb-4 mb-md-0"  itemprop="image" itemscope itemtype="http://schema.org/ImageObject" style="--portrait-url:url(https://truthout.org/app/uploads/2017/12/Goodbye-to-All-That-Reflections-of-a-GOP-Operative-Who-Left-the-Cult.jpg);"><img width="240" height="272" src="https://truthout.org/app/uploads/2017/12/Goodbye-to-All-That-Reflections-of-a-GOP-Operative-Who-Left-the-Cult.jpg" class="ar__media__img img-fluid w-100 portrait ar__media__img--sm w-auto h-100 wp-post-image" alt="" itemprop="url" loading="eager" decoding="async" fetchpriority="high" srcset="https://truthout.org/app/uploads/2017/12/Goodbye-to-All-That-Reflections-of-a-GOP-Operative-Who-Left-the-Cult.jpg 240w, https://truthout.org/app/uploads/2017/12/Goodbye-to-All-That-Reflections-of-a-GOP-Operative-Who-Left-the-Cult-200x227.jpg 200w" sizes="(max-width: 240px) 100vw, 240px" /><figcaption class="ar__media__text pt-4 font-sans" itemprop="caption"><span><p>
	(Photo: <a href="https://www.flickr.com/photos/carolyntiry/4034641618/">Carolyn Tiry / Flickr</a>)</p>
</span></figcaption></figure>

      </div>

</div>

<article itemprop="mainEntity" itemscope itemtype="https://schema.org/AnalysisNewsArticle" class="row pb-5 source-truthout container">

<header class="visually-hidden  mb-4" >

<div class="container row gx-3 gx-md-4 pb-4 pb-md-0 mx-auto">

      <div class="col-lg-6 d-flex flex-column justify-content-center order-1 order-md-0 my-md-6">

  <div class="before-headline mt-2 mt-md-0 mb-md-1 pb-4 d-inline text-uppercase font-sans text-decoration-none black-65">
  <!-- components/category-terms -->
  <div class="categories d-inline">
                  <a href="https://truthout.org/category/news-analysis/" rel='category' class="news-analysis text-decoration-none black-65">News Analysis</a>
            </div>
  <span class="separator px-1">|</span>

  </div>

    <h1 class="ar__ti " >Goodbye to All That: Reflections of a GOP Operative Who Left the Cult</h1>

<div class="ar__meta font-sans mt-2 my-md-3">

<!-- components/authors -->
    <dl class="byline list-inline font-sans d-inline mt-2 mb-0 white-70">
        <dt class="byline__label d-inline me-0">By</dt>
                  <dd class="byline__author author vcard d-inline me-0" itemprop="author" itemscope itemtype="https://schema.org/Person">
            <span class="byline__author__name" itemprop="name">
              <a class="byline__author__link url fn text-decoration-none white-70" href="https://truthout.org/authors/mike-lofgren/" itemprop="url" rel="author">Mike Lofgren</a>
            </span>

<span class="separator">, </span>
                      </dd>

                  <dd class="byline__source source org d-inline" itemprop="sourceOrganization" itemscope itemtype="https://schema.org/Organization"><span class="byline__source__name text-uppercase" itemprop="name"> <a class="byline__source__link text-decoration-none d-inline white-70" href="https://truthout.org" itemprop="url"><span class="byline__source__upper">T</span>ruthout</a></span></dd>
            </dl>

<dl class="dateline list-inline mb-0 fs-8">
    <dt class="dateline__label list-inline-item me-0 visually-hidden">
      Published
    </dt>
    <dd class="list-inline-item me-0">
      <time class="published updated meta-data d-inline mt-2 font-sans black-70"
    datetime="2011-09-03T15:09:39+00:00"
    itemprop="datePublished dateCreated"
    content="2011-09-03T15:09:39+00:00">
    September 3, 2011
  </time>
    </dd>
  </dl>
</div>

</div>

      <figure class="ar__media ar__media--v ar__media--p col-12 col-lg-6 order-0 order-md-1 position-relative d-flex flex-column flex-md-row align-items-center justify-content-center mb-4 mb-md-0"  itemprop="image" itemscope itemtype="http://schema.org/ImageObject" style="--portrait-url:url(https://truthout.org/app/uploads/2017/12/Goodbye-to-All-That-Reflections-of-a-GOP-Operative-Who-Left-the-Cult.jpg);"><img width="240" height="272" src="https://truthout.org/app/uploads/2017/12/Goodbye-to-All-That-Reflections-of-a-GOP-Operative-Who-Left-the-Cult.jpg" class="ar__media__img img-fluid w-100 portrait ar__media__img--sm w-auto h-100 wp-post-image" alt="" itemprop="url" loading="eager" decoding="async" fetchpriority="high" srcset="https://truthout.org/app/uploads/2017/12/Goodbye-to-All-That-Reflections-of-a-GOP-Operative-Who-Left-the-Cult.jpg 240w, https://truthout.org/app/uploads/2017/12/Goodbye-to-All-That-Reflections-of-a-GOP-Operative-Who-Left-the-Cult-200x227.jpg 200w" sizes="(max-width: 240px) 100vw, 240px" /><figcaption class="ar__media__text pt-4 font-sans" itemprop="caption"><span><p>
	(Photo: <a href="https://www.flickr.com/photos/carolyntiry/4034641618/">Carolyn Tiry / Flickr</a>)</p>
</span></figcaption></figure>

      </div>

</header>

<div id="articleContent" class="ar__con order-3 col-12 col-lg-7 mt-3 px-md-6">

<!-- begin partial/series-card -->

<html><body><div class="truth-post-content-before" id="truth-3057060375"><div class="popmake-campaign-banners-donate-modal callout callout inline-callout mb-5 callout--text callout--text" id="truth-304025" data-callout-id="304025" data-callout-theme="text" data-callout-placement="Undefined" data-callout-title="BCB 304025 Truthout is an indispensable resource..."><p><i><span style="font-weight: 400;">Truthout is an indispensable resource for activists, movement leaders and workers everywhere. Please make this work possible with a </span></i><a href="https://support.truthout.org/-/XXQLBDSX/&amp;utm_source=truthout&amp;utm_medium=bcb&amp;utm_campaign=304025"><i><span style="font-weight: 400;">quick donation</span></i></a><i><span style="font-weight: 400;">.</span></i></p>
</div></div>
<?xml encoding="utf-8" ?>
<div class="article_content">
<p>
	<em>Barbara Stanwyck: “We're both rotten!”</em></p>
<p>
	<em>Fred MacMurray: “Yeah – only you're a little more rotten.” -“Double Indemnity” (1944) </em></p>
<p>
	Those lines of dialogue from a classic film noir sum up the state of the two political parties in contemporary America. Both parties are rotten – how could they not be, given the complete infestation of the political system by corporate money on a scale that now requires a presidential candidate to raise upwards of a billion dollars to be competitive in the general election? Both parties are captives to corporate loot. The main reason the Democrats' health care bill will be a budget buster once it fully phases in is the Democrats' rank capitulation to corporate interests – no single-payer system, in order to mollify the insurers; and no negotiation of drug prices, a craven surrender to Big Pharma.</p><div class="truth-post-content-high" id="truth-964261929"><div class="callout inline-callout p-4 mb-5 callout--subscribe callout--light" id="truth-255392" data-callout-id="255392" data-callout-theme="light" data-callout-placement="Post Content - High" data-callout-title="Never miss another story"><h4>Never miss another story</h4>
<p>Get the news you want, delivered to your inbox every day.</p>

<div class="gf_browser_chrome gform_wrapper gform_legacy_markup_wrapper gform-theme--no-framework gform_wrapper gform_legacy_markup_wrapper gform-theme--no-framework_original_id_1 subscribe-form_wrapper input-group_wrapper" data-form-theme="legacy" data-form-index="0" id="gform_wrapper_809858788"><div id="gf_809858788" class="gform_anchor" tabindex="-1"></div><form method="post" enctype="multipart/form-data" target="gform_ajax_frame_809858788" id="gform_809858788" class="subscribe-form input-group" action="/articles/goodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult/#gf_809858788" data-formid="1" novalidate>
                        <div class="gform-body gform_body"><ul id="gform_fields_809858788" class="gform_fields top_label form_sublabel_below description_below validation_below"><li id="field_1_1" class="gfield gfield--type-email gfield_contains_required field_sublabel_below gfield--no-description field_description_below hidden_label field_validation_below gfield_visibility_visible"><label class="gfield_label gform-field-label" for="input_809858788_1">Email<span class="gfield_required"><span class="gfield_required gfield_required_asterisk">*</span></span></label><div class="ginput_container ginput_container_email">
                            <input name="input_1" id="input_809858788_1" type="email" value class="medium" placeholder="name@email.com" aria-required="true" aria-invalid="false">
                        </div></li><li id="field_1_5" class="gfield gfield--type-hidden gform_hidden field_sublabel_below gfield--no-description field_description_below field_validation_below gfield_visibility_visible"><div class="ginput_container ginput_container_text"><input name="input_5" id="input_809858788_5" type="hidden" class="gform_hidden" aria-invalid="false" value></div></li><li id="field_1_6" class="gfield gfield--type-hidden gform_hidden field_sublabel_below gfield--no-description field_description_below field_validation_below gfield_visibility_visible"><div class="ginput_container ginput_container_text"><input name="input_6" id="input_809858788_6" type="hidden" class="gform_hidden" aria-invalid="false" value></div></li><li id="field_1_7" class="gfield gfield--type-hidden gform_hidden field_sublabel_below gfield--no-description field_description_below field_validation_below gfield_visibility_visible"><div class="ginput_container ginput_container_text"><input name="input_7" id="input_809858788_7" type="hidden" class="gform_hidden" aria-invalid="false" value></div></li><li id="field_1_9" class="gfield gfield--type-hidden gform_hidden field_sublabel_below gfield--no-description field_description_below field_validation_below gfield_visibility_visible"><div class="ginput_container ginput_container_text"><input name="input_9" id="input_809858788_9" type="hidden" class="gform_hidden" aria-invalid="false" value></div></li><li id="field_1_8" class="gfield gfield--type-hidden gform_hidden field_sublabel_below gfield--no-description field_description_below field_validation_below gfield_visibility_visible"><div class="ginput_container ginput_container_text"><input name="input_8" id="input_809858788_8" type="hidden" class="gform_hidden" aria-invalid="false" value></div></li><li id="field_1_10" class="gfield gfield--type-hidden gform_hidden field_sublabel_below gfield--no-description field_description_below field_validation_below gfield_visibility_visible"><div class="ginput_container ginput_container_text"><input name="input_10" id="input_809858788_10" type="hidden" class="gform_hidden" aria-invalid="false" value></div></li><li id="field_1_11" class="gfield gfield--type-honeypot gform_validation_container field_sublabel_below gfield--has-description field_description_below field_validation_below gfield_visibility_visible"><label class="gfield_label gform-field-label" for="input_809858788_11">Comments</label><div class="ginput_container"><input name="input_11" id="input_809858788_11" type="text" value autocomplete="new-password"></div><div class="gfield_description" id="gfield_description_1_11">This field is for validation purposes and should be left unchanged.</div></li></ul></div>
        <div class="gform-footer gform_footer top_label"> <input type="submit" id="gform_submit_button_809858788" class="gform_button button" onclick="gform.submission.handleButtonClick(this);" data-submission-type="submit" value="Subscribe"> <input type="hidden" name="gform_ajax" value="form_id=1&amp;title=&amp;description=&amp;tabindex=0&amp;theme=legacy&amp;hash=593d1db39c763ae878bbad5d2b573973">
            <input type="hidden" class="gform_hidden" name="gform_submission_method" data-js="gform_submission_method_1" value="iframe">
            <input type="hidden" class="gform_hidden" name="gform_theme" data-js="gform_theme_1" id="gform_theme_1" value="legacy">
            <input type="hidden" class="gform_hidden" name="gform_style_settings" data-js="gform_style_settings_1" id="gform_style_settings_1" value>
            <input type="hidden" class="gform_hidden" name="is_submit_1" value="1">
            <input type="hidden" class="gform_hidden" name="gform_submit" value="1">

            <input type="hidden" class="gform_hidden" name="gform_unique_id" value>
            <input type="hidden" class="gform_hidden" name="state_1" value="WyJbXSIsIjY1ZDU1NDE3M2ZkMThlYjM4YzM3YTA3MGIxNTlkNjBhIl0=">
            <input type="hidden" autocomplete="off" class="gform_hidden" name="gform_target_page_number_1" id="gform_target_page_number_809858788_1" value="0">
            <input type="hidden" autocomplete="off" class="gform_hidden" name="gform_source_page_number_1" id="gform_source_page_number_809858788_1" value="1">
            <input type="hidden" name="gform_random_id" value="809858788"><input type="hidden" name="gform_field_values" value>

        </div>
                        </form>
                        </div>
		                <iframe style="display:none;width:0px;height:0px;" src="about:blank" name="gform_ajax_frame_809858788" id="gform_ajax_frame_809858788" title="This iframe contains the logic required to handle Ajax powered Gravity Forms." loading="lazy"></iframe>
		                <script>
gform.initializeOnLoaded( function() {gformInitSpinner( 809858788, 'https://truthout.org/app/plugins/gravityforms/images/spinner.svg', true );jQuery('#gform_ajax_frame_809858788').on('load',function(){var contents = jQuery(this).contents().find('*').html();var is_postback = contents.indexOf('GF_AJAX_POSTBACK') >= 0;if(!is_postback){return;}var form_content = jQuery(this).contents().find('#gform_wrapper_809858788');var is_confirmation = jQuery(this).contents().find('#gform_confirmation_wrapper_809858788').length > 0;var is_redirect = contents.indexOf('gformRedirect(){') >= 0;var is_form = form_content.length > 0 && ! is_redirect && ! is_confirmation;var mt = parseInt(jQuery('html').css('margin-top'), 10) + parseInt(jQuery('body').css('margin-top'), 10) + 100;if(is_form){jQuery('#gform_wrapper_809858788').html(form_content.html());if(form_content.hasClass('gform_validation_error')){jQuery('#gform_wrapper_809858788').addClass('gform_validation_error');} else {jQuery('#gform_wrapper_809858788').removeClass('gform_validation_error');}setTimeout( function() { /* delay the scroll by 50 milliseconds to fix a bug in chrome */ jQuery(document).scrollTop(jQuery('#gform_wrapper_809858788').offset().top - mt); }, 50 );if(window['gformInitDatepicker']) {gformInitDatepicker();}if(window['gformInitPriceFields']) {gformInitPriceFields();}var current_page = jQuery('#gform_source_page_number_809858788_1').val();gformInitSpinner( 809858788, 'https://truthout.org/app/plugins/gravityforms/images/spinner.svg', true );jQuery(document).trigger('gform_page_loaded', [809858788, current_page]);window['gf_submitting_809858788'] = false;}else if(!is_redirect){var confirmation_content = jQuery(this).contents().find('.GF_AJAX_POSTBACK').html();if(!confirmation_content){confirmation_content = contents;}jQuery('#gform_wrapper_809858788').replaceWith(confirmation_content);jQuery(document).scrollTop(jQuery('#gf_809858788').offset().top - mt);jQuery(document).trigger('gform_confirmation_loaded', [809858788]);window['gf_submitting_809858788'] = false;wp.a11y.speak(jQuery('#gform_confirmation_message_809858788').text());}else{jQuery('#gform_809858788').append(contents);if(window['gformRedirect']) {gformRedirect();}}jQuery(document).trigger("gform_pre_post_render", [{ formId: "1", currentPage: "current_page", abort: function() { this.preventDefault(); } }]);        if (event && event.defaultPrevented) {                return;        }        const gformWrapperDiv = document.getElementById( "gform_wrapper_1" );        if ( gformWrapperDiv ) {            const visibilitySpan = document.createElement( "span" );            visibilitySpan.id = "gform_visibility_test_1";            gformWrapperDiv.insertAdjacentElement( "afterend", visibilitySpan );        }        const visibilityTestDiv = document.getElementById( "gform_visibility_test_1" );        let postRenderFired = false;        function triggerPostRender() {            if ( postRenderFired ) {                return;            }            postRenderFired = true;            gform.core.triggerPostRenderEvents( 1, current_page );            if ( visibilityTestDiv ) {                visibilityTestDiv.parentNode.removeChild( visibilityTestDiv );            }        }        function debounce( func, wait, immediate ) {            var timeout;            return function() {                var context = this, args = arguments;                var later = function() {                    timeout = null;                    if ( !immediate ) func.apply( context, args );                };                var callNow = immediate && !timeout;                clearTimeout( timeout );                timeout = setTimeout( later, wait );                if ( callNow ) func.apply( context, args );            };        }        const debouncedTriggerPostRender = debounce( function() {            triggerPostRender();        }, 200 );        if ( visibilityTestDiv && visibilityTestDiv.offsetParent === null ) {            const observer = new MutationObserver( ( mutations ) => {                mutations.forEach( ( mutation ) => {                    if ( mutation.type === 'attributes' && visibilityTestDiv.offsetParent !== null ) {                        debouncedTriggerPostRender();                        observer.disconnect();                    }                });            });            observer.observe( document.body, {                attributes: true,                childList: false,                subtree: true,                attributeFilter: [ 'style', 'class' ],            });        } else {            triggerPostRender();        }    } );} );
</script>

</div></div>
<p>	But both parties are not rotten in quite the same way. The Democrats have their share of machine politicians, careerists, corporate bagmen, egomaniacs and kooks. Nothing, however, quite matches the modern GOP.</p>
<p>	To those millions of Americans who have finally begun paying attention to politics and watched with exasperation the tragicomedy of the debt ceiling extension, it may have come as a shock that the Republican Party is so full of lunatics. To be sure, the party, like any political party on earth, has always had its share of crackpots, like Robert K. Dornan or William E. Dannemeyer. But the crackpot outliers of two decades ago have become the vital center today: Steve King, Michele Bachman (now a leading presidential candidate as well), Paul Broun, Patrick McHenry, Virginia Foxx, Louie Gohmert, Allen West. The Congressional directory now reads like a casebook of lunacy.</p>
<p>	It was this cast of characters and the pernicious ideas they represent that impelled me to end a nearly 30-year career as a professional staff member on Capitol Hill. A couple of months ago, I retired; but I could see as early as last November that the Republican Party would use the debt limit vote, an otherwise routine legislative procedure that has been used 87 times since the end of World War II, in order to concoct an entirely artificial fiscal crisis. Then, they would use that fiscal crisis to get what they wanted, by literally holding the US and global economies as hostages.</p>
<p>	The debt ceiling extension is not the only example of this sort of political terrorism. Republicans were willing to lay off 4,000 Federal Aviation Administration (FAA) employees, 70,000 private construction workers and let FAA safety inspectors work without pay, in fact, forcing them to pay for their own work-related travel – how prudent is that? – in order to strong arm some union-busting provisions into the FAA reauthorization.</p>
<p>	Everyone knows that in a hostage situation, the reckless and amoral actor has the negotiating upper hand over the cautious and responsible actor because the latter is actually concerned about the life of the hostage, while the former does not care. This fact, which ought to be obvious, has nevertheless caused confusion among the professional pundit class, which is mostly still stuck in the Bob Dole era in terms of its orientation. For instance, Ezra Klein <a href="https://www.washingtonpost.com/blogs/ezra-klein/post/wonkbook-republicans-have-won-but-can-they-stop-there/2011/07/25/gIQAFHVIYI_blog.html?fb_ref=NetworkNews">wrote</a> of his puzzlement over the fact that while House Republicans essentially won the debt ceiling fight, enough of them were sufficiently dissatisfied that they might still scuttle the deal. Of course they might – the attitude of many freshman Republicans to national default was “bring it on!”</p>
<p>	It should have been evident to clear-eyed observers that the Republican Party is becoming less and less like a traditional political party in a representative democracy and becoming more like an apocalyptic cult, or one of the intensely ideological authoritarian parties of 20th century Europe. This trend has several implications, none of them pleasant.</p>
<p>	In his “Manual of Parliamentary Practice,” Thomas Jefferson wrote that it is less important that every rule and custom of a legislature be absolutely justifiable in a theoretical sense, than that they should be generally acknowledged and honored by all parties. These include unwritten rules, customs and courtesies that lubricate the legislative machinery and keep governance a relatively civilized procedure. The US Senate has more complex procedural rules than any other legislative body in the world; many of these rules are contradictory, and on any given day, the Senate parliamentarian may issue a ruling that contradicts earlier rulings on analogous cases.</p>
<p>	The only thing that can keep the Senate functioning is collegiality and good faith. During periods of political consensus, for instance, the World War II and early post-war eras, the Senate was a “high functioning” institution: filibusters were rare and the body was legislatively productive. Now, one can no more picture the current Senate producing the original Medicare Act than the old Supreme Soviet having legislated the Bill of Rights.</p>
<p>	Far from being a rarity, virtually every bill, every nominee for Senate confirmation and every routine procedural motion is now subject to a Republican filibuster. Under the circumstances, it is no wonder that Washington is gridlocked: legislating has now become war minus the shooting, something one could have observed 80 years ago in the Reichstag of the Weimar Republic. As Hannah Arendt observed, a disciplined minority of totalitarians can use the instruments of democratic government to undermine democracy itself.</p>
<p>	John P. Judis <a href="https://www.tnr.com/article/john-judis/92958/obama-lincoln-debt-ceiling">sums up</a> the modern GOP this way:</p>
<blockquote>
<p>
		“Over the last four decades, the Republican Party has transformed from a loyal opposition into an insurrectionary party that flouts the law when it is in the majority and threatens disorder when it is the minority. It is the party of Watergate and Iran-Contra, but also of the government shutdown in 1995 and the impeachment trial of 1999. If there is an earlier American precedent for today's Republican Party, it is the antebellum Southern Democrats of John Calhoun who threatened to nullify, or disregard, federal legislation they objected to and who later led the fight to secede from the union over slavery.”</p>
</blockquote>
<p>
	A couple of years ago, a Republican committee staff director told me candidly (and proudly) what the method was to all this obstruction and disruption. Should Republicans succeed in obstructing the Senate from doing its job, it would further lower Congress's generic favorability rating among the American people. By sabotaging the reputation of an institution of government, the party that is programmatically against government would come out the relative winner.</p>
<p>	A deeply cynical tactic, to be sure, but a psychologically insightful one that plays on the weaknesses both of the voting public and the news media. There are tens of millions of low-information voters who hardly know which party controls which branch of government, let alone which party is pursuing a particular legislative tactic. These voters' confusion over who did what allows them to form the conclusion that “they are all crooks,” and that “government is no good,” further leading them to think, “a plague on both your houses” and “the parties are like two kids in a school yard.” This ill-informed public cynicism, in its turn, further intensifies the long-term decline in public trust in government that has been taking place since the early 1960s – a distrust that has been stoked by Republican rhetoric at every turn (“Government is the problem,” declared Ronald Reagan in 1980).</p>
<p>	The media are also complicit in this phenomenon. Ever since the bifurcation of electronic media into a more or less respectable “hard news” segment and a rabidly ideological talk radio and cable TV political propaganda arm, the “respectable” media have been terrified of any criticism for perceived bias. Hence, they hew to the practice of false evenhandedness. Paul Krugman has <a href="https://www.nytimes.com/2011/07/29/opinion/krugman-the-centrist-cop-out.html?_r=4&amp;hp">skewered</a> this tactic as being the “centrist cop-out.” “I joked long ago,” he says, “that if one party declared that the earth was flat, the headlines would read 'Views Differ on Shape of Planet.'”</p>
<p>	Inside-the-Beltway wise guy Chris Cillizza merely proves Krugman right in his Washington Post analysis of “winners and losers” in the debt ceiling impasse. He <a href="https://www.washingtonpost.com/politics/the-debt-ceiling-deal-winners-and-losers/2011/07/31/gIQAHl7FmI_story.html">wrote</a> that the institution of Congress was a big loser in the fracas, which is, of course, correct, but then he opined: “Lawmakers – bless their hearts – seem entirely unaware of just how bad they looked during this fight and will almost certainly spend the next few weeks (or months) congratulating themselves on their tremendous magnanimity.” Note how the pundit's ironic deprecation falls like the rain on the just and unjust alike, on those who precipitated the needless crisis and those who despaired of it. He seems oblivious that one side – or a sizable faction of one side – has deliberately attempted to damage the reputation of Congress to achieve its political objectives.</p>
<p>	This constant drizzle of “there the two parties go again!” stories out of the news bureaus, combined with the hazy confusion of low-information voters, means that the long-term Republican strategy of undermining confidence in our democratic institutions has reaped electoral dividends. The United States has nearly the lowest voter participation among Western democracies; this, again, is a consequence of the decline of trust in government institutions – if government is a racket and both parties are the same, why vote? And if the uninvolved middle declines to vote, it increases the electoral clout of a minority that is constantly being whipped into a lather by three hours daily of Rush Limbaugh or Fox News. There were only 44 million Republican voters in the 2010 mid-term elections, but they effectively canceled the political results of the election of President Obama by 69 million voters.</p>
<p>	This tactic of inducing public distrust of government is not only cynical, it is schizophrenic. For people who profess to revere the Constitution, it is strange that they so caustically denigrate the very federal government that is the material expression of the principles embodied in that document. This is not to say that there is not some theoretical limit to the size or intrusiveness of government; I would be the first to say there are such limits, both fiscal and Constitutional. But most Republican officeholders seem strangely uninterested in the effective repeal of Fourth Amendment protections by the Patriot Act, the weakening of habeas corpus and self-incrimination protections in the public hysteria following 9/11 or the unpalatable fact that the United States has the largest incarcerated population of any country on earth. If anything, they would probably opt for more incarcerated persons, as imprisonment is a profit center for the prison privatization industry, which is itself a growth center for political contributions to these same politicians.<a href="#%5B1%5D">[1]</a> Instead, they prefer to rail against those government programs that actually help people. And when a program is too popular to attack directly, like Medicare or Social Security, they prefer to undermine it by feigning an agonized concern about the deficit. That concern, as we shall see, is largely fictitious.</p>
<p>	Undermining Americans' belief in their own institutions of self-government remains a prime GOP electoral strategy. But if this technique falls short of producing Karl Rove's dream of 30 years of unchallengeable one-party rule (as all such techniques always fall short of achieving the angry and embittered true believer's New Jerusalem), there are other even less savory techniques upon which to fall back. Ever since Republicans captured the majority in a number of state legislatures last November, they have systematically attempted to make it more difficult to vote: by onerous voter ID requirements (in Wisconsin, Republicans have legislated photo IDs while simultaneously shutting Department of Motor Vehicles (DMV) offices in Democratic constituencies while at the same time lengthening the hours of operation of DMV offices in GOP constituencies); by narrowing registration periods; and by residency requirements that may disenfranchise university students.</p>
<p>	This legislative assault is moving in a diametrically opposed direction to 200 years of American history, when the arrow of progress pointed toward more political participation by more citizens. Republicans are among the most shrill in self-righteously lecturing other countries about the wonders of democracy; exporting democracy (albeit at the barrel of a gun) to the Middle East was a signature policy of the Bush administration. But domestically, they don't want <em>those people</em> voting.</p>
<p>	You can probably guess who <em>those people</em> are. Above all, anyone not likely to vote Republican. As Sarah Palin would imply, the people who are not Real Americans. Racial minorities. Immigrants. Muslims. Gays. Intellectuals. Basically, anyone who doesn't look, think, or talk like the GOP base. This must account, at least to some degree, for their extraordinarily vitriolic hatred of President Obama. I have joked in the past that the main administration policy that Republicans object to is Obama's policy of being black.<a href="#%5B2%5D">[2]</a> Among the GOP base, there is constant harping about somebody else, some “other,” who is deliberately, assiduously and with malice aforethought subverting the Good, the True and the Beautiful: Subversives. Commies. Socialists. Ragheads. Secular humanists. Blacks. Fags. Feminazis. The list may change with the political needs of the moment, but they always seem to need a scapegoat to hate and fear.</p>
<p>	It is not clear to me how many GOP officeholders believe this reactionary and paranoid claptrap. I would bet that most do not. But they cynically feed the worst instincts of their fearful and angry low-information political base with a nod and a wink. During the disgraceful circus of the “birther” issue, Republican politicians subtly stoked the fires of paranoia by being suggestively equivocal – “I take the president at his word” – while never unambiguously slapping down the myth. John Huntsman was the first major GOP figure forthrightly to refute the birther calumny – albeit <em>after</em> release of the birth certificate.</p>
<p>	I do not mean to place too much emphasis on racial animus in the GOP. While it surely exists, it is also a fact that Republicans think that no Democratic president could conceivably be legitimate. Republicans also regarded Bill Clinton as somehow, in some manner, twice fraudulently elected (well do I remember the elaborate conspiracy theories that Republicans traded among themselves). Had it been Hillary Clinton, rather than Barack Obama, who had been elected in 2008, I am certain we would now be hearing, in lieu of the birther myths, conspiracy theories about Vince Foster's alleged murder.</p>
<p>	The reader may think that I am attributing Svengali-like powers to GOP operatives able to manipulate a zombie base to do their bidding. It is more complicated than that. Historical circumstances produced the raw material: the deindustrialization and financialization of America since about 1970 has spawned an increasingly downscale white middle class – without job security (or even without jobs), with pensions and health benefits evaporating and with their principal asset deflating in the collapse of the housing bubble. Their fears are not imaginary; their standard of living is shrinking.</p>
<p>	What do the Democrats offer these people? Essentially nothing. Democratic Leadership Council-style “centrist” Democrats were among the biggest promoters of disastrous trade deals in the 1990s that outsourced jobs abroad: NAFTA, World Trade Organization, permanent most-favored-nation status for China. At the same time, the identity politics/lifestyle wing of the Democratic Party was seen as a too illegal immigrant-friendly by downscaled and outsourced whites.<a href="#%5B3%5D">[3]</a></p>
<p>	While Democrats temporized, or even dismissed the fears of the white working class as racist or nativist, Republicans went to work. To be sure, the business wing of the Republican Party consists of the most energetic outsourcers, wage cutters and hirers of sub-minimum wage immigrant labor to be found anywhere on the globe. But the faux-populist wing of the party, knowing the mental compartmentalization that occurs in most low-information voters, played on the fears of that same white working class to focus their anger on scapegoats that do no damage to corporations' bottom lines: instead of raising the minimum wage, let's build a wall on the Southern border (then hire a defense contractor to incompetently manage it). Instead of predatory bankers, it's evil Muslims. Or evil gays. Or evil abortionists.</p>
<p>	How do they manage to do this? Because Democrats ceded the field. Above all, they do not understand language. Their initiatives are posed in impenetrable policy-speak: the Patient Protection and Affordable Care Act. The <em>what</em>? – can anyone even remember it? No wonder the pejorative “Obamacare” won out. Contrast that with the Republicans' Patriot Act. You're a patriot, aren't you? Does anyone at the GED level have a clue what a Stimulus Bill is supposed to be? Why didn't the White House call it the Jobs Bill and keep pounding on that theme?</p>
<p>	You know that Social Security and Medicare are in jeopardy when even Democrats refer to them as entitlements. “Entitlement” has a negative sound in colloquial English: somebody who is “entitled” selfishly claims something he doesn't really deserve. Why not call them “earned benefits,” which is what they are because we all contribute payroll taxes to fund them? That would never occur to the Democrats. Republicans don't make that mistake; they are relentlessly on message: it is never the “estate tax,” it is the “death tax.” Heaven forbid that the Walton family should give up one penny of its $86-billion fortune. All of that lucre is necessary to ensure that unions be kept out of Wal-Mart, that women employees not be promoted and that politicians be kept on a short leash.</p>
<p>	It was not always thus. It would have been hard to find an uneducated farmer during the depression of the 1890s who did not have a very accurate idea about exactly which economic interests were shafting him. An unemployed worker in a breadline in 1932 would have felt little gratitude to the Rockefellers or the Mellons. But that is not the case in the present economic crisis. After a riot of unbridled greed such as the world has not seen since the conquistadors' looting expeditions and after an unprecedented broad and rapid transfer of wealth upward by Wall Street and its corporate satellites, where is the popular anger directed, at least as depicted in the media? At “Washington spending” – which has increased primarily to provide unemployment compensation, food stamps and Medicaid to those economically damaged by the previous decade's corporate saturnalia. Or the popular rage is harmlessly diverted against pseudo-issues: death panels, birtherism, gay marriage, abortion, and so on, none of which stands to dent the corporate bottom line in the slightest.</p>
<p>	Thus far, I have concentrated on Republican tactics, rather than Republican beliefs, but the tactics themselves are important indicators of an absolutist, authoritarian mindset that is increasingly hostile to the democratic values of reason, compromise and conciliation. Rather, this mindset seeks polarizing division (Karl Rove has been very explicit that this is his principal campaign strategy), conflict and the crushing of opposition.</p>
<p>	As for what they really believe, the Republican Party of 2011 believes in three principal tenets I have laid out below. The rest of their platform one may safely dismiss as window dressing:</p>
<p>	<strong>1. The GOP cares solely and exclusively about its rich contributors.</strong> The party has built a whole catechism on the protection and further enrichment of America's plutocracy. Their caterwauling about deficit and debt is so much eyewash to con the public. Whatever else President Obama has accomplished (and many of his purported accomplishments are highly suspect), his $4-trillion deficit reduction package did perform the useful service of smoking out Republican hypocrisy. The GOP refused, because it could not abide so much as a one-tenth of one percent increase on the tax rates of the Walton family or the Koch brothers, much less a repeal of the carried interest rule that permits billionaire hedge fund managers to pay income tax at a lower effective rate than cops or nurses. Republicans finally settled on a deal that had far less deficit reduction – and even less spending reduction! – than Obama's offer, because of their iron resolution to protect at all costs our society's overclass.</p>
<p>	Republicans have attempted to camouflage their amorous solicitude for billionaires with a fog of misleading rhetoric. John Boehner is fond of saying, “we won't raise anyone's taxes,” as if the take-home pay of an Olive Garden waitress were inextricably bound up with whether Warren Buffett pays his capital gains as ordinary income or at a lower rate. Another chestnut is that millionaires and billionaires are “job creators.” US corporations have just had their most profitable quarters in history; Apple, for one, is sitting on $76 billion in cash, more than the GDP of most countries. So, where are the jobs?</p>
<p>	Another smokescreen is the “small business” meme, since standing up for Mom's and Pop's corner store is politically more attractive than to be seen shilling for a megacorporation. Raising taxes on the wealthy will kill small business' ability to hire; that is the GOP dirge every time Bernie Sanders or some Democrat offers an amendment to increase taxes on incomes above $1 million. But the number of small businesses that have a net annual income over a million dollars is de minimis, if not by definition impossible (as they would no longer be small businesses). And as data from the Center for Economic and Policy Research have shown, small businesses account for only 7.2 percent of total US employment, a significantly smaller share of total employment than in most Organisation for Economic Co-operation and Development (OECD) countries.</p>
<p>	Likewise, Republicans have assiduously spread the myth that Americans are conspicuously overtaxed. But compared to other OECD countries, the effective rates of US taxation are among the lowest. In particular, they point to the top corporate income rate of 35 percent as being confiscatory Bolshevism. But again, the effective rate is much lower. Did GE pay 35 percent on 2010 profits of $14 billion? No, it paid zero.</p>
<p>	When pressed, Republicans make up misleading statistics to “prove” that the America's fiscal burden is being borne by the rich and the rest of us are just freeloaders who don't appreciate that fact. “Half of Americans don't pay taxes” is a perennial meme. But what they leave out is that that statement refers to federal <em>income</em> taxes. There are millions of people who don't pay income taxes, but do contribute payroll taxes – among the most regressive forms of taxation. But according to GOP fiscal theology, payroll taxes don't count. Somehow, they have convinced themselves that since payroll taxes go into trust funds, they're not real taxes. Likewise, state and local sales taxes apparently don't count, although their effect on a poor person buying necessities like foodstuffs is far more regressive than on a millionaire.</p>
<p>	All of these half truths and outright lies have seeped into popular culture via the corporate-owned business press. Just listen to CNBC for a few hours and you will hear most of them in one form or another. More important politically, Republicans' myths about taxation have been internalized by millions of economically downscale “values voters,” who may have been attracted to the GOP for other reasons (which I will explain later), but who now accept this misinformation as dogma.</p>
<p>	And when misinformation isn't enough to sustain popular support for the GOP's agenda, concealment is needed. One fairly innocuous provision in the Dodd-Frank financial reform bill requires public companies to make a more transparent disclosure of CEO compensation, including bonuses. Note that it would not limit the compensation, only require full disclosure. Republicans are hell-bent on repealing this provision. Of course; it would not serve Wall Street interests if the public took an unhealthy interest in the disparity of their own incomes as against that of a bank CEO. As Spencer Bachus, the Republican chairman of the House Financial Services Committee, <a href="https://thehill.com/blogs/on-the-money/banking-financial-institutions/133379-bachus-tells-local-paper-that-washington-should-qserveq-banks">says</a>, “In Washington, the view is that the banks are to be regulated and my view is that Washington and the regulators are there to serve the banks.”</p>
<p>	<strong>2. They worship at the altar of Mars. </strong> While the me-too Democrats have set a horrible example of keeping up with the Joneses with respect to waging wars, they can never match GOP stalwarts such as John McCain or Lindsey Graham in their sheer, libidinous enthusiasm for invading other countries. McCain wanted to mix it up with Russia – a nuclear-armed state – during the latter's conflict with Georgia in 2008 (remember? – “we are all Georgians now,” a slogan that did not, fortunately, catch on), while Graham has been persistently agitating for attacks on Iran and intervention in Syria. And these are not fringe elements of the party; they are the leading “defense experts,” who always get tapped for the Sunday talk shows. About a month before Republicans began holding a gun to the head of the credit markets to get trillions of dollars of cuts, these same Republicans passed a defense appropriations bill that <em>increased</em> spending by $17 billion over the prior year's defense appropriation. To borrow Chris Hedges' <a href="https://www.amazon.com/War-Force-that-Gives-Meaning/dp/1400034639/ref=sr_1_1?s=books&amp;ie=UTF8&amp;qid=1312410221&amp;sr=1-1">formulation</a>, war is the force that gives meaning to their lives.</p>
<p>	A cynic might conclude that this militaristic enthusiasm is no more complicated than the fact that Pentagon contractors spread a lot of bribery money around Capitol Hill. That is true, but there is more to it than that. It is not necessarily even the fact that members of Congress feel they are protecting constituents' jobs. The wildly uneven concentration of defense contracts and military bases nationally means that some areas, like Washington, DC, and San Diego, are heavily dependent on Department of Defense (DOD) spending. But there are many more areas of the country whose net balance is negative: the citizenry pays more in taxes to support the Pentagon than it receives back in local contracts.</p>
<p>	And the economic justification for Pentagon spending is even more fallacious when one considers that the $700 billion annual DOD budget creates comparatively few jobs. The days of Rosie the Riveter are long gone; most weapons projects now require very little touch labor. Instead, a disproportionate share is siphoned off into high-cost research and development (from which the civilian economy benefits little); exorbitant management expenditures, overhead and out-and-out padding; and, of course, the money that flows back into the coffers of political campaigns. A million dollars appropriated for highway construction would create two to three times as many jobs as a million dollars appropriated for Pentagon weapons procurement, so the jobs argument is ultimately specious.</p>
<p>	Take away the cash nexus and there still remains a psychological predisposition toward war and militarism on the part of the GOP. This undoubtedly arises from a neurotic need to demonstrate toughness and dovetails perfectly with the belligerent tough-guy pose one constantly hears on right-wing talk radio. Militarism springs from the same psychological deficit that requires an endless series of enemies, both foreign and domestic.</p>
<p>	The results of the last decade of unbridled militarism and the Democrats' cowardly refusal to reverse it<a href="#%5B4%5D">[4]</a>, have been disastrous both strategically and fiscally. It has made the United States less prosperous, less secure and less free. Unfortunately, the militarism and the promiscuous intervention it gives rise to are only likely to abate when the Treasury is exhausted, just as it happened to the Dutch Republic and the British Empire.</p>
<p>	<strong>3. Give me that old time religion.</strong> Pandering to fundamentalism is a full-time vocation in the GOP. Beginning in the 1970s, religious cranks ceased simply to be a minor public nuisance in this country and grew into the major element of the Republican rank and file. Pat Robertson's strong showing in the 1988 Iowa Caucus signaled the gradual merger of politics and religion in the party. The results are all around us: if the American people poll more like Iranians or Nigerians than Europeans or Canadians on questions of evolution versus creationism, scriptural inerrancy, the existence of angels and demons, and so forth, that result is due to the rise of the religious right, its insertion into the public sphere by the Republican Party and the consequent normalizing of formerly reactionary or quaint beliefs. Also around us is a prevailing anti-intellectualism and hostility to science; it is this group that defines “low-information voter” – or, perhaps, “misinformation voter.”</p>
<p>
	The Constitution to the contrary notwithstanding, there is now a de facto religious test for the presidency: major candidates are encouraged (or coerced) to “share their feelings” about their “faith” in a revelatory speech; or, some televangelist like Rick Warren dragoons the candidates (as he did with Obama and McCain in 2008) to debate the finer points of Christology, with Warren himself, of course, as the arbiter. Politicized religion is also the sheet anchor of the culture wars. But how did the whole toxic stew of GOP beliefs – economic royalism, militarism and culture wars cum fundamentalism – come completely to displace an erstwhile civilized Eisenhower Republicanism?</p>
<p>	It is my view that the rise of politicized religious fundamentalism (which is a subset of the decline of rational problem solving in America) may have been the key ingredient of the takeover of the Republican Party. For politicized religion provides a substrate of beliefs that rationalizes – at least in the minds of followers – all three of the GOP's main tenets.</p>
<p>
	Televangelists have long espoused the health-and-wealth/name-it-and-claim it gospel. If you are wealthy, it is a sign of God's favor. If not, too bad! But don't forget to tithe in any case. This rationale may explain why some economically downscale whites defend the prerogatives of billionaires.</p>
<p>
	The GOP's fascination with war is also connected with the fundamentalist mindset. The Old Testament abounds in tales of slaughter – God ordering the killing of the Midianite male infants and enslavement of the balance of the population, the divinely-inspired genocide of the Canaanites, the slaying of various miscreants with the jawbone of an ass – and since American religious fundamentalist seem to prefer the Old Testament to the New (particularly that portion of the New Testament known as the Sermon on the Mount), it is but a short step to approving war as a divinely inspired mission. This sort of thinking has led, inexorably, to such phenomena as Jerry Falwell once writing that <a href="https://www.wnd.com/news/article.asp?ARTICLE_ID=36859">God is Pro-War</a>.</p>
<p>
	It is the apocalyptic frame of reference of fundamentalists, their belief in an imminent Armageddon, that psychologically conditions them to steer this country into conflict, not only on foreign fields (some evangelicals thought Saddam was the Antichrist and therefore a suitable target for cruise missiles), but also in the realm of domestic political controversy. It is hardly surprising that the most adamant proponent of the view that there was no debt ceiling problem was Michele Bachmann, the darling of the fundamentalist right. What does it matter, anyway, if the country defaults? – we shall presently abide in the bosom of the Lord.</p>
<p>
	Some liberal writers have opined that the different socio-economic perspectives separating the “business” wing of the GOP and the religious right make it an unstable coalition that could crack. I am not so sure. There is no fundamental disagreement on which direction the two factions want to take the country, merely how far in that direction they want to take it. The plutocrats would drag us back to the Gilded Age, the theocrats to the Salem witch trials. In any case, those consummate plutocrats, the Koch brothers, are <a href="https://motherjones.com/mojo/2011/07/michele-bachmann-koch-brothers-2012">pumping</a> large sums of money into Michele Bachman's presidential campaign, so one ought not make too much of a potential plutocrat-theocrat split.</p>
<p>
	Thus, the modern GOP; it hardly seems conceivable that a Republican could have written the following:</p>
<blockquote>
<p>
		“Should any political party attempt to abolish social security, unemployment insurance and eliminate labor laws and farm programs, you would not hear of that party again in our political history. There is a tiny splinter group, of course, that believes you can do these things. Among them are H. L. Hunt (you possibly know his background), a few other Texas oil millionaires and an occasional politician or business man from other areas. Their number is negligible and they are stupid.” (That was President Eisenhower, writing to his brother Edgar in 1954.)</p>
</blockquote>
<p>
	It is this broad and ever-widening gulf between the traditional Republicanism of an Eisenhower and the quasi-totalitarian cult of a Michele Bachmann that impelled my departure from Capitol Hill. It is not in my pragmatic nature to make a heroic gesture of self-immolation, or to make lurid revelations of personal martyrdom in the manner of <a href="https://www.amazon.com/Blinded-Right-Ex-Conservative-David-Brock/dp/1400047285/ref=sr_1_1?s=books&amp;ie=UTF8&amp;qid=1312417920&amp;sr=1-1">David Brock</a>. And I will leave a more detailed dissection of failed Republican economic policies to my fellow apostate <a href="https://www.amazon.com/New-American-Economy-Failure-Reaganomics/dp/0230615872/ref=sr_1_1?s=books&amp;ie=UTF8&amp;qid=1312418383&amp;sr=1-1">Bruce Bartlett</a>.</p>
<p>	I left because I was appalled at the headlong rush of Republicans, like Gadarene swine, to embrace policies that are deeply damaging to this country's future; and contemptuous of the feckless, craven incompetence of Democrats in their half-hearted attempts to stop them. And, in truth, I left as an act of rational self-interest. Having gutted private-sector pensions and health benefits as a result of their embrace of outsourcing, union busting and “shareholder value,” the GOP now thinks it is only fair that public-sector workers give up their pensions and benefits, too. Hence the intensification of the GOP's decades-long campaign of scorn against government workers. Under the circumstances, it is simply safer to be a current retiree rather than a prospective one.</p>
<p>	If you think Paul Ryan and his Ayn Rand-worshipping colleagues aren't after your Social Security and Medicare, I am here to disabuse you of your naiveté.<a href="#%5B5%5D">[5]</a> They will move heaven and earth to force through tax cuts that will so starve the government of revenue that they will be “forced” to make “hard choices” – and that doesn't mean repealing those very same tax cuts, it means cutting the benefits for which you worked.</p>
<p>	During the week that this piece was written, the debt ceiling fiasco reached its conclusion. The economy was already weak, but the GOP's disgraceful game of chicken roiled the markets even further. Foreigners could hardly believe it: Americans' own crazy political actions were destabilizing the safe-haven status of the dollar. Accordingly, during that same week, over one trillion dollars worth of assets evaporated on financial markets. Russia and China have stepped up their advocating that the dollar be replaced as the global reserve currency – a move as consequential and disastrous for US interests as any that can be imagined.</p>
<p>	If Republicans have perfected a new form of politics that is successful electorally at the same time that it unleashes major policy disasters, it means twilight both for the democratic process and America's status as the world's leading power.</p>
<p>
	Footnotes:</p>
<p>	<a name="%5B1%5D"></a>[1] I am not exaggerating for effect. A law passed in 2010 by the Arizona legislature mandating arrest and incarceration of suspected illegal aliens was actually drafted by the American Legislative Exchange Council, a conservative business front group that drafts “model” legislation on behalf of its corporate sponsors. The draft legislation in question was written for the private prison lobby, which sensed a growth opportunity in imprisoning more people.</p>
<p>	<a name="%5B2%5D"></a>[2] I am <em>not</em> a supporter of Obama and object to a number of his foreign and domestic policies. But when he took office amid the greatest financial collapse in 80 years, I wanted him to succeed, so that the country I served did not fail. But already in 2009, Mitch McConnell, the Senate Republican leader, declared that his greatest legislative priority was – jobs for Americans? Rescuing the financial system? Solving the housing collapse? – no, none of those things. His top priority was to ensure that Obama should be a one-term president. Evidently Senator McConnell hates Obama more than he loves his country. Note that the mainstream media have lately been hailing McConnell as “the adult in the room,” presumably because he is less visibly unstable than the Tea Party freshmen</p>
<p>	<a name="%5B3%5D"></a>[3] This is not a venue for immigrant bashing. It remains a fact that outsourcing jobs overseas, while insourcing sub-minimum wage immigrant labor, will exert downward pressure on US wages. The consequence will be popular anger, and failure to address that anger will result in a downward wage spiral and a breech of the social compact, not to mention a rise in nativism and other reactionary impulses. It does no good to claim that these economic consequences are an inevitable result of globalization; Germany has somehow managed to maintain a high-wage economy and a vigorous industrial base.</p>
<p>	<a name="%5B4%5D"></a>[4] The cowardice is not merely political. During the past ten years, I have observed that Democrats are actually growing afraid of Republicans. In a quirky and flawed, but insightful, little book, “<a href="https://www.amazon.com/Democracy-Populism-Hatred-John-Lukacs/dp/0300107730/ref=sr_1_1?s=books&amp;ie=UTF8&amp;qid=1312415333&amp;sr=1-1">Democracy and Populism: Fear and Hatred</a>,” John Lukacs concludes that the left fears, the right hates.</p>
<p>	<a name="%5B5%5D"></a>[5] The GOP cult of Ayn Rand is both revealing and mystifying. On the one hand, Rand's tough guy, every-man-for-himself posturing is a natural fit because it puts a philosophical gloss on the latent sociopathy so prevalent among the hard right. On the other, Rand exclaimed at every opportunity that she was a militant atheist who felt nothing but contempt for Christianity. Apparently, the ignorance of most fundamentalist “values voters” means that GOP candidates who enthuse over Rand at the same time they thump their Bibles never have to explain this stark contradiction. And I imagine a Democratic officeholder would have a harder time explaining why he named his offspring “Marx” than a GOP incumbent would in rationalizing naming his kid “Rand.”</p>
</div>

<div class="truth-post-content-after" id="truth-1889539488"><div class="callout inline-callout p-4 mb-5 callout-- callout--white" id="truth-331649" data-callout-id="331649" data-callout-theme="white" data-callout-placement="Post Content - After" data-callout-title="2025-09 Main Campaign (FRU) Support media that fights fascism">
<div class="p-2 text-start">
<h5 class="pb-2" style="text-transform: uppercase; font-family: var(--bs-font-sans-serif); text-align: center;">Support media that fights fascism</h5>
<p class="mb-3" style="text-align: left;"><span style="font-weight: 400;">Truthout is funded almost entirely by readers — that’s why we can speak truth to power, cut against the mainstream narrative and uplift the movements resisting fascism.</span></p>
<p class="mb-3" style="text-align: left;"><span style="font-weight: 400;">But independent journalists at Truthout face mounting political suppression under Trump.</span></p>
<p class="mb-3" style="text-align: left;"><span style="font-weight: 400;"><strong>To combat these challenges, Truthout has launched a fundraiser to raise $50,000 in the next 10 days. </strong>Please support independent journalism at this critical moment.</span></p>
<p class="m-0" style="text-align: center;"><a href="#XEGQPXGY" style="display: none;"></a></p>
</div>
</div></div></body></html>

    <aside class="ar__share border-bottom--gray d-block d-lg-none mb-5 pt-1 pb-3 px-0" aria-label="Share article">
      <div class="social sticky-top pt-0">
    <div class="meta-label visually-hidden">
      Share
    </div>

<ul class="social__btns nav social__btn--ar flex-row justify-content-between">



                  <li class="d-flex justify-content-center my-4">
                          <a
  class="social__btn social__fb d-flex justify-content-center" href="https://www.facebook.com/sharer/sharer.php?t=Goodbye%20to%20All%20That%3A%20Reflections%20of%20a%20GOP%20Operative%20Who%20Left%20the%20Cult&u=https%3A%2F%2Ftruthout.org%2Farticles%2Fgoodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult%2F%3Futm_campaign%3DTruthout%2BShare%2BButtons"
  target="_top"
  rel="nofollow"
  >

<span class="social__ti visually-hidden">Share via Facebook</span>

<svg aria-hidden="true" class="social__icon" version="1.1" role="img" focusable="false" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 x="0px" y="0px" viewBox="0 0 403.2 403.2" style="enable-background:new 0 0 403.2 403.2;" xml:space="preserve"><title>Facebook Circle Icon</title>
<path fill="currentColor" d="M201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S312.9,0,201.6,0z M174.8,310.3L174.8,310.3
	V222h-36.5v-41.5h36.5v-31.7c0-36,21.4-55.9,54.3-55.9c15.7,0,32.2,2.8,32.2,2.8v35.3h-18.1c-17.9,0-23.4,11.1-23.4,22.4v27h39.8
	l-6.4,41.5h-33.5v88.2l0,0"/>
</svg>
</a>                      </li>

                  <li class="d-flex justify-content-center my-4">
                          <a
  class="social__btn social__bsky d-flex justify-content-center" href="https://bsky.app/intent/compose?text=Goodbye%20to%20All%20That%3A%20Reflections%20of%20a%20GOP%20Operative%20Who%20Left%20the%20Cult https%3A%2F%2Ftruthout.org%2Farticles%2Fgoodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult%2F%3Futm_campaign%3DTruthout%2BShare%2BButtons"
  target="_top"
  rel="nofollow"
  >

<span class="social__ti visually-hidden">Share via Bluesky</span>

<svg aria-hidden="true" class="social__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 403.2 403.2"><title>Bluesky Circle Icon</title><defs><style>.cls-1{stroke-width:0px;}</style></defs><g id="Layer_1" focusable="false"><path fill="currentColor" class="cls-1" d="m201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6,201.6-90.3,201.6-201.6S312.9,0,201.6,0Zm126.12,198.07c-9.35,33.42-43.43,41.94-73.74,36.79,52.99,9.02,66.47,38.89,37.36,68.76-55.29,56.73-79.46-14.23-85.66-32.42-1.14-3.33-1.67-4.89-1.67-3.57,0-1.33-.54.23-1.67,3.57-6.19,18.18-30.37,89.15-85.66,32.42-29.11-29.87-15.63-59.75,37.36-68.76-30.31,5.16-64.39-3.36-73.74-36.79-2.69-9.61-7.28-68.82-7.28-76.82,0-40.06,35.12-27.47,56.79-11.2h0c30.04,22.55,62.35,68.27,74.21,92.81,11.86-24.54,44.17-70.26,74.21-92.81,21.67-16.27,56.79-28.86,56.79,11.2,0,8-4.59,67.21-7.28,76.82Z"/></g></svg>
</a>                      </li>

                  <li class="d-flex justify-content-center my-4">
                          <a
  class="social__btn social__flip d-flex justify-content-center" href="https://flipboard.com"
  target="_top"
  rel="nofollow"
      data-flip-widget="shareflip"
  >

<span class="social__ti visually-hidden">Share via Flipboard</span>

<svg aria-hidden="true" class="social__icon" version="1.1" role="img" focusable="false" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 x="0px" y="0px" viewBox="0 0 403.2 403.2" style="enable-background:new 0 0 403.2 403.2;" xml:space="preserve"><title>Flipboard Circle Icon</title>
<path fill="currentColor" d="M201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S312.9,0,201.6,0z M294.1,180.8h-60.9v60.9
	h-60.9v60.9h-60.9V119.9h182.6V180.8z"/>
</svg>
</a>                      </li>

                  <li class="d-flex justify-content-center my-4">
                          <a class="social__btn social__em d-flex justify-content-center" href="/cdn-cgi/l/email-protection#7c430f091e16191f08413b1313181e0519594e4c0813594e4c3d1010594e4c28141d08594f3d594e4c2e191a10191f081513120f594e4c131a594e4c1d594e4c3b332c594e4c330c190e1d08150a19594e4c2b1413594e4c30191a08594e4c081419594e4c3f0910085a1e131805411408080c0f594f3d594e3a594e3a080e09081413090852130e1b594e3a1d0e08151f10190f594e3a1b1313181e0519510813511d10105108141d08510e191a10191f081513120f51131a511d511b130c51130c190e1d08150a19510b14135110191a0851081419511f091008594e3a594f3a090811231f1d110c1d151b12594f38280e090814130908594e3e2f141d0e19594e3e3e09080813120f" target="_top" rel="nofollow">

<span class="social__ti visually-hidden">Share via Mail</span>

<svg aria-hidden="true" class="social__icon" version="1.1" role="img" focusable="false" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 x="0px" y="0px" viewBox="0 0 403.2 403.2" style="enable-background:new 0 0 403.2 403.2;" xml:space="preserve"><title>Mail Circle Icon</title>
<path fill="currentColor" d="M201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S312.9,0,201.6,0z M317.9,252.5
	c0,12.8-10.4,23.3-23.3,23.3H108.5c-12.8,0-23.3-10.4-23.3-23.3v-80L186,222.9c4.9,2.4,10.2,3.7,15.6,3.7s10.7-1.2,15.6-3.7
	l100.7-50.3V252.5z M317.9,160.9l-111.1,55.5c-3.3,1.6-7.1,1.6-10.4,0L85.3,160.9v-10.2c0-12.8,10.4-23.3,23.3-23.3h186.1
	c12.8,0,23.3,10.4,23.3,23.3V160.9z"/>
</svg>
</a>                      </li>

                  <li class="d-flex justify-content-center my-4">
                          <button
  class="social__btn social__prnt social__btn--b d-flex justify-content-center" href=""
  target="_top"
  rel="nofollow"
  >

<span class="social__ti visually-hidden">Share via Print</span>

<svg aria-hidden="true" class="social__icon" version="1.1" id="Layer_2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 403.2 403.2" style="enable-background:new 0 0 403.2 403.2;" xml:space="preserve">
<g>
	<polygon fill="currentColor" points="134.5,260.3 134.5,268.7 134.5,302.3 268.7,302.3 268.7,268.7 268.7,251.9 134.5,251.9 	"/>
	<circle cx="293.9" cy="210" r="12.6"/>
	<path fill="currentColor" d="M201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S312.9,0,201.6,0z M100.9,100.9
		c0-18.5,15.1-33.6,33.6-33.6h118.9c8.9,0,17.5,3.5,23.8,9.8l15.4,15.4c6.3,6.3,9.8,14.8,9.8,23.8v35h-33.6v-35l-15.4-15.4H134.5
		v50.3h-33.6V100.9z M335.9,251.9c0,9.3-7.5,16.8-16.8,16.8h-16.8v33.6c0,18.5-15.1,33.6-33.6,33.6H134.5
		c-18.5,0-33.6-15.1-33.6-33.6v-33.6H84.1c-9.3,0-16.8-7.5-16.8-16.8v-50.3c0-18.5,15.1-33.6,33.6-33.6h201.4
		c18.5,0,33.6,15.1,33.6,33.6V251.9z"/>
</g>
</svg>
</button>                      </li>


                                                  <li class="social__btns__drop d-flex justify-content-center my-4 dropdown">
                <button
                  class="social__btn social__btn--b social__mr dropdown-toggle d-flex"
                  id="socialMrBtn"
                  type="button"
                  aria-haspopup="true"
                  aria-expanded="false"
                  data-bs-toggle="dropdown"
                >
                  <span class="social__ti visually-hidden">More</span>
                  <svg aria-hidden="true" class="social__icon" version="1.1" id="ellipsesCircleIcon" focusable="false" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 x="0px" y="0px" viewBox="0 0 403.2 403.2" style="enable-background:new 0 0 403.2 403.2;" xml:space="preserve">
<style type="text/css">
	.st0{fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:round;stroke-linejoin:round;}
</style>
<g id="XMLID_00000174564128502558812610000000387774599914555028_">
	<g>
		<path fill="currentColor" d="M98.5,242.8c22.8,0,41.2-18.5,41.2-41.2s-18.5-41.2-41.2-41.2c-22.8,0-41.2,18.5-41.2,41.2S75.7,242.8,98.5,242.8z
			 M201,242.8c22.8,0,41.2-18.5,41.2-41.2s-18.5-41.2-41.2-41.2c-22.8,0-41.2,18.5-41.2,41.2S178.2,242.8,201,242.8z M304.7,242.8
			c22.8,0,41.2-18.5,41.2-41.2s-18.5-41.2-41.2-41.2c-22.8,0-41.2,18.5-41.2,41.2S281.9,242.8,304.7,242.8z M201.6,0
			c111.3,0,201.6,90.3,201.6,201.6s-90.3,201.6-201.6,201.6S0,312.9,0,201.6S90.3,0,201.6,0z"/>
	</g>
	<g>
		<circle class="st0" cx="98.5" cy="201.6" r="41.2"/>
		<circle class="st0" cx="201" cy="201.6" r="41.2"/>
		<circle class="st0" cx="304.7" cy="201.6" r="41.2"/>
	</g>
</g>
</svg>                </button>
                <ul class="dropdown-menu mt-3" aria-labelledby="socialMrBtn">

          <li class="d-flex justify-content-center my-4 dropdown-item px-0">
            <a
  class="social__btn social__thd d-flex justify-content-center" href="https://www.threads.net/intent/post?text=Goodbye%20to%20All%20That%3A%20Reflections%20of%20a%20GOP%20Operative%20Who%20Left%20the%20Cult https%3A%2F%2Ftruthout.org%2Farticles%2Fgoodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult%2F%3Futm_campaign%3DTruthout%2BShare%2BButtons"
  target="_top"
  rel="nofollow"
  >

<span class="social__ti visually-hidden">Share via Threads</span>

<svg aria-hidden="true" class="social__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 403.2 403.2"><defs><style>.cls-1{stroke-width:0px;}</style></defs><g id="Layer_1" focusable="false"><path fill="currentColor" class="cls-1" d="m201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6,201.6-90.3,201.6-201.6S312.9,0,201.6,0Zm-72.31,284.74c16.27,20.68,41.29,31.29,74.38,31.54,29.83-.22,49.56-7.31,65.98-23.72,18.74-18.72,18.39-41.69,12.4-55.67-3.52-8.22-9.91-15.06-18.52-20.26-2.1,15.63-6.85,28.04-14.36,37.61-9.89,12.61-24.07,19.5-42.14,20.49-13.68.75-26.85-2.55-37.07-9.3-12.09-7.98-19.17-20.2-19.92-34.4-1.49-28,20.72-48.15,55.27-50.14,12.27-.7,23.74-.15,34.35,1.65-1.41-8.61-4.25-15.44-8.51-20.38-5.84-6.78-14.87-10.26-26.84-10.34-.11,0-.22,0-.33,0-9.61,0-22.65,2.69-30.97,15.3l-19.99-13.71c11.13-16.88,29.21-26.16,50.94-26.16.16,0,.33,0,.49,0,36.34.23,57.98,22.91,60.13,62.52,1.23.53,2.45,1.08,3.65,1.66,16.96,8.13,29.36,20.45,35.86,35.61,9.07,21.15,9.89,55.59-17.61,83.07-21.02,21.01-46.54,30.48-82.75,30.74h-.16c-40.72-.28-72.04-13.99-93.08-40.73-18.72-23.8-28.38-56.91-28.7-98.42v-.1s0-.1,0-.1c.32-41.51,9.98-74.62,28.7-98.42,21.04-26.74,52.35-40.45,93.08-40.73h.16c40.81.28,72.48,13.93,94.13,40.58,10.68,13.14,18.54,28.99,23.53,47.39l-23.42,6.25c-4.12-14.94-10.36-27.76-18.64-37.95-16.89-20.78-42.35-31.44-75.67-31.69-33.09.25-58.11,10.86-74.38,31.54-15.23,19.37-23.11,47.34-23.4,83.14.29,35.8,8.17,63.77,23.4,83.14Z"/><path class="cls-1" d="m206.66,205.42c-24.9,1.43-33.16,13.48-32.58,24.27.78,14.56,16.51,21.36,31.65,20.5,14.83-.81,31.66-6.63,34.52-42.46-7.69-1.68-16.15-2.56-25.2-2.56-2.75,0-5.55.08-8.4.24Z"/></g></svg>
</a>          </li>




          <li class="d-flex justify-content-center my-4 dropdown-item px-0">
            <a
  class="social__btn social__red d-flex justify-content-center" href="http://www.reddit.com/submit?title=Goodbye%20to%20All%20That%3A%20Reflections%20of%20a%20GOP%20Operative%20Who%20Left%20the%20Cult&url=https%3A%2F%2Ftruthout.org%2Farticles%2Fgoodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult%2F%3Futm_campaign%3DTruthout%2BShare%2BButtons"
  target="_top"
  rel="nofollow"
  >

<span class="social__ti visually-hidden">Share via Reddit</span>

<svg aria-hidden="true" class="social__icon" version="1.1" role="img" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 404.2 404.2" style="enable-background:new 0 0 404.2 404.2;" xml:space="preserve"><title>Reddit Cirlce Icon</title>
<path fill="currentColor" d="M175.6,221.8c0.1-11.8-9.5-21.5-21.3-21.5c-11.8-0.1-21.5,9.5-21.5,21.3c-0.1,11.8,9.5,21.5,21.3,21.5c0.1,0,0.2,0,0.2,0
	C166.1,243.1,175.6,233.5,175.6,221.8z"/>
<path fill="currentColor" d="M241.8,265c-15.7,15.8-65.7,15.4-80.8,0c-2-1.9-5.2-1.9-7.1,0c-2,1.9-2.2,5-0.3,7.1c0.1,0.1,0.2,0.2,0.3,0.3
	c19.8,19.8,75.5,19.7,95.1,0c2-1.9,2.2-5,0.3-7.1c-0.1-0.1-0.2-0.2-0.3-0.3C246.9,263.2,243.8,263.2,241.8,265z"/>
<path fill="currentColor" d="M248.5,200.3c-11.8,0.1-21.4,9.7-21.3,21.5s9.7,21.4,21.5,21.3c11.7-0.1,21.2-9.6,21.3-21.3c0.1-11.8-9.4-21.5-21.2-21.5
	C248.7,200.3,248.6,200.3,248.5,200.3z"/>
<path fill="currentColor" d="M202.1,0.5C90.8,0.5,0.5,90.8,0.5,202.1s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S313.4,0.5,202.1,0.5z M314.3,218.7
	c1.2,4.5,1.7,9.1,1.7,13.7c0,45.4-51.2,82.2-114.3,82.2c-62.9,0-114-36.8-114-82.2c0-4.5,0.5-9,1.4-13.4
	c-27.6-13.7-17.7-54.2,12.4-54.2c7.9,0,15.4,3.2,20.8,8.8c19.4-13.4,45.2-22,73.9-23.2l16.5-74.6c0.7-2.7,3.3-4.6,5.9-3.9l52.8,11.7
	c5.3-10.6,18.2-14.9,28.8-9.6s14.9,18.2,9.6,28.8c-3.7,7.3-11.1,11.9-19.3,11.8c-11.8,0-21.3-9.5-21.3-21.3l-47.8-10.8l-15,67.7
	c28.9,1,55,9.6,74.3,23c5.4-5.5,12.9-8.6,20.6-8.6C331.3,164.7,341.3,204.8,314.3,218.7z"/>
</svg>
</a>          </li>




          <li class="d-flex justify-content-center my-4 dropdown-item px-0">
            <a
  class="social__btn social__pct d-flex justify-content-center" href="https://getpocket.com/save?title=Goodbye%20to%20All%20That%3A%20Reflections%20of%20a%20GOP%20Operative%20Who%20Left%20the%20Cult&url=https%3A%2F%2Ftruthout.org%2Farticles%2Fgoodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult%2F%3Futm_campaign%3DTruthout%2BShare%2BButtons"
  target="_top"
  rel="nofollow"
  >

<span class="social__ti visually-hidden">Share via Pocket</span>

<svg aria-hidden="true" class="social__icon" role="img" data-name="Pocket Circle Icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 403.2 403.2"><title>Pocket Circle Icon</title><path fill="currentColor" d="M202.1.5C90.8.5.5,90.8.5,202.1S90.8,403.7,202.1,403.7s201.6-90.3,201.6-201.6S313.4.5,202.1.5ZM324.91,206a122.62,122.62,0,1,1-245.24,0V132a22.46,22.46,0,0,1,22.23-22.23H302.8A22,22,0,0,1,324.91,132Z" transform="translate(-0.5 -0.5)"/><path fill="currentColor" d="M260.15,172.49c-9.25,0-8.15,1.31-57.75,48.88-48.77-46.8-48.28-48.88-57.59-48.88a16.84,16.84,0,0,0-16.8,16.8c0,9.91.65,7.83,62.9,67.44a16.66,16.66,0,0,0,23.21,0C275.37,197.89,277,199,277,189.29A16.85,16.85,0,0,0,260.15,172.49Z" transform="translate(-0.5 -0.5)"/></svg>
</a>          </li>




          <li class="d-flex justify-content-center my-4 dropdown-item px-0">
            <a
  class="social__btn social__lin d-flex justify-content-center" href="http://www.linkedin.com/shareArticle?mini=true&title=Goodbye%20to%20All%20That%3A%20Reflections%20of%20a%20GOP%20Operative%20Who%20Left%20the%20Cult&url=https%3A%2F%2Ftruthout.org%2Farticles%2Fgoodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult%2F%3Futm_campaign%3DTruthout%2BShare%2BButtons&summary=&source=%3Cp%3E%28Photo%3A%20Carolyn%20Tiry%20%2F%20Flickr%29%20%20%20Barbara%20Stanwyck%3A%20%22We%26%23039%3Bre%20both%20rotten%21%22%20%20%20Fred%20MacMurray%3A%20%22Yeah%20-%20only%20you%26%23039%3Bre%20a%20little%20more%20rotten.%22%20-%22Double%20Indemnity%22%20%281944%29%3C%2Fp%3E"
  target="_top"
  rel="nofollow"
  >

<span class="social__ti visually-hidden">Share via Linkedin</span>

<svg aria-hidden="true" class="social__icon" role="img" data-name="LinkedIn Circle Icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 404.2 404.2"><title>LinkedIn Circle Icon</title><defs><style>.cls-1{stroke:#000;stroke-miterlimit:10;}</style></defs><path fill="currentColor" class="cls-1" d="M201.6,0C90.3,0,0,90.3,0,201.6S90.3,403.2,201.6,403.2s201.6-90.3,201.6-201.6S312.9,0,201.6,0ZM142.37,302.07H97.91V158.88h44.46ZM120.11,139.35a25.87,25.87,0,1,1,25.76-26A26,26,0,0,1,120.11,139.35ZM308.84,302.07H264.42v-69.7c0-16.62-.34-37.92-23.12-37.92-23.12,0-26.66,18.05-26.66,36.72v70.9H170.22V158.88h42.65v19.53h.62c5.94-11.25,20.44-23.12,42.07-23.12,45,0,53.28,29.63,53.28,68.12Z" transform="translate(0.5 0.5)"/></svg>
</a>          </li>




          <li class="d-flex justify-content-center my-4 dropdown-item px-0">
            <a
  class="social__btn social__tw d-flex justify-content-center" href="https://twitter.com/intent/tweet?text=Goodbye%20to%20All%20That%3A%20Reflections%20of%20a%20GOP%20Operative%20Who%20Left%20the%20Cult&url=https%3A%2F%2Ftruthout.org%2Farticles%2Fgoodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult%2F%3Futm_campaign%3DTruthout%2BShare%2BButtons&via=truthout"
  target="_top"
  rel="nofollow"
  >

<span class="social__ti visually-hidden">Share via Twitter</span>

<svg aria-hidden="true" class="social__icon" version="1.1" role="img" focusable="false" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 x="0px" y="0px" viewBox="0 0 403.2 403.2" style="enable-background:new 0 0 403.2 403.2;" xml:space="preserve"><title>Twitter Circle Icon</title>
<path fill="currentColor" d="M201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S312.9,0,201.6,0z M302,161.5
	c0.1,2,0.1,4.1,0.1,6.1c0,62.5-47.6,134.5-134.5,134.5c-26.8,0-51.7-7.8-72.6-21.2c3.8,0.4,7.5,0.6,11.4,0.6
	c22.1,0,42.5-7.5,58.7-20.2c-20.8-0.4-38.2-14.1-44.2-32.8c7.3,1.1,13.8,1.1,21.3-0.9c-21.6-4.4-37.8-23.4-37.8-46.4v-0.6
	c6.3,3.5,13.6,5.7,21.3,6c-13.2-8.8-21.1-23.5-21.1-39.4c0-8.8,2.3-16.9,6.4-23.9c23.3,28.7,58.3,47.4,97.5,49.5
	c-6.7-32.1,17.3-58.1,46.1-58.1c13.6,0,25.9,5.7,34.5,14.9c10.7-2,20.9-6,30-11.4c-3.5,11-11,20.2-20.8,26c9.5-1,18.7-3.7,27.3-7.4
	C319.3,146.4,311.2,154.8,302,161.5z"/>
</svg>
</a>          </li>

                        </ul>
            </li>
                            </ul>
  </div>
    </aside>

<aside class="ar__authors vcard mt-4 border-top--gray" aria-label="Author">

<div class="ar__author vcard meta-data no-img flex-wrap flex-md-nowrap row position-relative pt-4" itemprop="author" itemscope itemtype="https://schema.org/Person">

<figure class="ar__author__fig col-4 offset-sm-4 col-md-2 offset-md-0 ms-2 p-0">
            <img class="article-thumbnail img-fluid cover" src="https://truthout.org/app/uploads/2018/03/Truthout-Default-Image-1200x900.png" alt="Truthout Logo" loading="lazy">
          </figure>
          <div class="ar__author__con col-12 col-md-10 ps-md-4">

<div class="ar__author__name text-uppercase font-sans">
            <a href="https://truthout.org/authors/mike-lofgren/" itemprop="url"><span itemprop="name">Mike Lofgren</span></a>
          </div>

<div class="ar__author__description" itemprop="description">
            <p>Mike Lofgren is a former congressional staff member and the author of <a href="https://www.amazon.com/Party-Over-Republicans-Democrats-Useless/dp/0670026263/ref=tmm_hrd_swatch_0?_encoding=UTF8&amp;qid=&amp;sr="><em>The Party is Over: How Republicans Went Crazy, Democrats Became Useless, and the Middle Class Got Shafted</em></a> and <em><a href="https://www.amazon.com/Deep-State-Constitution-Shadow-Government/dp/0143109936/ref=sr_1_1?crid=1SWFGCMONDHKI&amp;keywords=the+deep+state+mike+lofgren&amp;qid=1553173945&amp;s=books&amp;sprefix=Lofgren+dee%2Cstripbooks%2C132&amp;sr=1-1-catcorr">The Deep State: The Fall of the Constitution and the Rise of a Shadow Government</a>.</em></p>

</div>

</div>

</div>

</aside>

<div class="d-none" itemprop="publisher" itemscope itemtype="http://schema.org/Organization">
  <a href="https://truthout.org" itemprop="url">
    <span itemprop="name">
      Truthout
    </span>
  </a>
</div>

</div>

<aside class="ar__share order-1 d-none d-lg-block" aria-label="Share article">
    <div class="social sticky-top pt-3">
    <div class="meta-label visually-hidden">
      Share
    </div>

<ul class="social__btns nav flex-column">



                  <li class="mb-4 mt-1">
                          <a
  class="social__btn social__fb d-flex justify-content-center" href="https://www.facebook.com/sharer/sharer.php?t=Goodbye%20to%20All%20That%3A%20Reflections%20of%20a%20GOP%20Operative%20Who%20Left%20the%20Cult&u=https%3A%2F%2Ftruthout.org%2Farticles%2Fgoodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult%2F%3Futm_campaign%3DTruthout%2BShare%2BButtons"
  target="_top"
  rel="nofollow"
  >

<span class="social__ti visually-hidden">Share via Facebook</span>

<svg aria-hidden="true" class="social__icon" version="1.1" role="img" focusable="false" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 x="0px" y="0px" viewBox="0 0 403.2 403.2" style="enable-background:new 0 0 403.2 403.2;" xml:space="preserve"><title>Facebook Circle Icon</title>
<path fill="currentColor" d="M201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S312.9,0,201.6,0z M174.8,310.3L174.8,310.3
	V222h-36.5v-41.5h36.5v-31.7c0-36,21.4-55.9,54.3-55.9c15.7,0,32.2,2.8,32.2,2.8v35.3h-18.1c-17.9,0-23.4,11.1-23.4,22.4v27h39.8
	l-6.4,41.5h-33.5v88.2l0,0"/>
</svg>
</a>                      </li>

                  <li class="mb-4 mt-1">
                          <a
  class="social__btn social__bsky d-flex justify-content-center" href="https://bsky.app/intent/compose?text=Goodbye%20to%20All%20That%3A%20Reflections%20of%20a%20GOP%20Operative%20Who%20Left%20the%20Cult https%3A%2F%2Ftruthout.org%2Farticles%2Fgoodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult%2F%3Futm_campaign%3DTruthout%2BShare%2BButtons"
  target="_top"
  rel="nofollow"
  >

<span class="social__ti visually-hidden">Share via Bluesky</span>

<svg aria-hidden="true" class="social__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 403.2 403.2"><title>Bluesky Circle Icon</title><defs><style>.cls-1{stroke-width:0px;}</style></defs><g id="Layer_1" focusable="false"><path fill="currentColor" class="cls-1" d="m201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6,201.6-90.3,201.6-201.6S312.9,0,201.6,0Zm126.12,198.07c-9.35,33.42-43.43,41.94-73.74,36.79,52.99,9.02,66.47,38.89,37.36,68.76-55.29,56.73-79.46-14.23-85.66-32.42-1.14-3.33-1.67-4.89-1.67-3.57,0-1.33-.54.23-1.67,3.57-6.19,18.18-30.37,89.15-85.66,32.42-29.11-29.87-15.63-59.75,37.36-68.76-30.31,5.16-64.39-3.36-73.74-36.79-2.69-9.61-7.28-68.82-7.28-76.82,0-40.06,35.12-27.47,56.79-11.2h0c30.04,22.55,62.35,68.27,74.21,92.81,11.86-24.54,44.17-70.26,74.21-92.81,21.67-16.27,56.79-28.86,56.79,11.2,0,8-4.59,67.21-7.28,76.82Z"/></g></svg>
</a>                      </li>

                  <li class="mb-4 mt-1">
                          <a
  class="social__btn social__flip d-flex justify-content-center" href="https://flipboard.com"
  target="_top"
  rel="nofollow"
      data-flip-widget="shareflip"
  >

<span class="social__ti visually-hidden">Share via Flipboard</span>

<svg aria-hidden="true" class="social__icon" version="1.1" role="img" focusable="false" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 x="0px" y="0px" viewBox="0 0 403.2 403.2" style="enable-background:new 0 0 403.2 403.2;" xml:space="preserve"><title>Flipboard Circle Icon</title>
<path fill="currentColor" d="M201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S312.9,0,201.6,0z M294.1,180.8h-60.9v60.9
	h-60.9v60.9h-60.9V119.9h182.6V180.8z"/>
</svg>
</a>                      </li>

                  <li class="mb-4 mt-1">
                          <a class="social__btn social__em d-flex justify-content-center" href="/cdn-cgi/l/email-protection#efd09c9a8d858a8c9bd2a880808b8d968acadddf9b80cadddfae8383cadddfbb878e9bcadcaecadddfbd8a89838a8c9b8680819ccadddf8089cadddf8ecadddfa8a0bfcadddfa09f8a9d8e9b86998acadddfb88780cadddfa38a899bcadddf9b878acadddfac9a839bc98d808b96d2879b9b9f9ccadcaecadda9cadda99b9d9a9b87809a9bc1809d88cadda98e9d9b868c838a9ccadda98880808b8d968ac29b80c28e8383c29b878e9bc29d8a89838a8c9b8680819cc28089c28ec288809fc2809f8a9d8e9b86998ac2988780c2838a899bc29b878ac28c9a839bcadda9cadca99a9b82b08c8e829f8e868881cadcabbb9d9a9b87809a9bcaddadbc878e9d8acaddadad9a9b9b80819c" target="_top" rel="nofollow">

<span class="social__ti visually-hidden">Share via Mail</span>

<svg aria-hidden="true" class="social__icon" version="1.1" role="img" focusable="false" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 x="0px" y="0px" viewBox="0 0 403.2 403.2" style="enable-background:new 0 0 403.2 403.2;" xml:space="preserve"><title>Mail Circle Icon</title>
<path fill="currentColor" d="M201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S312.9,0,201.6,0z M317.9,252.5
	c0,12.8-10.4,23.3-23.3,23.3H108.5c-12.8,0-23.3-10.4-23.3-23.3v-80L186,222.9c4.9,2.4,10.2,3.7,15.6,3.7s10.7-1.2,15.6-3.7
	l100.7-50.3V252.5z M317.9,160.9l-111.1,55.5c-3.3,1.6-7.1,1.6-10.4,0L85.3,160.9v-10.2c0-12.8,10.4-23.3,23.3-23.3h186.1
	c12.8,0,23.3,10.4,23.3,23.3V160.9z"/>
</svg>
</a>                      </li>

                  <li class="mb-4 mt-1">
                          <button
  class="social__btn social__prnt social__btn--b d-flex justify-content-center" href=""
  target="_top"
  rel="nofollow"
  >

<span class="social__ti visually-hidden">Share via Print</span>

<svg aria-hidden="true" class="social__icon" version="1.1" id="Layer_2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 403.2 403.2" style="enable-background:new 0 0 403.2 403.2;" xml:space="preserve">
<g>
	<polygon fill="currentColor" points="134.5,260.3 134.5,268.7 134.5,302.3 268.7,302.3 268.7,268.7 268.7,251.9 134.5,251.9 	"/>
	<circle cx="293.9" cy="210" r="12.6"/>
	<path fill="currentColor" d="M201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S312.9,0,201.6,0z M100.9,100.9
		c0-18.5,15.1-33.6,33.6-33.6h118.9c8.9,0,17.5,3.5,23.8,9.8l15.4,15.4c6.3,6.3,9.8,14.8,9.8,23.8v35h-33.6v-35l-15.4-15.4H134.5
		v50.3h-33.6V100.9z M335.9,251.9c0,9.3-7.5,16.8-16.8,16.8h-16.8v33.6c0,18.5-15.1,33.6-33.6,33.6H134.5
		c-18.5,0-33.6-15.1-33.6-33.6v-33.6H84.1c-9.3,0-16.8-7.5-16.8-16.8v-50.3c0-18.5,15.1-33.6,33.6-33.6h201.4
		c18.5,0,33.6,15.1,33.6,33.6V251.9z"/>
</g>
</svg>
</button>                      </li>


                                                  <li class="social__btns__drop mb-4 mt-1 dropdown">
                <button
                  class="social__btn social__btn--b social__mr dropdown-toggle d-flex"
                  id="socialMrBtnSm"
                  type="button"
                  aria-haspopup="true"
                  aria-expanded="false"
                  data-bs-toggle="dropdown"
                >
                  <span class="social__ti visually-hidden">More</span>
                  <svg aria-hidden="true" class="social__icon" version="1.1" id="ellipsesCircleIcon" focusable="false" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 x="0px" y="0px" viewBox="0 0 403.2 403.2" style="enable-background:new 0 0 403.2 403.2;" xml:space="preserve">
<style type="text/css">
	.st0{fill:none;stroke:#000000;stroke-width:0.5;stroke-linecap:round;stroke-linejoin:round;}
</style>
<g id="XMLID_00000174564128502558812610000000387774599914555028_">
	<g>
		<path fill="currentColor" d="M98.5,242.8c22.8,0,41.2-18.5,41.2-41.2s-18.5-41.2-41.2-41.2c-22.8,0-41.2,18.5-41.2,41.2S75.7,242.8,98.5,242.8z
			 M201,242.8c22.8,0,41.2-18.5,41.2-41.2s-18.5-41.2-41.2-41.2c-22.8,0-41.2,18.5-41.2,41.2S178.2,242.8,201,242.8z M304.7,242.8
			c22.8,0,41.2-18.5,41.2-41.2s-18.5-41.2-41.2-41.2c-22.8,0-41.2,18.5-41.2,41.2S281.9,242.8,304.7,242.8z M201.6,0
			c111.3,0,201.6,90.3,201.6,201.6s-90.3,201.6-201.6,201.6S0,312.9,0,201.6S90.3,0,201.6,0z"/>
	</g>
	<g>
		<circle class="st0" cx="98.5" cy="201.6" r="41.2"/>
		<circle class="st0" cx="201" cy="201.6" r="41.2"/>
		<circle class="st0" cx="304.7" cy="201.6" r="41.2"/>
	</g>
</g>
</svg>                </button>
                <ul class="dropdown-menu mt-3" aria-labelledby="socialMrBtnSm">

          <li class="mb-4 mt-1 dropdown-item px-0 dropdown-item px-0">
            <a
  class="social__btn social__thd d-flex justify-content-center" href="https://www.threads.net/intent/post?text=Goodbye%20to%20All%20That%3A%20Reflections%20of%20a%20GOP%20Operative%20Who%20Left%20the%20Cult https%3A%2F%2Ftruthout.org%2Farticles%2Fgoodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult%2F%3Futm_campaign%3DTruthout%2BShare%2BButtons"
  target="_top"
  rel="nofollow"
  >

<span class="social__ti visually-hidden">Share via Threads</span>

<svg aria-hidden="true" class="social__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 403.2 403.2"><defs><style>.cls-1{stroke-width:0px;}</style></defs><g id="Layer_1" focusable="false"><path fill="currentColor" class="cls-1" d="m201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6,201.6-90.3,201.6-201.6S312.9,0,201.6,0Zm-72.31,284.74c16.27,20.68,41.29,31.29,74.38,31.54,29.83-.22,49.56-7.31,65.98-23.72,18.74-18.72,18.39-41.69,12.4-55.67-3.52-8.22-9.91-15.06-18.52-20.26-2.1,15.63-6.85,28.04-14.36,37.61-9.89,12.61-24.07,19.5-42.14,20.49-13.68.75-26.85-2.55-37.07-9.3-12.09-7.98-19.17-20.2-19.92-34.4-1.49-28,20.72-48.15,55.27-50.14,12.27-.7,23.74-.15,34.35,1.65-1.41-8.61-4.25-15.44-8.51-20.38-5.84-6.78-14.87-10.26-26.84-10.34-.11,0-.22,0-.33,0-9.61,0-22.65,2.69-30.97,15.3l-19.99-13.71c11.13-16.88,29.21-26.16,50.94-26.16.16,0,.33,0,.49,0,36.34.23,57.98,22.91,60.13,62.52,1.23.53,2.45,1.08,3.65,1.66,16.96,8.13,29.36,20.45,35.86,35.61,9.07,21.15,9.89,55.59-17.61,83.07-21.02,21.01-46.54,30.48-82.75,30.74h-.16c-40.72-.28-72.04-13.99-93.08-40.73-18.72-23.8-28.38-56.91-28.7-98.42v-.1s0-.1,0-.1c.32-41.51,9.98-74.62,28.7-98.42,21.04-26.74,52.35-40.45,93.08-40.73h.16c40.81.28,72.48,13.93,94.13,40.58,10.68,13.14,18.54,28.99,23.53,47.39l-23.42,6.25c-4.12-14.94-10.36-27.76-18.64-37.95-16.89-20.78-42.35-31.44-75.67-31.69-33.09.25-58.11,10.86-74.38,31.54-15.23,19.37-23.11,47.34-23.4,83.14.29,35.8,8.17,63.77,23.4,83.14Z"/><path class="cls-1" d="m206.66,205.42c-24.9,1.43-33.16,13.48-32.58,24.27.78,14.56,16.51,21.36,31.65,20.5,14.83-.81,31.66-6.63,34.52-42.46-7.69-1.68-16.15-2.56-25.2-2.56-2.75,0-5.55.08-8.4.24Z"/></g></svg>
</a>          </li>




          <li class="mb-4 mt-1 dropdown-item px-0 dropdown-item px-0">
            <a
  class="social__btn social__red d-flex justify-content-center" href="http://www.reddit.com/submit?title=Goodbye%20to%20All%20That%3A%20Reflections%20of%20a%20GOP%20Operative%20Who%20Left%20the%20Cult&url=https%3A%2F%2Ftruthout.org%2Farticles%2Fgoodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult%2F%3Futm_campaign%3DTruthout%2BShare%2BButtons"
  target="_top"
  rel="nofollow"
  >

<span class="social__ti visually-hidden">Share via Reddit</span>

<svg aria-hidden="true" class="social__icon" version="1.1" role="img" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 404.2 404.2" style="enable-background:new 0 0 404.2 404.2;" xml:space="preserve"><title>Reddit Cirlce Icon</title>
<path fill="currentColor" d="M175.6,221.8c0.1-11.8-9.5-21.5-21.3-21.5c-11.8-0.1-21.5,9.5-21.5,21.3c-0.1,11.8,9.5,21.5,21.3,21.5c0.1,0,0.2,0,0.2,0
	C166.1,243.1,175.6,233.5,175.6,221.8z"/>
<path fill="currentColor" d="M241.8,265c-15.7,15.8-65.7,15.4-80.8,0c-2-1.9-5.2-1.9-7.1,0c-2,1.9-2.2,5-0.3,7.1c0.1,0.1,0.2,0.2,0.3,0.3
	c19.8,19.8,75.5,19.7,95.1,0c2-1.9,2.2-5,0.3-7.1c-0.1-0.1-0.2-0.2-0.3-0.3C246.9,263.2,243.8,263.2,241.8,265z"/>
<path fill="currentColor" d="M248.5,200.3c-11.8,0.1-21.4,9.7-21.3,21.5s9.7,21.4,21.5,21.3c11.7-0.1,21.2-9.6,21.3-21.3c0.1-11.8-9.4-21.5-21.2-21.5
	C248.7,200.3,248.6,200.3,248.5,200.3z"/>
<path fill="currentColor" d="M202.1,0.5C90.8,0.5,0.5,90.8,0.5,202.1s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S313.4,0.5,202.1,0.5z M314.3,218.7
	c1.2,4.5,1.7,9.1,1.7,13.7c0,45.4-51.2,82.2-114.3,82.2c-62.9,0-114-36.8-114-82.2c0-4.5,0.5-9,1.4-13.4
	c-27.6-13.7-17.7-54.2,12.4-54.2c7.9,0,15.4,3.2,20.8,8.8c19.4-13.4,45.2-22,73.9-23.2l16.5-74.6c0.7-2.7,3.3-4.6,5.9-3.9l52.8,11.7
	c5.3-10.6,18.2-14.9,28.8-9.6s14.9,18.2,9.6,28.8c-3.7,7.3-11.1,11.9-19.3,11.8c-11.8,0-21.3-9.5-21.3-21.3l-47.8-10.8l-15,67.7
	c28.9,1,55,9.6,74.3,23c5.4-5.5,12.9-8.6,20.6-8.6C331.3,164.7,341.3,204.8,314.3,218.7z"/>
</svg>
</a>          </li>




          <li class="mb-4 mt-1 dropdown-item px-0 dropdown-item px-0">
            <a
  class="social__btn social__pct d-flex justify-content-center" href="https://getpocket.com/save?title=Goodbye%20to%20All%20That%3A%20Reflections%20of%20a%20GOP%20Operative%20Who%20Left%20the%20Cult&url=https%3A%2F%2Ftruthout.org%2Farticles%2Fgoodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult%2F%3Futm_campaign%3DTruthout%2BShare%2BButtons"
  target="_top"
  rel="nofollow"
  >

<span class="social__ti visually-hidden">Share via Pocket</span>

<svg aria-hidden="true" class="social__icon" role="img" data-name="Pocket Circle Icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 403.2 403.2"><title>Pocket Circle Icon</title><path fill="currentColor" d="M202.1.5C90.8.5.5,90.8.5,202.1S90.8,403.7,202.1,403.7s201.6-90.3,201.6-201.6S313.4.5,202.1.5ZM324.91,206a122.62,122.62,0,1,1-245.24,0V132a22.46,22.46,0,0,1,22.23-22.23H302.8A22,22,0,0,1,324.91,132Z" transform="translate(-0.5 -0.5)"/><path fill="currentColor" d="M260.15,172.49c-9.25,0-8.15,1.31-57.75,48.88-48.77-46.8-48.28-48.88-57.59-48.88a16.84,16.84,0,0,0-16.8,16.8c0,9.91.65,7.83,62.9,67.44a16.66,16.66,0,0,0,23.21,0C275.37,197.89,277,199,277,189.29A16.85,16.85,0,0,0,260.15,172.49Z" transform="translate(-0.5 -0.5)"/></svg>
</a>          </li>




          <li class="mb-4 mt-1 dropdown-item px-0 dropdown-item px-0">
            <a
  class="social__btn social__lin d-flex justify-content-center" href="http://www.linkedin.com/shareArticle?mini=true&title=Goodbye%20to%20All%20That%3A%20Reflections%20of%20a%20GOP%20Operative%20Who%20Left%20the%20Cult&url=https%3A%2F%2Ftruthout.org%2Farticles%2Fgoodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult%2F%3Futm_campaign%3DTruthout%2BShare%2BButtons&summary=&source=%3Cp%3E%28Photo%3A%20Carolyn%20Tiry%20%2F%20Flickr%29%20%20%20Barbara%20Stanwyck%3A%20%22We%26%23039%3Bre%20both%20rotten%21%22%20%20%20Fred%20MacMurray%3A%20%22Yeah%20-%20only%20you%26%23039%3Bre%20a%20little%20more%20rotten.%22%20-%22Double%20Indemnity%22%20%281944%29%3C%2Fp%3E"
  target="_top"
  rel="nofollow"
  >

<span class="social__ti visually-hidden">Share via Linkedin</span>

<svg aria-hidden="true" class="social__icon" role="img" data-name="LinkedIn Circle Icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 404.2 404.2"><title>LinkedIn Circle Icon</title><defs><style>.cls-1{stroke:#000;stroke-miterlimit:10;}</style></defs><path fill="currentColor" class="cls-1" d="M201.6,0C90.3,0,0,90.3,0,201.6S90.3,403.2,201.6,403.2s201.6-90.3,201.6-201.6S312.9,0,201.6,0ZM142.37,302.07H97.91V158.88h44.46ZM120.11,139.35a25.87,25.87,0,1,1,25.76-26A26,26,0,0,1,120.11,139.35ZM308.84,302.07H264.42v-69.7c0-16.62-.34-37.92-23.12-37.92-23.12,0-26.66,18.05-26.66,36.72v70.9H170.22V158.88h42.65v19.53h.62c5.94-11.25,20.44-23.12,42.07-23.12,45,0,53.28,29.63,53.28,68.12Z" transform="translate(0.5 0.5)"/></svg>
</a>          </li>




          <li class="mb-4 mt-1 dropdown-item px-0 dropdown-item px-0">
            <a
  class="social__btn social__tw d-flex justify-content-center" href="https://twitter.com/intent/tweet?text=Goodbye%20to%20All%20That%3A%20Reflections%20of%20a%20GOP%20Operative%20Who%20Left%20the%20Cult&url=https%3A%2F%2Ftruthout.org%2Farticles%2Fgoodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult%2F%3Futm_campaign%3DTruthout%2BShare%2BButtons&via=truthout"
  target="_top"
  rel="nofollow"
  >

<span class="social__ti visually-hidden">Share via Twitter</span>

<svg aria-hidden="true" class="social__icon" version="1.1" role="img" focusable="false" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 x="0px" y="0px" viewBox="0 0 403.2 403.2" style="enable-background:new 0 0 403.2 403.2;" xml:space="preserve"><title>Twitter Circle Icon</title>
<path fill="currentColor" d="M201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S312.9,0,201.6,0z M302,161.5
	c0.1,2,0.1,4.1,0.1,6.1c0,62.5-47.6,134.5-134.5,134.5c-26.8,0-51.7-7.8-72.6-21.2c3.8,0.4,7.5,0.6,11.4,0.6
	c22.1,0,42.5-7.5,58.7-20.2c-20.8-0.4-38.2-14.1-44.2-32.8c7.3,1.1,13.8,1.1,21.3-0.9c-21.6-4.4-37.8-23.4-37.8-46.4v-0.6
	c6.3,3.5,13.6,5.7,21.3,6c-13.2-8.8-21.1-23.5-21.1-39.4c0-8.8,2.3-16.9,6.4-23.9c23.3,28.7,58.3,47.4,97.5,49.5
	c-6.7-32.1,17.3-58.1,46.1-58.1c13.6,0,25.9,5.7,34.5,14.9c10.7-2,20.9-6,30-11.4c-3.5,11-11,20.2-20.8,26c9.5-1,18.7-3.7,27.3-7.4
	C319.3,146.4,311.2,154.8,302,161.5z"/>
</svg>
</a>          </li>

                        </ul>
            </li>
                            </ul>
  </div>
  </aside>

<aside class="ar__sidebar col-12 col-lg-2 order-2 order-lg-4 d-none d-md-block mt-0 mt-lg-3 py-0 px-1 py-lg-1 px-lg-1" aria-label="Article sidebar">

<div class="ar__caption d-none d-md-block mt-0 mb-6 font-sans fs-13 black-70" aria-hidden="true">
        <div class="mb-2" aria-hidden="true"><span><p>
	(Photo: <a href="https://www.flickr.com/photos/carolyntiry/4034641618/">Carolyn Tiry / Flickr</a>)</p>
</span></div>
      </div>

    <!-- begin partial/series-card -->

<section class="ar__read d-none d-lg-block">
    <header>
      <h4 class="ar__side__ti mb-4 font-sans--con text-uppercase fw-900">&hellip;Reading List</h4>
    </header>

<article class="ar__read__item mb-4">
        <div class="section mb-2 font-sans text-uppercase fs-13">Politics &amp; Elections</div>
        <h5><a class="ar__read__link text-decoration-none fw-normal" href="https://truthout.org/articles/rising-tenant-led-movement-aims-to-bring-down-corporate-landlords/">Rising Tenant-Led Movement Aims to Bring Down Corporate Landlords</a></h5>

</article>
          <article class="ar__read__item mb-4">
        <div class="section mb-2 font-sans text-uppercase fs-13">War &amp; Peace</div>
        <h5><a class="ar__read__link text-decoration-none fw-normal" href="https://truthout.org/articles/15k-gaza-students-have-been-killed-survivors-are-denied-their-education/">15K Gaza Students Have Been Killed. Survivors Are Denied Their Education.</a></h5>

</article>
          <article class="ar__read__item mb-4">
        <div class="section mb-2 font-sans text-uppercase fs-13">War &amp; Peace</div>
        <h5><a class="ar__read__link text-decoration-none fw-normal" href="https://truthout.org/articles/targeting-venezuela-trump-escalates-us-campaign-of-aggression-in-latin-america/">Targeting Venezuela, Trump Escalates US Campaign of Aggression in Latin America</a></h5>

</article>
          <article class="ar__read__item mb-4">
        <div class="section mb-2 font-sans text-uppercase fs-13">Racial Justice</div>
        <h5><a class="ar__read__link text-decoration-none fw-normal" href="https://truthout.org/articles/trumps-education-plan-seeks-to-make-cruel-domination-into-common-sense/">Trump’s Education Plan Seeks to Make Cruel Domination Into “Common Sense”</a></h5>

</article>
          <article class="ar__read__item mb-4">
        <div class="section mb-2 font-sans text-uppercase fs-13">Environment &amp; Health</div>
        <h5><a class="ar__read__link text-decoration-none fw-normal" href="https://truthout.org/articles/fda-guidelines-on-covid-19-vaccines-are-throwing-those-most-at-risk-into-despair/">FDA Guidelines on COVID-19 Vaccines Are Throwing Those Most at Risk Into Despair</a></h5>

</article>
          <article class="ar__read__item mb-4">
        <div class="section mb-2 font-sans text-uppercase fs-13">Politics &amp; Elections</div>
        <h5><a class="ar__read__link text-decoration-none fw-normal" href="https://truthout.org/articles/charlie-kirks-death-is-a-symptom-of-a-national-political-culture-in-crisis/">Charlie Kirk’s Death Is a Symptom of a National Political Culture in Crisis</a></h5>

</article>
      </section>

</aside>

<aside class="rel col-12 col-lg-7 order-5 offset-lg-2 ps-md-0 mt-5" aria-label="Related articles">
          <h5 class="rel__ti  text-uppercase font-sans--con"><span>Related Stories</span></h5>


    <div class="related__container">

        <article class="ar-list row ms-0 me-0 mb-4 mb-md-3 pb-3 pb-md-0 border-bottom--gray--sm" itemscope itemtype="https://schema.org/OpinionNewsArticle">

<figure class="ar-list__th col ps-0 pe-0 pe-md-3">
    <a class="ar-list__th__lnk d-block" href="https://truthout.org/articles/a-medicare-moment-for-gop/" title="A Medicare Moment for GOP">
      <img width="240" height="272" src="https://truthout.org/app/uploads/2017/12/A-Medicare-Moment-for-GOP.jpg" class="img-fluid cover wp-post-image" alt="" loading="lazy" decoding="async" srcset="https://truthout.org/app/uploads/2017/12/A-Medicare-Moment-for-GOP.jpg 240w, https://truthout.org/app/uploads/2017/12/A-Medicare-Moment-for-GOP-200x227.jpg 200w" sizes="auto, (max-width: 240px) 100vw, 240px" />
    </a>
  </figure>

<header class="ar-list__con col d-flex flex-column ps-md-3 pe-md-0">

<div class="before-headline mt-0 mb-3 mb-md-2 fs-13 d-inline text-uppercase font-sans text-decoration-none black-65">
  <!-- components/category-terms -->
  <div class="categories d-inline">
                  <a href="https://truthout.org/category/op-ed/" rel='category' class="op-ed text-decoration-none black-65">Op-Ed</a>
            </div>
  <span class="separator px-1">|</span>

  </div>

<h2 class="ar-list__ti mb-3 mb-md-2" itemprop="headline">
      <a href="https://truthout.org/articles/a-medicare-moment-for-gop/">A Medicare Moment for GOP</a>
    </h2>

<div class="ar-list__sum mb-3 mb-md-1" itemprop="description">
         Congressman Paul Ryan of Wisconsin speaking at CPAC 2011 in Washington, DC. (Photo: Gage Skidmore)   Washington - Rep. Paul Ryan, R-Wis., the architect of his party's radical &hellip;
      </div>



      <div class="ar-list__meta d-inline mb-auto">
        <!-- components/authors -->
    <dl class="byline list-inline font-sans d-inline mt-2 mb-0 white-70">
        <dt class="byline__label d-inline me-0">By</dt>
                  <dd class="byline__author author vcard d-inline me-0" itemprop="author" itemscope itemtype="https://schema.org/Person">
            <span class="byline__author__name" itemprop="name">
              <a class="byline__author__link url fn text-decoration-none white-70" href="https://truthout.org/authors/eugene-robinson/" itemprop="url" rel="author">Eugene Robinson</a>
            </span>

<span class="separator">, </span>
                      </dd>

                  <dd class="byline__source source org d-inline" itemprop="sourceOrganization" itemscope itemtype="https://schema.org/Organization"><span class="byline__source__name text-uppercase" itemprop="name"> </span></dd>
            </dl>
        <time class="published updated meta-data visually-hidden"
    datetime="2011-05-24T08:56:05+00:00"
    itemprop="datePublished dateCreated"
    content="2011-05-24T08:56:05+00:00">
    May 24, 2011
  </time>
        <div class="d-none" itemprop="publisher" itemscope itemtype="http://schema.org/Organization">
  <a href="https://truthout.org" itemprop="url">
    <span itemprop="name">
      Truthout
    </span>
  </a>
</div>
      </div>

</header>

</article>

        <article class="ar-list row ms-0 me-0 mb-4 mb-md-3 pb-3 pb-md-0 border-bottom--gray--sm" itemscope itemtype="https://schema.org/AnalysisNewsArticle">

<figure class="ar-list__th col ps-0 pe-0 pe-md-3">
    <a class="ar-list__th__lnk d-block" href="https://truthout.org/articles/connecting-the-dots-of-the-gop-assault-on-women/" title="Connecting the Dots of the GOP Assault on Women">
      <img class="article-thumbnail img-fluid cover" src="https://truthout.org/app/uploads/2018/03/Truthout-Default-Image-1200x900.png" alt="Truthout Logo" loading="lazy">
    </a>
  </figure>

<header class="ar-list__con col d-flex flex-column ps-md-3 pe-md-0">

<div class="before-headline mt-0 mb-3 mb-md-2 fs-13 d-inline text-uppercase font-sans text-decoration-none black-65">
  <!-- components/category-terms -->
  <div class="categories d-inline">
                  <a href="https://truthout.org/category/news-analysis/" rel='category' class="news-analysis text-decoration-none black-65">News Analysis</a>
            </div>
  <span class="separator px-1">|</span>

  </div>

<h2 class="ar-list__ti mb-3 mb-md-2" itemprop="headline">
      <a href="https://truthout.org/articles/connecting-the-dots-of-the-gop-assault-on-women/">Connecting the Dots of the GOP Assault on Women</a>
    </h2>

<div class="ar-list__sum mb-3 mb-md-1" itemprop="description">
         At a time when women in other countries like those in newly liberated Egypt, for example, are rising up to demand their rights, we women here in the United &hellip;
      </div>



      <div class="ar-list__meta d-inline mb-auto">
        <!-- components/authors -->
    <dl class="byline list-inline font-sans d-inline mt-2 mb-0 white-70">
        <dt class="byline__label d-inline me-0">By</dt>
                  <dd class="byline__author author vcard d-inline me-0" itemprop="author" itemscope itemtype="https://schema.org/Person">
            <span class="byline__author__name" itemprop="name">
              <a class="byline__author__link url fn text-decoration-none white-70" href="https://truthout.org/authors/mary-wentworth/" itemprop="url" rel="author">Mary Wentworth</a>
            </span>

<span class="separator">, </span>
                      </dd>

                  <dd class="byline__source source org d-inline" itemprop="sourceOrganization" itemscope itemtype="https://schema.org/Organization"><span class="byline__source__name text-uppercase" itemprop="name"> <a class="byline__source__link text-decoration-none d-inline white-70" href="https://truthout.org" itemprop="url"><span class="byline__source__upper">T</span>ruthout</a></span></dd>
            </dl>
        <time class="published updated meta-data visually-hidden"
    datetime="2011-04-14T13:55:33+00:00"
    itemprop="datePublished dateCreated"
    content="2011-04-14T13:55:33+00:00">
    April 14, 2011
  </time>
        <div class="d-none" itemprop="publisher" itemscope itemtype="http://schema.org/Organization">
  <a href="https://truthout.org" itemprop="url">
    <span itemprop="name">
      Truthout
    </span>
  </a>
</div>
      </div>

</header>

</article>



    </div>
  </aside>

      <aside class="rel col-12 col-lg-7 order-5 offset-lg-2 ps-md-0 mt-2" aria-label="Latest Articles">
          <h5 class="rel__ti  text-uppercase font-sans--con"><span>Latest Stories</span></h5>


    <div class="related__container">

        <article class="ar-list row ms-0 me-0 mb-4 mb-md-3 pb-3 pb-md-0 border-bottom--gray--sm" itemscope itemtype="https://schema.org/ReportageNewsArticle">

<figure class="ar-list__th col ps-0 pe-0 pe-md-3">
    <a class="ar-list__th__lnk d-block" href="https://truthout.org/articles/this-researcher-studied-how-climate-change-hurts-children-trump-shut-her-down/" title="This Researcher Studied How Climate Change Hurts Children — Trump Shut Her Down">
      <img width="400" height="300" src="https://truthout.org/app/uploads/2025/09/GettyImages-2230337485-400x300.jpg" class="img-fluid cover wp-post-image" alt="Children play basketball as the sun sets on August 19, 2025, in San Pedro, California after the National Weather Service issued an extreme heat warning for parts of Los Angeles County." loading="lazy" decoding="async" srcset="https://truthout.org/app/uploads/2025/09/GettyImages-2230337485-400x300.jpg 400w, https://truthout.org/app/uploads/2025/09/GettyImages-2230337485-200x150.jpg 200w, https://truthout.org/app/uploads/2025/09/GettyImages-2230337485-800x600.jpg 800w, https://truthout.org/app/uploads/2025/09/GettyImages-2230337485-1200x900.jpg 1200w, https://truthout.org/app/uploads/2025/09/GettyImages-2230337485-2400x1800.jpg 2400w" sizes="auto, (max-width: 400px) 100vw, 400px" />
    </a>
  </figure>

<header class="ar-list__con col d-flex flex-column ps-md-3 pe-md-0">

<div class="before-headline mt-0 mb-3 mb-md-2 fs-13 d-inline text-uppercase font-sans text-decoration-none black-65">
  <!-- components/category-terms -->
  <div class="categories d-inline">
                  <a href="https://truthout.org/category/news/" rel='category' class="news text-decoration-none black-65">News</a>
            </div>
  <span class="separator px-1">|</span>

      <div class="ar__section d-inline"><a href="https://truthout.org/section/environment-and-health/" rel="section" class="ar__section__link environment-and-health text-decoration-none black-70" >Environment &amp; Health</a></div>
  </div>

<h2 class="ar-list__ti mb-3 mb-md-2" itemprop="headline">
      <a href="https://truthout.org/articles/this-researcher-studied-how-climate-change-hurts-children-trump-shut-her-down/">This Researcher Studied How Climate Change Hurts Children — Trump Shut Her Down</a>
    </h2>

<div class="ar-list__sum mb-3 mb-md-1" itemprop="description">
         Jane Clougherty spent years studying how extreme weather affects kids’ health. Trump’s EPA cancelled her work.
      </div>



      <div class="ar-list__meta d-inline mb-auto">
        <!-- components/authors -->
    <dl class="byline list-inline font-sans d-inline mt-2 mb-0 white-70">
        <dt class="byline__label d-inline me-0">By</dt>
                  <dd class="byline__author author vcard d-inline me-0" itemprop="author" itemscope itemtype="https://schema.org/Person">
            <span class="byline__author__name" itemprop="name">
              <a class="byline__author__link url fn text-decoration-none white-70" href="https://truthout.org/authors/jessica-kutz/" itemprop="url" rel="author">Jessica Kutz</a>
            </span>

<span class="separator">, </span>
                      </dd>

                  <dd class="byline__source source org d-inline" itemprop="sourceOrganization" itemscope itemtype="https://schema.org/Organization"><span class="byline__source__name text-uppercase" itemprop="name"> <a class="byline__source__link text-decoration-none d-inline white-70" href="https://19thnews.org/2025/09/epa-ends-research-climate-childrens-health/" itemprop="url"><span class="byline__source__upper">T</span>he<span class="byline__source__upper">1</span>9th</a></span></dd>
            </dl>
        <time class="published updated meta-data visually-hidden"
    datetime="2025-09-13T21:53:10+00:00"
    itemprop="datePublished dateCreated"
    content="2025-09-13T21:53:10+00:00">
    September 13, 2025
  </time>
        <div class="d-none" itemprop="publisher" itemscope itemtype="http://schema.org/Organization">
  <a href="https://truthout.org" itemprop="url">
    <span itemprop="name">
      Truthout
    </span>
  </a>
</div>
      </div>

</header>

</article>

        <article class="ar-list row ms-0 me-0 mb-4 mb-md-3 pb-3 pb-md-0 border-bottom--gray--sm" itemscope itemtype="https://schema.org/ReportageNewsArticle">

<figure class="ar-list__th col ps-0 pe-0 pe-md-3">
    <a class="ar-list__th__lnk d-block" href="https://truthout.org/articles/new-bill-would-allow-rubio-to-strip-us-citizens-passports-over-political-speech/" title="New Bill Would Allow Rubio to Strip US Citizens&#8217; Passports Over Political Speech">
      <img width="400" height="300" src="https://truthout.org/app/uploads/2025/09/GettyImages-2234583045-400x300.jpg" class="img-fluid cover wp-post-image" alt="U.S. Secretary of State Marco Rubio speaks to members of the media before departing for Israel at Joint Base Andrews, Maryland, on September 13, 2025." loading="lazy" decoding="async" srcset="https://truthout.org/app/uploads/2025/09/GettyImages-2234583045-400x300.jpg 400w, https://truthout.org/app/uploads/2025/09/GettyImages-2234583045-200x150.jpg 200w, https://truthout.org/app/uploads/2025/09/GettyImages-2234583045-800x600.jpg 800w, https://truthout.org/app/uploads/2025/09/GettyImages-2234583045-1200x900.jpg 1200w, https://truthout.org/app/uploads/2025/09/GettyImages-2234583045-2400x1800.jpg 2400w" sizes="auto, (max-width: 400px) 100vw, 400px" />
    </a>
  </figure>

<header class="ar-list__con col d-flex flex-column ps-md-3 pe-md-0">

<div class="before-headline mt-0 mb-3 mb-md-2 fs-13 d-inline text-uppercase font-sans text-decoration-none black-65">
  <!-- components/category-terms -->
  <div class="categories d-inline">
                  <a href="https://truthout.org/category/news/" rel='category' class="news text-decoration-none black-65">News</a>
            </div>
  <span class="separator px-1">|</span>

      <div class="ar__section d-inline"><a href="https://truthout.org/section/politics-and-elections/" rel="section" class="ar__section__link politics-and-elections text-decoration-none black-70" >Politics &amp; Elections</a></div>
  </div>

<h2 class="ar-list__ti mb-3 mb-md-2" itemprop="headline">
      <a href="https://truthout.org/articles/new-bill-would-allow-rubio-to-strip-us-citizens-passports-over-political-speech/">New Bill Would Allow Rubio to Strip US Citizens&#8217; Passports Over Political Speech</a>
    </h2>

<div class="ar-list__sum mb-3 mb-md-1" itemprop="description">
         The legislation would allow the Secretary of State to strip anyone's US passport with no legal due process.
      </div>



      <div class="ar-list__meta d-inline mb-auto">
        <!-- components/authors -->
    <dl class="byline list-inline font-sans d-inline mt-2 mb-0 white-70">
        <dt class="byline__label d-inline me-0">By</dt>
                  <dd class="byline__author author vcard d-inline me-0" itemprop="author" itemscope itemtype="https://schema.org/Person">
            <span class="byline__author__name" itemprop="name">
              <a class="byline__author__link url fn text-decoration-none white-70" href="https://truthout.org/authors/stephen-prager/" itemprop="url" rel="author">Stephen Prager</a>
            </span>

<span class="separator">, </span>
                      </dd>

                  <dd class="byline__source source org d-inline" itemprop="sourceOrganization" itemscope itemtype="https://schema.org/Organization"><span class="byline__source__name text-uppercase" itemprop="name"> <a class="byline__source__link text-decoration-none d-inline white-70" href="https://www.commondreams.org/news/rubio-thought-policing-bill" itemprop="url"><span class="byline__source__upper">C</span>ommon<span class="byline__source__upper">D</span>reams</a></span></dd>
            </dl>
        <time class="published updated meta-data visually-hidden"
    datetime="2025-09-13T21:51:52+00:00"
    itemprop="datePublished dateCreated"
    content="2025-09-13T21:51:52+00:00">
    September 13, 2025
  </time>
        <div class="d-none" itemprop="publisher" itemscope itemtype="http://schema.org/Organization">
  <a href="https://truthout.org" itemprop="url">
    <span itemprop="name">
      Truthout
    </span>
  </a>
</div>
      </div>

</header>

</article>

        <article class="ar-list row ms-0 me-0 mb-4 mb-md-3 pb-3 pb-md-0 border-bottom--gray--sm" itemscope itemtype="https://schema.org/ReportageNewsArticle">

<figure class="ar-list__th col ps-0 pe-0 pe-md-3">
    <a class="ar-list__th__lnk d-block" href="https://truthout.org/articles/stephen-miller-vows-to-dismantle-the-left-after-charlie-kirk-assassination/" title="Stephen Miller Vows to &#8220;Dismantle&#8221; the Left After Charlie Kirk Assassination">
      <img width="400" height="300" src="https://truthout.org/app/uploads/2025/09/GettyImages-2232756062-400x300.jpg" class="img-fluid cover wp-post-image" alt="White House Deputy Chief Of Staff Stephen Miller speaks to members of the media outside the White House on August 29, 2025, in Washington, D.C." loading="lazy" decoding="async" srcset="https://truthout.org/app/uploads/2025/09/GettyImages-2232756062-400x300.jpg 400w, https://truthout.org/app/uploads/2025/09/GettyImages-2232756062-200x150.jpg 200w, https://truthout.org/app/uploads/2025/09/GettyImages-2232756062-800x600.jpg 800w, https://truthout.org/app/uploads/2025/09/GettyImages-2232756062-1200x900.jpg 1200w, https://truthout.org/app/uploads/2025/09/GettyImages-2232756062-2400x1800.jpg 2400w" sizes="auto, (max-width: 400px) 100vw, 400px" />
    </a>
  </figure>

<header class="ar-list__con col d-flex flex-column ps-md-3 pe-md-0">

<div class="before-headline mt-0 mb-3 mb-md-2 fs-13 d-inline text-uppercase font-sans text-decoration-none black-65">
  <!-- components/category-terms -->
  <div class="categories d-inline">
                  <a href="https://truthout.org/category/news/" rel='category' class="news text-decoration-none black-65">News</a>
            </div>
  <span class="separator px-1">|</span>

      <div class="ar__section d-inline"><a href="https://truthout.org/section/politics-and-elections/" rel="section" class="ar__section__link politics-and-elections text-decoration-none black-70" >Politics &amp; Elections</a></div>
  </div>

<h2 class="ar-list__ti mb-3 mb-md-2" itemprop="headline">
      <a href="https://truthout.org/articles/stephen-miller-vows-to-dismantle-the-left-after-charlie-kirk-assassination/">Stephen Miller Vows to &#8220;Dismantle&#8221; the Left After Charlie Kirk Assassination</a>
    </h2>

<div class="ar-list__sum mb-3 mb-md-1" itemprop="description">
         Miller threatened to deploy RICO and terrorism charges to persecute progressive organizations and individuals.
      </div>



      <div class="ar-list__meta d-inline mb-auto">
        <!-- components/authors -->
    <dl class="byline list-inline font-sans d-inline mt-2 mb-0 white-70">
        <dt class="byline__label d-inline me-0">By</dt>
                  <dd class="byline__author author vcard d-inline me-0" itemprop="author" itemscope itemtype="https://schema.org/Person">
            <span class="byline__author__name" itemprop="name">
              <a class="byline__author__link url fn text-decoration-none white-70" href="https://truthout.org/authors/stephen-prager/" itemprop="url" rel="author">Stephen Prager</a>
            </span>

<span class="separator">, </span>
                      </dd>

                  <dd class="byline__source source org d-inline" itemprop="sourceOrganization" itemscope itemtype="https://schema.org/Organization"><span class="byline__source__name text-uppercase" itemprop="name"> <a class="byline__source__link text-decoration-none d-inline white-70" href="https://www.commondreams.org/news/stephen-miller-dismantle-the-left" itemprop="url"><span class="byline__source__upper">C</span>ommon<span class="byline__source__upper">D</span>reams</a></span></dd>
            </dl>
        <time class="published updated meta-data visually-hidden"
    datetime="2025-09-13T21:49:57+00:00"
    itemprop="datePublished dateCreated"
    content="2025-09-13T21:49:57+00:00">
    September 13, 2025
  </time>
        <div class="d-none" itemprop="publisher" itemscope itemtype="http://schema.org/Organization">
  <a href="https://truthout.org" itemprop="url">
    <span itemprop="name">
      Truthout
    </span>
  </a>
</div>
      </div>

</header>

</article>

        <article class="ar-list row ms-0 me-0 mb-4 mb-md-3 pb-3 pb-md-0 border-bottom--gray--sm" itemscope itemtype="https://schema.org/AnalysisNewsArticle">

<figure class="ar-list__th col ps-0 pe-0 pe-md-3">
    <a class="ar-list__th__lnk d-block" href="https://truthout.org/articles/15k-gaza-students-have-been-killed-survivors-are-denied-their-education/" title="15K Gaza Students Have Been Killed. Survivors Are Denied Their Education.">
      <img width="400" height="300" src="https://truthout.org/app/uploads/2025/09/GettyImages-2234017735-400x300.jpg" class="img-fluid cover wp-post-image" alt="A Palestinian woman reacts as she checks the rubble of a school building destroyed in an Israeli strike in Gaza City the previous day, on September 10, 2025." loading="lazy" decoding="async" srcset="https://truthout.org/app/uploads/2025/09/GettyImages-2234017735-400x300.jpg 400w, https://truthout.org/app/uploads/2025/09/GettyImages-2234017735-200x150.jpg 200w, https://truthout.org/app/uploads/2025/09/GettyImages-2234017735-800x600.jpg 800w, https://truthout.org/app/uploads/2025/09/GettyImages-2234017735-1200x900.jpg 1200w, https://truthout.org/app/uploads/2025/09/GettyImages-2234017735-2400x1800.jpg 2400w" sizes="auto, (max-width: 400px) 100vw, 400px" />
    </a>
  </figure>

<header class="ar-list__con col d-flex flex-column ps-md-3 pe-md-0">

<div class="before-headline mt-0 mb-3 mb-md-2 fs-13 d-inline text-uppercase font-sans text-decoration-none black-65">
  <!-- components/category-terms -->
  <div class="categories d-inline">
                  <a href="https://truthout.org/category/news-analysis/" rel='category' class="news-analysis text-decoration-none black-65">News Analysis</a>
            </div>
  <span class="separator px-1">|</span>

      <div class="ar__section d-inline"><a href="https://truthout.org/section/education-and-youth/" rel="section" class="ar__section__link education-and-youth text-decoration-none black-70" >Education &amp; Youth</a></div>
  </div>

<h2 class="ar-list__ti mb-3 mb-md-2" itemprop="headline">
      <a href="https://truthout.org/articles/15k-gaza-students-have-been-killed-survivors-are-denied-their-education/">15K Gaza Students Have Been Killed. Survivors Are Denied Their Education.</a>
    </h2>

<div class="ar-list__sum mb-3 mb-md-1" itemprop="description">
         Israel has killed over 800 teachers and staff, along with 15,000 school-aged kids. Schools are in ruins.
      </div>



      <div class="ar-list__meta d-inline mb-auto">
        <!-- components/authors -->
    <dl class="byline list-inline font-sans d-inline mt-2 mb-0 white-70">
        <dt class="byline__label d-inline me-0">By</dt>
                  <dd class="byline__author author vcard d-inline me-0" itemprop="author" itemscope itemtype="https://schema.org/Person">
            <span class="byline__author__name" itemprop="name">
              <a class="byline__author__link url fn text-decoration-none white-70" href="https://truthout.org/authors/hend-salama-abo-helow/" itemprop="url" rel="author">Hend Salama Abo Helow</a>
            </span>

<span class="separator">, </span>
                      </dd>

                  <dd class="byline__source source org d-inline" itemprop="sourceOrganization" itemscope itemtype="https://schema.org/Organization"><span class="byline__source__name text-uppercase" itemprop="name"> <a class="byline__source__link text-decoration-none d-inline white-70" href="https://truthout.org" itemprop="url"><span class="byline__source__upper">T</span>ruthout</a></span></dd>
            </dl>
        <time class="published updated meta-data visually-hidden"
    datetime="2025-09-13T21:48:08+00:00"
    itemprop="datePublished dateCreated"
    content="2025-09-13T21:48:08+00:00">
    September 13, 2025
  </time>
        <div class="d-none" itemprop="publisher" itemscope itemtype="http://schema.org/Organization">
  <a href="https://truthout.org" itemprop="url">
    <span itemprop="name">
      Truthout
    </span>
  </a>
</div>
      </div>

</header>

</article>

        <article class="ar-list row ms-0 me-0 mb-4 mb-md-3 pb-3 pb-md-0 border-bottom--gray--sm" itemscope itemtype="https://schema.org/NewsArticle">

<figure class="ar-list__th col ps-0 pe-0 pe-md-3">
    <a class="ar-list__th__lnk d-block" href="https://truthout.org/articles/rising-tenant-led-movement-aims-to-bring-down-corporate-landlords/" title="Rising Tenant-Led Movement Aims to Bring Down Corporate Landlords">
      <img width="400" height="300" src="https://truthout.org/app/uploads/2025/09/DSC_4790-400x300.jpg" class="img-fluid cover wp-post-image" alt="Tenant leaders in South Minneapolis take action in March 2025 to demand better housing conditions from their landlord." loading="lazy" decoding="async" srcset="https://truthout.org/app/uploads/2025/09/DSC_4790-400x300.jpg 400w, https://truthout.org/app/uploads/2025/09/DSC_4790-200x150.jpg 200w, https://truthout.org/app/uploads/2025/09/DSC_4790-800x600.jpg 800w, https://truthout.org/app/uploads/2025/09/DSC_4790-1200x900.jpg 1200w, https://truthout.org/app/uploads/2025/09/DSC_4790-2400x1800.jpg 2400w" sizes="auto, (max-width: 400px) 100vw, 400px" />
    </a>
  </figure>

<header class="ar-list__con col d-flex flex-column ps-md-3 pe-md-0">

<div class="before-headline mt-0 mb-3 mb-md-2 fs-13 d-inline text-uppercase font-sans text-decoration-none black-65">
  <!-- components/category-terms -->
  <div class="categories d-inline">
                  <a href="https://truthout.org/category/interview/" rel='category' class="interview text-decoration-none black-65">Interview</a>
            </div>
  <span class="separator px-1">|</span>

      <div class="ar__section d-inline"><a href="https://truthout.org/section/politics-and-elections/" rel="section" class="ar__section__link politics-and-elections text-decoration-none black-70" >Politics &amp; Elections</a></div>
  </div>

<h2 class="ar-list__ti mb-3 mb-md-2" itemprop="headline">
      <a href="https://truthout.org/articles/rising-tenant-led-movement-aims-to-bring-down-corporate-landlords/">Rising Tenant-Led Movement Aims to Bring Down Corporate Landlords</a>
    </h2>

<div class="ar-list__sum mb-3 mb-md-1" itemprop="description">
         Tenant union organizers from Kentucky, Minnesota, Montana, and New York share hopeful news from the growing movement.
      </div>



      <div class="ar-list__meta d-inline mb-auto">
        <!-- components/authors -->
    <dl class="byline list-inline font-sans d-inline mt-2 mb-0 white-70">
        <dt class="byline__label d-inline me-0">By</dt>
                  <dd class="byline__author author vcard d-inline me-0" itemprop="author" itemscope itemtype="https://schema.org/Person">
            <span class="byline__author__name" itemprop="name">
              <a class="byline__author__link url fn text-decoration-none white-70" href="https://truthout.org/authors/derek-seidman/" itemprop="url" rel="author">Derek Seidman</a>
            </span>

<span class="separator">, </span>
                      </dd>

                  <dd class="byline__source source org d-inline" itemprop="sourceOrganization" itemscope itemtype="https://schema.org/Organization"><span class="byline__source__name text-uppercase" itemprop="name"> <a class="byline__source__link text-decoration-none d-inline white-70" href="https://truthout.org" itemprop="url"><span class="byline__source__upper">T</span>ruthout</a></span></dd>
            </dl>
        <time class="published updated meta-data visually-hidden"
    datetime="2025-09-13T21:45:05+00:00"
    itemprop="datePublished dateCreated"
    content="2025-09-13T21:45:05+00:00">
    September 13, 2025
  </time>
        <div class="d-none" itemprop="publisher" itemscope itemtype="http://schema.org/Organization">
  <a href="https://truthout.org" itemprop="url">
    <span itemprop="name">
      Truthout
    </span>
  </a>
</div>
      </div>

</header>

</article>

        <article class="ar-list row ms-0 me-0 mb-4 mb-md-3 pb-3 pb-md-0 border-bottom--gray--sm" itemscope itemtype="https://schema.org/AnalysisNewsArticle">

<figure class="ar-list__th col ps-0 pe-0 pe-md-3">
    <a class="ar-list__th__lnk d-block" href="https://truthout.org/articles/trumps-health-care-funding-cuts-leave-states-with-impossible-budget-choices/" title="Trump&#8217;s Health Care Funding Cuts Leave States With Impossible Budget Choices">
      <img width="400" height="267" src="https://truthout.org/app/uploads/2025/09/GettyImages-2228341074.jpg" class="img-fluid cover wp-post-image" alt="Medical students volunteer at a Remote Area Medical (RAM) mobile dental and medical clinic on August 2, 2025, in Terre Haute, Indiana." loading="lazy" decoding="async" srcset="https://truthout.org/app/uploads/2025/09/GettyImages-2228341074.jpg 8368w, https://truthout.org/app/uploads/2025/09/GettyImages-2228341074-400x267.jpg 400w, https://truthout.org/app/uploads/2025/09/GettyImages-2228341074-1200x801.jpg 1200w, https://truthout.org/app/uploads/2025/09/GettyImages-2228341074-200x133.jpg 200w, https://truthout.org/app/uploads/2025/09/GettyImages-2228341074-800x534.jpg 800w, https://truthout.org/app/uploads/2025/09/GettyImages-2228341074-1536x1025.jpg 1536w" sizes="auto, (max-width: 400px) 100vw, 400px" />
    </a>
  </figure>

<header class="ar-list__con col d-flex flex-column ps-md-3 pe-md-0">

<div class="before-headline mt-0 mb-3 mb-md-2 fs-13 d-inline text-uppercase font-sans text-decoration-none black-65">
  <!-- components/category-terms -->
  <div class="categories d-inline">
                  <a href="https://truthout.org/category/news-analysis/" rel='category' class="news-analysis text-decoration-none black-65">News Analysis</a>
            </div>
  <span class="separator px-1">|</span>

      <div class="ar__section d-inline"><a href="https://truthout.org/section/environment-and-health/" rel="section" class="ar__section__link environment-and-health text-decoration-none black-70" >Environment &amp; Health</a></div>
  </div>

<h2 class="ar-list__ti mb-3 mb-md-2" itemprop="headline">
      <a href="https://truthout.org/articles/trumps-health-care-funding-cuts-leave-states-with-impossible-budget-choices/">Trump&#8217;s Health Care Funding Cuts Leave States With Impossible Budget Choices</a>
    </h2>

<div class="ar-list__sum mb-3 mb-md-1" itemprop="description">
         Some state leaders are warning constituents to expect massive Medicaid rollbacks forced by Trump's federal budget.
      </div>



      <div class="ar-list__meta d-inline mb-auto">
        <!-- components/authors -->
    <dl class="byline list-inline font-sans d-inline mt-2 mb-0 white-70">
        <dt class="byline__label d-inline me-0">By</dt>
                  <dd class="byline__author author vcard d-inline me-0" itemprop="author" itemscope itemtype="https://schema.org/Person">
            <span class="byline__author__name" itemprop="name">
              <a class="byline__author__link url fn text-decoration-none white-70" href="https://truthout.org/authors/stephanie-armour/" itemprop="url" rel="author">Stephanie Armour</a>
            </span>

<span class="separator">, </span>

                      </dd>
                  <dd class="byline__author author vcard d-inline me-0" itemprop="author" itemscope itemtype="https://schema.org/Person">
            <span class="byline__author__name" itemprop="name">
              <a class="byline__author__link url fn text-decoration-none white-70" href="https://truthout.org/authors/christine-mai-duc/" itemprop="url" rel="author">Christine Mai-Duc</a>
            </span>

<span class="separator">, </span>

                      </dd>
                  <dd class="byline__author author vcard d-inline me-0" itemprop="author" itemscope itemtype="https://schema.org/Person">
            <span class="byline__author__name" itemprop="name">
              <a class="byline__author__link url fn text-decoration-none white-70" href="https://truthout.org/authors/sam-whitehead/" itemprop="url" rel="author">Sam Whitehead</a>
            </span>

<span class="separator">, </span>

                      </dd>
                  <dd class="byline__author author vcard d-inline me-0" itemprop="author" itemscope itemtype="https://schema.org/Person">
            <span class="byline__author__name" itemprop="name">
              <a class="byline__author__link url fn text-decoration-none white-70" href="https://truthout.org/authors/arielle-zionts/" itemprop="url" rel="author">Arielle Zionts</a>
            </span>

<span class="separator">, </span>
                      </dd>

                  <dd class="byline__source source org d-inline" itemprop="sourceOrganization" itemscope itemtype="https://schema.org/Organization"><span class="byline__source__name text-uppercase" itemprop="name"> <a class="byline__source__link text-decoration-none d-inline white-70" href="https://kffhealthnews.org/news/article/state-budget-fallout-trump-health-funding-cuts-obbba/" itemprop="url"><span class="byline__source__upper">K</span>FF<span class="byline__source__upper">H</span>ealth<span class="byline__source__upper">N</span>ews</a></span></dd>
            </dl>
        <time class="published updated meta-data visually-hidden"
    datetime="2025-09-13T15:25:04+00:00"
    itemprop="datePublished dateCreated"
    content="2025-09-13T15:25:04+00:00">
    September 13, 2025
  </time>
        <div class="d-none" itemprop="publisher" itemscope itemtype="http://schema.org/Organization">
  <a href="https://truthout.org" itemprop="url">
    <span itemprop="name">
      Truthout
    </span>
  </a>
</div>
      </div>

</header>

</article>

        <article class="ar-list row ms-0 me-0 mb-4 mb-md-3 pb-3 pb-md-0 border-bottom--gray--sm" itemscope itemtype="https://schema.org/ReportageNewsArticle">

<figure class="ar-list__th col ps-0 pe-0 pe-md-3">
    <a class="ar-list__th__lnk d-block" href="https://truthout.org/articles/netanyahu-signs-settlement-agreement-that-would-displace-7000-palestinians/" title="Netanyahu Signs Settlement Agreement That Would Displace 7,000 Palestinians">
      <img width="400" height="300" src="https://truthout.org/app/uploads/2025/09/GettyImages-2234185098-400x300.jpg" class="img-fluid cover wp-post-image" alt="Israeli Prime Minister Benjamin Netanyahu delivers a speech during a signing ceremony for a framework agreement, aiming to speed up development in the Israeli settlement of Maale Adumim, in the occupied-West Bank settlement on September 11, 2025." loading="lazy" decoding="async" srcset="https://truthout.org/app/uploads/2025/09/GettyImages-2234185098-400x300.jpg 400w, https://truthout.org/app/uploads/2025/09/GettyImages-2234185098-200x150.jpg 200w, https://truthout.org/app/uploads/2025/09/GettyImages-2234185098-800x600.jpg 800w, https://truthout.org/app/uploads/2025/09/GettyImages-2234185098-1200x900.jpg 1200w, https://truthout.org/app/uploads/2025/09/GettyImages-2234185098-2400x1800.jpg 2400w" sizes="auto, (max-width: 400px) 100vw, 400px" />
    </a>
  </figure>

<header class="ar-list__con col d-flex flex-column ps-md-3 pe-md-0">

<div class="before-headline mt-0 mb-3 mb-md-2 fs-13 d-inline text-uppercase font-sans text-decoration-none black-65">
  <!-- components/category-terms -->
  <div class="categories d-inline">
                  <a href="https://truthout.org/category/news/" rel='category' class="news text-decoration-none black-65">News</a>
            </div>
  <span class="separator px-1">|</span>

      <div class="ar__section d-inline"><a href="https://truthout.org/section/war-and-peace/" rel="section" class="ar__section__link war-and-peace text-decoration-none black-70" >War &amp; Peace</a></div>
  </div>

<h2 class="ar-list__ti mb-3 mb-md-2" itemprop="headline">
      <a href="https://truthout.org/articles/netanyahu-signs-settlement-agreement-that-would-displace-7000-palestinians/">Netanyahu Signs Settlement Agreement That Would Displace 7,000 Palestinians</a>
    </h2>

<div class="ar-list__sum mb-3 mb-md-1" itemprop="description">
         The Israeli Prime Minister declared “there will be no Palestinian state” as he signed the plan.
      </div>



      <div class="ar-list__meta d-inline mb-auto">
        <!-- components/authors -->
    <dl class="byline list-inline font-sans d-inline mt-2 mb-0 white-70">
        <dt class="byline__label d-inline me-0">By</dt>
                  <dd class="byline__author author vcard d-inline me-0" itemprop="author" itemscope itemtype="https://schema.org/Person">
            <span class="byline__author__name" itemprop="name">
              <a class="byline__author__link url fn text-decoration-none white-70" href="https://truthout.org/authors/julia-conley/" itemprop="url" rel="author">Julia Conley</a>
            </span>

<span class="separator">, </span>
                      </dd>

                  <dd class="byline__source source org d-inline" itemprop="sourceOrganization" itemscope itemtype="https://schema.org/Organization"><span class="byline__source__name text-uppercase" itemprop="name"> <a class="byline__source__link text-decoration-none d-inline white-70" href="https://www.commondreams.org/news/netanyahu-west-bank" itemprop="url"><span class="byline__source__upper">C</span>ommon<span class="byline__source__upper">D</span>reams</a></span></dd>
            </dl>
        <time class="published updated meta-data visually-hidden"
    datetime="2025-09-13T15:23:10+00:00"
    itemprop="datePublished dateCreated"
    content="2025-09-13T15:23:10+00:00">
    September 13, 2025
  </time>
        <div class="d-none" itemprop="publisher" itemscope itemtype="http://schema.org/Organization">
  <a href="https://truthout.org" itemprop="url">
    <span itemprop="name">
      Truthout
    </span>
  </a>
</div>
      </div>

</header>

</article>

        <article class="ar-list row ms-0 me-0 mb-4 mb-md-3 pb-3 pb-md-0 border-bottom--gray--sm" itemscope itemtype="https://schema.org/ReportageNewsArticle">

<figure class="ar-list__th col ps-0 pe-0 pe-md-3">
    <a class="ar-list__th__lnk d-block" href="https://truthout.org/articles/israeli-army-conducts-mass-arrests-in-west-bank-city-detaining-over-1000/" title="Israeli Army Conducts Mass Arrests in West Bank City, Detaining Over 1,000">
      <img width="400" height="300" src="https://truthout.org/app/uploads/2025/09/GettyImages-2234178050-400x300.jpg" class="img-fluid cover wp-post-image" alt="Israeli soldiers detain Palestinians during a raid following the reported explosion of an Israeli military vehicle near a checkpoint west of Tulkarem in the occupied West Bank, on September 11, 2025." loading="lazy" decoding="async" srcset="https://truthout.org/app/uploads/2025/09/GettyImages-2234178050-400x300.jpg 400w, https://truthout.org/app/uploads/2025/09/GettyImages-2234178050-200x150.jpg 200w, https://truthout.org/app/uploads/2025/09/GettyImages-2234178050-800x600.jpg 800w, https://truthout.org/app/uploads/2025/09/GettyImages-2234178050-1200x900.jpg 1200w" sizes="auto, (max-width: 400px) 100vw, 400px" />
    </a>
  </figure>

<header class="ar-list__con col d-flex flex-column ps-md-3 pe-md-0">

<div class="before-headline mt-0 mb-3 mb-md-2 fs-13 d-inline text-uppercase font-sans text-decoration-none black-65">
  <!-- components/category-terms -->
  <div class="categories d-inline">
                  <a href="https://truthout.org/category/news/" rel='category' class="news text-decoration-none black-65">News</a>
            </div>
  <span class="separator px-1">|</span>

      <div class="ar__section d-inline"><a href="https://truthout.org/section/humanrights/" rel="section" class="ar__section__link humanrights text-decoration-none black-70" >Human Rights</a></div>
  </div>

<h2 class="ar-list__ti mb-3 mb-md-2" itemprop="headline">
      <a href="https://truthout.org/articles/israeli-army-conducts-mass-arrests-in-west-bank-city-detaining-over-1000/">Israeli Army Conducts Mass Arrests in West Bank City, Detaining Over 1,000</a>
    </h2>

<div class="ar-list__sum mb-3 mb-md-1" itemprop="description">
         Images show hundreds of Palestinian men, seemingly grabbed at random, being marched through the streets of Tulkarem.
      </div>



      <div class="ar-list__meta d-inline mb-auto">
        <!-- components/authors -->
    <dl class="byline list-inline font-sans d-inline mt-2 mb-0 white-70">
        <dt class="byline__label d-inline me-0">By</dt>
                  <dd class="byline__author author vcard d-inline me-0" itemprop="author" itemscope itemtype="https://schema.org/Person">
            <span class="byline__author__name" itemprop="name">
              <a class="byline__author__link url fn text-decoration-none white-70" href="https://truthout.org/authors/qassam-muaddi/" itemprop="url" rel="author">Qassam Muaddi</a>
            </span>

<span class="separator">, </span>
                      </dd>

                  <dd class="byline__source source org d-inline" itemprop="sourceOrganization" itemscope itemtype="https://schema.org/Organization"><span class="byline__source__name text-uppercase" itemprop="name"> <a class="byline__source__link text-decoration-none d-inline white-70" href="https://mondoweiss.net/2025/09/in-display-of-humiliation-israeli-army-detains-over-1000-palestinians-at-random-in-west-bank-city/" itemprop="url"><span class="byline__source__upper">M</span>ondoweiss</a></span></dd>
            </dl>
        <time class="published updated meta-data visually-hidden"
    datetime="2025-09-13T14:35:41+00:00"
    itemprop="datePublished dateCreated"
    content="2025-09-13T14:35:41+00:00">
    September 13, 2025
  </time>
        <div class="d-none" itemprop="publisher" itemscope itemtype="http://schema.org/Organization">
  <a href="https://truthout.org" itemprop="url">
    <span itemprop="name">
      Truthout
    </span>
  </a>
</div>
      </div>

</header>

</article>

        <article class="ar-list row ms-0 me-0 mb-4 mb-md-3 pb-3 pb-md-0 border-bottom--gray--sm" itemscope itemtype="https://schema.org/NewsArticle">

<figure class="ar-list__th col ps-0 pe-0 pe-md-3">
    <a class="ar-list__th__lnk d-block" href="https://truthout.org/articles/trumps-education-plan-seeks-to-make-cruel-domination-into-common-sense/" title="Trump’s Education Plan Seeks to Make Cruel Domination Into “Common Sense”">
      <img width="400" height="267" src="https://truthout.org/app/uploads/2025/09/GettyImages-1255159396.jpg" class="img-fluid cover wp-post-image" alt="Protestors on the campus of New College of Florida chase after Christopher Rufo, a conservative activist and New College of Florida trustee, after he attended a bill signing event featuring Florida Governor Ron DeSantis, who signed three education bills in Sarasota, Florida, on Monday, May 15, 2023." loading="lazy" decoding="async" srcset="https://truthout.org/app/uploads/2025/09/GettyImages-1255159396.jpg 8660w, https://truthout.org/app/uploads/2025/09/GettyImages-1255159396-400x267.jpg 400w, https://truthout.org/app/uploads/2025/09/GettyImages-1255159396-1200x800.jpg 1200w, https://truthout.org/app/uploads/2025/09/GettyImages-1255159396-200x133.jpg 200w, https://truthout.org/app/uploads/2025/09/GettyImages-1255159396-800x533.jpg 800w" sizes="auto, (max-width: 400px) 100vw, 400px" />
    </a>
  </figure>

<header class="ar-list__con col d-flex flex-column ps-md-3 pe-md-0">

<div class="before-headline mt-0 mb-3 mb-md-2 fs-13 d-inline text-uppercase font-sans text-decoration-none black-65">
  <!-- components/category-terms -->
  <div class="categories d-inline">
                  <a href="https://truthout.org/category/interview/" rel='category' class="interview text-decoration-none black-65">Interview</a>
            </div>
  <span class="separator px-1">|</span>

      <div class="ar__section d-inline"><a href="https://truthout.org/section/education-and-youth/" rel="section" class="ar__section__link education-and-youth text-decoration-none black-70" >Education &amp; Youth</a></div>
  </div>

<h2 class="ar-list__ti mb-3 mb-md-2" itemprop="headline">
      <a href="https://truthout.org/articles/trumps-education-plan-seeks-to-make-cruel-domination-into-common-sense/">Trump’s Education Plan Seeks to Make Cruel Domination Into “Common Sense”</a>
    </h2>

<div class="ar-list__sum mb-3 mb-md-1" itemprop="description">
         Trump isn’t even trying to hide his authoritarianism within social acceptability.
      </div>



      <div class="ar-list__meta d-inline mb-auto">
        <!-- components/authors -->
    <dl class="byline list-inline font-sans d-inline mt-2 mb-0 white-70">
        <dt class="byline__label d-inline me-0">By</dt>
                  <dd class="byline__author author vcard d-inline me-0" itemprop="author" itemscope itemtype="https://schema.org/Person">
            <span class="byline__author__name" itemprop="name">
              <a class="byline__author__link url fn text-decoration-none white-70" href="https://truthout.org/authors/george-yancy/" itemprop="url" rel="author">George Yancy</a>
            </span>

<span class="separator">, </span>
                      </dd>

                  <dd class="byline__source source org d-inline" itemprop="sourceOrganization" itemscope itemtype="https://schema.org/Organization"><span class="byline__source__name text-uppercase" itemprop="name"> <a class="byline__source__link text-decoration-none d-inline white-70" href="https://truthout.org" itemprop="url"><span class="byline__source__upper">T</span>ruthout</a></span></dd>
            </dl>
        <time class="published updated meta-data visually-hidden"
    datetime="2025-09-13T13:42:40+00:00"
    itemprop="datePublished dateCreated"
    content="2025-09-13T13:42:40+00:00">
    September 13, 2025
  </time>
        <div class="d-none" itemprop="publisher" itemscope itemtype="http://schema.org/Organization">
  <a href="https://truthout.org" itemprop="url">
    <span itemprop="name">
      Truthout
    </span>
  </a>
</div>
      </div>

</header>

</article>

        <article class="ar-list row ms-0 me-0 mb-4 mb-md-3 pb-3 pb-md-0 border-bottom--gray--sm" itemscope itemtype="https://schema.org/AnalysisNewsArticle">

<figure class="ar-list__th col ps-0 pe-0 pe-md-3">
    <a class="ar-list__th__lnk d-block" href="https://truthout.org/articles/targeting-venezuela-trump-escalates-us-campaign-of-aggression-in-latin-america/" title="Targeting Venezuela, Trump Escalates US Campaign of Aggression in Latin America">
      <img width="400" height="300" src="https://truthout.org/app/uploads/2025/09/GettyImages-2227283732-400x300.jpg" class="img-fluid cover wp-post-image" alt="An activist holds a poster depicting U.S. President Donald Trump bearing devil horns during a protest in defense of national sovereignty following the U.S. government trade taxes and sanctions on Brazil, near the U.S. consulate, in Sao Paulo, Brazil, on August 1, 2025." loading="lazy" decoding="async" srcset="https://truthout.org/app/uploads/2025/09/GettyImages-2227283732-400x300.jpg 400w, https://truthout.org/app/uploads/2025/09/GettyImages-2227283732-200x150.jpg 200w, https://truthout.org/app/uploads/2025/09/GettyImages-2227283732-800x600.jpg 800w, https://truthout.org/app/uploads/2025/09/GettyImages-2227283732-1200x900.jpg 1200w, https://truthout.org/app/uploads/2025/09/GettyImages-2227283732-2400x1800.jpg 2400w" sizes="auto, (max-width: 400px) 100vw, 400px" />
    </a>
  </figure>

<header class="ar-list__con col d-flex flex-column ps-md-3 pe-md-0">

<div class="before-headline mt-0 mb-3 mb-md-2 fs-13 d-inline text-uppercase font-sans text-decoration-none black-65">
  <!-- components/category-terms -->
  <div class="categories d-inline">
                  <a href="https://truthout.org/category/news-analysis/" rel='category' class="news-analysis text-decoration-none black-65">News Analysis</a>
            </div>
  <span class="separator px-1">|</span>

      <div class="ar__section d-inline"><a href="https://truthout.org/section/war-and-peace/" rel="section" class="ar__section__link war-and-peace text-decoration-none black-70" >War &amp; Peace</a></div>
  </div>

<h2 class="ar-list__ti mb-3 mb-md-2" itemprop="headline">
      <a href="https://truthout.org/articles/targeting-venezuela-trump-escalates-us-campaign-of-aggression-in-latin-america/">Targeting Venezuela, Trump Escalates US Campaign of Aggression in Latin America</a>
    </h2>

<div class="ar-list__sum mb-3 mb-md-1" itemprop="description">
         The US and Latin American right have long mobilized to remove challenges to their traditional privileges and control.
      </div>



      <div class="ar-list__meta d-inline mb-auto">
        <!-- components/authors -->
    <dl class="byline list-inline font-sans d-inline mt-2 mb-0 white-70">
        <dt class="byline__label d-inline me-0">By</dt>
                  <dd class="byline__author author vcard d-inline me-0" itemprop="author" itemscope itemtype="https://schema.org/Person">
            <span class="byline__author__name" itemprop="name">
              <a class="byline__author__link url fn text-decoration-none white-70" href="https://truthout.org/authors/jonathan-ng/" itemprop="url" rel="author">Jonathan Ng</a>
            </span>

<span class="separator">, </span>
                      </dd>

                  <dd class="byline__source source org d-inline" itemprop="sourceOrganization" itemscope itemtype="https://schema.org/Organization"><span class="byline__source__name text-uppercase" itemprop="name"> <a class="byline__source__link text-decoration-none d-inline white-70" href="https://truthout.org" itemprop="url"><span class="byline__source__upper">T</span>ruthout</a></span></dd>
            </dl>
        <time class="published updated meta-data visually-hidden"
    datetime="2025-09-13T13:38:29+00:00"
    itemprop="datePublished dateCreated"
    content="2025-09-13T13:38:29+00:00">
    September 13, 2025
  </time>
        <div class="d-none" itemprop="publisher" itemscope itemtype="http://schema.org/Organization">
  <a href="https://truthout.org" itemprop="url">
    <span itemprop="name">
      Truthout
    </span>
  </a>
</div>
      </div>

</header>

</article>



    </div>
  </aside>
  </article>
      </main>

<aside id="exclusivesBlock" class="mt-md-5 mb-6" aria-label="Featured articles only on Truthout"
    >
  <app-exclusives-block />
</aside>
<footer id="footer" class="footer container pb-5 py-md-5">
  <div class="row px-2">
    <div class="footer__first col-12 order-1 order-md-0">
      <div class="row">
        <section class="widget nav_menu-3 widget_nav_menu"><h3 class="widget__ti font-sans--con">News</h3><div class="menu-news-container"><ul id="menu-news" class="menu"><li id="menu-item-239543" class="menu-item menu-item-type-taxonomy menu-item-object-section menu-item-239543"><a href="https://truthout.org/section/culture-media/">Culture &amp; Media</a></li>
<li id="menu-item-239536" class="menu-item menu-item-type-taxonomy menu-item-object-section menu-item-239536"><a href="https://truthout.org/section/economy-and-labor/">Economy &amp; Labor</a></li>
<li id="menu-item-239542" class="menu-item menu-item-type-taxonomy menu-item-object-section menu-item-239542"><a href="https://truthout.org/section/education-and-youth/">Education &amp; Youth</a></li>
<li id="menu-item-239537" class="menu-item menu-item-type-taxonomy menu-item-object-section menu-item-239537"><a href="https://truthout.org/section/environment-and-health/">Environment &amp; Health</a></li>
<li id="menu-item-239540" class="menu-item menu-item-type-taxonomy menu-item-object-section menu-item-239540"><a href="https://truthout.org/section/humanrights/">Human Rights</a></li>
<li id="menu-item-250772" class="menu-item menu-item-type-taxonomy menu-item-object-section menu-item-250772"><a href="https://truthout.org/section/immigration/">Immigration</a></li>
<li id="menu-item-250773" class="menu-item menu-item-type-taxonomy menu-item-object-section menu-item-250773"><a href="https://truthout.org/section/lgbtq-rights/">LGBTQ Rights</a></li>
<li id="menu-item-239538" class="menu-item menu-item-type-taxonomy menu-item-object-section menu-item-239538"><a href="https://truthout.org/section/politics-and-elections/">Politics &amp; Elections</a></li>
<li id="menu-item-239541" class="menu-item menu-item-type-taxonomy menu-item-object-section menu-item-239541"><a href="https://truthout.org/section/prisons-and-policing/">Prisons &amp; Policing</a></li>
<li id="menu-item-250774" class="menu-item menu-item-type-taxonomy menu-item-object-section menu-item-250774"><a href="https://truthout.org/section/racial-justice/">Racial Justice</a></li>
<li id="menu-item-250775" class="menu-item menu-item-type-taxonomy menu-item-object-section menu-item-250775"><a href="https://truthout.org/section/reproductive-rights/">Reproductive Rights</a></li>
<li id="menu-item-239539" class="menu-item menu-item-type-taxonomy menu-item-object-section menu-item-239539"><a href="https://truthout.org/section/war-and-peace/">War &amp; Peace</a></li>
<li id="menu-item-269693" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-269693"><a href="https://truthout.org/series/">Series &#038; Podcasts</a></li>
</ul></div></section>      </div>
    </div>
    <div class="footer__middle col-12 order-2">
      <div class="row">
        <section class="widget nav_menu-6 widget_nav_menu"><h3 class="widget__ti font-sans--con">Series</h3><div class="menu-top-series-container"><ul id="menu-top-series" class="menu"><li id="menu-item-321224" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-321224"><a href="https://truthout.org/series/struggle-and-solidarity-writing-toward-palestinian-liberation/">Struggle and Solidarity: Writing Toward Palestinian Liberation</a></li>
<li id="menu-item-301981" class="menu-item menu-item-type-taxonomy menu-item-object-series menu-item-301981"><a href="https://truthout.org/series/despair-and-disparity-the-uneven-burdens-of-covid-19/">Despair and Disparity: The Uneven Burdens of COVID-19</a></li>
<li id="menu-item-301982" class="menu-item menu-item-type-taxonomy menu-item-object-series menu-item-301982"><a href="https://truthout.org/series/human-rights-and-global-wrongs/">Human Rights and Global Wrongs</a></li>
<li id="menu-item-301984" class="menu-item menu-item-type-taxonomy menu-item-object-series menu-item-301984"><a href="https://truthout.org/series/the-road-to-abolition/">The Road to Abolition</a></li>
<li id="menu-item-301983" class="menu-item menu-item-type-taxonomy menu-item-object-series menu-item-301983"><a href="https://truthout.org/series/public-intellectual/">The Public Intellectual</a></li>
<li id="menu-item-301986" class="menu-item menu-item-type-taxonomy menu-item-object-series menu-item-301986"><a href="https://truthout.org/series/movement-memos/">Movement Memos</a></li>
<li id="menu-item-301987" class="menu-item menu-item-type-taxonomy menu-item-object-series menu-item-301987"><a href="https://truthout.org/series/voting-wrongs/">Voting Wrongs</a></li>
<li id="menu-item-321225" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-321225"><a href="https://truthout.org/series/challenging-the-corporate-university/">Challenging the Corporate University</a></li>
<li id="menu-item-301985" class="menu-item menu-item-type-taxonomy menu-item-object-series menu-item-301985"><a href="https://truthout.org/series/covering-climate-now/">Covering Climate Now</a></li>
</ul></div></section><section class="widget nav_menu-7 widget_nav_menu"><h3 class="widget__ti font-sans--con">More</h3><div class="menu-more-container"><ul id="menu-more" class="menu"><li id="menu-item-235247" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-235247"><a href="https://truthout.org/about/">About</a></li>
<li id="menu-item-301966" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-301966"><a href="/?form=donate">Donate</a></li>
<li id="menu-item-302596" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-302596"><a href="https://truthout.org/manage-your-donation/">Manage Your Donation</a></li>
<li id="menu-item-304290" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-304290"><a href="https://truthout.org/more-ways-to-give/">Support Our Work</a></li>
<li id="menu-item-301964" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-301964"><a href="https://truthout.org/subscribe/">Subscribe</a></li>
<li id="menu-item-271195" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-271195"><a href="https://truthout.org/submission-guidelines/">Submission Guidelines</a></li>
<li id="menu-item-302491" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-302491"><a href="https://truthout.org/about/#financial">Financial Information</a></li>
<li id="menu-item-304262" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-304262"><a href="https://truthout.org/about/#dtpp">Privacy Policy</a></li>
<li id="menu-item-303901" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-303901"><a href="https://truthout.org/articles/keeley-schenwar-memorial-essay-prize/">Memorial Essay Prize</a></li>
<li id="menu-item-305046" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-305046"><a href="https://truthout.org/articles/truthout-center-for-grassroots-journalism/">Truthout Center for Grassroots Journalism</a></li>
<li id="menu-item-301961" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-301961"><a href="https://truthout.org/job-openings/">Job Openings</a></li>
<li id="menu-item-235007" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-235007"><a href="https://truthout.org/contact-us">Contact Us</a></li>
</ul></div></section>      </div>
    </div>
    <div class="footer__last col-12 order-0 order-md-3">
      <div class="row">
        <section class="widget_text widget custom_html-4 widget_custom_html"><div class="textwidget custom-html-widget"><ul class="nav--social nav flex-nowrap">

<li class="nav--social__item menu-item mb-3">
      <a class="me-md-4 social__btn d-flex flex-row align-items-center" href="https://www.facebook.com/truthout" aria-label="Facebook" target="_top" rel="nofollow">
        <span class="social-follow__label visually-hidden">Facebook</span>
        <svg aria-hidden="true" class="social__icon" version="1.1" role="img" focusable="false" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 x="0px" y="0px" viewBox="0 0 403.2 403.2" style="enable-background:new 0 0 403.2 403.2;" xml:space="preserve"><title>Facebook Circle Icon</title>
<path fill="currentColor" d="M201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S312.9,0,201.6,0z M174.8,310.3L174.8,310.3
	V222h-36.5v-41.5h36.5v-31.7c0-36,21.4-55.9,54.3-55.9c15.7,0,32.2,2.8,32.2,2.8v35.3h-18.1c-17.9,0-23.4,11.1-23.4,22.4v27h39.8
	l-6.4,41.5h-33.5v88.2l0,0"/>
</svg>      </a>
    </li>

<li class="nav--social__item menu-item mb-3">
      <a class="me-md-4 social__btn d-flex flex-row align-items-center" href="https://bsky.app/profile/truthout.org" aria-label="Bluesky" target="_top" rel="nofollow">
        <span class="social-follow__label visually-hidden">Bluesky</span>
        <svg aria-hidden="true" class="social__icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 403.2 403.2"><title>Bluesky Circle Icon</title><defs><style>.cls-1{stroke-width:0px;}</style></defs><g id="Layer_1" focusable="false"><path fill="currentColor" class="cls-1" d="m201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6,201.6-90.3,201.6-201.6S312.9,0,201.6,0Zm126.12,198.07c-9.35,33.42-43.43,41.94-73.74,36.79,52.99,9.02,66.47,38.89,37.36,68.76-55.29,56.73-79.46-14.23-85.66-32.42-1.14-3.33-1.67-4.89-1.67-3.57,0-1.33-.54.23-1.67,3.57-6.19,18.18-30.37,89.15-85.66,32.42-29.11-29.87-15.63-59.75,37.36-68.76-30.31,5.16-64.39-3.36-73.74-36.79-2.69-9.61-7.28-68.82-7.28-76.82,0-40.06,35.12-27.47,56.79-11.2h0c30.04,22.55,62.35,68.27,74.21,92.81,11.86-24.54,44.17-70.26,74.21-92.81,21.67-16.27,56.79-28.86,56.79,11.2,0,8-4.59,67.21-7.28,76.82Z"/></g></svg>      </a>
    </li>

<li class="nav--social__item menu-item mb-3">
      <a class="me-md-4 social__btn d-flex flex-row align-items-center" href="https://flipboard.com/@Truthout" aria-label="Flipboard" target="_top" rel="nofollow">
        <span class="social-follow__label visually-hidden">Flipboard</span>
        <svg aria-hidden="true" class="social__icon" version="1.1" role="img" focusable="false" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 x="0px" y="0px" viewBox="0 0 403.2 403.2" style="enable-background:new 0 0 403.2 403.2;" xml:space="preserve"><title>Flipboard Circle Icon</title>
<path fill="currentColor" d="M201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S312.9,0,201.6,0z M294.1,180.8h-60.9v60.9
	h-60.9v60.9h-60.9V119.9h182.6V180.8z"/>
</svg>      </a>
    </li>

<li class="nav--social__item menu-item mb-3">
      <a class="me-md-4 social__btn d-flex flex-row align-items-center" href="https://www.instagram.com/truthout/" aria-label="Instagram" target="_top" rel="nofollow">
        <span class="social-follow__label visually-hidden">Instagram</span>
        <svg aria-hidden="true" class="social__icon" role="img" data-name="Instagram Circle Icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 403.2 403.2"><title>Instagram Circle Icon</title><defs><style>.cls-1{stroke:#000;stroke-miterlimit:10;}</style></defs><path fill="currentColor" class="cls-1" d="M201.56,162.78A38.85,38.85,0,1,0,229,174.13,38.84,38.84,0,0,0,201.56,162.78Z"/><path fill="currentColor" d="M292.4,132.93h-.07A39.35,39.35,0,0,0,270.2,110.8c-15.29-6-51.69-4.68-68.65-4.68s-53.32-1.41-68.65,4.68a39.35,39.35,0,0,0-22.13,22.13c-6,15.29-4.68,51.72-4.68,68.67s-1.34,53.33,4.72,68.62a39.27,39.27,0,0,0,22.13,22.13c15.29,6,51.68,4.68,68.65,4.68s53.31,1.41,68.64-4.68a39.32,39.32,0,0,0,22.14-22.13c6.08-15.29,4.68-51.72,4.68-68.67S298.45,148.22,292.4,132.93Zm-35.67,91.5a59.83,59.83,0,1,1,4.52-22.86A59.75,59.75,0,0,1,256.73,224.43Zm19.85-79.72a13.77,13.77,0,0,1-3,4.52,13.82,13.82,0,0,1-9.85,4.08h0A13.84,13.84,0,0,1,256,151a13.94,13.94,0,1,1,21.66-11.59A13.73,13.73,0,0,1,276.58,144.71Z"/><path fill="currentColor" d="M201.6,0C90.3,0,0,90.3,0,201.6S90.3,403.2,201.6,403.2s201.6-90.3,201.6-201.6S312.9,0,201.6,0ZM317.23,249.62c-.94,18.65-5.2,35.18-18.82,48.77s-30.14,17.92-48.77,18.81c-19.22,1.09-76.87,1.09-96.08,0-18.66-.94-35.13-5.2-48.77-18.81S86.86,268.24,86,249.62c-1.09-19.23-1.09-76.87,0-96.09.94-18.65,5.15-35.18,18.82-48.77S135,86.89,153.56,86c19.22-1.09,76.86-1.09,96.08,0,18.66.94,35.18,5.2,48.77,18.81s17.93,30.15,18.82,48.81C318.32,172.75,318.32,230.4,317.23,249.62Z"/></svg>      </a>
    </li>

<li class="nav--social__item menu-item mb-3">
      <a class="me-md-4 social__btn d-flex flex-row align-items-center" href="https://twitter.com/truthout" aria-label="Twitter" target="_top" rel="nofollow">
        <span class="social-follow__label visually-hidden">Twitter</span>
        <svg aria-hidden="true" class="social__icon" version="1.1" role="img" focusable="false" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
	 x="0px" y="0px" viewBox="0 0 403.2 403.2" style="enable-background:new 0 0 403.2 403.2;" xml:space="preserve"><title>Twitter Circle Icon</title>
<path fill="currentColor" d="M201.6,0C90.3,0,0,90.3,0,201.6s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S312.9,0,201.6,0z M302,161.5
	c0.1,2,0.1,4.1,0.1,6.1c0,62.5-47.6,134.5-134.5,134.5c-26.8,0-51.7-7.8-72.6-21.2c3.8,0.4,7.5,0.6,11.4,0.6
	c22.1,0,42.5-7.5,58.7-20.2c-20.8-0.4-38.2-14.1-44.2-32.8c7.3,1.1,13.8,1.1,21.3-0.9c-21.6-4.4-37.8-23.4-37.8-46.4v-0.6
	c6.3,3.5,13.6,5.7,21.3,6c-13.2-8.8-21.1-23.5-21.1-39.4c0-8.8,2.3-16.9,6.4-23.9c23.3,28.7,58.3,47.4,97.5,49.5
	c-6.7-32.1,17.3-58.1,46.1-58.1c13.6,0,25.9,5.7,34.5,14.9c10.7-2,20.9-6,30-11.4c-3.5,11-11,20.2-20.8,26c9.5-1,18.7-3.7,27.3-7.4
	C319.3,146.4,311.2,154.8,302,161.5z"/>
</svg>      </a>
    </li>

<li class="nav--social__item menu-item mb-3">
      <a class="me-md-4 social__btn d-flex flex-row align-items-center" href="https://truthout.org/latest/feed/" aria-label="RSS" target="_top" rel="nofollow">
        <span class="social-follow__label visually-hidden">RSS</span>
        <svg aria-hidden="true" class="social__icon" version="1.1" role="img" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 viewBox="0 0 404.2 404.2" style="enable-background:new 0 0 404.2 404.2;" xml:space="preserve"><title>RSS Circle Icon</title>
<path fill="currentColor" d="M202.1,0.5C90.8,0.5,0.5,90.8,0.5,202.1s90.3,201.6,201.6,201.6s201.6-90.3,201.6-201.6S313.4,0.5,202.1,0.5z M151.1,287.6
	c-4,4-9.4,6.3-15.1,6.3c-11.8,0-21.4-9.5-21.4-21.3c0-11.8,9.5-21.4,21.3-21.4c11.8,0,21.4,9.5,21.4,21.3
	C157.4,278.1,155.1,283.6,151.1,287.6z M217.2,293.8c-0.4-0.5-0.7,0.1-1.7,0.1c-8.5,0-15.5-6.6-16-15c-1.8-36.5-33.4-68.1-69.9-70.5
	c-8.8-0.6-15.5-8.2-14.9-17c0,0,0,0,0,0c0.6-8.8,8.3-15.2,17-14.9c51.9,3.4,96.9,48.4,100.3,100.3
	C232.6,285.5,226,293.1,217.2,293.8C217.2,293.8,217.2,293.8,217.2,293.8L217.2,293.8z M280.8,293.2c-0.2,0.6-0.5,0.6-1.3,0.6
	c-8.6,0-15.7-6.8-16-15.4c-2.4-71-62.5-131.2-133.5-134.7c-8.4,0.1-15.2-6.6-15.4-15c0-0.4,0-0.7,0-1.1c0.4-8.8,7.8-15.7,16.6-15.3
	c0,0,0,0,0,0c87.2,3.6,161.1,77.6,164.2,164.2C296.4,286,289.6,293.5,280.8,293.2L280.8,293.2z"/>
</svg>      </a>
    </li>

</ul></div></section><section class="widget_text widget custom_html-2 widget_custom_html"><div class="textwidget custom-html-widget"><h3>
	Never Miss Another Story
</h3>
<p>
Get the news you want, delivered to your inbox every day.
</p>
<div class="subscribe--footer" data-callout-id="footerSubscribe" data-callout-theme="undefined" data-callout-placement="Footer Subscribe" data-callout-title="Undefined">

<div class='gf_browser_chrome gform_wrapper gform_legacy_markup_wrapper gform-theme--no-framework gform_wrapper gform_legacy_markup_wrapper gform-theme--no-framework_original_id_1 subscribe-form_wrapper input-group_wrapper' data-form-theme='legacy' data-form-index='0' id='gform_wrapper_1837364025' ><div id='gf_1837364025' class='gform_anchor' tabindex='-1'></div><form method='post' enctype='multipart/form-data' target='gform_ajax_frame_1837364025' id='gform_1837364025' class='subscribe-form input-group' action='/articles/goodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult/#gf_1837364025' data-formid='1' novalidate>
                        <div class='gform-body gform_body'><ul id='gform_fields_1837364025' class='gform_fields top_label form_sublabel_below description_below validation_below'><li id="field_1_1" class="gfield gfield--type-email gfield_contains_required field_sublabel_below gfield--no-description field_description_below hidden_label field_validation_below gfield_visibility_visible"  ><label class='gfield_label gform-field-label' for='input_1837364025_1'>Email<span class="gfield_required"><span class="gfield_required gfield_required_asterisk">*</span></span></label><div class='ginput_container ginput_container_email'>
                            <input name='input_1' id='input_1837364025_1' type='email' value='' class='medium'   placeholder='&#x6e;&#x61;&#x6d;&#101;&#64;em&#x61;&#x69;&#x6c;&#46;&#99;om' aria-required="true" aria-invalid="false"  />
                        </div></li><li id="field_1_5" class="gfield gfield--type-hidden gform_hidden field_sublabel_below gfield--no-description field_description_below field_validation_below gfield_visibility_visible"  ><div class='ginput_container ginput_container_text'><input name='input_5' id='input_1837364025_5' type='hidden' class='gform_hidden'  aria-invalid="false" value='' /></div></li><li id="field_1_6" class="gfield gfield--type-hidden gform_hidden field_sublabel_below gfield--no-description field_description_below field_validation_below gfield_visibility_visible"  ><div class='ginput_container ginput_container_text'><input name='input_6' id='input_1837364025_6' type='hidden' class='gform_hidden'  aria-invalid="false" value='' /></div></li><li id="field_1_7" class="gfield gfield--type-hidden gform_hidden field_sublabel_below gfield--no-description field_description_below field_validation_below gfield_visibility_visible"  ><div class='ginput_container ginput_container_text'><input name='input_7' id='input_1837364025_7' type='hidden' class='gform_hidden'  aria-invalid="false" value='' /></div></li><li id="field_1_9" class="gfield gfield--type-hidden gform_hidden field_sublabel_below gfield--no-description field_description_below field_validation_below gfield_visibility_visible"  ><div class='ginput_container ginput_container_text'><input name='input_9' id='input_1837364025_9' type='hidden' class='gform_hidden'  aria-invalid="false" value='' /></div></li><li id="field_1_8" class="gfield gfield--type-hidden gform_hidden field_sublabel_below gfield--no-description field_description_below field_validation_below gfield_visibility_visible"  ><div class='ginput_container ginput_container_text'><input name='input_8' id='input_1837364025_8' type='hidden' class='gform_hidden'  aria-invalid="false" value='' /></div></li><li id="field_1_10" class="gfield gfield--type-hidden gform_hidden field_sublabel_below gfield--no-description field_description_below field_validation_below gfield_visibility_visible"  ><div class='ginput_container ginput_container_text'><input name='input_10' id='input_1837364025_10' type='hidden' class='gform_hidden'  aria-invalid="false" value='' /></div></li><li id="field_1_11" class="gfield gfield--type-honeypot gform_validation_container field_sublabel_below gfield--has-description field_description_below field_validation_below gfield_visibility_visible"  ><label class='gfield_label gform-field-label' for='input_1837364025_11'>Name</label><div class='ginput_container'><input name='input_11' id='input_1837364025_11' type='text' value='' autocomplete='new-password'/></div><div class='gfield_description' id='gfield_description_1_11'>This field is for validation purposes and should be left unchanged.</div></li></ul></div>
        <div class='gform-footer gform_footer top_label'> <input type='submit' id='gform_submit_button_1837364025' class='gform_button button' onclick='gform.submission.handleButtonClick(this);' data-submission-type='submit' value='Subscribe'  /> <input type='hidden' name='gform_ajax' value='form_id=1&amp;title=&amp;description=&amp;tabindex=0&amp;theme=legacy&amp;hash=593d1db39c763ae878bbad5d2b573973' />
            <input type='hidden' class='gform_hidden' name='gform_submission_method' data-js='gform_submission_method_1' value='iframe' />
            <input type='hidden' class='gform_hidden' name='gform_theme' data-js='gform_theme_1' id='gform_theme_1' value='legacy' />
            <input type='hidden' class='gform_hidden' name='gform_style_settings' data-js='gform_style_settings_1' id='gform_style_settings_1' value='' />
            <input type='hidden' class='gform_hidden' name='is_submit_1' value='1' />
            <input type='hidden' class='gform_hidden' name='gform_submit' value='1' />

            <input type='hidden' class='gform_hidden' name='gform_unique_id' value='' />
            <input type='hidden' class='gform_hidden' name='state_1' value='WyJbXSIsIjY1ZDU1NDE3M2ZkMThlYjM4YzM3YTA3MGIxNTlkNjBhIl0=' />
            <input type='hidden' autocomplete='off' class='gform_hidden' name='gform_target_page_number_1' id='gform_target_page_number_1837364025_1' value='0' />
            <input type='hidden' autocomplete='off' class='gform_hidden' name='gform_source_page_number_1' id='gform_source_page_number_1837364025_1' value='1' />
            <input type='hidden' name='gform_random_id' value='1837364025' /><input type='hidden' name='gform_field_values' value='' />

        </div>
                        </form>
                        </div>
		                <iframe style='display:none;width:0px;height:0px;' src='about:blank' name='gform_ajax_frame_1837364025' id='gform_ajax_frame_1837364025' title='This iframe contains the logic required to handle Ajax powered Gravity Forms.'></iframe>
		                <script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script>
gform.initializeOnLoaded( function() {gformInitSpinner( 1837364025, 'https://truthout.org/app/plugins/gravityforms/images/spinner.svg', true );jQuery('#gform_ajax_frame_1837364025').on('load',function(){var contents = jQuery(this).contents().find('*').html();var is_postback = contents.indexOf('GF_AJAX_POSTBACK') >= 0;if(!is_postback){return;}var form_content = jQuery(this).contents().find('#gform_wrapper_1837364025');var is_confirmation = jQuery(this).contents().find('#gform_confirmation_wrapper_1837364025').length > 0;var is_redirect = contents.indexOf('gformRedirect(){') >= 0;var is_form = form_content.length > 0 && ! is_redirect && ! is_confirmation;var mt = parseInt(jQuery('html').css('margin-top'), 10) + parseInt(jQuery('body').css('margin-top'), 10) + 100;if(is_form){jQuery('#gform_wrapper_1837364025').html(form_content.html());if(form_content.hasClass('gform_validation_error')){jQuery('#gform_wrapper_1837364025').addClass('gform_validation_error');} else {jQuery('#gform_wrapper_1837364025').removeClass('gform_validation_error');}setTimeout( function() { /* delay the scroll by 50 milliseconds to fix a bug in chrome */ jQuery(document).scrollTop(jQuery('#gform_wrapper_1837364025').offset().top - mt); }, 50 );if(window['gformInitDatepicker']) {gformInitDatepicker();}if(window['gformInitPriceFields']) {gformInitPriceFields();}var current_page = jQuery('#gform_source_page_number_1837364025_1').val();gformInitSpinner( 1837364025, 'https://truthout.org/app/plugins/gravityforms/images/spinner.svg', true );jQuery(document).trigger('gform_page_loaded', [1837364025, current_page]);window['gf_submitting_1837364025'] = false;}else if(!is_redirect){var confirmation_content = jQuery(this).contents().find('.GF_AJAX_POSTBACK').html();if(!confirmation_content){confirmation_content = contents;}jQuery('#gform_wrapper_1837364025').replaceWith(confirmation_content);jQuery(document).scrollTop(jQuery('#gf_1837364025').offset().top - mt);jQuery(document).trigger('gform_confirmation_loaded', [1837364025]);window['gf_submitting_1837364025'] = false;wp.a11y.speak(jQuery('#gform_confirmation_message_1837364025').text());}else{jQuery('#gform_1837364025').append(contents);if(window['gformRedirect']) {gformRedirect();}}jQuery(document).trigger("gform_pre_post_render", [{ formId: "1", currentPage: "current_page", abort: function() { this.preventDefault(); } }]);        if (event && event.defaultPrevented) {                return;        }        const gformWrapperDiv = document.getElementById( "gform_wrapper_1" );        if ( gformWrapperDiv ) {            const visibilitySpan = document.createElement( "span" );            visibilitySpan.id = "gform_visibility_test_1";            gformWrapperDiv.insertAdjacentElement( "afterend", visibilitySpan );        }        const visibilityTestDiv = document.getElementById( "gform_visibility_test_1" );        let postRenderFired = false;        function triggerPostRender() {            if ( postRenderFired ) {                return;            }            postRenderFired = true;            gform.core.triggerPostRenderEvents( 1, current_page );            if ( visibilityTestDiv ) {                visibilityTestDiv.parentNode.removeChild( visibilityTestDiv );            }        }        function debounce( func, wait, immediate ) {            var timeout;            return function() {                var context = this, args = arguments;                var later = function() {                    timeout = null;                    if ( !immediate ) func.apply( context, args );                };                var callNow = immediate && !timeout;                clearTimeout( timeout );                timeout = setTimeout( later, wait );                if ( callNow ) func.apply( context, args );            };        }        const debouncedTriggerPostRender = debounce( function() {            triggerPostRender();        }, 200 );        if ( visibilityTestDiv && visibilityTestDiv.offsetParent === null ) {            const observer = new MutationObserver( ( mutations ) => {                mutations.forEach( ( mutation ) => {                    if ( mutation.type === 'attributes' && visibilityTestDiv.offsetParent !== null ) {                        debouncedTriggerPostRender();                        observer.disconnect();                    }                });            });            observer.observe( document.body, {                attributes: true,                childList: false,                subtree: true,                attributeFilter: [ 'style', 'class' ],            });        } else {            triggerPostRender();        }    } );} );
</script>

</div></div></section>      </div>
    </div>
  </div>

<small class="footer__copyright d-block py-5 text-center text-black fw-bolder">&copy; 2025 Truthout</small>
</footer>

<aside id="c5bc0f85a9fea2e3310de5d7086f96222" class="hello hello--visible fixed-bottom" aria-label="Hellobar notification">
    <button class="hello__toggle btn-reset" type="button" data-bs-toggle="collapse" data-bs-target="#c5bc0f85a9fea2e3310de5d7086f96222" aria-expanded="false" aria-controls="c5bc0f85a9fea2e3310de5d7086f96222"><span class="visually-hidden">Toggle Donation Bar</span><i class="fal fa-angle-up" aria-hidden="true"></i><i class="fal fa-angle-down" aria-hidden="true"></i>
</button>  <div class="truth-hellobar-placement" id="truth-1156375436"><div class="callout p-4 m-0 callout--hellobar callout--dark" id="truth-303544" data-callout-id="303544" data-callout-theme="dark" data-callout-placement="Hellobar" data-callout-title="Hellobar Two-Column (FRU)"><div class="container px-0">
  <div class="row justify-content-center">
    <div class="col me-auto">
		<h4 class="hello__title text-left" style="text-transform:uppercase;">Critical Fundraiser: 10 Days to Raise $50,000</h4>
    </div>
  </div>
  <div class="row">
	  <div class="col-12 col-md-10"><p style="font-family:sans-serif;">Truthout relies on reader support to publish nonprofit, independent journalism. Help us meet our publishing costs this month — make a tax-deductible donation today!</p></div>
    <div class="col-12 col-md-2 d-flex flex-column justify-content-center align-items-center mt-2">
		<a href="#XKQKBZSK" style="display: none"></a>
    </div>
  </div>
</div>
</div></div></aside>

</div>

<script type='text/javascript'>
/* <![CDATA[ */
var advancedAds = {"adHealthNotice":{"enabled":true,"pattern":"AdSense fallback was loaded for empty AdSense ad \"[ad_title]\""},"frontendPrefix":"truth-"};

/* ]]> */
</script>
<script>(function(){var advanced_ads_ga_UID="G-3WMTR7B28R",advanced_ads_ga_anonymIP=!!1;window.advanced_ads_check_adblocker=function(){var t=[],n=null;function e(t){var n=window.requestAnimationFrame||window.mozRequestAnimationFrame||window.webkitRequestAnimationFrame||function(t){return setTimeout(t,16)};n.call(window,t)}return e((function(){var a=document.createElement("div");a.innerHTML="&nbsp;",a.setAttribute("class","ad_unit ad-unit text-ad text_ad pub_300x250"),a.setAttribute("style","width: 1px !important; height: 1px !important; position: absolute !important; left: 0px !important; top: 0px !important; overflow: hidden !important;"),document.body.appendChild(a),e((function(){var e,o,i=null===(e=(o=window).getComputedStyle)||void 0===e?void 0:e.call(o,a),d=null==i?void 0:i.getPropertyValue("-moz-binding");n=i&&"none"===i.getPropertyValue("display")||"string"==typeof d&&-1!==d.indexOf("about:");for(var c=0,r=t.length;c<r;c++)t[c](n);t=[]}))})),function(e){"undefined"==typeof advanced_ads_adblocker_test&&(n=!0),null!==n?e(n):t.push(e)}}(),(()=>{function t(t){this.UID=t,this.analyticsObject="function"==typeof gtag;var n=this;return this.count=function(){gtag("event","AdBlock",{event_category:"Advanced Ads",event_label:"Yes",non_interaction:!0,send_to:n.UID})},function(){if(!n.analyticsObject){var e=document.createElement("script");e.src="https://www.googletagmanager.com/gtag/js?id="+t,e.async=!0,document.body.appendChild(e),window.dataLayer=window.dataLayer||[],window.gtag=function(){dataLayer.push(arguments)},n.analyticsObject=!0,gtag("js",new Date)}var a={send_page_view:!1,transport_type:"beacon"};window.advanced_ads_ga_anonymIP&&(a.anonymize_ip=!0),gtag("config",t,a)}(),this}advanced_ads_check_adblocker((function(n){n&&new t(advanced_ads_ga_UID).count()}))})();})();</script><script type="speculationrules">
{"prefetch":[{"source":"document","where":{"and":[{"href_matches":"\/*"},{"not":{"href_matches":["\/wp\/wp-*.php","\/wp\/wp-admin\/*","\/app\/uploads\/*","\/app\/*","\/app\/plugins\/*","\/app\/themes\/truthout5\/*","\/*\\?(.+)"]}},{"not":{"selector_matches":"a[rel~=\"nofollow\"]"}},{"not":{"selector_matches":".no-prefetch, .no-prefetch a"}}]},"eagerness":"conservative"}]}
</script>
<script src="https://truthout.org/app/plugins/advanced-ads-pro/assets/js/postscribe.js?ver=3.0.5" id="advanced-ads-pro/postscribe-js"></script>
<script id="advanced-ads-pro/cache_busting-js-extra">
var advanced_ads_pro_ajax_object = {"ajax_url":"https:\/\/truthout.org\/wp\/wp-admin\/admin-ajax.php","lazy_load_module_enabled":"1","lazy_load":{"default_offset":100,"offsets":[]},"moveintohidden":"","wp_timezone_offset":"-14400","the_id":"218684","is_singular":"1"};
var advanced_ads_responsive = {"reload_on_resize":"0"};
</script>
<script src="https://truthout.org/app/plugins/advanced-ads-pro/assets/dist/front.js?ver=3.0.5" id="advanced-ads-pro/cache_busting-js"></script>
<script id="advanced-ads-layer-footer-js-js-extra">
var advanced_ads_layer_settings = {"layer_class":"truth-layer","placements":[329219,329218,329217]};
</script>
<script src="https://truthout.org/app/plugins/advanced-ads-layer/public/assets/js/layer.js?ver=2.0.2" id="advanced-ads-layer-footer-js-js"></script>
<script id="advanced-ads-pro-main-js-extra">
var advanced_ads_cookies = {"cookie_path":"\/","cookie_domain":""};
</script>
<script src="https://truthout.org/app/plugins/advanced-ads-pro/assets/dist/advanced-ads-pro.js?ver=3.0.5" id="advanced-ads-pro-main-js"></script>
<script id="advanced-ads-sticky-footer-js-js-extra">
var advanced_ads_sticky_settings = {"check_position_fixed":"","sticky_class":"truth-sticky","placements":[]};
</script>
<script src="https://truthout.org/app/plugins/advanced-ads-sticky-ads/assets/dist/sticky.js?ver=2.0.2" id="advanced-ads-sticky-footer-js-js"></script>
<script id="truthout/vendor.js-js-before">
!function(){"use strict";var n,e={},r={};function t(n){var o=r[n];if(void 0!==o)return o.exports;var u=r[n]={exports:{}};return e[n](u,u.exports,t),u.exports}t.m=e,n=[],t.O=function(e,r,o,u){if(!r){var i=1/0;for(l=0;l<n.length;l++){r=n[l][0],o=n[l][1],u=n[l][2];for(var f=!0,c=0;c<r.length;c++)(!1&u||i>=u)&&Object.keys(t.O).every((function(n){return t.O[n](r[c])}))?r.splice(c--,1):(f=!1,u<i&&(i=u));if(f){n.splice(l--,1);var a=o();void 0!==a&&(e=a)}}return e}u=u||0;for(var l=n.length;l>0&&n[l-1][2]>u;l--)n[l]=n[l-1];n[l]=[r,o,u]},t.n=function(n){var e=n&&n.__esModule?function(){return n.default}:function(){return n};return t.d(e,{a:e}),e},t.d=function(n,e){for(var r in e)t.o(e,r)&&!t.o(n,r)&&Object.defineProperty(n,r,{enumerable:!0,get:e[r]})},t.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(n){if("object"==typeof window)return window}}(),t.o=function(n,e){return Object.prototype.hasOwnProperty.call(n,e)},t.r=function(n){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(n,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(n,"__esModule",{value:!0})},function(){var n={546:0,126:0,692:0};t.O.j=function(e){return 0===n[e]};var e=function(e,r){var o,u,i=r[0],f=r[1],c=r[2],a=0;if(i.some((function(e){return 0!==n[e]}))){for(o in f)t.o(f,o)&&(t.m[o]=f[o]);if(c)var l=c(t)}for(e&&e(r);a<i.length;a++)u=i[a],t.o(n,u)&&n[u]&&n[u][0](),n[u]=0;return t.O(l)},r=self.webpackChunk=self.webpackChunk||[];r.forEach(e.bind(null,0)),r.push=e.bind(null,r.push.bind(r))}()}();
</script>
<script src="https://truthout.org/app/themes/truthout5/public/scripts/vendor.js?id=34b0e8733ea8c9c5d349cd1e76694465" id="truthout/vendor.js-js"></script>
<script src="https://truthout.org/app/themes/truthout5/public/scripts/app.js?id=4d2c2d405acb4eccf529c3a7286513de" id="truthout/app.js-js"></script>
<script id="truthout/exclusives-js-before">
const articleData = {"restUrl":"https:\/\/truthout.org\/wp-json","ID":218684,"appPath":"goodbye-to-all-that-reflections-of-a-gop-operative-who-left-the-cult","logo":"https:\/\/truthout.org\/app\/themes\/truthout5\/public\/images\/t-logo-white.svg?id=728ea422e90b9afb23229e29468b3ecf"}
</script>
<script src="https://truthout.org/app/themes/truthout5/public/scripts/exclusives.js?id=b78a7979e278f26fa44de4f6f009ccbe" id="truthout/exclusives-js"></script>
<script src="https://truthout.org/wp/wp-includes/js/dist/dom-ready.min.js?ver=f77871ff7694fffea381" id="wp-dom-ready-js"></script>
<script src="https://truthout.org/wp/wp-includes/js/dist/hooks.min.js?ver=4d63a3d491d11ffd8ac6" id="wp-hooks-js"></script>
<script src="https://truthout.org/wp/wp-includes/js/dist/i18n.min.js?ver=5e580eb46a90c2b997e6" id="wp-i18n-js"></script>
<script id="wp-i18n-js-after">
wp.i18n.setLocaleData( { 'text direction\u0004ltr': [ 'ltr' ] } );
</script>
<script src="https://truthout.org/wp/wp-includes/js/dist/a11y.min.js?ver=3156534cc54473497e14" id="wp-a11y-js"></script>
<script defer='defer' src="https://truthout.org/app/plugins/gravityforms/js/jquery.json.min.js?ver=2.9.13" id="gform_json-js"></script>
<script id="gform_gravityforms-js-extra">
var gform_i18n = {"datepicker":{"days":{"monday":"Mo","tuesday":"Tu","wednesday":"We","thursday":"Th","friday":"Fr","saturday":"Sa","sunday":"Su"},"months":{"january":"January","february":"February","march":"March","april":"April","may":"May","june":"June","july":"July","august":"August","september":"September","october":"October","november":"November","december":"December"},"firstDay":1,"iconText":"Select date"}};
var gf_legacy_multi = [];
var gform_gravityforms = {"strings":{"invalid_file_extension":"This type of file is not allowed. Must be one of the following:","delete_file":"Delete this file","in_progress":"in progress","file_exceeds_limit":"File exceeds size limit","illegal_extension":"This type of file is not allowed.","max_reached":"Maximum number of files reached","unknown_error":"There was a problem while saving the file on the server","currently_uploading":"Please wait for the uploading to complete","cancel":"Cancel","cancel_upload":"Cancel this upload","cancelled":"Cancelled"},"vars":{"images_url":"https:\/\/truthout.org\/app\/plugins\/gravityforms\/images"}};
var gf_global = {"gf_currency_config":{"name":"U.S. Dollar","symbol_left":"$","symbol_right":"","symbol_padding":"","thousand_separator":",","decimal_separator":".","decimals":2,"code":"USD"},"base_url":"https:\/\/truthout.org\/app\/plugins\/gravityforms","number_formats":[],"spinnerUrl":"https:\/\/truthout.org\/app\/plugins\/gravityforms\/images\/spinner.svg","version_hash":"d0543887d01b4a5fc60436654a5ef58d","strings":{"newRowAdded":"New row added.","rowRemoved":"Row removed","formSaved":"The form has been saved.  The content contains the link to return and complete the form."}};
var gf_global = {"gf_currency_config":{"name":"U.S. Dollar","symbol_left":"$","symbol_right":"","symbol_padding":"","thousand_separator":",","decimal_separator":".","decimals":2,"code":"USD"},"base_url":"https:\/\/truthout.org\/app\/plugins\/gravityforms","number_formats":[],"spinnerUrl":"https:\/\/truthout.org\/app\/plugins\/gravityforms\/images\/spinner.svg","version_hash":"d0543887d01b4a5fc60436654a5ef58d","strings":{"newRowAdded":"New row added.","rowRemoved":"Row removed","formSaved":"The form has been saved.  The content contains the link to return and complete the form."}};
</script>
<script defer='defer' src="https://truthout.org/app/plugins/gravityforms/js/gravityforms.min.js?ver=2.9.13" id="gform_gravityforms-js"></script>
<script defer='defer' src="https://truthout.org/app/plugins/gravityforms/js/placeholders.jquery.min.js?ver=2.9.13" id="gform_placeholder-js"></script>
<script defer='defer' src="https://truthout.org/app/plugins/gravityforms/assets/js/dist/utils.min.js?ver=380b7a5ec0757c78876bc8a59488f2f3" id="gform_gravityforms_utils-js"></script>
<script defer='defer' src="https://truthout.org/app/plugins/gravityforms/assets/js/dist/vendor-theme.min.js?ver=21e5a4db1670166692ac5745329bfc80" id="gform_gravityforms_theme_vendors-js"></script>
<script id="gform_gravityforms_theme-js-extra">
var gform_theme_config = {"common":{"form":{"honeypot":{"version_hash":"d0543887d01b4a5fc60436654a5ef58d"},"ajax":{"ajaxurl":"https:\/\/truthout.org\/wp\/wp-admin\/admin-ajax.php","ajax_submission_nonce":"eeb85d7ef7","i18n":{"step_announcement":"Step %1$s of %2$s, %3$s","unknown_error":"There was an unknown error processing your request. Please try again."}}}},"hmr_dev":"","public_path":"https:\/\/truthout.org\/app\/plugins\/gravityforms\/assets\/js\/dist\/","config_nonce":"8d70855cea"};
</script>
<script defer='defer' src="https://truthout.org/app/plugins/gravityforms/assets/js/dist/scripts-theme.min.js?ver=b436459e6f25ebcd9e95ea18e1a35e19" id="gform_gravityforms_theme-js"></script>
<script>window.advads_admin_bar_items = [{"title":"Hellobar Placement","type":"placement","count":140},{"title":"Hellobar \u2014 FRU","type":"group","count":1},{"title":"Never miss another story","type":"ad","count":1},{"title":"Banners \u2014 Subscribe","type":"group","count":1},{"title":"Post Content \u2014\u00a0High","type":"placement","count":1},{"title":"2025-09 Main Campaign (FRU) Support media that fights fascism","type":"ad","count":1},{"title":"Banners \u2014\u00a0FRU","type":"group","count":1},{"title":"Post Content \u2014\u00a0After","type":"placement","count":1},{"title":"BCB 304025 Truthout is an indispensable resource...","type":"ad","count":1},{"title":"Banners \u2014 Top of Article Blurbs","type":"group","count":1},{"title":"Post Content - Before","type":"placement","count":1},{"title":"Hellobar Two-Column (FRU)","type":"ad","count":1}];</script><script>window.advads_has_ads = [["255392","ad","Never miss another story","off"],["331649","ad","2025-09 Main Campaign (FRU) Support media that fights fascism","off"],["304025","ad","BCB 304025 Truthout is an indispensable resource...","off"],["303544","ad","Hellobar Two-Column (FRU)","off"]];
( window.advanced_ads_ready || jQuery( document ).ready ).call( null, function() {if ( !window.advanced_ads_pro ) {console.log("Advanced Ads Pro: cache-busting can not be initialized");} });</script><script>!function(){window.advanced_ads_ready_queue=window.advanced_ads_ready_queue||[],advanced_ads_ready_queue.push=window.advanced_ads_ready;for(var d=0,a=advanced_ads_ready_queue.length;d<a;d++)advanced_ads_ready(advanced_ads_ready_queue[d])}();</script><script>
gform.initializeOnLoaded( function() { jQuery(document).on('gform_post_render', function(event, formId, currentPage){if(formId == 1) {if(typeof Placeholders != 'undefined'){
                        Placeholders.enable();
                    }} } );jQuery(document).on('gform_post_conditional_logic', function(event, formId, fields, isInit){} ) } );
</script>
<script>
gform.initializeOnLoaded( function() {jQuery(document).trigger("gform_pre_post_render", [{ formId: "1", currentPage: "1", abort: function() { this.preventDefault(); } }]);        if (event && event.defaultPrevented) {                return;        }        const gformWrapperDiv = document.getElementById( "gform_wrapper_1" );        if ( gformWrapperDiv ) {            const visibilitySpan = document.createElement( "span" );            visibilitySpan.id = "gform_visibility_test_1";            gformWrapperDiv.insertAdjacentElement( "afterend", visibilitySpan );        }        const visibilityTestDiv = document.getElementById( "gform_visibility_test_1" );        let postRenderFired = false;        function triggerPostRender() {            if ( postRenderFired ) {                return;            }            postRenderFired = true;            gform.core.triggerPostRenderEvents( 1, 1 );            if ( visibilityTestDiv ) {                visibilityTestDiv.parentNode.removeChild( visibilityTestDiv );            }        }        function debounce( func, wait, immediate ) {            var timeout;            return function() {                var context = this, args = arguments;                var later = function() {                    timeout = null;                    if ( !immediate ) func.apply( context, args );                };                var callNow = immediate && !timeout;                clearTimeout( timeout );                timeout = setTimeout( later, wait );                if ( callNow ) func.apply( context, args );            };        }        const debouncedTriggerPostRender = debounce( function() {            triggerPostRender();        }, 200 );        if ( visibilityTestDiv && visibilityTestDiv.offsetParent === null ) {            const observer = new MutationObserver( ( mutations ) => {                mutations.forEach( ( mutation ) => {                    if ( mutation.type === 'attributes' && visibilityTestDiv.offsetParent !== null ) {                        debouncedTriggerPostRender();                        observer.disconnect();                    }                });            });            observer.observe( document.body, {                attributes: true,                childList: false,                subtree: true,                attributeFilter: [ 'style', 'class' ],            });        } else {            triggerPostRender();        }    } );
</script>
  <script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","licenseKey":"549d3cf919","applicationID":"1385775879","transactionName":"MgdTY0cDCENVBkRYDgtNcFRBCwleGwxeVQQd","queueTime":0,"applicationTime":1134,"atts":"HkBQFQ8ZG00=","errorBeacon":"bam.nr-data.net","agent":""}</script></body>
</html>
