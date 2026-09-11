const CACHE='dessica-328767d6fd1c';
const ASSETS=['./','./index.html','./campaign.json','./Dessica_Campaign.md','./manifest.webmanifest','./icon-180.png','./icon-192.png','./icon-512.png'];
self.addEventListener('install',event=>event.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS)).then(()=>self.skipWaiting())));
self.addEventListener('activate',event=>event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith('dessica-')&&k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim())));
self.addEventListener('fetch',event=>{
 if(event.request.method!=='GET'||new URL(event.request.url).origin!==self.location.origin)return;
 event.respondWith(fetch(event.request).then(response=>{
  if(!response.ok)throw Error('HTTP '+response.status);
  const copy=response.clone();event.waitUntil(caches.open(CACHE).then(c=>c.put(event.request,copy)));
  return response;
 }).catch(async()=>{const cached=await caches.match(event.request);if(cached){const headers=new Headers(cached.headers);headers.set('X-Dessica-Cache','offline');return new Response(cached.body,{status:cached.status,statusText:cached.statusText,headers});}if(event.request.mode==='navigate')return(await caches.match('./index.html'))||Response.error();return Response.error();}));
});
