import rawGames from '../data/games.json';
import rawConsoles from '../data/consoles.json';
import rawFranchises from '../data/franchises.json';
import rawHistory from '../data/history.json';
import rawCharacters from '../data/characters.json';
import rawQuiz from '../data/quiz.json';
import rawMedia from '../data/media.json';
import gameSources from '../data/game-sources.json';
import historySources from '../data/history-sources.json';
import type {Game,Console,Franchise,HistoryEvent,Character,Question,Media,Source} from '../types';
export const games=rawGames as unknown as Game[];
export const consoles=rawConsoles as unknown as Console[];
export const franchises=rawFranchises as Franchise[];
export const events=rawHistory as HistoryEvent[];
export const characters=rawCharacters as Character[];
export const questions=rawQuiz as Question[];
export const media=rawMedia as Media[];
export const sources=[...gameSources,...historySources] as Source[];
export const sourceById=new Map(sources.map(s=>[s.id,s]));
export const franchiseById=new Map(franchises.map(f=>[f.id,f]));
export const normalize=(text:string)=>text.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().trim();
export const findMedia=(id:string)=>media.find(m=>m.entityId===id);
export const matches=(query:string,...values:(string|undefined)[])=>normalize(query).split(/\s+/).every(q=>normalize(values.filter(Boolean).join(' ')).includes(q));
export const gameMatches=(game:Game,query:string)=>matches(query,game.title,game.originalTitle,franchiseById.get(game.franchise)?.name,game.developer,game.publisher,game.year.toString(),...game.genres,...game.platforms);
export const getConsoleGames=(item:Console)=>games.filter(g=>g.platforms.some(p=>normalize(p)===normalize(item.name)||normalize(p)===normalize(item.id)||platformAliases[item.id]?.some(a=>normalize(a)===normalize(p))));
const platformAliases:Record<string,string[]>={nes:['NES','Famicom','Nintendo Entertainment System'],snes:['SNES','Super Famicom','Super Nintendo'],gamecube:['GameCube','Nintendo GameCube'],'nintendo-gamecube':['GameCube','Nintendo GameCube'],'nintendo-64':['Nintendo 64','N64'],switch:['Nintendo Switch','Switch'],'nintendo-switch':['Nintendo Switch','Switch'],'switch-2':['Nintendo Switch 2','Switch 2'],'game-boy-advance':['Game Boy Advance','GBA'],'nintendo-ds':['Nintendo DS','DS'],'nintendo-3ds':['Nintendo 3DS','3DS']};
export function getRoutes(){return ['/', '/historia','/linha-do-tempo','/consoles','/franquias','/jogos','/personagens','/busca','/colecao','/quiz','/museu','/pokedex','/evolucoes','/comparar','/sobre','/fontes',...games.map(x=>'/jogos/'+x.id),...consoles.map(x=>'/consoles/'+x.id),...franchises.map(x=>'/franquias/'+x.id),...characters.map(x=>'/personagens/'+x.id)];}
export function pageMeta(path:string){
 const [,section,id]=path.split('/');
 const name=section==='jogos'?games.find(g=>g.id===id)?.title:section==='consoles'?consoles.find(c=>c.id===id)?.name:section==='franquias'?franchiseById.get(id)?.name:section==='personagens'?characters.find(c=>c.id===id)?.name:undefined;
 const labels:Record<string,string>={historia:'A história da Nintendo','linha-do-tempo':'Linha do tempo',consoles:'Explorador de consoles',franquias:'Universos para descobrir',jogos:'Biblioteca de jogos',personagens:'Personagens',busca:'Busca no acervo',colecao:'Minha coleção',quiz:'Quiz Nintendo',museu:'Museu e curiosidades',pokedex:'Pokédex',evolucoes:'Evoluções',comparar:'Comparar consoles',sobre:'Sobre o projeto',fontes:'Fontes e créditos'};
 return {title:path==='/'?'Nintendo Universe — Cada jogo, uma história':`${name||labels[section]||'Página não encontrada'} | Nintendo Universe`,description:name?`Explore ${name}: dados, contexto histórico e fontes no Nintendo Universe, uma enciclopédia independente de fãs.`:'Um museu digital independente para explorar a história, os consoles, os jogos e os personagens da Nintendo, em português brasileiro.'};
}
