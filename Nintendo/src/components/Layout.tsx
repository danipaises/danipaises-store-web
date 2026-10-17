import {publicUrl} from '../lib/paths';
import { useState, useEffect, useRef, type ReactNode } from 'react';
import { Home, BookOpen, Clock3, Gamepad2, Layers, LibraryBig, Users, Heart, Search, Sun, Moon, Menu, X, ArrowUpRight, Landmark, GitBranch, HelpCircle, ScanLine, WifiOff, Check, Command, ChevronRight } from 'lucide-react';
import { useCollection } from '../lib/state';
const nav = [{ label: 'Explorar', items: [['/', 'Visão geral', Home], ['/historia', 'A história da Nintendo', BookOpen], ['/linha-do-tempo', 'Linha do tempo', Clock3], ['/consoles', 'Consoles', Gamepad2], ['/franquias', 'Franquias', Layers], ['/jogos', 'Biblioteca de jogos', LibraryBig], ['/personagens', 'Personagens', Users]] }, { label: 'Descobrir & jogar', items: [['/museu', 'Museu & curiosidades', Landmark], ['/pokedex', 'Pokédex', ScanLine], ['/evolucoes', 'Evoluções', GitBranch], ['/quiz', 'Quiz Nintendo', HelpCircle], ['/colecao', 'Minha coleção', Heart]] }];
export function Layout({ path, children }: {
    path: string;
    children: ReactNode;
}) {
    const [menu, setMenu] = useState(false), [dark, setDark] = useState(false), [offline, setOffline] = useState(false);
    const { collection, message, setMessage } = useCollection();
    const wasOpen = useRef(false);
    const search = useRef<HTMLInputElement>(null);
    const menuButton = useRef<HTMLButtonElement>(null);
    const aside = useRef<HTMLElement>(null);
    useEffect(() => { try {
        const t = localStorage.getItem('nu-theme');
        const d = t ? t === 'dark' : matchMedia('(prefers-color-scheme:dark)').matches;
        setDark(d);
        document.documentElement.dataset.theme = d ? 'dark' : 'light';
    }
    catch { } const online = () => setOffline(!navigator.onLine); online(); window.addEventListener('online', online); window.addEventListener('offline', online); const keyboard = (e: KeyboardEvent) => { if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        search.current?.focus();
    } if (e.key === 'Escape') {
        setMenu(false);
        menuButton.current?.focus();
    } }; window.addEventListener('keydown', keyboard); return () => { window.removeEventListener('online', online); window.removeEventListener('offline', online); window.removeEventListener('keydown', keyboard); }; }, []);
    useEffect(() => { if (!message)
        return; const t = setTimeout(() => setMessage(''), 5500); return () => clearTimeout(t); }, [message, setMessage]);
    useEffect(() => { if (menu) {
        aside.current?.querySelector<HTMLAnchorElement>('a')?.focus();
        wasOpen.current = true;
    }
    else if (wasOpen.current) {
        menuButton.current?.focus();
        wasOpen.current = false;
    } }, [menu]);
    const toggleTheme = () => { const d = !dark; setDark(d); document.documentElement.dataset.theme = d ? 'dark' : 'light'; try {
        localStorage.setItem('nu-theme', d ? 'dark' : 'light');
    }
    catch { } };
    const current = nav.flatMap(s => s.items).find(i => i[0] === path)?.[1] || 'Acervo';
    return <><a className="skip-link" href={publicUrl("#conteudo")}>Pular para o conteúdo</a>{menu && <button className="menu-overlay" aria-label="Fechar navegação" onClick={() => setMenu(false)}/>}
 <aside ref={aside} className={`sidebar ${menu ? 'open' : ''}`} id="navegacao" role={menu ? 'dialog' : undefined} aria-modal={menu ? true : undefined} aria-label={menu ? 'Navegação principal' : undefined} onKeyDown={e => { if (!menu || e.key !== 'Tab')
        return; const items = aside.current?.querySelectorAll<HTMLElement>('a,button'); if (!items?.length)
        return; const first = items[0], last = items[items.length - 1]; if (e.shiftKey && document.activeElement === first) {
        e.preventDefault();
        last.focus();
    }
    else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault();
        first.focus();
    } }}><button className="drawer-close icon-button" aria-label="Fechar navegação" onClick={() => { setMenu(false); menuButton.current?.focus(); }}><X size={19}/></button><a href={publicUrl("/")} className="brand" aria-label="Nintendo Universe, início"><span className="brand-mark" aria-hidden="true">n<span>u</span><i /></span><span>NINTENDO<strong>UNIVERSE<span>✦</span></strong></span></a><div className="sidebar-rule"/>
 {nav.map(section => <nav aria-label={section.label} key={section.label}><p className="nav-label">{section.label}</p>{section.items.map(([href, label, Icon]) => { const LinkIcon = Icon as typeof Home; return <a key={href as string} href={publicUrl(href as string)} className={path == href || (href !== '/' && path.startsWith(href as string)) ? 'nav-link active' : 'nav-link'} aria-current={path === href ? 'page' : undefined}><LinkIcon size={18}/><span>{label as string}</span>{href === '/colecao' && <small>{Object.keys(collection).length}</small>}</a>; })}</nav>)}
 <a className="sidebar-note" href={publicUrl("/sobre")}><span className="live-dot"/>Um acervo em construção<span>Feito por fãs. Para quem ama jogar.<ArrowUpRight size={13}/></span></a><a href={publicUrl("/fontes")} className="sidebar-bottom">Sobre as fontes & créditos <ArrowUpRight size={13}/></a></aside>
 <div className="app-body" inert={menu || undefined}><header className="topbar"><button ref={menuButton} className="icon-button mobile-menu" aria-label={menu ? 'Fechar menu' : 'Abrir menu'} aria-expanded={menu} aria-controls="navegacao" onClick={() => setMenu(!menu)}>{menu ? <X size={22}/> : <Menu size={22}/>}</button><div className="breadcrumb"><span>O universo Nintendo</span><ChevronRight size={13}/><strong>{current as string}</strong></div><form action={publicUrl("/busca")} className="global-search" role="search"><Search size={17}/><input ref={search} name="q" aria-label="Buscar no universo Nintendo" placeholder="O que você quer descobrir?" autoComplete="off"/><kbd>⌘ K</kbd></form><button className="icon-button theme-button" onClick={toggleTheme} aria-label={dark ? 'Ativar modo claro' : 'Ativar modo escuro'}>{dark ? <Sun size={20}/> : <Moon size={20}/>}</button><a className="top-collection icon-button" href={publicUrl("/colecao")} aria-label="Abrir minha coleção"><Heart size={20}/></a></header>
 {offline && <div className="offline-bar"><WifiOff size={15}/>Você está offline. O acervo salvo e sua coleção continuam disponíveis.</div>}
 <main id="conteudo" tabIndex={-1}>{children}</main><footer className="footer"><div><strong>NINTENDO UNIVERSE</strong><span>Cada jogo, uma história.</span></div><p>Projeto independente de fãs. Sem afiliação, patrocínio ou aprovação da Nintendo.<br />Nintendo e suas marcas pertencem aos respectivos titulares.</p><div><a href={publicUrl("/sobre")}>Sobre o projeto</a><a href={publicUrl("/fontes")}>Fontes & créditos</a></div></footer></div>
 <div className={`toast ${message ? 'visible' : ''}`} role="status" aria-live="polite"><Check size={17}/>{message}</div></>;
}
