import type {Collection,CollectionStatus} from '../types';
export const STORAGE_KEY='nintendo-universe:collection:v1';
export const statusLabels:Record<CollectionStatus,string>={favorite:'Favorito',played:'Já joguei',completed:'Zerei',wishlist:'Quero jogar',playing:'Estou jogando'};
export function parseCollection(text:string,validIds:Set<string>):Collection {
 if(text.length>2_000_000) throw new Error('Arquivo maior que o limite de 2 MB.');
 let data:unknown;try{data=JSON.parse(text)}catch{throw new Error('O arquivo não contém JSON válido.');}
 if(!data||typeof data!=='object'||Array.isArray(data))throw new Error('Formato de coleção inválido.');
 const root=data as Record<string,unknown>;
 if(root.version!==1||!root.games||typeof root.games!=='object'||Array.isArray(root.games))throw new Error('Versão ou estrutura incompatível. Use uma exportação do Nintendo Universe.');
 const result:Collection={};
 for(const [id,status] of Object.entries(root.games)){
  if(!validIds.has(id))throw new Error(`O jogo “${id}” não existe nesta versão do catálogo.`);
  if(!Array.isArray(status)||status.length>5||!status.every(s=>typeof s==='string'&&Object.hasOwn(statusLabels,s)))throw new Error(`Marcações inválidas no jogo “${id}”.`);
  if(status.length) result[id]=[...new Set(status)] as CollectionStatus[];
 }
 return result;
}
export function toggleStatus(current:Collection,id:string,status:CollectionStatus):Collection {
 const values=current[id]||[]; const next=values.includes(status)?values.filter(s=>s!==status):[...values,status];
 const copy={...current}; if(next.length)copy[id]=next;else delete copy[id];return copy;
}
export function exportCollection(games:Collection){return JSON.stringify({app:'Nintendo Universe',version:1,exportedAt:new Date().toISOString(),games},null,2)}
