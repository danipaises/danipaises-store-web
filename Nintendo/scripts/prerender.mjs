import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {render,getRoutes,pageMeta} from '../.ssr/entry-server.js';
const origin=process.env.SITE_URL||'https://danipaises.com.br/nintendo';
const template=await fs.readFile('../nintendo/index.html','utf8');
const escape=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const routes=getRoutes();
for(const route of routes){
 const {title,description}=pageMeta(route);
 const canonical=origin+route;
 const meta=`<link rel="canonical" href="${escape(canonical)}"/><meta property="og:type" content="website"/><meta property="og:locale" content="pt_BR"/><meta property="og:title" content="${escape(title)}"/><meta property="og:description" content="${escape(description)}"/><meta property="og:url" content="${escape(canonical)}"/><script type="application/ld+json">${JSON.stringify({'@context':'https://schema.org','@type':route==='/'?'WebSite':'WebPage',name:title,description,inLanguage:'pt-BR',url:canonical,isPartOf:{'@type':'WebSite',name:'Nintendo Universe',url:origin},about:'Enciclopédia independente de fãs sobre a Nintendo'}).replace(/</g,'\\u003c')}</script>`;
 const html=template.replace(/<title>[\s\S]*?<\/title>/,`<title>${escape(title)}</title>`).replace(/<meta name="description" content="[^"]*"\s*\/>/,`<meta name="description" content="${escape(description)}"/>`).replace('<!--page-meta-->',meta).replace('data-path="/"',`data-path="${route}"`).replace('<!--app-html-->',render(route));
 const target=route==='/'?'../nintendo/index.html':path.join('../nintendo',route.slice(1),'index.html');await fs.mkdir(path.dirname(target),{recursive:true});await fs.writeFile(target,html);
}
await fs.copyFile('../nintendo/index.html','../nintendo/offline.html');
const notFound=template.replace('<!--app-html-->',render('/404')).replace('<title>Nintendo Universe — Cada jogo, uma história</title>','<title>Página não encontrada | Nintendo Universe</title>').replace('data-path="/"','data-path="/404"');await fs.writeFile('../nintendo/404.html',notFound);
await fs.writeFile('../nintendo/sitemap.xml',`<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${routes.filter(r=>!['/busca','/colecao','/comparar'].includes(r)).map(r=>`<url><loc>${origin}${r}</loc></url>`).join('')}</urlset>`);
await fs.writeFile('../nintendo/robots.txt',`User-agent: *\nAllow: /\nSitemap: ${origin}/sitemap.xml\n`);
await fs.mkdir('../nintendo/dados',{recursive:true});const files=['games','consoles','franchises','characters','history','quiz','media','game-sources','history-sources'];const catalog={project:'Nintendo Universe',version:1,researchedAt:'2026-10-17',scope:'Acervo em expansão; não é uma lista completa de todos os jogos Nintendo.'};for(const f of files)catalog[f]=JSON.parse(await fs.readFile(`src/data/${f}.json`,'utf8'));await fs.writeFile('../nintendo/dados/catalogo.json',JSON.stringify(catalog,null,2));
const assets=(await fs.readdir('../nintendo/assets')).filter(f=>/\.(js|css)$/.test(f)).map(f=>'/nintendo/assets/'+f);
const version=crypto.createHash('sha256').update(assets.join(',')+JSON.stringify(catalog)).digest('hex').slice(0,12);
const precache=['/','/offline.html','/jogos','/consoles','/franquias','/personagens','/historia','/linha-do-tempo','/colecao','/quiz','/pokedex','/evolucoes','/comparar','/museu','/busca','/sobre','/fontes','/manifest.webmanifest','/icon.svg','/icons/icon-192.png','/icons/icon-512.png'].map(url=>'/nintendo'+url).concat(assets);
const worker=`const VERSION='nu-nintendo-v1-${version}';
const PRECACHE=${JSON.stringify(precache)};
self.addEventListener('install',event=>{event.waitUntil(caches.open(VERSION).then(cache=>cache.addAll(PRECACHE)).then(()=>self.skipWaiting()))});
self.addEventListener('activate',event=>{event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(key=>key.startsWith('nu-nintendo-v1-')&&key!==VERSION).map(key=>caches.delete(key)))).then(()=>self.clients.claim()))});
self.addEventListener('fetch',event=>{const req=event.request;const url=new URL(req.url);if(req.method!=='GET'||url.origin!==self.location.origin||!url.pathname.startsWith('/nintendo/'))return;
 if(req.mode==='navigate'){event.respondWith((async()=>{const cache=await caches.open(VERSION);try{const response=await fetch(req);if(response.ok&&response.headers.get('content-type')?.includes('text/html'))await cache.put(url.pathname,response.clone());return response}catch{return await cache.match(url.pathname)||await cache.match('/nintendo/offline.html')||Response.error()}})());return}
 if(url.pathname.startsWith('/nintendo/assets/')||url.pathname.startsWith('/nintendo/media/')||url.pathname.startsWith('/nintendo/icons/')||PRECACHE.includes(url.pathname)){event.respondWith((async()=>{const cache=await caches.open(VERSION);const saved=await cache.match(req);if(saved)return saved;const response=await fetch(req);if(response.ok)await cache.put(req,response.clone());return response})())}
});`;
await fs.writeFile('../nintendo/sw.js',worker);
await fs.writeFile('../nintendo/_headers','/sw.js\n  Cache-Control: no-cache\n/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n');
console.log(JSON.stringify({pages:routes.length,assets:assets.length,serviceWorker:`nu-nintendo-v1-${version}`,output:'../nintendo'}));
