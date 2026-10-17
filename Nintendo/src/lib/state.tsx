import {createContext,useContext,useState,useEffect,useCallback,type ReactNode} from 'react';
import {games} from './catalog';
import {STORAGE_KEY,parseCollection,toggleStatus,exportCollection} from './collection';
import type {Collection,CollectionStatus} from '../types';
const ids=new Set(games.map(g=>g.id));
const Context=createContext<{collection:Collection;toggle:(id:string,status:CollectionStatus)=>void;importData:(text:string)=>void;message:string;setMessage:(s:string)=>void}>({collection:{},toggle:()=>{},importData:()=>{},message:'',setMessage:()=>{}});
export function CollectionProvider({children}:{children:ReactNode}){
 const [collection,setCollection]=useState<Collection>({});const [message,setMessage]=useState('');
 useEffect(()=>{try{const s=localStorage.getItem(STORAGE_KEY);if(s)setCollection(parseCollection(s,ids))}catch{setMessage('Não foi possível ler a coleção salva. Exporte seus dados antes de limpar o navegador.')}},[]);
 useEffect(()=>{const sync=(event:StorageEvent)=>{if(event.key===STORAGE_KEY){try{setCollection(event.newValue?parseCollection(event.newValue,ids):{})}catch{setMessage('A coleção de outra aba não pôde ser lida.')}}};window.addEventListener('storage',sync);return()=>window.removeEventListener('storage',sync)},[]);
 const save=useCallback((next:Collection)=>{try{localStorage.setItem(STORAGE_KEY,exportCollection(next));setCollection(next);return true}catch{setMessage('O navegador não permitiu salvar. Sua alteração não foi persistida.');return false}},[]);
 const toggle=(id:string,status:CollectionStatus)=>{const next=toggleStatus(collection,id,status);if(save(next))setMessage(next[id]?.includes(status)?'Jogo adicionado à sua coleção.':'Marcação removida.')};
 const importData=(text:string)=>{const incoming=parseCollection(text,ids);const next={...collection};for(const [id,status] of Object.entries(incoming))next[id]=[...new Set([...(next[id]||[]),...status])];if(save(next))setMessage(`${Object.keys(incoming).length} jogos importados. As marcações foram combinadas com sua coleção.`)};
 return <Context.Provider value={{collection,toggle,importData,message,setMessage}}>{children}</Context.Provider>;
}
export const useCollection=()=>useContext(Context);
