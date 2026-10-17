import {appPath,publicUrl} from './lib/paths';
import {hydrateRoot,createRoot} from 'react-dom/client';
import App from './App';
import {pageMeta} from './lib/catalog';
import './styles.css';
const root=document.getElementById('root')!;
const path=appPath(window.location.pathname).replace(/\/$/,'')||'/';
const app=<App url={path}/>;
// O fallback offline pode entregar a home para uma URL ainda não visitada.
if(root.dataset.path===path&&root.childElementCount>0)hydrateRoot(root,app);else createRoot(root).render(app);
document.title=pageMeta(path).title;
if('serviceWorker' in navigator&&import.meta.env.PROD){window.addEventListener('load',()=>{navigator.serviceWorker.register(publicUrl('/sw.js')!,{scope:publicUrl('/')}).catch(()=>{/* O site continua funcional quando o navegador bloqueia a PWA. */})})}
