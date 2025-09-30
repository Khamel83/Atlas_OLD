# Content from https://fivethirtyeight.com/features/two-special-elections-on-tuesday-could-hint-at-another-blue-wave-in-2020/

*Retrieved: 2025-09-15T00:05:03.531445*

---

<!DOCTYPE html>
<html lang="en-US" class="no-js">
<head>
	<meta charset="UTF-8"><script type="text/javascript">(window.NREUM||(NREUM={})).init={ajax:{deny_list:["bam.nr-data.net"]}};(window.NREUM||(NREUM={})).loader_config={licenseKey:"f6169b8cc4",applicationID:"100041457"};;/*! For license information please see nr-loader-rum-1.297.0.min.js.LICENSE.txt */
(()=>{var e,t,r={122:(e,t,r)=>{"use strict";r.d(t,{a:()=>i});var n=r(944);function i(e,t){try{if(!e||"object"!=typeof e)return(0,n.R)(3);if(!t||"object"!=typeof t)return(0,n.R)(4);const r=Object.create(Object.getPrototypeOf(t),Object.getOwnPropertyDescriptors(t)),a=0===Object.keys(r).length?e:r;for(let s in a)if(void 0!==e[s])try{if(null===e[s]){r[s]=null;continue}Array.isArray(e[s])&&Array.isArray(t[s])?r[s]=Array.from(new Set([...e[s],...t[s]])):"object"==typeof e[s]&&"object"==typeof t[s]?r[s]=i(e[s],t[s]):r[s]=e[s]}catch(e){r[s]||(0,n.R)(1,e)}return r}catch(e){(0,n.R)(2,e)}}},555:(e,t,r)=>{"use strict";r.d(t,{D:()=>o,f:()=>s});var n=r(384),i=r(122);const a={beacon:n.NT.beacon,errorBeacon:n.NT.errorBeacon,licenseKey:void 0,applicationID:void 0,sa:void 0,queueTime:void 0,applicationTime:void 0,ttGuid:void 0,user:void 0,account:void 0,product:void 0,extra:void 0,jsAttributes:{},userAttributes:void 0,atts:void 0,transactionName:void 0,tNamePlain:void 0};function s(e){try{return!!e.licenseKey&&!!e.errorBeacon&&!!e.applicationID}catch(e){return!1}}const o=e=>(0,i.a)(e,a)},324:(e,t,r)=>{"use strict";r.d(t,{F3:()=>i,Xs:()=>a,xv:()=>n});const n="1.297.0",i="PROD",a="CDN"},154:(e,t,r)=>{"use strict";r.d(t,{OF:()=>c,RI:()=>i,WN:()=>d,bv:()=>a,gm:()=>s,mw:()=>o,sb:()=>u});var n=r(863);const i="undefined"!=typeof window&&!!window.document,a="undefined"!=typeof WorkerGlobalScope&&("undefined"!=typeof self&&self instanceof WorkerGlobalScope&&self.navigator instanceof WorkerNavigator||"undefined"!=typeof globalThis&&globalThis instanceof WorkerGlobalScope&&globalThis.navigator instanceof WorkerNavigator),s=i?window:"undefined"!=typeof WorkerGlobalScope&&("undefined"!=typeof self&&self instanceof WorkerGlobalScope&&self||"undefined"!=typeof globalThis&&globalThis instanceof WorkerGlobalScope&&globalThis),o=Boolean("hidden"===s?.document?.visibilityState),c=/iPad|iPhone|iPod/.test(s.navigator?.userAgent),u=c&&"undefined"==typeof SharedWorker,d=((()=>{const e=s.navigator?.userAgent?.match(/Firefox[/\s](\d+\.\d+)/);Array.isArray(e)&&e.length>=2&&e[1]})(),Date.now()-(0,n.t)())},241:(e,t,r)=>{"use strict";r.d(t,{W:()=>a});var n=r(154);const i="newrelic";function a(e={}){try{n.gm.dispatchEvent(new CustomEvent(i,{detail:e}))}catch(e){}}},687:(e,t,r)=>{"use strict";r.d(t,{Ak:()=>u,Ze:()=>f,x3:()=>d});var n=r(241),i=r(836),a=r(606),s=r(860),o=r(646);const c={};function u(e,t){const r={staged:!1,priority:s.P3[t]||0};l(e),c[e].get(t)||c[e].set(t,r)}function d(e,t){e&&c[e]&&(c[e].get(t)&&c[e].delete(t),p(e,t,!1),c[e].size&&g(e))}function l(e){if(!e)throw new Error("agentIdentifier required");c[e]||(c[e]=new Map)}function f(e="",t="feature",r=!1){if(l(e),!e||!c[e].get(t)||r)return p(e,t);c[e].get(t).staged=!0,g(e)}function g(e){const t=Array.from(c[e]);t.every((([e,t])=>t.staged))&&(t.sort(((e,t)=>e[1].priority-t[1].priority)),t.forEach((([t])=>{c[e].delete(t),p(e,t)})))}function p(e,t,r=!0){const s=e?i.ee.get(e):i.ee,c=a.i.handlers;if(!s.aborted&&s.backlog&&c){if((0,n.W)({agentIdentifier:e,type:"lifecycle",name:"drain",feature:t}),r){const e=s.backlog[t],r=c[t];if(r){for(let t=0;e&&t<e.length;++t)m(e[t],r);Object.entries(r).forEach((([e,t])=>{Object.values(t||{}).forEach((t=>{t[0]?.on&&t[0]?.context()instanceof o.y&&t[0].on(e,t[1])}))}))}}s.isolatedBacklog||delete c[t],s.backlog[t]=null,s.emit("drain-"+t,[])}}function m(e,t){var r=e[1];Object.values(t[r]||{}).forEach((t=>{var r=e[0];if(t[0]===r){var n=t[1],i=e[3],a=e[2];n.apply(i,a)}}))}},836:(e,t,r)=>{"use strict";r.d(t,{P:()=>o,ee:()=>c});var n=r(384),i=r(990),a=r(646),s=r(607);const o="nr@context:".concat(s.W),c=function e(t,r){var n={},s={},d={},l=!1;try{l=16===r.length&&u.initializedAgents?.[r]?.runtime.isolatedBacklog}catch(e){}var f={on:p,addEventListener:p,removeEventListener:function(e,t){var r=n[e];if(!r)return;for(var i=0;i<r.length;i++)r[i]===t&&r.splice(i,1)},emit:function(e,r,n,i,a){!1!==a&&(a=!0);if(c.aborted&&!i)return;t&&a&&t.emit(e,r,n);var o=g(n);m(e).forEach((e=>{e.apply(o,r)}));var u=v()[s[e]];u&&u.push([f,e,r,o]);return o},get:h,listeners:m,context:g,buffer:function(e,t){const r=v();if(t=t||"feature",f.aborted)return;Object.entries(e||{}).forEach((([e,n])=>{s[n]=t,t in r||(r[t]=[])}))},abort:function(){f._aborted=!0,Object.keys(f.backlog).forEach((e=>{delete f.backlog[e]}))},isBuffering:function(e){return!!v()[s[e]]},debugId:r,backlog:l?{}:t&&"object"==typeof t.backlog?t.backlog:{},isolatedBacklog:l};return Object.defineProperty(f,"aborted",{get:()=>{let e=f._aborted||!1;return e||(t&&(e=t.aborted),e)}}),f;function g(e){return e&&e instanceof a.y?e:e?(0,i.I)(e,o,(()=>new a.y(o))):new a.y(o)}function p(e,t){n[e]=m(e).concat(t)}function m(e){return n[e]||[]}function h(t){return d[t]=d[t]||e(f,t)}function v(){return f.backlog}}(void 0,"globalEE"),u=(0,n.Zm)();u.ee||(u.ee=c)},646:(e,t,r)=>{"use strict";r.d(t,{y:()=>n});class n{constructor(e){this.contextId=e}}},908:(e,t,r)=>{"use strict";r.d(t,{d:()=>n,p:()=>i});var n=r(836).ee.get("handle");function i(e,t,r,i,a){a?(a.buffer([e],i),a.emit(e,t,r)):(n.buffer([e],i),n.emit(e,t,r))}},606:(e,t,r)=>{"use strict";r.d(t,{i:()=>a});var n=r(908);a.on=s;var i=a.handlers={};function a(e,t,r,a){s(a||n.d,i,e,t,r)}function s(e,t,r,i,a){a||(a="feature"),e||(e=n.d);var s=t[a]=t[a]||{};(s[r]=s[r]||[]).push([e,i])}},878:(e,t,r)=>{"use strict";function n(e,t){return{capture:e,passive:!1,signal:t}}function i(e,t,r=!1,i){window.addEventListener(e,t,n(r,i))}function a(e,t,r=!1,i){document.addEventListener(e,t,n(r,i))}r.d(t,{DD:()=>a,jT:()=>n,sp:()=>i})},607:(e,t,r)=>{"use strict";r.d(t,{W:()=>n});const n=(0,r(566).bz)()},566:(e,t,r)=>{"use strict";r.d(t,{LA:()=>o,bz:()=>s});var n=r(154);const i="xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx";function a(e,t){return e?15&e[t]:16*Math.random()|0}function s(){const e=n.gm?.crypto||n.gm?.msCrypto;let t,r=0;return e&&e.getRandomValues&&(t=e.getRandomValues(new Uint8Array(30))),i.split("").map((e=>"x"===e?a(t,r++).toString(16):"y"===e?(3&a()|8).toString(16):e)).join("")}function o(e){const t=n.gm?.crypto||n.gm?.msCrypto;let r,i=0;t&&t.getRandomValues&&(r=t.getRandomValues(new Uint8Array(e)));const s=[];for(var o=0;o<e;o++)s.push(a(r,i++).toString(16));return s.join("")}},614:(e,t,r)=>{"use strict";r.d(t,{BB:()=>s,H3:()=>n,g:()=>u,iL:()=>c,tS:()=>o,uh:()=>i,wk:()=>a});const n="NRBA",i="SESSION",a=144e5,s=18e5,o={STARTED:"session-started",PAUSE:"session-pause",RESET:"session-reset",RESUME:"session-resume",UPDATE:"session-update"},c={SAME_TAB:"same-tab",CROSS_TAB:"cross-tab"},u={OFF:0,FULL:1,ERROR:2}},863:(e,t,r)=>{"use strict";function n(){return Math.floor(performance.now())}r.d(t,{t:()=>n})},944:(e,t,r)=>{"use strict";r.d(t,{R:()=>i});var n=r(241);function i(e,t){"function"==typeof console.debug&&(console.debug("New Relic Warning: https://github.com/newrelic/newrelic-browser-agent/blob/main/docs/warning-codes.md#".concat(e),t),(0,n.W)({agentIdentifier:null,drained:null,type:"data",name:"warn",feature:"warn",data:{code:e,secondary:t}}))}},701:(e,t,r)=>{"use strict";r.d(t,{B:()=>a,t:()=>s});var n=r(241);const i=new Set,a={};function s(e,t){const r=t.agentIdentifier;a[r]??={},e&&"object"==typeof e&&(i.has(r)||(t.ee.emit("rumresp",[e]),a[r]=e,i.add(r),(0,n.W)({agentIdentifier:r,loaded:!0,drained:!0,type:"lifecycle",name:"load",feature:void 0,data:e})))}},990:(e,t,r)=>{"use strict";r.d(t,{I:()=>i});var n=Object.prototype.hasOwnProperty;function i(e,t,r){if(n.call(e,t))return e[t];var i=r();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,t,{value:i,writable:!0,enumerable:!1}),i}catch(e){}return e[t]=i,i}},389:(e,t,r)=>{"use strict";function n(e,t=500,r={}){const n=r?.leading||!1;let i;return(...r)=>{n&&void 0===i&&(e.apply(this,r),i=setTimeout((()=>{i=clearTimeout(i)}),t)),n||(clearTimeout(i),i=setTimeout((()=>{e.apply(this,r)}),t))}}function i(e){let t=!1;return(...r)=>{t||(t=!0,e.apply(this,r))}}r.d(t,{J:()=>i,s:()=>n})},910:(e,t,r)=>{"use strict";r.d(t,{i:()=>a});var n=r(944);const i=new Map;function a(...e){return e.every((e=>{if(i.has(e))return i.get(e);const t="function"==typeof e&&e.toString().includes("[native code]");return t||(0,n.R)(64,e?.name||e?.toString()),i.set(e,t),t}))}},289:(e,t,r)=>{"use strict";r.d(t,{GG:()=>a,Qr:()=>o,sB:()=>s});var n=r(878);function i(){return"undefined"==typeof document||"complete"===document.readyState}function a(e,t){if(i())return e();(0,n.sp)("load",e,t)}function s(e){if(i())return e();(0,n.DD)("DOMContentLoaded",e)}function o(e){if(i())return e();(0,n.sp)("popstate",e)}},384:(e,t,r)=>{"use strict";r.d(t,{NT:()=>s,US:()=>d,Zm:()=>o,bQ:()=>u,dV:()=>c,pV:()=>l});var n=r(154),i=r(863),a=r(910);const s={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net"};function o(){return n.gm.NREUM||(n.gm.NREUM={}),void 0===n.gm.newrelic&&(n.gm.newrelic=n.gm.NREUM),n.gm.NREUM}function c(){let e=o();return e.o||(e.o={ST:n.gm.setTimeout,SI:n.gm.setImmediate||n.gm.setInterval,CT:n.gm.clearTimeout,XHR:n.gm.XMLHttpRequest,REQ:n.gm.Request,EV:n.gm.Event,PR:n.gm.Promise,MO:n.gm.MutationObserver,FETCH:n.gm.fetch,WS:n.gm.WebSocket},(0,a.i)(...Object.values(e.o))),e}function u(e,t){let r=o();r.initializedAgents??={},t.initializedAt={ms:(0,i.t)(),date:new Date},r.initializedAgents[e]=t}function d(e,t){o()[e]=t}function l(){return function(){let e=o();const t=e.info||{};e.info={beacon:s.beacon,errorBeacon:s.errorBeacon,...t}}(),function(){let e=o();const t=e.init||{};e.init={...t}}(),c(),function(){let e=o();const t=e.loader_config||{};e.loader_config={...t}}(),o()}},843:(e,t,r)=>{"use strict";r.d(t,{u:()=>i});var n=r(878);function i(e,t=!1,r,i){(0,n.DD)("visibilitychange",(function(){if(t)return void("hidden"===document.visibilityState&&e());e(document.visibilityState)}),r,i)}},773:(e,t,r)=>{"use strict";r.d(t,{z_:()=>a,XG:()=>o,TZ:()=>n,rs:()=>i,xV:()=>s});r(154),r(566),r(384);const n=r(860).K7.metrics,i="sm",a="cm",s="storeSupportabilityMetrics",o="storeEventMetrics"},630:(e,t,r)=>{"use strict";r.d(t,{T:()=>n});const n=r(860).K7.pageViewEvent},782:(e,t,r)=>{"use strict";r.d(t,{T:()=>n});const n=r(860).K7.pageViewTiming},234:(e,t,r)=>{"use strict";r.d(t,{W:()=>a});var n=r(836),i=r(687);class a{constructor(e,t){this.agentIdentifier=e,this.ee=n.ee.get(e),this.featureName=t,this.blocked=!1}deregisterDrain(){(0,i.x3)(this.agentIdentifier,this.featureName)}}},741:(e,t,r)=>{"use strict";r.d(t,{W:()=>a});var n=r(944),i=r(261);class a{#e(e,...t){if(this[e]!==a.prototype[e])return this[e](...t);(0,n.R)(35,e)}addPageAction(e,t){return this.#e(i.hG,e,t)}register(e){return this.#e(i.eY,e)}recordCustomEvent(e,t){return this.#e(i.fF,e,t)}setPageViewName(e,t){return this.#e(i.Fw,e,t)}setCustomAttribute(e,t,r){return this.#e(i.cD,e,t,r)}noticeError(e,t){return this.#e(i.o5,e,t)}setUserId(e){return this.#e(i.Dl,e)}setApplicationVersion(e){return this.#e(i.nb,e)}setErrorHandler(e){return this.#e(i.bt,e)}addRelease(e,t){return this.#e(i.k6,e,t)}log(e,t){return this.#e(i.$9,e,t)}start(){return this.#e(i.d3)}finished(e){return this.#e(i.BL,e)}recordReplay(){return this.#e(i.CH)}pauseReplay(){return this.#e(i.Tb)}addToTrace(e){return this.#e(i.U2,e)}setCurrentRouteName(e){return this.#e(i.PA,e)}interaction(){return this.#e(i.dT)}wrapLogger(e,t,r){return this.#e(i.Wb,e,t,r)}measure(e,t){return this.#e(i.V1,e,t)}}},261:(e,t,r)=>{"use strict";r.d(t,{$9:()=>u,BL:()=>o,CH:()=>g,Dl:()=>_,Fw:()=>y,PA:()=>h,Pl:()=>n,Tb:()=>l,U2:()=>a,V1:()=>k,Wb:()=>x,bt:()=>b,cD:()=>v,d3:()=>w,dT:()=>c,eY:()=>p,fF:()=>f,hG:()=>i,k6:()=>s,nb:()=>m,o5:()=>d});const n="api-",i="addPageAction",a="addToTrace",s="addRelease",o="finished",c="interaction",u="log",d="noticeError",l="pauseReplay",f="recordCustomEvent",g="recordReplay",p="register",m="setApplicationVersion",h="setCurrentRouteName",v="setCustomAttribute",b="setErrorHandler",y="setPageViewName",_="setUserId",w="start",x="wrapLogger",k="measure"},163:(e,t,r)=>{"use strict";r.d(t,{j:()=>E});var n=r(384),i=r(741);var a=r(555);r(860).K7.genericEvents;const s="experimental.marks",o="experimental.measures",c="experimental.resources",u=e=>{if(!e||"string"!=typeof e)return!1;try{document.createDocumentFragment().querySelector(e)}catch{return!1}return!0};var d=r(614),l=r(944),f=r(122);const g="[data-nr-mask]",p=e=>(0,f.a)(e,(()=>{const e={feature_flags:[],experimental:{marks:!1,measures:!1,resources:!1},mask_selector:"*",block_selector:"[data-nr-block]",mask_input_options:{color:!1,date:!1,"datetime-local":!1,email:!1,month:!1,number:!1,range:!1,search:!1,tel:!1,text:!1,time:!1,url:!1,week:!1,textarea:!1,select:!1,password:!0}};return{ajax:{deny_list:void 0,block_internal:!0,enabled:!0,autoStart:!0},api:{allow_registered_children:!0,duplicate_registered_data:!1},distributed_tracing:{enabled:void 0,exclude_newrelic_header:void 0,cors_use_newrelic_header:void 0,cors_use_tracecontext_headers:void 0,allowed_origins:void 0},get feature_flags(){return e.feature_flags},set feature_flags(t){e.feature_flags=t},generic_events:{enabled:!0,autoStart:!0},harvest:{interval:30},jserrors:{enabled:!0,autoStart:!0},logging:{enabled:!0,autoStart:!0},metrics:{enabled:!0,autoStart:!0},obfuscate:void 0,page_action:{enabled:!0},page_view_event:{enabled:!0,autoStart:!0},page_view_timing:{enabled:!0,autoStart:!0},performance:{get capture_marks(){return e.feature_flags.includes(s)||e.experimental.marks},set capture_marks(t){e.experimental.marks=t},get capture_measures(){return e.feature_flags.includes(o)||e.experimental.measures},set capture_measures(t){e.experimental.measures=t},capture_detail:!0,resources:{get enabled(){return e.feature_flags.includes(c)||e.experimental.resources},set enabled(t){e.experimental.resources=t},asset_types:[],first_party_domains:[],ignore_newrelic:!0}},privacy:{cookies_enabled:!0},proxy:{assets:void 0,beacon:void 0},session:{expiresMs:d.wk,inactiveMs:d.BB},session_replay:{autoStart:!0,enabled:!1,preload:!1,sampling_rate:10,error_sampling_rate:100,collect_fonts:!1,inline_images:!1,fix_stylesheets:!0,mask_all_inputs:!0,get mask_text_selector(){return e.mask_selector},set mask_text_selector(t){u(t)?e.mask_selector="".concat(t,",").concat(g):""===t||null===t?e.mask_selector=g:(0,l.R)(5,t)},get block_class(){return"nr-block"},get ignore_class(){return"nr-ignore"},get mask_text_class(){return"nr-mask"},get block_selector(){return e.block_selector},set block_selector(t){u(t)?e.block_selector+=",".concat(t):""!==t&&(0,l.R)(6,t)},get mask_input_options(){return e.mask_input_options},set mask_input_options(t){t&&"object"==typeof t?e.mask_input_options={...t,password:!0}:(0,l.R)(7,t)}},session_trace:{enabled:!0,autoStart:!0},soft_navigations:{enabled:!0,autoStart:!0},spa:{enabled:!0,autoStart:!0},ssl:void 0,user_actions:{enabled:!0,elementAttributes:["id","className","tagName","type"]}}})());var m=r(154),h=r(324);let v=0;const b={buildEnv:h.F3,distMethod:h.Xs,version:h.xv,originTime:m.WN},y={appMetadata:{},customTransaction:void 0,denyList:void 0,disabled:!1,entityManager:void 0,harvester:void 0,isolatedBacklog:!1,isRecording:!1,loaderType:void 0,maxBytes:3e4,obfuscator:void 0,onerror:void 0,ptid:void 0,releaseIds:{},session:void 0,timeKeeper:void 0,jsAttributesMetadata:{bytes:0},get harvestCount(){return++v}},_=e=>{const t=(0,f.a)(e,y),r=Object.keys(b).reduce(((e,t)=>(e[t]={value:b[t],writable:!1,configurable:!0,enumerable:!0},e)),{});return Object.defineProperties(t,r)};var w=r(701);const x=e=>{const t=e.startsWith("http");e+="/",r.p=t?e:"https://"+e};var k=r(836),A=r(241);const S={accountID:void 0,trustKey:void 0,agentID:void 0,licenseKey:void 0,applicationID:void 0,xpid:void 0},T=e=>(0,f.a)(e,S),R=new Set;function E(e,t={},r,s){let{init:o,info:c,loader_config:u,runtime:d={},exposed:l=!0}=t;if(!c){const e=(0,n.pV)();o=e.init,c=e.info,u=e.loader_config}e.init=p(o||{}),e.loader_config=T(u||{}),c.jsAttributes??={},m.bv&&(c.jsAttributes.isWorker=!0),e.info=(0,a.D)(c);const f=e.init,g=[c.beacon,c.errorBeacon];R.has(e.agentIdentifier)||(f.proxy.assets&&(x(f.proxy.assets),g.push(f.proxy.assets)),f.proxy.beacon&&g.push(f.proxy.beacon),function(e){const t=(0,n.pV)();Object.getOwnPropertyNames(i.W.prototype).forEach((r=>{const n=i.W.prototype[r];if("function"!=typeof n||"constructor"===n)return;let a=t[r];e[r]&&!1!==e.exposed&&"micro-agent"!==e.runtime?.loaderType&&(t[r]=(...t)=>{const n=e[r](...t);return a?a(...t):n})}))}(e),(0,n.US)("activatedFeatures",w.B),e.runSoftNavOverSpa&&=!0===f.soft_navigations.enabled&&f.feature_flags.includes("soft_nav")),d.denyList=[...f.ajax.deny_list||[],...f.ajax.block_internal?g:[]],d.ptid=e.agentIdentifier,d.loaderType=r,e.runtime=_(d),R.has(e.agentIdentifier)||(e.ee=k.ee.get(e.agentIdentifier),e.exposed=l,(0,A.W)({agentIdentifier:e.agentIdentifier,drained:!!w.B?.[e.agentIdentifier],type:"lifecycle",name:"initialize",feature:void 0,data:e.config})),R.add(e.agentIdentifier)}},374:(e,t,r)=>{r.nc=(()=>{try{return document?.currentScript?.nonce}catch(e){}return""})()},860:(e,t,r)=>{"use strict";r.d(t,{$J:()=>d,K7:()=>c,P3:()=>u,XX:()=>i,Yy:()=>o,df:()=>a,qY:()=>n,v4:()=>s});const n="events",i="jserrors",a="browser/blobs",s="rum",o="browser/logs",c={ajax:"ajax",genericEvents:"generic_events",jserrors:i,logging:"logging",metrics:"metrics",pageAction:"page_action",pageViewEvent:"page_view_event",pageViewTiming:"page_view_timing",sessionReplay:"session_replay",sessionTrace:"session_trace",softNav:"soft_navigations",spa:"spa"},u={[c.pageViewEvent]:1,[c.pageViewTiming]:2,[c.metrics]:3,[c.jserrors]:4,[c.spa]:5,[c.ajax]:6,[c.sessionTrace]:7,[c.softNav]:8,[c.sessionReplay]:9,[c.logging]:10,[c.genericEvents]:11},d={[c.pageViewEvent]:s,[c.pageViewTiming]:n,[c.ajax]:n,[c.spa]:n,[c.softNav]:n,[c.metrics]:i,[c.jserrors]:i,[c.sessionTrace]:a,[c.sessionReplay]:a,[c.logging]:o,[c.genericEvents]:"ins"}}},n={};function i(e){var t=n[e];if(void 0!==t)return t.exports;var a=n[e]={exports:{}};return r[e](a,a.exports,i),a.exports}i.m=r,i.d=(e,t)=>{for(var r in t)i.o(t,r)&&!i.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})},i.f={},i.e=e=>Promise.all(Object.keys(i.f).reduce(((t,r)=>(i.f[r](e,t),t)),[])),i.u=e=>"nr-rum-1.297.0.min.js",i.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),e={},t="NRBA-1.297.0.PROD:",i.l=(r,n,a,s)=>{if(e[r])e[r].push(n);else{var o,c;if(void 0!==a)for(var u=document.getElementsByTagName("script"),d=0;d<u.length;d++){var l=u[d];if(l.getAttribute("src")==r||l.getAttribute("data-webpack")==t+a){o=l;break}}if(!o){c=!0;var f={296:"sha512-n/1z7EiYHaupoJ3s8MajMxY/CH6se33KTGkEkqAgtuatNOjpM3V8Fm2j4AZJGysIchvpcxiQG5GRqMG0rnAWqQ=="};(o=document.createElement("script")).charset="utf-8",o.timeout=120,i.nc&&o.setAttribute("nonce",i.nc),o.setAttribute("data-webpack",t+a),o.src=r,0!==o.src.indexOf(window.location.origin+"/")&&(o.crossOrigin="anonymous"),f[s]&&(o.integrity=f[s])}e[r]=[n];var g=(t,n)=>{o.onerror=o.onload=null,clearTimeout(p);var i=e[r];if(delete e[r],o.parentNode&&o.parentNode.removeChild(o),i&&i.forEach((e=>e(n))),t)return t(n)},p=setTimeout(g.bind(null,void 0,{type:"timeout",target:o}),12e4);o.onerror=g.bind(null,o.onerror),o.onload=g.bind(null,o.onload),c&&document.head.appendChild(o)}},i.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.p="https://js-agent.newrelic.com/",(()=>{var e={374:0,840:0};i.f.j=(t,r)=>{var n=i.o(e,t)?e[t]:void 0;if(0!==n)if(n)r.push(n[2]);else{var a=new Promise(((r,i)=>n=e[t]=[r,i]));r.push(n[2]=a);var s=i.p+i.u(t),o=new Error;i.l(s,(r=>{if(i.o(e,t)&&(0!==(n=e[t])&&(e[t]=void 0),n)){var a=r&&("load"===r.type?"missing":r.type),s=r&&r.target&&r.target.src;o.message="Loading chunk "+t+" failed.\n("+a+": "+s+")",o.name="ChunkLoadError",o.type=a,o.request=s,n[1](o)}}),"chunk-"+t,t)}};var t=(t,r)=>{var n,a,[s,o,c]=r,u=0;if(s.some((t=>0!==e[t]))){for(n in o)i.o(o,n)&&(i.m[n]=o[n]);if(c)c(i)}for(t&&t(r);u<s.length;u++)a=s[u],i.o(e,a)&&e[a]&&e[a][0](),e[a]=0},r=self["webpackChunk:NRBA-1.297.0.PROD"]=self["webpackChunk:NRBA-1.297.0.PROD"]||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))})(),(()=>{"use strict";i(374);var e=i(566),t=i(741);class r extends t.W{agentIdentifier=(0,e.LA)(16)}var n=i(860);const a=Object.values(n.K7);var s=i(163);var o=i(908),c=i(863),u=i(261),d=i(241),l=i(944),f=i(701),g=i(773);function p(e,t,i,a){const s=a||i;!s||s[e]&&s[e]!==r.prototype[e]||(s[e]=function(){(0,o.p)(g.xV,["API/"+e+"/called"],void 0,n.K7.metrics,i.ee),(0,d.W)({agentIdentifier:i.agentIdentifier,drained:!!f.B?.[i.agentIdentifier],type:"data",name:"api",feature:u.Pl+e,data:{}});try{return t.apply(this,arguments)}catch(e){(0,l.R)(23,e)}})}function m(e,t,r,n,i){const a=e.info;null===r?delete a.jsAttributes[t]:a.jsAttributes[t]=r,(i||null===r)&&(0,o.p)(u.Pl+n,[(0,c.t)(),t,r],void 0,"session",e.ee)}var h=i(687),v=i(234),b=i(289),y=i(154),_=i(384);const w=e=>y.RI&&!0===e?.privacy.cookies_enabled;function x(e){return!!(0,_.dV)().o.MO&&w(e)&&!0===e?.session_trace.enabled}var k=i(389);class A extends v.W{constructor(e,t){super(e.agentIdentifier,t),this.abortHandler=void 0,this.featAggregate=void 0,this.onAggregateImported=void 0,this.deferred=Promise.resolve(),!1===e.init[this.featureName].autoStart?this.deferred=new Promise(((t,r)=>{this.ee.on("manual-start-all",(0,k.J)((()=>{(0,h.Ak)(e.agentIdentifier,this.featureName),t()})))})):(0,h.Ak)(e.agentIdentifier,t)}importAggregator(e,t,r={}){if(this.featAggregate)return;let a;this.onAggregateImported=new Promise((e=>{a=e}));const s=async()=>{let s;await this.deferred;try{if(w(e.init)){const{setupAgentSession:t}=await i.e(296).then(i.bind(i,305));s=t(e)}}catch(e){(0,l.R)(20,e),this.ee.emit("internal-error",[e]),this.featureName===n.K7.sessionReplay&&this.abortHandler?.()}try{if(!this.#t(this.featureName,s,e.init))return(0,h.Ze)(this.agentIdentifier,this.featureName),void a(!1);const{Aggregate:n}=await t();this.featAggregate=new n(e,r),e.runtime.harvester.initializedAggregates.push(this.featAggregate),a(!0)}catch(e){(0,l.R)(34,e),this.abortHandler?.(),(0,h.Ze)(this.agentIdentifier,this.featureName,!0),a(!1),this.ee&&this.ee.abort()}};y.RI?(0,b.GG)((()=>s()),!0):s()}#t(e,t,r){switch(e){case n.K7.sessionReplay:return x(r)&&!!t;case n.K7.sessionTrace:return!!t;default:return!0}}}var S=i(630),T=i(614);class R extends A{static featureName=S.T;constructor(e){var t;super(e,S.T),this.setupInspectionEvents(e.agentIdentifier),t=e,p(u.Fw,(function(e,r){"string"==typeof e&&("/"!==e.charAt(0)&&(e="/"+e),t.runtime.customTransaction=(r||"http://custom.transaction")+e,(0,o.p)(u.Pl+u.Fw,[(0,c.t)()],void 0,void 0,t.ee))}),t),this.ee.on("api-send-rum",((e,t)=>(0,o.p)("send-rum",[e,t],void 0,this.featureName,this.ee))),this.importAggregator(e,(()=>i.e(296).then(i.bind(i,108))))}setupInspectionEvents(e){const t=(t,r)=>{t&&(0,d.W)({agentIdentifier:e,timeStamp:t.timeStamp,loaded:"complete"===t.target.readyState,type:"window",name:r,data:t.target.location+""})};(0,b.sB)((e=>{t(e,"DOMContentLoaded")})),(0,b.GG)((e=>{t(e,"load")})),(0,b.Qr)((e=>{t(e,"navigate")})),this.ee.on(T.tS.UPDATE,((t,r)=>{(0,d.W)({agentIdentifier:e,type:"lifecycle",name:"session",data:r})}))}}var E=i(843),N=i(878),j=i(782);class I extends A{static featureName=j.T;constructor(e){super(e,j.T),y.RI&&((0,E.u)((()=>(0,o.p)("docHidden",[(0,c.t)()],void 0,j.T,this.ee)),!0),(0,N.sp)("pagehide",(()=>(0,o.p)("winPagehide",[(0,c.t)()],void 0,j.T,this.ee))),this.importAggregator(e,(()=>i.e(296).then(i.bind(i,350)))))}}class O extends A{static featureName=g.TZ;constructor(e){super(e,g.TZ),y.RI&&document.addEventListener("securitypolicyviolation",(e=>{(0,o.p)(g.xV,["Generic/CSPViolation/Detected"],void 0,this.featureName,this.ee)})),this.importAggregator(e,(()=>i.e(296).then(i.bind(i,373))))}}new class extends r{constructor(e){var t;(super(),y.gm)?(this.features={},(0,_.bQ)(this.agentIdentifier,this),this.desiredFeatures=new Set(e.features||[]),this.desiredFeatures.add(R),this.runSoftNavOverSpa=[...this.desiredFeatures].some((e=>e.featureName===n.K7.softNav)),(0,s.j)(this,e,e.loaderType||"agent"),t=this,p(u.cD,(function(e,r,n=!1){if("string"==typeof e){if(["string","number","boolean"].includes(typeof r)||null===r)return m(t,e,r,u.cD,n);(0,l.R)(40,typeof r)}else(0,l.R)(39,typeof e)}),t),function(e){p(u.Dl,(function(t){if("string"==typeof t||null===t)return m(e,"enduser.id",t,u.Dl,!0);(0,l.R)(41,typeof t)}),e)}(this),function(e){p(u.nb,(function(t){if("string"==typeof t||null===t)return m(e,"application.version",t,u.nb,!1);(0,l.R)(42,typeof t)}),e)}(this),function(e){p(u.d3,(function(){e.ee.emit("manual-start-all")}),e)}(this),this.run()):(0,l.R)(21)}get config(){return{info:this.info,init:this.init,loader_config:this.loader_config,runtime:this.runtime}}get api(){return this}run(){try{const e=function(e){const t={};return a.forEach((r=>{t[r]=!!e[r]?.enabled})),t}(this.init),t=[...this.desiredFeatures];t.sort(((e,t)=>n.P3[e.featureName]-n.P3[t.featureName])),t.forEach((t=>{if(!e[t.featureName]&&t.featureName!==n.K7.pageViewEvent)return;if(this.runSoftNavOverSpa&&t.featureName===n.K7.spa)return;if(!this.runSoftNavOverSpa&&t.featureName===n.K7.softNav)return;const r=function(e){switch(e){case n.K7.ajax:return[n.K7.jserrors];case n.K7.sessionTrace:return[n.K7.ajax,n.K7.pageViewEvent];case n.K7.sessionReplay:return[n.K7.sessionTrace];case n.K7.pageViewTiming:return[n.K7.pageViewEvent];default:return[]}}(t.featureName).filter((e=>!(e in this.features)));r.length>0&&(0,l.R)(36,{targetFeature:t.featureName,missingDependencies:r}),this.features[t.featureName]=new t(this)}))}catch(e){(0,l.R)(22,e);for(const e in this.features)this.features[e].abortHandler?.();const t=(0,_.Zm)();delete t.initializedAgents[this.agentIdentifier]?.features,delete this.sharedAggregator;return t.ee.get(this.agentIdentifier).abort(),!1}}}({features:[R,I,O],loaderType:"lite"})})()})();</script>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
			<link rel='dns-prefetch' href='//dcf.espn.com' />

<script type="text/javascript">
			function setCountryCookie(value,days) {
				var expires = "";
				if (days) {
					var date = new Date();
					date.setTime(date.getTime() + (days*24*60*60*1000));
					expires = "; expires=" + date.toUTCString();
				}
				document.cookie = "country=" + (value || "") + expires + "; path=/";
			}

function getCountryCookie() {
				let value = decodeURIComponent(document.cookie);
				let parts = value.split(`; country=`);
  				if (parts.length === 2) {
					return parts.pop().split(';').shift();
				}
				return "";
			}

var countryCookie = getCountryCookie();
			if ( ! countryCookie || 'us' !== countryCookie ) {
				setCountryCookie('us',1);
			}
		</script>
				<script type="text/javascript">
			var dtciDataLayer = {"page":{"content_publish_date":"05\/11\/2020","content_publish_time":"13:29","content_last_update_date":"05\/12\/2020","content_last_update_time":"13:47","contentcategory":"2020 Election,2020 House Elections,California,Special Elections,Wisconsin","section_1":"politics","section_2":"politics:special elections","story_title":"Two Special Elections On Tuesday Could Hint At Another Blue Wave In 2020","story_id":271962,"author":"Geoffrey Skelley and Nathaniel Rakich","page_name":"fivethirtyeight:politics:features","content_type":"features","app_version":"1.1.2","device_type":"Desktop","prev_page":false,"template":"standard_layout","editorial_other_subjects":["2020 Election","2020 House Elections","California","Special Elections","Wisconsin"],"word_count":1536},"site":{"edition":"en-us","language":"en","site":"fivethirtyeight"},"detailsEndpoint":"https:\/\/fivethirtyeight.com\/wp-json\/dtci_datalayer\/v1\/get_page_details\/","device":{"device_type":"Desktop"}};
		</script>

		<script src="https://dcf.espn.com/TWDC-DTCI/prod/Bootstrap.js"></script>
<title>Two Special Elections On Tuesday Could Hint At Another Blue Wave In 2020 | FiveThirtyEight</title>
<meta name='robots' content='max-image-preview:large' />
	<style>img:is([sizes="auto" i], [sizes^="auto," i]) { contain-intrinsic-size: 3000px 1500px }</style>
	<!-- Jetpack Site Verification Tags -->
<meta name="google-site-verification" content="-j2BzwWZ0QSsFphrQ_5sJtlT_ZF5B5qkZhCQHF2MRz8" />
<link rel='dns-prefetch' href='//cdn.registerdisney.go.com' />
<link rel='dns-prefetch' href='//platform.twitter.com' />
<link rel='dns-prefetch' href='//datawrapper.dwcdn.net' />
<link rel='dns-prefetch' href='//use.typekit.net' />
<link rel='stylesheet' id='wp-block-library-css' href='https://fivethirtyeight.com/wp-includes/css/dist/block-library/style.min.css?ver=6.8.2' media='all' />
<style id='classic-theme-styles-inline-css'>
/*! This file is auto-generated */
.wp-block-button__link{color:#fff;background-color:#32373c;border-radius:9999px;box-shadow:none;text-decoration:none;padding:calc(.667em + 2px) calc(1.333em + 2px);font-size:1.125em}.wp-block-file__button{background:#32373c;color:#fff;text-decoration:none}
</style>
<style id='co-authors-plus-coauthors-style-inline-css'>
.wp-block-co-authors-plus-coauthors.is-layout-flow [class*=wp-block-co-authors-plus]{display:inline}

</style>
<style id='co-authors-plus-avatar-style-inline-css'>
.wp-block-co-authors-plus-avatar :where(img){height:auto;max-width:100%;vertical-align:bottom}.wp-block-co-authors-plus-coauthors.is-layout-flow .wp-block-co-authors-plus-avatar :where(img){vertical-align:middle}.wp-block-co-authors-plus-avatar:is(.alignleft,.alignright){display:table}.wp-block-co-authors-plus-avatar.aligncenter{display:table;margin-inline:auto}

</style>
<style id='co-authors-plus-image-style-inline-css'>
.wp-block-co-authors-plus-image{margin-bottom:0}.wp-block-co-authors-plus-image :where(img){height:auto;max-width:100%;vertical-align:bottom}.wp-block-co-authors-plus-coauthors.is-layout-flow .wp-block-co-authors-plus-image :where(img){vertical-align:middle}.wp-block-co-authors-plus-image:is(.alignfull,.alignwide) :where(img){width:100%}.wp-block-co-authors-plus-image:is(.alignleft,.alignright){display:table}.wp-block-co-authors-plus-image.aligncenter{display:table;margin-inline:auto}

</style>
<link rel='stylesheet' id='mediaelement-css' href='https://fivethirtyeight.com/wp-includes/js/mediaelement/mediaelementplayer-legacy.min.css?ver=4.2.17' media='all' />
<link rel='stylesheet' id='wp-mediaelement-css' href='https://fivethirtyeight.com/wp-includes/js/mediaelement/wp-mediaelement.min.css?ver=6.8.2' media='all' />
<style id='jetpack-sharing-buttons-style-inline-css'>
.jetpack-sharing-buttons__services-list{display:flex;flex-direction:row;flex-wrap:wrap;gap:0;list-style-type:none;margin:5px;padding:0}.jetpack-sharing-buttons__services-list.has-small-icon-size{font-size:12px}.jetpack-sharing-buttons__services-list.has-normal-icon-size{font-size:16px}.jetpack-sharing-buttons__services-list.has-large-icon-size{font-size:24px}.jetpack-sharing-buttons__services-list.has-huge-icon-size{font-size:36px}@media print{.jetpack-sharing-buttons__services-list{display:none!important}}.editor-styles-wrapper .wp-block-jetpack-sharing-buttons{gap:0;padding-inline-start:0}ul.jetpack-sharing-buttons__services-list.has-background{padding:1.25em 2.375em}
</style>
<style id='elasticpress-facet-style-inline-css'>
.widget_ep-facet input[type=search],.wp-block-elasticpress-facet input[type=search]{margin-bottom:1rem}.widget_ep-facet .searchable .inner,.wp-block-elasticpress-facet .searchable .inner{max-height:20em;overflow:scroll}.widget_ep-facet .term.hide,.wp-block-elasticpress-facet .term.hide{display:none}.widget_ep-facet .empty-term,.wp-block-elasticpress-facet .empty-term{opacity:.5;position:relative}.widget_ep-facet .empty-term:after,.wp-block-elasticpress-facet .empty-term:after{bottom:0;content:" ";display:block;left:0;position:absolute;right:0;top:0;width:100%;z-index:2}.widget_ep-facet .level-1,.wp-block-elasticpress-facet .level-1{padding-left:20px}.widget_ep-facet .level-2,.wp-block-elasticpress-facet .level-2{padding-left:40px}.widget_ep-facet .level-3,.wp-block-elasticpress-facet .level-3{padding-left:60px}.widget_ep-facet .level-4,.wp-block-elasticpress-facet .level-4{padding-left:5pc}.widget_ep-facet .level-5,.wp-block-elasticpress-facet .level-5{padding-left:75pt}.widget_ep-facet input[disabled],.wp-block-elasticpress-facet input[disabled]{cursor:pointer;opacity:1}.widget_ep-facet .term a,.wp-block-elasticpress-facet .term a{-webkit-box-align:center;-ms-flex-align:center;align-items:center;display:-webkit-box;display:-ms-flexbox;display:flex;position:relative}.widget_ep-facet .term a:hover .ep-checkbox,.wp-block-elasticpress-facet .term a:hover .ep-checkbox{background-color:#ccc}.ep-checkbox{-webkit-box-align:center;-ms-flex-align:center;-ms-flex-negative:0;-webkit-box-pack:center;-ms-flex-pack:center;align-items:center;background-color:#eee;display:-webkit-box;display:-ms-flexbox;display:flex;flex-shrink:0;height:1em;justify-content:center;margin-right:.25em;width:1em}.ep-checkbox:after{border:solid #fff;border-width:0 .125em .125em 0;content:"";display:none;height:.5em;-webkit-transform:rotate(45deg);transform:rotate(45deg);width:.25em}.ep-checkbox.checked{background-color:#5e5e5e}.ep-checkbox.checked:after{display:block}

</style>
<link rel='stylesheet' id='elasticpress-related-posts-block-css' href='https://fivethirtyeight.com/wp-content/mu-plugins/search/elasticpress/dist/css/related-posts-block-styles.min.css?ver=4.2.2' media='all' />
<style id='global-styles-inline-css'>
:root{--wp--preset--aspect-ratio--square: 1;--wp--preset--aspect-ratio--4-3: 4/3;--wp--preset--aspect-ratio--3-4: 3/4;--wp--preset--aspect-ratio--3-2: 3/2;--wp--preset--aspect-ratio--2-3: 2/3;--wp--preset--aspect-ratio--16-9: 16/9;--wp--preset--aspect-ratio--9-16: 9/16;--wp--preset--color--black: #000000;--wp--preset--color--cyan-bluish-gray: #abb8c3;--wp--preset--color--white: #ffffff;--wp--preset--color--pale-pink: #f78da7;--wp--preset--color--vivid-red: #cf2e2e;--wp--preset--color--luminous-vivid-orange: #ff6900;--wp--preset--color--luminous-vivid-amber: #fcb900;--wp--preset--color--light-green-cyan: #7bdcb5;--wp--preset--color--vivid-green-cyan: #00d084;--wp--preset--color--pale-cyan-blue: #8ed1fc;--wp--preset--color--vivid-cyan-blue: #0693e3;--wp--preset--color--vivid-purple: #9b51e0;--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple: linear-gradient(135deg,rgba(6,147,227,1) 0%,rgb(155,81,224) 100%);--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan: linear-gradient(135deg,rgb(122,220,180) 0%,rgb(0,208,130) 100%);--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange: linear-gradient(135deg,rgba(252,185,0,1) 0%,rgba(255,105,0,1) 100%);--wp--preset--gradient--luminous-vivid-orange-to-vivid-red: linear-gradient(135deg,rgba(255,105,0,1) 0%,rgb(207,46,46) 100%);--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray: linear-gradient(135deg,rgb(238,238,238) 0%,rgb(169,184,195) 100%);--wp--preset--gradient--cool-to-warm-spectrum: linear-gradient(135deg,rgb(74,234,220) 0%,rgb(151,120,209) 20%,rgb(207,42,186) 40%,rgb(238,44,130) 60%,rgb(251,105,98) 80%,rgb(254,248,76) 100%);--wp--preset--gradient--blush-light-purple: linear-gradient(135deg,rgb(255,206,236) 0%,rgb(152,150,240) 100%);--wp--preset--gradient--blush-bordeaux: linear-gradient(135deg,rgb(254,205,165) 0%,rgb(254,45,45) 50%,rgb(107,0,62) 100%);--wp--preset--gradient--luminous-dusk: linear-gradient(135deg,rgb(255,203,112) 0%,rgb(199,81,192) 50%,rgb(65,88,208) 100%);--wp--preset--gradient--pale-ocean: linear-gradient(135deg,rgb(255,245,203) 0%,rgb(182,227,212) 50%,rgb(51,167,181) 100%);--wp--preset--gradient--electric-grass: linear-gradient(135deg,rgb(202,248,128) 0%,rgb(113,206,126) 100%);--wp--preset--gradient--midnight: linear-gradient(135deg,rgb(2,3,129) 0%,rgb(40,116,252) 100%);--wp--preset--font-size--small: 13px;--wp--preset--font-size--medium: 20px;--wp--preset--font-size--large: 36px;--wp--preset--font-size--x-large: 42px;--wp--preset--spacing--20: 0.44rem;--wp--preset--spacing--30: 0.67rem;--wp--preset--spacing--40: 1rem;--wp--preset--spacing--50: 1.5rem;--wp--preset--spacing--60: 2.25rem;--wp--preset--spacing--70: 3.38rem;--wp--preset--spacing--80: 5.06rem;--wp--preset--shadow--natural: 6px 6px 9px rgba(0, 0, 0, 0.2);--wp--preset--shadow--deep: 12px 12px 50px rgba(0, 0, 0, 0.4);--wp--preset--shadow--sharp: 6px 6px 0px rgba(0, 0, 0, 0.2);--wp--preset--shadow--outlined: 6px 6px 0px -3px rgba(255, 255, 255, 1), 6px 6px rgba(0, 0, 0, 1);--wp--preset--shadow--crisp: 6px 6px 0px rgba(0, 0, 0, 1);}:where(.is-layout-flex){gap: 0.5em;}:where(.is-layout-grid){gap: 0.5em;}body .is-layout-flex{display: flex;}.is-layout-flex{flex-wrap: wrap;align-items: center;}.is-layout-flex > :is(*, div){margin: 0;}body .is-layout-grid{display: grid;}.is-layout-grid > :is(*, div){margin: 0;}:where(.wp-block-columns.is-layout-flex){gap: 2em;}:where(.wp-block-columns.is-layout-grid){gap: 2em;}:where(.wp-block-post-template.is-layout-flex){gap: 1.25em;}:where(.wp-block-post-template.is-layout-grid){gap: 1.25em;}.has-black-color{color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-color{color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-color{color: var(--wp--preset--color--white) !important;}.has-pale-pink-color{color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-color{color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-color{color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-color{color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-color{color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-color{color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-color{color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-color{color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-color{color: var(--wp--preset--color--vivid-purple) !important;}.has-black-background-color{background-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-background-color{background-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-background-color{background-color: var(--wp--preset--color--white) !important;}.has-pale-pink-background-color{background-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-background-color{background-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-background-color{background-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-background-color{background-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-background-color{background-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-background-color{background-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-background-color{background-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-background-color{background-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-background-color{background-color: var(--wp--preset--color--vivid-purple) !important;}.has-black-border-color{border-color: var(--wp--preset--color--black) !important;}.has-cyan-bluish-gray-border-color{border-color: var(--wp--preset--color--cyan-bluish-gray) !important;}.has-white-border-color{border-color: var(--wp--preset--color--white) !important;}.has-pale-pink-border-color{border-color: var(--wp--preset--color--pale-pink) !important;}.has-vivid-red-border-color{border-color: var(--wp--preset--color--vivid-red) !important;}.has-luminous-vivid-orange-border-color{border-color: var(--wp--preset--color--luminous-vivid-orange) !important;}.has-luminous-vivid-amber-border-color{border-color: var(--wp--preset--color--luminous-vivid-amber) !important;}.has-light-green-cyan-border-color{border-color: var(--wp--preset--color--light-green-cyan) !important;}.has-vivid-green-cyan-border-color{border-color: var(--wp--preset--color--vivid-green-cyan) !important;}.has-pale-cyan-blue-border-color{border-color: var(--wp--preset--color--pale-cyan-blue) !important;}.has-vivid-cyan-blue-border-color{border-color: var(--wp--preset--color--vivid-cyan-blue) !important;}.has-vivid-purple-border-color{border-color: var(--wp--preset--color--vivid-purple) !important;}.has-vivid-cyan-blue-to-vivid-purple-gradient-background{background: var(--wp--preset--gradient--vivid-cyan-blue-to-vivid-purple) !important;}.has-light-green-cyan-to-vivid-green-cyan-gradient-background{background: var(--wp--preset--gradient--light-green-cyan-to-vivid-green-cyan) !important;}.has-luminous-vivid-amber-to-luminous-vivid-orange-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-amber-to-luminous-vivid-orange) !important;}.has-luminous-vivid-orange-to-vivid-red-gradient-background{background: var(--wp--preset--gradient--luminous-vivid-orange-to-vivid-red) !important;}.has-very-light-gray-to-cyan-bluish-gray-gradient-background{background: var(--wp--preset--gradient--very-light-gray-to-cyan-bluish-gray) !important;}.has-cool-to-warm-spectrum-gradient-background{background: var(--wp--preset--gradient--cool-to-warm-spectrum) !important;}.has-blush-light-purple-gradient-background{background: var(--wp--preset--gradient--blush-light-purple) !important;}.has-blush-bordeaux-gradient-background{background: var(--wp--preset--gradient--blush-bordeaux) !important;}.has-luminous-dusk-gradient-background{background: var(--wp--preset--gradient--luminous-dusk) !important;}.has-pale-ocean-gradient-background{background: var(--wp--preset--gradient--pale-ocean) !important;}.has-electric-grass-gradient-background{background: var(--wp--preset--gradient--electric-grass) !important;}.has-midnight-gradient-background{background: var(--wp--preset--gradient--midnight) !important;}.has-small-font-size{font-size: var(--wp--preset--font-size--small) !important;}.has-medium-font-size{font-size: var(--wp--preset--font-size--medium) !important;}.has-large-font-size{font-size: var(--wp--preset--font-size--large) !important;}.has-x-large-font-size{font-size: var(--wp--preset--font-size--x-large) !important;}
:where(.wp-block-post-template.is-layout-flex){gap: 1.25em;}:where(.wp-block-post-template.is-layout-grid){gap: 1.25em;}
:where(.wp-block-columns.is-layout-flex){gap: 2em;}:where(.wp-block-columns.is-layout-grid){gap: 2em;}
:root :where(.wp-block-pullquote){font-size: 1.5em;line-height: 1.6;}
</style>
<link rel='stylesheet' id='gif-play-button-styles-css' href='https://fivethirtyeight.com/wp-content/plugins/gif-play-button/assets/css/gif-play-button.min.css?ver=1.1.2' media='all' />
<link rel='stylesheet' id='fte-css' href='https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/dist/css/fiveThirtyEight.css?ver=1.1.2' media='' />
<link rel='stylesheet' id='fte-CCfonts-css' href='https://use.typekit.net/ktz4wdi.css?ver=1.1.2' media='' />
<style id='admin-announcements-inline-css'>
.st0, .st1 { fill: #fcdfc5; }
</style>
<script type="text/javascript" id="disney-oneid-js-extra">
/* <![CDATA[ */
var DisneyOneID = {"config":{"clientId":"DATG-FIVETHIRTYEIGHT.WEB","langPref":"en-US","debug":false,"responderPage":"https:\/\/fivethirtyeight.com\/oneid-responder","campaignName":"FiveThirtyEight"}};
/* ]]> */
</script>
<script type="text/javascript" src="https://cdn.registerdisney.go.com/v4/OneID.js" id="disney-oneid-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/disney-messaging/assets/js/oneid.min.js?ver=1.1.2" id="disney-oneid-config-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/dtci-data-privacy/assets/js/adobe-datalayer.min.js?ver=1.1" id="dtci-datalayer-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-includes/js/jquery/jquery.min.js?ver=3.7.1" id="jquery-core-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=3.4.1" id="jquery-migrate-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/espn-social/assets/js/facebook.min.js?ver=1.1.2" id="facebook-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/espn-social/assets/js/twitter-prompt.min.js?ver=1.1.2" id="twitter-prompt-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/disney-messaging/assets/js/vendor/purify.min.js?ver=1.1.2" id="purify-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-includes/js/underscore.min.js?ver=1.13.7" id="underscore-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/dist/js/fivethirtyeightHeader.js?ver=1.1.2" id="fte-js"></script>
<script type="text/javascript" async="async" src="https://fivethirtyeight.com/wp-content/plugins/dtci-data-privacy/assets/js/twitter-platform.min.js" id="platform-twitter-js" defer></script>
<script type="text/javascript" id="abc-analytics-js-extra">
/* <![CDATA[ */
var ABCAnalytics = {"nielsen":{"asset_id":271962,"section":"politicsspecial-elections","seg_a":"","seg_b":"","seg_c":"","debug":""},"chartbeat":{"uid":"12240","domain":"fivethirtyeight.com","path":"\/features\/two-special-elections-on-tuesday-could-hint-at-another-blue-wave-in-2020\/","sections":"politics,features","authors":"Geoffrey Skelley","title":"Two Special Elections On Tuesday Could Hint At Another Blue Wave In 2020","loadPubJS":false,"loadVidJS":true},"gtm":{"id":"GTM-KLHT6T2"},"omniture":{"pageName":"politics:features:two-special-elections-on-tuesday-could-hint-at-another-blue-wave-in-2020","prop1":"fivethirtyeight","prop2":"","prop5":"features","prop6":"Geoffrey Skelley","prop7":"politics","prop8":"politics:special-elections","prop12":"Two Special Elections On Tuesday Could Hint At Another Blue Wave In 2020","prop13":"271962:Two Special Elections On Tuesday Could Hint At Another Blue Wave In 2020","prop14":"","prop15":"https:\/\/fivethirtyeight.com\/features\/two-special-elections-on-tuesday-could-hint-at-another-blue-wave-in-2020\/","prop16":"https:\/\/fivethirtyeight.com\/features\/two-special-elections-on-tuesday-could-hint-at-another-blue-wave-in-2020\/","prop20":"Desktop","prop23":"2020 Election, 2020 House Elections, California, Special Elections, Wisconsin","eVar5":"features","eVar6":"Geoffrey Skelley","eVar7":"politics","eVar8":"politics:special-elections","eVar9":"2020-05-11","eVar10":"13:29","eVar12":"Two Special Elections On Tuesday Could Hint At Another Blue Wave In 2020","eVar13":"271962:Two Special Elections On Tuesday Could Hint At Another Blue Wave In 2020","eVar14":"","eVar15":"https:\/\/fivethirtyeight.com\/features\/two-special-elections-on-tuesday-could-hint-at-another-blue-wave-in-2020\/","eVar16":"https:\/\/fivethirtyeight.com\/features\/two-special-elections-on-tuesday-could-hint-at-another-blue-wave-in-2020\/","eVar20":"Desktop","eVar21":null,"eVar22":null,"prop35":"2020-05-11"},"account":"wdgnewfivethirtyeight"};
/* ]]> */
</script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/abc-analytics/assets/js/analytics.min.js?ver=1.1.2" id="abc-analytics-js"></script>
<link rel="https://api.w.org/" href="https://fivethirtyeight.com/wp-json/" /><link rel="alternate" title="JSON" type="application/json" href="https://fivethirtyeight.com/wp-json/wp/v2/fte_features/271962" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://fivethirtyeight.com/xmlrpc.php?rsd" />
<meta name="generator" content="WordPress 6.8.2" />
<link rel='shortlink' href='https://53eig.ht/2WmDtlB' />
<link rel="alternate" title="oEmbed (JSON)" type="application/json+oembed" href="https://fivethirtyeight.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ffivethirtyeight.com%2Ffeatures%2Ftwo-special-elections-on-tuesday-could-hint-at-another-blue-wave-in-2020%2F" />
<link rel="alternate" title="oEmbed (XML)" type="text/xml+oembed" href="https://fivethirtyeight.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Ffivethirtyeight.com%2Ffeatures%2Ftwo-special-elections-on-tuesday-could-hint-at-another-blue-wave-in-2020%2F&#038;format=xml" />
<meta name="color-scheme" content="only light" />
        <style>
        .getty.aligncenter {
            text-align: center;
        }
        .getty.alignleft {
            float: none;
            margin-right: 0;
        }
        .getty.alignleft > div {
            float: left;
            margin-right: 5px;
        }
        .getty.alignright {
            float: none;
            margin-left: 0;
        }
        .getty.alignright > div {
            float: right;
            margin-left: 5px;
        }
        </style>

<!-- Jetpack Open Graph Tags -->
<meta property="og:type" content="article" />
<meta property="og:title" content="Two Special Elections On Tuesday Could Hint At Another Blue Wave In 2020" />
<meta property="og:url" content="https://fivethirtyeight.com/features/two-special-elections-on-tuesday-could-hint-at-another-blue-wave-in-2020/" />
<meta property="og:description" content="Former Vice President Joe Biden leads President Trump in most early polls, Democrats are leading polls of the generic congressional ballot by 2018-level margins&#8230;" />
<meta property="article:published_time" content="2020-05-11T17:29:48+00:00" />
<meta property="article:modified_time" content="2020-05-11T17:29:48+00:00" />
<meta property="og:site_name" content="FiveThirtyEight" />
<meta property="og:image" content="https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_16x9.png?w=712" />
<meta property="og:image:width" content="712" />
<meta property="og:image:height" content="401" />
<meta property="og:image:alt" content="" />
<meta property="og:locale" content="en_US" />
<meta property="article:author" content="https://fivethirtyeight.com/contributors/geoffrey-skelley/" />
<meta name="twitter:text:title" content="Two Special Elections On Tuesday Could Hint At Another Blue Wave In 2020" />
<meta name="twitter:image" content="https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?w=640" />
<meta name="twitter:card" content="summary_large_image" />
<meta property="article:publisher" content="https://www.facebook.com/fivethirtyeight" />
<meta property="fb:app_id" content="797620670264818" />
<meta property="fb:pages" content="687958677914631" />
<meta name="twitter:site" content="FiveThirtyEight" />
<meta name="twitter:site:id" content="2303751216" />
<meta name="twitter:widgets:csp" content="on" />
<meta name="twitter:maxage" content="300" />
<meta name="twitter:creator" content="geoffreyvs" />
<meta name="twitter:creator:id" content="82673602" />
<meta name="twitter:image:src" content="https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_16x9.png?w=712" />
<meta name="twitter:label1" content="Written by" />
<meta name="twitter:data1" content="Geoffrey Skelley and Nathaniel Rakich" />
<meta name="twitter:label2" content="Filed under" />
<meta name="twitter:data2" content="2020 Election, 2020 House Elections, California, Special Elections, Wisconsin" />

<!-- End Jetpack Open Graph Tags -->
<meta name="DC.date.issued" content="2020-05-11T17:29:48+00:00" />
<meta name="description" content="Former Vice President Joe Biden leads President Trump in most early polls, Democrats are leading polls of the generic congressional ballot by 2018-level margins&#8230;" />
<meta name='author' content='Geoffrey Skelley' />
<link rel='author' href='https://fivethirtyeight.com/contributors/geoffrey-skelley/' />
<link rel="alternate" type="application/rss+xml" title="Posts feed for Geoffrey Skelley" href="https://fivethirtyeight.com/contributors/geoffrey-skelley/feed/">
<link type="text/plain" rel="author" href="https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/humans.txt" /><link rel='canonical' href='https://fivethirtyeight.com/features/two-special-elections-on-tuesday-could-hint-at-another-blue-wave-in-2020/' />
<script type='application/ld+json'>
{"@context":"http://schema.org","@type":"NewsArticle","mainEntityOfPage":{"@type":"WebPage","@id":"https://fivethirtyeight.com/features/two-special-elections-on-tuesday-could-hint-at-another-blue-wave-in-2020/"},"headline":"Two Special Elections On Tuesday Could Hint At Another Blue Wave In 2020","datePublished":"2020-05-11T13:29:48-04:00","dateModified":"2020-05-12T13:47:59-04:00","publisher":{"@type":"Organization","name":"FiveThirtyEight","logo":{"url":"https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/dist/images/fivethirtyeight-logo-rich-snippets.png","height":60,"width":546,"@type":"ImageObject"}},"author":{"@type":"Person","name":"Geoffrey Skelley and Nathaniel Rakich"},"articleSection":"Politics","image":{"@type":"ImageObject","url":"https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png","width":1024,"height":768}}
</script>
		<style type="text/css" id="wp-custom-css">
			section.viz {
background-color: #fff;
}
div.liveblog-entry-content>header.single-post-header{
display: none;
}		</style>
			<link rel="mask-icon" color="#ed713a" href="https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/assets/images/logo-fox-head-black.svg?v=1.1.2">
	<link rel="shortcut icon" href="https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/assets/images/favicon.ico?v=1.1.2">
	<link rel="apple-touch-icon" href="https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/assets/images/fivethirtyeight-logo-touch.png?v=1.1.2">
</head>
<body class="wp-singular fte_features-template-default single single-fte_features postid-271962 wp-theme-espn-fivethirtyeight vertical-politics slug-two-special-elections-on-tuesday-could-hint-at-another-blue-wave-in-2020 topic-slug-special-elections no-ads">

<a href="#content" class="skip-to-content-link visually-hidden">Skip to main content</a>
<i class="header-global-bground"></i>
<header class="header-global" id="header-global">
	<div class="site-wrapper header-global-top">
							<h2 class="header-global-logo">
							<a href="/" name="&amp;lpos=fivethirtyeight&amp;lid=Header Home" class="header-global-logo-link">
					<span class="visually-hidden">FiveThirtyEight</span>
					<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="163.451" viewBox="0 318.275 1280 163.451" class="site-logo" role="presentation"><path d="M0 318.275h76.009v24.323H27.363v30.403h45.606v24.323H27.363v51.687H0zm94.252 109.453h15.202v-54.727H94.252v-24.323h39.525v79.05h12.162v21.283H94.252v-21.283zm15.202-109.453h24.323v24.323h-24.323v-24.323zm434.774 109.453h15.202v-54.727h-15.202v-24.323h39.525v79.05h12.162v21.283h-51.686v-21.283zm15.202-109.453h24.323v24.323H559.43v-24.323zm401.33 109.453h15.202v-54.727H960.76v-24.323h39.525v79.05h12.161v21.283H960.76v-21.283zm15.202-109.453h24.323v24.323h-24.323v-24.323zm-811.781 82.09v-51.687h24.323v45.606l12.161 30.343h3.04l12.162-30.343v-45.606h24.323v51.687l-21.283 48.646h-33.444zm173.301 48.646h-41.288c-24.901 0-37.762-11.584-37.762-35.968v-27.88c0-23.016 13.074-39.525 39.525-39.525 28.367 0 39.525 15.415 39.525 42.565v21.283h-51.686v5.29c0 7.966 3.04 12.952 10.398 12.952h41.288v21.283zm-51.686-60.808h24.323v-4.713c0-7.966-3.223-16.57-12.557-16.57-8.483 0-11.766 6.689-11.766 16.57v4.713zm94.251-45.605h-30.403v-24.323h88.171v24.323h-30.404v106.413h-27.364zm234.11 106.413V348.678h24.323v12.161c3.466-7.449 11.401-12.161 21.952-12.161h8.452v24.323h-18.242c-8.635 0-12.161 2.858-12.161 11.857v64.152h-24.324zm130.736 0h-14.715c-21.617 0-30.89-11.219-30.89-33.9v-42.109h-18.242v-24.323h18.242v-21.283h24.323v21.283h21.283v24.323H723.61l-.213 42.353c0 6.75 2.828 12.374 11.128 12.374h10.368v21.282zm535.107 0h-14.715c-21.617 0-30.89-11.219-30.89-33.9v-42.109h-18.242v-24.323h18.242v-21.283h24.323v21.283H1280v24.323h-21.283l-.213 42.353c0 6.75 2.828 12.374 11.128 12.374H1280v21.282zm-506.953 32.714l14.016-28.883-23.928-52.477v-51.687h24.323v45.606l12.162 30.404h3.04l12.162-30.404v-45.606h24.323v51.687l-37.397 81.36zm90.421-163.45h76.009v24.323h-48.646v27.363h45.606v24.323h-45.606v30.404h48.646v24.323h-76.009zm161.14 145.938v-6.081h48.95c6.081 0 8.817-.547 8.817-3.861v-1.034c0-3.284-2.767-4.226-8.817-4.226h-39.829v-15.202l15.202-15.202c-16.084-4.5-24.323-16.509-24.323-33.444v-3.04c0-22.985 13.499-36.485 42.565-36.485a66.672 66.672 0 0 1 18.09 3.04l12.313-18.242 15.202 9.121-12.161 18.242c4.165 5.868 9.121 14.989 9.121 24.323v3.04c0 21.283-10.033 32.41-36.484 33.444l-9.121 12.161h18.242c17.999 0 27.363 7.966 27.363 23.35v.334c0 15.384-8.239 24.962-26.208 24.962h-39.525c-13.043.002-19.397-5.593-19.397-15.2zm57.767-76.01v-9.121c0-10.033-4.044-12.161-15.202-12.161-11.158 0-15.202 2.128-15.202 12.161v9.121c0 10.033 4.226 12.162 15.202 12.162s15.202-2.128 15.202-12.162zm72.969 60.808h-24.323V318.275h24.323v42.565c3.466-8.118 10.337-12.161 21.283-12.161 19.033 0 27.363 9.364 27.363 32.714v67.618h-24.323v-63.848c0-9.516-3.253-15.202-12.162-15.202-8.908 0-12.161 5.686-12.161 15.202v63.848zm-678.004 0h-24.323V318.275h24.323v42.565c3.466-8.118 11.888-12.161 22.772-12.161 19.033 0 25.874 9.516 25.874 32.867v67.466h-24.323v-66.888c0-9.516-3.253-13.499-12.161-13.499s-12.162 6.871-12.162 16.388v63.998z"/></svg>
					<img src="https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/assets/images/logo-fox-head-color.svg" alt="FiveThirtyEight" width="57" height="55" class="site-logo-small" id="site-logo-small" />
				</a>
							</h2>

			<form action="https://fivethirtyeight.com/" method="get" id="searchform" class="search-form">
				<label for="search-field" class="search-form-label">Search</label>
				<div class="search-form-input-wrapper"><input type="search" name="s" id="search-field" class="search-form-input" placeholder="Search" tabindex="-1"></div>
				<input type="submit" value="Search" class="search-form-submit" tabindex="-1">
				<button aria-label="Search" class="search-button" id="search-button" aria-expanded="false">
					<span class="visually-hidden">Search</span>
				</button>
			</form>

<a href="https://abcnews.go.com/" rel="noopener" title="ABC News" target="_blank" class="header-espn-link" name="&amp;lpos=fivethirtyeightHeader&amp;lid=Header ABC News">
				<svg width="65" height="23" xmlns="http://www.w3.org/2000/svg" role="presentation"><path d="M25.089 6.709c-.47-.496-.974-.798-1.322-.798h-.313v-.275h.261c.121 0 1.548.058 1.687.058.227 0 .886-.058 1.026-.058h.278l6.618 7.345V7.187c0-.921-.4-1.276-1.407-1.276h-.296v-.275h.313c.035 0 1.529.058 1.65.058.173 0 1.164-.058 1.355-.058h.192l.017.275c-.922.071-1.165.32-1.165 1.135v9.16h-.312l-7.904-8.77v6.6c0 1.384.314 1.756 1.46 1.756h.295v.296h-.331c-.243 0-1.441-.06-1.72-.06-.156 0-1.269.06-1.512.06h-.279v-.296c1.166-.107 1.41-.302 1.41-1.153v-7.93h-.001zm11.98.106c0-.691-.261-.904-1.079-.904h-.26v-.275h.678c.47 0 3.008.058 3.026.058.364 0 2.777-.058 3.296-.058h.695l.035 2.277h-.27c-.053-1.188-.58-1.667-1.795-1.667h-2.43v4.026h2.1c.816 0 1.268-.39 1.389-1.225l.31.018v3.178h-.293c-.138-.993-.642-1.383-1.857-1.383h-1.666v3.672c0 .603.296.905.885.905h1.736c1.126 0 1.944-.515 2.43-1.58h.314l-.731 2.23c-.505 0-2.898-.058-3.696-.058-.539 0-3.13.04-3.722.058h-.452v-.295h.278c.818-.017 1.08-.23 1.08-.923V6.815zm16.701 9.41h-.487l-1.984-5.511-2.035 5.512h-.47L45.4 6.975c-.26-.71-.505-.993-.957-1.08v-.26h.296c.191 0 1.149.059 1.375.059.191 0 1.182-.058 1.391-.058h.314v.275c-.505.019-.714.16-.714.443 0 .16.052.39.14.639l2.383 6.557 1.357-3.74-.887-2.516c-.383-1.081-.714-1.364-1.55-1.383v-.275h.28c.243 0 1.496.058 1.793.058.242 0 1.495-.058 1.773-.058h.417v.275h-.417c-.574 0-.852.142-.852.443 0 .16.07.444.174.727l2.314 6.522 1.827-5.53c.226-.709.33-1.17.33-1.453 0-.496-.243-.71-.782-.71h-.313v-.274h.087c.243 0 .851.058 1.217.058.173 0 .851-.058 1.18-.058h.123v.275c-.436.125-.66.443-1.007 1.525l-2.923 8.79zm4.01-2.563c.278.688.52 1.008.988 1.361.59.46 1.37.69 2.237.69 1.491 0 2.497-.796 2.497-1.946 0-.85-.486-1.31-2.282-2.175-1.74-.85-2.174-1.274-2.538-1.628-.537-.584-.762-1.114-.762-1.822 0-1.627 1.3-2.704 3.265-2.704.592 0 1.236.088 1.933.264.278.07.557.106.714.106.138 0 .209-.035.26-.153h.3l.034 2.229h-.247c-.156-.531-.26-.76-.487-1.05-.488-.585-1.254-.903-2.237-.903-1.248 0-2.064.601-2.064 1.504 0 .778.47 1.22 2.134 1.998 2.134 1.008 3.426 1.911 3.426 3.573 0 1.91-1.537 3.2-3.807 3.2a8.04 8.04 0 0 1-1.838-.229 3.676 3.676 0 0 0-.624-.089c-.209 0-.277.036-.415.2h-.295l-.035-.248c-.118-.7-.258-1.398-.418-2.09l.261-.089zM3.97 9.732c-.262 0-.51.06-.73.168-.587.291-.957.89-.955 1.546 0 .946.755 1.714 1.684 1.714.931 0 1.684-.768 1.684-1.714 0-.947-.753-1.715-1.684-1.715zm7.259 0c-.93 0-1.685.767-1.685 1.714 0 .946.754 1.714 1.685 1.714.93 0 1.684-.768 1.684-1.714 0-.947-.755-1.715-1.684-1.715z"/><path d="M18.47 14.875c-1.862 0-3.37-1.535-3.37-3.43 0-1.893 1.508-3.428 3.37-3.428 1.596 0 2.932 1.132 3.28 2.65h-1.78a1.68 1.68 0 0 0-1.5-.936c-.932 0-1.686.768-1.686 1.715 0 .946.754 1.714 1.685 1.714a1.68 1.68 0 0 0 1.502-.94l1.783-.017c-.339 1.53-1.68 2.672-3.285 2.672zm-7.241 0c-1.853 0-3.356-1.522-3.369-3.405l-.04-6.016h1.704l.01 3.228c.499-.396 1.077-.665 1.695-.665 1.86 0 3.368 1.535 3.368 3.429s-1.509 3.429-3.368 3.429zm-5.546 0l-.007-.859c-.382.389-1.043.859-1.824.859-1.86 0-3.251-1.535-3.251-3.43 0-1.893 1.508-3.428 3.368-3.428.29 0 .573.037.843.108 1.453.38 2.526 1.723 2.526 3.32v.01l.02 3.42H5.682zM11.229.017C5.027.017 0 5.134 0 11.446s5.027 11.43 11.229 11.43c6.2 0 11.228-5.118 11.228-11.43 0-6.312-5.028-11.429-11.228-11.429z"/></svg>
				<span class="visually-hidden">ABC News</span>
			</a>

<button class="nav-global-toggle" id="nav-global-toggle" aria-expanded="false">Menu</button>

</div>
			<div class="single-sticky">

							<div class="single-sticky-vertical"></div>
				<div class="single-sticky-title">
											Two Special Elections On Tuesday Could Hint At Another Blue Wave In 2020									</div>
				<a href="https://fivethirtyeight.com/features/two-special-elections-on-tuesday-could-hint-at-another-blue-wave-in-2020/?share=facebook" class="button share-sticky sticky-facebook">Share on Facebook</a>
				<a href="https://fivethirtyeight.com/features/two-special-elections-on-tuesday-could-hint-at-another-blue-wave-in-2020/?share=twitter"  class="button share-sticky sticky-twitter">Share on Twitter</a>

			</div>
			<div class="site-wrapper header-global-bottom" role="dialog" aria-label="Main menu">
		<nav class="nav-global" id="nav-global">
			<ul class="nav-global-menu">
				<li class="nav-global-menu-item menu-politics -current-vertical">
					<a
						href="https://fivethirtyeight.com/politics/"
						name="&amp;lpos=fivethirtyeight&amp;lid=Header Politics"
						aria-current=page					>
						Politics					</a>
				</li>
				<li class="nav-global-menu-item menu-sports">
					<a
						href="https://fivethirtyeight.com/sports/"
						name="&amp;lpos=fivethirtyeight&amp;lid=Header Sports"
											>
						Sports					</a>
				</li>
				<li class="nav-global-menu-item menu-science">
					<a
						href="https://fivethirtyeight.com/science/"
						name="&amp;lpos=fivethirtyeight&amp;lid=Header Science"
											>
						Science					</a>
				</li>
				<li class="nav-global-menu-item menu-podcast">
					<a
						href="https://fivethirtyeight.com/podcasts/"
						name="&amp;lpos=fivethirtyeight&amp;lid=Header Podcasts"
											>
						Podcasts					</a>
				</li>
				<li class="nav-global-menu-item menu-video">
					<a
						href="https://fivethirtyeight.com/videos/"
						name="&amp;lpos=fivethirtyeight&amp;lid=Header Video"
											>
						Video					</a>
				</li>
				<li class="nav-global-menu-item menu-interactive">
					<a
						href="https://projects.fivethirtyeight.com/"
						name="&amp;lpos=fivethirtyeight&amp;lid=Header Interactives"
					>
						Interactives					</a>
				</li>
				<li class="nav-global-menu-item menu-abcn -mobile-only">
					<a href="https://abcnews.go.com/" rel="noopener" name="&amp;lpos=fivethirtyeightHeader&amp;lid=Header ABC News">
						ABC News					</a>
				</li>
			</ul>

</nav><!-- #nav-global -->
		</div><!-- .site-wrapper -->
</header><!-- #header-global -->

<div class="site-main">
	<div id="wrapper" class="site-wrapper">
<div class="espn-announcement-banner"
			style="background-color: #dd9933;"
		>

<a href="http://abcnews.com/538" class="banner-content">

		<div class="banner-icon lightning">
			<svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 100 100"><path class="st0" d="M78.8 26.6c-.5-.5-1.3-.9-2-.9-.2 0-.5.1-.7.1l-23.7 5.9L62.6 3.9c.2-.4.3-.7.3-1.1 0-1.4-1.2-2.5-2.7-2.5H40.6c-1.3 0-2.3.8-2.6 1.9L26 51.6c-.2.8.1 1.7.8 2.3.5.4 1.2.7 1.9.7.2 0 .5 0 .7-.1l24.3-6.1-11.9 48.5c-.3 1.3.5 2.5 1.8 2.9.3.1.6.1.8.1 1.1 0 2-.6 2.5-1.5l32.3-69.3c.5-.8.3-1.8-.4-2.5"/></svg>		</div>

<div class="banner-content-text">This is an archived site and is no longer being updated. New 538 articles can be found at www.abcnews.com/538.</div>

<div class="banner-icon chevron">
			<svg xmlns="http://www.w3.org/2000/svg" width="10" height="10" viewBox="0 0 100 100"><path class="st1" d="M83.5 50c0-.8-.4-1.7-1-2.3L36.1 1.3c-.6-.6-1.5-1-2.3-1-.8 0-1.7.4-2.3 1l-5 5c-.6.6-1 1.5-1 2.3 0 .8.4 1.7 1 2.3L65.6 50 26.5 89.1c-.6.6-1 1.5-1 2.3 0 .9.4 1.7 1 2.3l5 5c.6.6 1.5 1 2.3 1 .8 0 1.7-.4 2.3-1l46.4-46.4c.6-.6 1-1.5 1-2.3"/></svg>		</div>
		</a>

</div>

<div id="content" class="single single-feature" data-col="2">

<div class="single-feature__row">
			<div id="primary" class="single-feature__col">
				<div id="article-main">
					<article id="post-271962" class="post-271962 fte_features type-fte_features status-publish has-post-thumbnail hentry tag-2020-election tag-2020-house-elections tag-california tag-special-elections tag-wisconsin espn_verticals-politics vertical-politics topic-slug-special-elections">

<header class="post-info single-post-header">
														<p class="topic single-topic">
								<time class="datetime">May 11, 2020</time>,
								at
								<time class="datetime updated" title="2020-05-11T17:29:48+00:00">1:29 PM</time>

</p>

							<div class="single-header">
								<h1 class="article-title article-title-single entry-title">
									Two Special Elections On Tuesday Could Hint At Another Blue Wave In 2020								</h1>

</div>

<div class="single-header-metadata-and-share-wrap">
								<div class="single-header-metadata-wrap">
																			<p class="single-metadata single-byline vcard">By <a href="https://fivethirtyeight.com/contributors/geoffrey-skelley/" title="" class="author url fn" rel="author">Geoffrey Skelley</a> and <a href="https://fivethirtyeight.com/contributors/nathaniel-rakich/" title="" class="author url fn" rel="author">Nathaniel Rakich</a></p>

																		<p class="single-metadata single-topic">Filed under <a href="https://fivethirtyeight.com/tag/special-elections/" class="term " name="">Special Elections</a></p>


																	</div>
								<div class="share">
																	</div> <!-- .share -->
							</div>

</header><!-- .post-info -->

<figure id="single-featured-image" class="single-featured-image">
	<span class="has-bugs post-thumbnail">
					<div class="bug-container">
				<picture class="featured-picture">
											<source media="(min-width: 768px)" srcset="https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?w=575 1x, https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?w=1150 2x">

											<source srcset="https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?w=575 1x, https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?w=1150 2x">
						<img width="575" height="432" src="https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?w=575" class="attachment-lede size-lede" alt="" srcset="https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png 1200w, https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?resize=100,75 100w, https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?resize=300,225 300w, https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?resize=768,576 768w, https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?resize=1024,768 1024w, https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?resize=683,512 683w, https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?resize=575,432 575w, https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?resize=470,352 470w, https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?resize=600,450 600w, https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?resize=347,260 347w, https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?resize=213,160 213w, https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?resize=207,155 207w, https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?resize=60,45 60w, https://fivethirtyeight.com/wp-content/uploads/2020/05/EU-SPECIAL-0511_4x3.png?resize=916,687 916w" sizes="(max-width: 575px) 100vw, 575px" />									</picture>

</div>

</span><!-- .has-bugs -->

<figcaption class="caption featured-image-caption">
													<p class="credits">ILLUSTRATION BY FIVETHIRTYEIGHT</p>
							</figcaption>

</figure><!-- .single-featured-image -->

						<div class="entry-content single-post-content">
							<p>Former Vice President Joe Biden leads President Trump in <a href="https://projects.fivethirtyeight.com/polls/president-general/">most early polls</a>, Democrats are leading polls of the <a href="https://projects.fivethirtyeight.com/congress-generic-ballot-polls/">generic congressional ballot</a> by 2018-level margins, and <a href="https://projects.fivethirtyeight.com/coronavirus-polls/?ex_cid=rrpromo">general disapproval</a> of the administration&#8217;s handling of the coronavirus pandemic threatens to <a href="https://www.nytimes.com/2020/04/25/us/politics/trump-election-briefings.html">sink Republican prospects</a> across the board. On Tuesday, we’ll get a taste of whether Democrats’ electoral advantage on paper will hold up in practice, as California and Wisconsin hold special elections for two vacant congressional seats. The main event is in the <a href="https://www.govtrack.us/congress/members/CA/25">California 25th Congressional District</a>, a bellwether seat in the north Los Angeles suburbs, where both parties see a chance to add to their ranks in the House. But if Democrats are also competitive in the quickly reddening, rural <a href="https://www.govtrack.us/congress/members/WI/7">Wisconsin 7th Congressional District</a>, it could <a href="https://fivethirtyeight.com/features/special-elections-so-far-point-to-a-democratic-wave-in-2018/">signal another blue wave</a> in the fall. Here’s everything you need to know about the two races.</p>
<h2><b>California 25th</b></h2>
<p>The California contest will test whether Democrats can hold onto a suburban and formerly GOP seat they captured during the 2018 blue wave. This election &#8212; <a href="https://fivethirtyeight.com/features/the-special-election-for-katie-hills-seat-will-test-democrats-strength-in-the-suburbs/">precipitated by the resignation</a> of Democratic Rep. Katie Hill in November after she admitted to an <a href="https://abcnews.go.com/Politics/reflecting-2019-photo-scandal-rep-katie-hill-fully/story?id=69105515">affair with a campaign staffer</a> &#8212; marks the second round of voting as <a href="https://elections.cdn.sos.ca.gov/sov/2020-primary/cd25-prim-official-canvass.pdf">no candidate won an outright majority</a> on March 3 to claim the seat. So now Democrat Christy Smith and Republican Mike Garcia &#8212; the top-two finishers in that initial vote &#8212; are battling it out on Tuesday to serve out the remainder of Hill&#8217;s term, which ends January 2021. But regardless of who wins, Smith and Garcia will face off again in November because <a href="https://elections.cdn.sos.ca.gov/sov/2020-primary/126-us-rep-congress.pdf">they both advanced</a> from the regular primary, also held on March 3.</p>
<p>We don’t have much polling to go on, but the contest looks close. The last public poll of the race dates back to an <a href="https://www.politico.com/f/?id=00000170-f5c6-d588-ab77-fdd79f1a0000">internal poll</a> the Garcia campaign released in March. In it, Garcia led Smith, 43 percent to 39 percent. According to <a href="https://www.insideelections.com/news/article/california-25-can-garcia-win-the-battle-and-the-war">Inside Elections</a>, private polling has consistently found Garcia leading by the low single digits. Election handicappers <a href="https://fivethirtyeight.com/features/the-2020-house-map-looks-good-for-democrats-but-republicans-still-have-a-shot/">rate it a toss-up</a>. And Smith &#8212; a first-term <a href="https://a38.asmdc.org/">assemblywoman in California’s legislature</a> &#8212; and Garcia &#8212; <a href="https://www.usnews.com/news/best-states/california/articles/2020-03-05/legislator-ex-navy-pilot-matched-in-california-house-race">a businessman and former Navy fighter pilot</a> &#8212; <a href="https://www.fec.gov/data/elections/house/CA/25/2020/">have each raised and spent</a> around $2 million. (The national party campaign arms &#8212; the Democratic Congressional Campaign Committee and the National Republican Congressional Committee &#8212; have also been busy, too, <a href="https://www.opensecrets.org/races/outside-spending?cycle=2020&amp;id=CA25&amp;spec=N">collectively spending</a> over $3 million in the district.) However, the once-conservative district has shifted left over the last few years: Mitt Romney won it by 2 points in 2012, but Hillary Clinton carried it by 7 points in 2016, according to <a href="https://www.dailykos.com/stories/2012/11/19/1163009/-Daily-Kos-Elections-presidential-results-by-congressional-district-for-the-2012-2008-elections">data from Daily Kos Elections</a>.</p>
<p><a href="https://www.dailynews.com/2020/04/24/christy-smith-mike-garcia-face-off-in-online-forum-for-northern-la-county-seat-in-congress/">One of the big issues</a> in the race, though, may be a state issue: Assembly Bill 5, a new law <a href="https://legiscan.com/CA/rollcall/AB5/id/874384">Smith supported in the legislature</a> that limits <a href="https://www.usatoday.com/story/news/politics/2020/01/21/california-lawmaker-promises-refine-ab-5-amid-lawsuits-confusion/4505702002/">businesses’ ability</a> to label workers as independent contractors, rather than employees (who are entitled to employment-related benefits that independent contractors would otherwise not receive), has experienced widespread backlash. Critics argue it&#8217;s <a href="https://www.latimes.com/business/technology/story/2020-03-26/coronavirus-disrupted-their-income-now-their-calls-for-california-to-take-action-on-ab5-are-getting-louder">made it harder</a> for freelancers and gig workers to find jobs, and <a href="https://fivethirtyeight.com/features/the-terrible-jobs-report-gets-worse-the-more-you-read-it/">the economic crisis</a> wrought by the coronavirus pandemic has made it a potential landmine for Smith &#8212; it’s one of Garcia’s <a href="https://www.avpress.com/news/house-hopefuls-garcia-smith-discuss-issues-at-forum/article_786f89a0-876b-11ea-b505-a32f3ab99ebe.html">main talking points</a>. It’s not Smith’s only controversy either; she’s also <a href="https://www.dailynews.com/2020/05/07/christy-smiths-smear-of-jet-pilot-mike-garcia-runs-into-turbulence-in-25th-district-race/">received blowback</a> after a video leaked in which she appeared to mock the Garcia campaign’s focus on highlighting his military service.</p>
<p>The special election will also be a testing ground for conducting an election during a pandemic. Democratic Gov. Gavin Newsom <a href="https://www.sos.ca.gov/administration/news-releases-and-advisories/2020-news-releases-and-advisories/ap20036-governor-newsom-signs-executive-order-requiring-counties-mail-every-voter-ballot-special-elections-cd-25-and-sd-28/">issued an executive order</a> requiring counties to mail every voter a ballot, though that doesn’t mean everyone will vote by mail. The district has a <a href="https://abc7.com/special-election-voting-in-time-of-coronavirus-katie-hill-25th-congressional-district/6143796/">limited number of in-person voting sites</a>, and the late addition of one in the city of Lancaster &#8212; a move supported by the city’s Republican mayor &#8212; <a href="https://www.washingtonpost.com/politics/trump-attacks-decision-to-add-in-person-voting-center-in-california-house-race/2020/05/09/6c1d1f92-922d-11ea-9e23-6914ee410a5f_story.html">prompted Trump to tweet</a> that the election is being “rigged” by Democrats. But Garcia and Smith haven’t been able to rely on traditional get-out-the-vote techniques as they fight for every vote in the final days of the campaign. Instead, they’ve <a href="https://www.rollcall.com/2020/05/05/race-to-replace-katie-hill-tests-tactics-of-pandemic-politicking/">had to mount campaigns</a> built more on videoconferencing, virtual town halls and phone banking than typical door-knocking.</p>
<p>And as always, who votes will matter. About 118,000 ballots had been returned as of May 11, <a href="https://tableau.the-pdi.com/t/CampaignTools/views/25thCDSpecialAVTracker/2020SpecialElectionTrackerVB?:isGuestRedirectFromVizportal=y&amp;:embed=y">according to Political Data, Inc</a>, and at first blush, they bode well for Garcia &#8212; registered Republicans have cast 44.5 percent of them versus 35.6 percent by Democrats, plus 20.0 percent by independents or other parties. But these figures aren’t all that different from the <a href="https://www.politicaldata.com/2020-primary-election-tracker/">ballots that had been returned the day before the March 3 contest</a>, when registered Republicans had cast 45.0 percent of ballots compared to 36.6 percent by Democrats, plus 18.4 percent by others. Yet in the first round of voting, the Democratic candidates combined to win 51 percent of the vote, while Republicans won 49 percent. (It’s worth noting, though, that about twice as many voters have returned mail ballots for this election than just before the March 3 contest, as most votes will be cast by mail because of the pandemic.) In other words, party registration data at this point doesn’t tell the whole story because younger and minority voters are more likely to cast <a href="https://www.buzzfeednews.com/article/skbaer/california-election-blue-wave-democrats-ballots">late-arriving ballots</a> and they’re more likely to vote Democratic. In California, <a href="https://www.sos.ca.gov/elections/voter-registration/vote-mail/">ballots must be postmarked on or by Election Day</a>, but they can be received up to three days after.</p>
<p>There’s a lot at stake in the California 25th &#8212; and as is often the case with California, <a href="https://www.sacbee.com/news/politics-government/capitol-alert/article240828386.html">it could be a few days</a> before we know the outcome.</p>
<h2><b>Wisconsin 7th</b></h2>
<p>Halfway across the country, Wisconsin is holding <i>another</i> election just five weeks after drawing widespread criticism for <a href="https://fivethirtyeight.com/features/election-preview-yes-wisconsin-is-still-holding-its-primary-on-tuesday/">not canceling its presidential primary</a> amid the pandemic. After the <a href="https://fivethirtyeight.com/features/voters-experiences-in-wisconsin-amid-the-coronavirus/">many mishaps of that election</a>, Gov. Tony Evers reportedly considered <a href="https://www.jsonline.com/story/news/politics/elections/2020/04/10/tony-evers-taking-close-look-postponing-7th-district-election/5125548002/">postponing the 7th District special</a>, but never pulled the trigger — perhaps fearing that a court would overturn his decision <a href="https://www.jsonline.com/story/news/politics/elections/2020/04/06/tony-evers-issues-order-shutting-down-tuesdays-election/2954626001/">yet again</a>.</p>
<p>So just like last month, polling places will be open in Wisconsin on Tuesday, and just like last month, some poll workers are <a href="https://www.wuwm.com/post/wisconsin-set-hold-more-elections-during-coronavirus-pandemic#stream/0">begging out</a> of working the election and the National Guard is being called in to help. It’s unclear, however, how many headaches will ensue. There have been no widespread reports of polling-place closures, and the ruralness of the district minimizes the potential for long lines. (In April, the longest lines were reported in urban areas like Milwaukee and Green Bay, which are not voting on Tuesday; the biggest city in the 7th District is Wausau, population less than 40,000.) Indeed, the Wisconsin Elections Commission <a href="https://www.wxpr.org/post/state-official-tuesday-s-special-election-much-better-shape-chaotic-april-voting#stream/0">insists that the state is better prepared</a> for May’s election than it was for April’s, because there have been no legal challenges pushing to change the rules of the election and officials now have experience running an election mid-pandemic.</p>
<p>However, just like last month, many more Wisconsinites than normal are opting to vote by mail. As of Monday morning, local officials had reported receiving <a href="https://elections.wi.gov/publications/statistics/absentee">112,892 absentee-ballot applications</a>, a comparable number to the April election. Indeed, in the 21 counties wholly contained within the 7th District, 103,402 ballots had been requested for the special election compared with 101,846 for the <a href="https://elections.wi.gov/node/6862">April primary</a>. Last month, this volume of absentee-ballot requests <a href="https://www.jsonline.com/story/news/2020/04/21/wisconsin-absentee-ballot-crisis-fueled-multiple-failures/5156825002/">overwhelmed election offices</a> and led to many people not getting mailed their ballot in time to vote.</p>
<p>However they vote, residents of the Wisconsin 7th will <a href="https://www.wausaudailyherald.com/story/news/politics/elections/2020/05/06/7th-congressional-district-tom-tiffany-tricia-zunker-face-off/3060660001/">elect</a> either Republican state Sen. Tom Tiffany or Democrat Tricia Zunker, the president of the Wausau School Board, to be their next member of Congress. This northwestern Wisconsin district was once a <a href="https://madison.com/ct/opinion/column/john_nichols/john-nichols-road-to-future-of-the-democratic-party-runs/article_77926000-0058-5582-8aff-04e61cae3e53.html">hotbed of Democratic populism</a>, represented by progressive former Rep. Dave Obey for 42 years and voting for Barack Obama <a href="https://www.dailykos.com/stories/2012/11/19/1163009/-Daily-Kos-Elections-presidential-results-by-congressional-district-for-the-2012-2008-elections">by 8 points</a> in 2008.<span class="espn-footnote-link" data-footnote-id="1" data-footnote-url="#fn-1" data-footnote-content="&amp;lt;p&amp;gt;According to Daily Kos Elections calculations based on the district&amp;rsquo;s current boundaries.&amp;lt;/p&amp;gt;
"><sup id="ss-1">1</sup></span> But a huge bloc of non-Hispanic white residents without bachelor’s degrees — 72 percent of the population age 25 or older — has turned the 7th District into Republican turf. Former Rep. Sean Duffy, whose <a href="https://www.rollcall.com/2019/08/26/gop-rep-sean-duffy-resigning-on-sept-23/">resignation for family reasons</a> in September triggered this special election, flipped the seat red in 2010, and Romney won here by a narrow margin in 2012. But Trump put an exclamation point on the district’s realignment when he carried it by more than 20 points in 2016.</p>
<p>Zunker can hope that the district’s ancestral Democratic tradition means there are latent Democratic votes for her to activate. But even the strongest liberal candidates have failed to carry the Wisconsin 7th in recent years. According to <a href="https://docs.google.com/spreadsheets/d/17yr9mcAtuUdNjI9NEPYKxXsEldzzQ2ZaDwEAbnPRyS4/edit#gid=553790267">Daily Kos Elections</a>, Sen. Tammy Baldwin lost it by 5 points in 2018, and according to <a href="https://twitter.com/JMilesColeman/status/1250117932010569736">J. Miles Coleman</a> of Sabato’s Crystal Ball, Wisconsin Supreme Court Justice-elect Jill Karofsky lost it by 6 points last month.</p>
<p>In addition, as of April 22, Tiffany had outspent Zunker <a href="https://www.fec.gov/data/elections/house/WI/07/2020/">$1.1 million to $328,000</a>. So even though there have been <a href="https://projects.fivethirtyeight.com/polls/house/wisconsin/">no public polls</a> of the race, the GOP is the clear favorite on Tuesday, with election handicappers rating it “Solid Republican.”</p>
<p>Still, pay attention to the final margin, both here and in California. When a party consistently <a href="https://www.dailykos.com/stories/2018/1/9/1698453/-Special-elections-are-correlated-with-House-election-results-and-that-s-good-news-for-Democrats">overperforms its usual partisan baseline</a> in special elections, it bodes well for that party in the general election as well. So even a narrow loss by Zunker, if paired with a comfortable Smith win, would add to the evidence that another Democratic wave is building.</p>
<div class="ornamental-rule">
<hr>
<p><span></span></div>
<h3 class="video-title">FiveThirtyEight Politics Podcast: Does The U.S. Have A Coronavirus Recovery Plan?</h3>
<div class="video-placeholder videoplayer abc"><iframe title="FiveThirtyEight Politics Podcast: Does The U.S. Have A Coronavirus Recovery Plan?" allow="autoplay; fullscreen; picture-in-picture; encrypted-media" loading="lazy" class="abc-player" src="https://assets.espn.go.com/players/web-player-bundle/5.5.4/embed/index.html?id=70626713&amp;brand=fivethirtyeight&amp;section=politics" width="100%" height="100%" scrolling="no" data-omniture="video-on-storypage|271962|Two Special Elections On Tuesday Could Hint At Another Blue Wave In 2020|70626713"></iframe></div>
<div class="video-footer">
<div class="video-footer-links"><a href="/videos/">All Videos</a><a target="_blank" href="https://www.youtube.com/FiveThirtyEight">YouTube</a></div>
<hr>
</div>
						</div><!-- .entry-content -->
					</article>
				</div>
				<div id="article-additional">
											<div class="entry-footnotes print-only">
	<h2>Footnotes</h2>
	<div class="entry-footnotes-content">
		<ol class="footnotes"><li data-wrap="false" data-footnote-id="1" id="fn-1"><span><p>According to Daily Kos Elections calculations based on the district’s current boundaries.</p>
</span></li></ol>	</div><!-- .entry-footnotes-content -->
</div><!-- .entry-footnotes -->
<div class="mini-bio">
		<p>Geoffrey Skelley is a senior elections analyst at FiveThirtyEight. <span class="mail"><a aria-label="Email Geoffrey Skelley" href="mailto:geoffrey.skelley@abc.com"><i class="icon icon-mail"></i></a></span> <span class="twitter"><a href="https://twitter.com/geoffreyvs" target="_blank"><i class="icon icon-twitter"></i> <span class="twitter-username">@geoffreyvs</span></a></span></p>
</div>
<!-- .post-author -->
<div class="mini-bio">
		<p>Nathaniel Rakich is a senior editor and senior elections analyst at FiveThirtyEight. <span class="mail"><a aria-label="Email Nathaniel Rakich" href="mailto:nathaniel.rakich@fivethirtyeight.com"><i class="icon icon-mail"></i></a></span> <span class="twitter"><a href="https://twitter.com/baseballot" target="_blank"><i class="icon icon-twitter"></i> <span class="twitter-username">@baseballot</span></a></span></p>
</div>
<!-- .post-author -->
<div id="entry-comments" class="fte-expandable">
	<h3 class="fte-expandable-title">Comments</h3>

<div class="entry-comments-content fte-expandable-content">
		<div class="fb-comments" data-href="http://fivethirtyeight.com/?post_type=fte_features&#038;p=271962" data-numposts="5" data-colorscheme="light"
														></div>
	</div>
	<!-- .entry-comments-content -->
</div>
<!-- .entry-comments -->
<div class="tags">
	<p class="filed-under">Filed under</p>
	<p class="tag-links"><a class="tag" href="https://fivethirtyeight.com/tag/2020-election/">2020 Election <span class="count">(1214 posts)</span></a>
<a class="tag" href="https://fivethirtyeight.com/tag/special-elections/">Special Elections <span class="count">(148)</span></a>
<a class="tag" href="https://fivethirtyeight.com/tag/wisconsin/">Wisconsin <span class="count">(124)</span></a>
<a class="tag" href="https://fivethirtyeight.com/tag/california/">California <span class="count">(109)</span></a>
<a class="tag" href="https://fivethirtyeight.com/tag/2020-house-elections/">2020 House Elections <span class="count">(27)</span></a>
</p>
</div>
									</div>
			</div>
						<div class="single-feature__col">
				<div id="secondary" class="single-col vertical-col blog-col">

<div class="sidebar-feature visually-hidden"><aside id="fivethirtyeight-embed-490" class="widget flexible interactives embed "><h2 class="widget-title">Interactives</h2>
					<iframe id="pym-fivethirtyeight_embed_490" title="Interactives" src="https://projects.fivethirtyeight.com/polls/president-primary-r/2024/national/" width="300" height="250" scrolling="no"></iframe>
			</aside>

<aside class="widget fivethirtyeight-featured-video-widget">
		<h2 class="widget-title">Latest Videos</h2>
					<ul>
										<li>
							<article id="post-271962" class="widget-video">
								<div class="widget-video__content">
									<h3 class="widget-video__title">
										<a href="https://fivethirtyeight.com/videos/why-biden-is-losing-support-among-voters-of-color/?cid=rrfeaturedvideo" data-adl-event-name="content select interaction" data-placement="Latest Videos" data-position_number="1" data-content_title="Why Biden Is Losing Support Among Voters Of Color" data-content_id="362896" data-content_select_type="fte_videos">
											Why Biden Is Losing Support Among Voters Of Color										</a>
									</h3>
								</div>
								<div class="widget-video__poster">
									<a href="https://fivethirtyeight.com/videos/why-biden-is-losing-support-among-voters-of-color/?cid=rrfeaturedvideo" class="post-thumbnail" data-adl-event-name="content select interaction" data-placement="Latest Videos" data-position_number="1" data-content_title="Why Biden Is Losing Support Among Voters Of Color" data-content_id="362896" data-content_select_type="fte_videos">
																					<button class="orange-play-button thumbnail-play-button" aria-label="Play"></button>
																				<img width="300" height="225" class="attachment-small size-small" alt="" srcset="https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg 1200w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=100,75 100w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=300,225 300w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=768,576 768w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=1024,768 1024w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=683,512 683w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=575,432 575w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=470,352 470w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=600,450 600w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=347,260 347w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=213,160 213w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=207,155 207w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=60,45 60w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230911_538_PoliticsPod_4x3.jpg?resize=916,687 916w" sizes="(max-width: 300px) 100vw, 300px" />									</a>
								</div>
							</article>
						</li>
												<li>
							<article id="post-271962" class="widget-video">
								<div class="widget-video__content">
									<h3 class="widget-video__title">
										<a href="https://fivethirtyeight.com/videos/should-we-trust-polls-campaigns-leak-to-the-press/?cid=rrfeaturedvideo" data-adl-event-name="content select interaction" data-placement="Latest Videos" data-position_number="2" data-content_title="Should We Trust Polls Campaigns Leak To The Press?" data-content_id="362859" data-content_select_type="fte_videos">
											Should We Trust Polls Campaigns Leak To The Press?										</a>
									</h3>
								</div>
								<div class="widget-video__poster">
									<a href="https://fivethirtyeight.com/videos/should-we-trust-polls-campaigns-leak-to-the-press/?cid=rrfeaturedvideo" class="post-thumbnail" data-adl-event-name="content select interaction" data-placement="Latest Videos" data-position_number="2" data-content_title="Should We Trust Polls Campaigns Leak To The Press?" data-content_id="362859" data-content_select_type="fte_videos">
																					<button class="orange-play-button thumbnail-play-button" aria-label="Play"></button>
																				<img width="300" height="225" class="attachment-small size-small" alt="" srcset="https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg 1200w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=100,75 100w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=300,225 300w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=768,576 768w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=1024,768 1024w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=683,512 683w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=575,432 575w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=470,352 470w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=600,450 600w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=347,260 347w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=213,160 213w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=207,155 207w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=60,45 60w, https://fivethirtyeight.com/wp-content/uploads/2023/09/230906_538_PoliticsPod_4x3.jpg?resize=916,687 916w" sizes="(max-width: 300px) 100vw, 300px" />									</a>
								</div>
							</article>
						</li>
												<li>
							<article id="post-271962" class="widget-video">
								<div class="widget-video__content">
									<h3 class="widget-video__title">
										<a href="https://fivethirtyeight.com/videos/how-well-can-you-tell-the-2024-gop-candidates-apart/?cid=rrfeaturedvideo" data-adl-event-name="content select interaction" data-placement="Latest Videos" data-position_number="3" data-content_title="How Well Can You Tell The 2024 GOP Candidates Apart?" data-content_id="362601" data-content_select_type="fte_videos">
											How Well Can You Tell The 2024 GOP Candidates Apart?										</a>
									</h3>
								</div>
								<div class="widget-video__poster">
									<a href="https://fivethirtyeight.com/videos/how-well-can-you-tell-the-2024-gop-candidates-apart/?cid=rrfeaturedvideo" class="post-thumbnail" data-adl-event-name="content select interaction" data-placement="Latest Videos" data-position_number="3" data-content_title="How Well Can You Tell The 2024 GOP Candidates Apart?" data-content_id="362601" data-content_select_type="fte_videos">
																					<button class="orange-play-button thumbnail-play-button" aria-label="Play"></button>
																				<img width="300" height="225" class="attachment-small size-small" alt="" srcset="https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg 1200w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=100,75 100w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=300,225 300w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=768,576 768w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=1024,768 1024w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=683,512 683w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=575,432 575w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=470,352 470w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=600,450 600w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=347,260 347w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=213,160 213w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=207,155 207w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=60,45 60w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_WhoSaidThis_4x3.jpg?resize=916,687 916w" sizes="auto, (max-width: 300px) 100vw, 300px" />									</a>
								</div>
							</article>
						</li>
												<li>
							<article id="post-271962" class="widget-video">
								<div class="widget-video__content">
									<h3 class="widget-video__title">
										<a href="https://fivethirtyeight.com/videos/what-the-gop-primary-looks-like-in-the-early-states/?cid=rrfeaturedvideo" data-adl-event-name="content select interaction" data-placement="Latest Videos" data-position_number="4" data-content_title="What The GOP Primary Looks Like In The Early States" data-content_id="362590" data-content_select_type="fte_videos">
											What The GOP Primary Looks Like In The Early States										</a>
									</h3>
								</div>
								<div class="widget-video__poster">
									<a href="https://fivethirtyeight.com/videos/what-the-gop-primary-looks-like-in-the-early-states/?cid=rrfeaturedvideo" class="post-thumbnail" data-adl-event-name="content select interaction" data-placement="Latest Videos" data-position_number="4" data-content_title="What The GOP Primary Looks Like In The Early States" data-content_id="362590" data-content_select_type="fte_videos">
																					<button class="orange-play-button thumbnail-play-button" aria-label="Play"></button>
																				<img width="300" height="225" class="attachment-small size-small" alt="" srcset="https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg 1200w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=100,75 100w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=300,225 300w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=768,576 768w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=1024,768 1024w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=683,512 683w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=575,432 575w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=470,352 470w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=600,450 600w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=347,260 347w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=213,160 213w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=207,155 207w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=60,45 60w, https://fivethirtyeight.com/wp-content/uploads/2023/08/230818_538_PoliticsPod_4x3.jpg?resize=916,687 916w" sizes="auto, (max-width: 300px) 100vw, 300px" />									</a>
								</div>
							</article>
						</li>
									</ul>
			</aside>
			<!-- end widget -->
		</div></div><!-- #secondary -->
			</div>
					</div>

</div><!-- .single -->

</div><!-- #wrapper .site-wrapper -->
	</div><!-- .site-main -->

<footer id="colophon" class="site-footer">

<div class="site-wrapper footer-main-content">

<div class="footer-section-get-more">
			Get more FiveThirtyEight		</div>

<div class="footer-section-primary-links">
			<ul class="footer-menu">
				<li class="footer-menu-item">
					<a href="https://cottonbureau.com/stores/fivethirtyeight#/shop" name="&amp;lpos=fivethirtyeightFooter&amp;lid=store">Store</a>
				</li>
				<li class="footer-menu-item">
					<a href="https://twitter.com/fivethirtyeight" name="&amp;lpos=fivethirtyeightFooter&amp;lid=twitter">Twitter</a>
				</li>
				<li class="footer-menu-item">
					<a href="https://www.facebook.com/fivethirtyeight" name="&amp;lpos=fivethirtyeightFooter&amp;lid=facebook">Facebook</a>
				</li>
				<li class="footer-menu-item">
					<a href="https://data.fivethirtyeight.com/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=data">Data</a>
				</li>
				<li class="footer-menu-item">
					<a href="https://fivethirtyeight.com/features/fear-not-readers-we-have-rss-feeds/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=rss">RSS</a>
				</li>
			</ul>
		</div><!-- .footer-primary-links -->

<div class="footer-section-social-follow">
			<ul class="footer-menu">
				<li class="footer-menu-item social-share-item">
					<div class="fb-like" data-href="https://www.facebook.com/fivethirtyeight" data-layout="button_count"></div>
				</li>
				<li class="footer-menu-item social-share-item">
					<a href="https://twitter.com/FiveThirtyEight" class="twitter-follow-button" data-show-count="true">Follow @FiveThirtyEight</a>
				</li>
			</ul>
		</div>

<div class="footer-section-secondary-links">
			<ul class="footer-menu">
				<li class="footer-menu-item">
					<a href="https://fivethirtyeight.com/about-us/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=about-us">About Us</a>
				</li>
				<li class="footer-menu-item">
					<a href="https://fivethirtyeight.com/jobs/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=jobs">Jobs</a>
				</li>
				<li class="footer-menu-item">
					<a href="https://fivethirtyeight.com/masthead/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=masthead">Masthead</a>
				</li>
				<li class="footer-menu-item">
					<a href="https://fivethirtyeight.com/how-to-pitch-fivethirtyeight/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=pitch">Pitch FiveThirtyEight</a>
				</li>
				<li class="footer-menu-item">
					<a href="https://disneyadsales.com/our-brands/abc-news/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=advertise">Advertise With Us</a>
				</li>
				<li class="footer-menu-item">
					<a href="http://priv-policy.imrworldwide.com/priv/browser/us/en/optout.html" name="&amp;lpos=fivethirtyeightFooter&amp;lid=nielsen">About Nielsen Measurement</a>
				</li>
			</ul>
		</div><!-- .footer-secondary-links -->

<div class="footer-section-powered-by">
			Powered by <a href="https://wpvip.com/?utm_source=vip_powered_wpcom&#038;utm_medium=web&#038;utm_campaign=VIP%20Footer%20Credit&#038;utm_term=fivethirtyeight.com" rel="generator nofollow" class="powered-by-wpcom">WordPress VIP</a>		</div><!-- .powered-by -->

<div class="footer-section-tertiary-links">
			<ul class="footer-menu">
				<li class="menu-item">
					<a href="https://disneytermsofuse.com/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=disneyTOS" target="_blank" rel="noopener noreferrer">Terms of Use</a>
				</li>
				<li class="menu-item">
					<a href="https://disneyprivacycenter.com/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=disneyPrivacy" target="_blank" rel="noopener noreferrer">Privacy Policy</a>
				</li>

<li class="menu-item"><a href="https://privacy.thewaltdisneycompany.com/en/dnssmpi/" class="ot-cmp-link">Do Not Sell or Share My Personal Information</a></li>
				<li class="menu-item">
					<a href="https://privacy.thewaltdisneycompany.com/en/current-privacy-policy/your-us-state-privacy-rights/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=californiaPrivacyRights" target="_blank" rel="noopener noreferrer">Your US State Privacy Rights</a>
				</li>
				<li class="menu-item">
					<a href="https://disneyprivacycenter.com/kids-privacy-policy/english/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=childrensPrivacy" target="_blank" rel="noopener noreferrer">Children's Online Privacy Policy</a>
				</li>
				<li class="menu-item">
					<a href="https://privacy.thewaltdisneycompany.com/en/privacy-controls/online-tracking-and-advertising/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=adPreferences" target="_blank" rel="noopener noreferrer">Interest-Based Ads</a>
				</li>
			</ul>
			<p>
				&copy; 2025 ABC News Internet Ventures. All rights reserved.
			</p>
		</div>
		<!-- / .footer-section-tertiary-links -->
	</div><!-- .site-wrapper -->

<div class="footer-section-additional-info" id="footer-additional-info">
		<div class="site-wrapper">
			<button class="close-additional-info" id="close-additional-info" aria-label="Close"><span class="visually-hidden">Close Additional Information</span></button>
			<a href="https://disneytermsofuse.com/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=disneyTOS">Terms of Use</a> and <a href="https://disneyprivacycenter.com/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=disneyPrivacy">Privacy Policy</a> and Safety Information/<a href="https://disneyprivacycenter.com/notice-to-california-residents/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=californiaPrivacyRights">Your California Privacy Rights</a>/<a href="https://disneyprivacycenter.com/kids-privacy-policy/english/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=childrensPrivacy">Children's Online Privacy Policy</a> are applicable to you. © 2025 ABC News Internet Ventures. All rights reserved. <a href="https://privacy.thewaltdisneycompany.com/en/privacy-controls/online-tracking-and-advertising/" name="&amp;lpos=fivethirtyeightFooter&amp;lid=adPreferences">Interest-Based Ads</a>. <a href="https://disneyprivacycenter.com/cookies-policy-translations/cookies-policy/">Cookie Policy</a>.
		</div><!-- .site-wrapper -->
	</div><!-- .footer-section-additional-info -->
</footer><!-- .site-footer -->
<script type="speculationrules">
{"prefetch":[{"source":"document","where":{"and":[{"href_matches":"\/*"},{"not":{"href_matches":["\/wp-*.php","\/wp-admin\/*","\/wp-content\/uploads\/*","\/wp-content\/*","\/wp-content\/plugins\/*","\/wp-content\/themes\/espn-fivethirtyeight\/*","\/*\\?(.+)"]}},{"not":{"selector_matches":"a[rel~=\"nofollow\"]"}},{"not":{"selector_matches":".no-prefetch, .no-prefetch a"}}]},"eagerness":"conservative"}]}
</script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/abc-blocks/assets/js/pym.min.js" id="abc-ai2html-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/abc-audio-features/assets/js/blocks.min.js?ver=1.2.2" id="abc-audio-features-blocks-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/abc-blocks/assets/js/blocks.min.js?ver=1.1.2" id="abc-blocks-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/gif-play-button/assets/js/gif-play-button.min.js?ver=1.1.2" id="gif-play-button-scripts-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/utilities/assets/js/video.min.js?ver=1.1.2" id="video-js"></script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/plugins/disney-messaging/assets/js/newsletter.min.js?ver=1.1.2" id="newsletter-oneid-js"></script>
<script type="text/javascript" id="wp-util-js-extra">
/* <![CDATA[ */
var _wpUtilSettings = {"ajax":{"url":"\/wp-admin\/admin-ajax.php"}};
/* ]]> */
</script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-includes/js/wp-util.min.js?ver=6.8.2" id="wp-util-js"></script>
<script type="text/javascript" id="fte-main-js-extra">
/* <![CDATA[ */
var ESPNSocial = {"fbVersion":"6.0","fbAppId":"797620670264818"};
/* ]]> */
</script>
<script type="text/javascript" src="https://fivethirtyeight.com/wp-content/themes/espn-fivethirtyeight/dist/js/frontend.js?ver=1.1.2" id="fte-main-js"></script>
<script type="text/javascript" src="//datawrapper.dwcdn.net/lib/embed.js?ver=1.1.2" id="datawrapper-js"></script>
<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","licenseKey":"f6169b8cc4","applicationID":"100041457","transactionName":"bwcDZBYEW0ZVVhEMXVZNIFMQDFpbG0YMC1VUB0xWEABqU1FUERBAXRE=","queueTime":0,"applicationTime":305,"atts":"Q0AUEl4eSBkWVEdfSUUf","errorBeacon":"bam.nr-data.net","agent":""}</script></body>
</html>
