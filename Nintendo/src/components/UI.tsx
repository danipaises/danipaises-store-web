import {publicUrl} from '../lib/paths';
import { ArrowUpRight, ArrowRight, Gamepad2, Plus, Heart, Check, BookOpen, ExternalLink, Sparkles, Layers, Zap, Leaf, Star, Orbit, Flame, Shield, Compass, Disc3 } from 'lucide-react';
import { useState, type ReactNode, type CSSProperties } from 'react';
import type { Game, Console, Franchise } from '../types';
import { findMedia, franchiseById, sourceById, games } from '../lib/catalog';
import { useCollection } from '../lib/state';
export function Eyebrow({ children }: {
    children: ReactNode;
}) { return <p className="eyebrow"><span className="pixel-cross" aria-hidden="true"/>{children}</p>; }
export function Heading({ eyebrow, title, description, children }: {
    eyebrow: string;
    title: string;
    description?: string;
    children?: ReactNode;
}) { return <div className="page-heading"><div><Eyebrow>{eyebrow}</Eyebrow><h1>{title}</h1>{description && <p className="lede">{description}</p>}</div>{children}</div>; }
export function SectionTitle({ eyebrow, title, href, link = 'Explorar tudo' }: {
    eyebrow: string;
    title: string;
    href?: string;
    link?: string;
}) { return <div className="section-title"><div><Eyebrow>{eyebrow}</Eyebrow><h2>{title}</h2></div>{href && <a className="text-link" href={publicUrl(href)}>{link}<ArrowUpRight size={17}/></a>}</div>; }
export function Empty({ title = 'Nenhum resultado encontrado.', description = 'Tente mudar os filtros ou usar uma busca mais curta.', children }: {
    title?: string;
    description?: string;
    children?: ReactNode;
}) { return <div className="empty"><Compass size={38}/><h3>{title}</h3><p>{description}</p>{children}</div>; }
export function Pill({ children }: {
    children: ReactNode;
}) { return <span className="pill">{children}</span>; }
export function Sources({ ids }: {
    ids: string[];
}) { const list = [...new Set(ids)].map(id => sourceById.get(id)).filter(Boolean); return <details className="source-box"><summary>Fontes e referências <span>{list.length}</span></summary><ul>{list.map(s => <li key={s!.id}><a href={publicUrl(s!.url)} target="_blank" rel="noopener noreferrer">{s!.title}<ExternalLink size={13}/></a><small>{s!.publisher} · Consultado em 17/10/2026{s!.note ? ` · ${s!.note}` : ''}</small></li>)}</ul></details>; }
export function Photo({ id, className = '', priority = false }: {
    id: string;
    className?: string;
    priority?: boolean;
}) { const [failed, setFailed] = useState(false); const m = findMedia(id); return m && !failed ? <img className={className} src={publicUrl(m.src)} alt={m.alt} loading={priority ? 'eager' : 'lazy'} fetchPriority={priority ? 'high' : 'auto'} width="800" height="700" onError={() => setFailed(true)}/> : <div className={`photo-fallback ${className}`}><Gamepad2 size={64}/><span>Fotografia em pesquisa</span></div>; }
export function MediaCredit({ id }: {
    id: string;
}) { const m = findMedia(id); return m ? <small className="media-credit">Foto: {m.author} · <a href={publicUrl(m.sourceUrl)} target="_blank" rel="noopener noreferrer">{m.license}</a></small> : null; }
export function FranchiseSymbol({ id, size = 60 }: {
    id: string;
    size?: number;
}) { const Icon = ({ mario: Star, zelda: Shield, pokemon: Zap, kirby: Sparkles, 'donkey-kong': Leaf, metroid: Orbit, 'animal-crossing': Leaf, pikmin: Flame, splatoon: Layers, 'star-fox': Compass, 'f-zero': Zap, 'fire-emblem': Shield, earthbound: Orbit, yoshi: Star, wario: Gamepad2, 'smash-bros': Plus, 'kid-icarus': Flame, 'advance-wars': Shield, 'golden-sun': Star, xenoblade: Compass, 'rhythm-heaven': Disc3, 'punch-out': Zap, 'luigis-mansion': Orbit } as Record<string, typeof Star>)[id] || Gamepad2; return <Icon size={size} strokeWidth={1.3} aria-hidden="true"/>; }
export function FranchiseCard({ item, index = 0 }: {
    item: Franchise;
    index?: number;
}) { const count = games.filter(g => g.franchise === item.id).length; return <a href={publicUrl('/franquias/' + item.id)} className="franchise-card" style={{ '--franchise-color': item.color } as CSSProperties}><div className="franchise-art"><span className="card-number">0{index + 1}</span><span className="orbit-ring"/><FranchiseSymbol id={item.id} size={76}/><span className="pixel-small p1"/><span className="pixel-small p2"/></div><div className="franchise-info"><div><h3>{item.name}</h3><p>{count} jogos no acervo</p></div><ArrowUpRight size={21}/></div></a>; }
export function GameCard({ game, compact = false }: {
    game: Game;
    compact?: boolean;
}) { const franchise = franchiseById.get(game.franchise); const { collection, toggle } = useCollection(); const favorite = collection[game.id]?.includes('favorite'); return <article className={`game-card ${compact ? 'compact' : ''}`}><a className="game-cover" href={publicUrl('/jogos/' + game.id)} style={{ '--franchise-color': franchise?.color || '#e60012' } as CSSProperties}><div className="cover-top"><span>NINTENDO UNIVERSE</span><span>{game.year}</span></div><FranchiseSymbol id={game.franchise} size={48}/><strong>{game.title}</strong><small>FICHA DO ACERVO</small></a><div className="game-info"><div><p>{game.platforms.slice(0, 2).join(' · ')}</p><a href={publicUrl('/jogos/' + game.id)}><h3>{game.title}</h3></a><small>{game.year} <span>·</span> {game.genres[0] || 'Jogo eletrônico'}</small></div><button className={`icon-button favorite ${favorite ? 'is-saved' : ''}`} onClick={() => toggle(game.id, 'favorite')} aria-pressed={!!favorite} aria-label={`${favorite ? 'Remover dos' : 'Adicionar aos'} favoritos: ${game.title}`}><Heart size={17} fill={favorite ? 'currentColor' : 'none'}/></button></div></article>; }
export function ConsoleCard({ item }: {
    item: Console;
}) { return <a className="console-card" href={publicUrl('/consoles/' + item.id)}><div className="console-photo"><span className="console-year">{item.year}</span><Photo id={item.id}/><span className="console-arrow"><ArrowUpRight size={20}/></span></div><div className="console-info"><h3>{item.name}</h3><p>{item.type}</p></div></a>; }
export function ReadMore({ href, children }: {
    href: string;
    children: ReactNode;
}) { return <a className="button primary" href={publicUrl(href)}>{children}<ArrowRight size={17}/></a>; }
export function Pagination({ page, total, onChange, size = 24 }: {
    page: number;
    total: number;
    onChange: (p: number) => void;
    size?: number;
}) { const count = Math.ceil(total / size); return count > 1 ? <nav className="pagination" aria-label="Paginação"><button className="button secondary" disabled={page <= 1} onClick={() => onChange(page - 1)}>Anterior</button><span>Página {page} de {count}</span><button className="button secondary" disabled={page >= count} onClick={() => onChange(page + 1)}>Próxima<ArrowRight size={15}/></button></nav> : null; }
