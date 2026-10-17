export interface Source {id:string;title:string;url:string;publisher:string;accessed:string;type:string;note?:string}
export interface Game {id:string;title:string;originalTitle?:string;franchise:string;year:number;platforms:string[];developer?:string;publisher?:string;genres:string[];description:string;depth:'basic'|'deep';sourceIds:string[];details?:Record<string,string>;relatedIds?:string[]}
export interface Console {id:string;name:string;year:number;type:string;description:string;history:string[];specs:Record<string,string>;releases:Record<string,string>;models:string[];accessories:string[];legacy:string;sourceIds:string[];parentId?:string}
export interface Franchise {id:string;name:string;year:number;color:string;description:string;history:string[];ownership:string;sourceIds:string[];topics?:{title:string;body:string}[]}
export interface HistoryEvent {id:string;year:number;title:string;category:string;description:string;content?:string[];sourceIds:string[];consoleId?:string;franchise?:string}
export interface Character {id:string;name:string;franchise:string;debut:number;description:string;sourceIds:string[];evolution?:{year:number;title:string;description:string}[]}
export interface Question {id:string;category:string;difficulty:string;question:string;options:string[];answer:number;explanation:string;sourceIds:string[]}
export interface Media {id:string;entityId:string;entityType:string;src:string;alt:string;author:string;license:string;licenseUrl:string;sourceUrl:string;note?:string}
export interface Pokemon {id:number;name:string;generation:number;types:string[];height:number;weight:number;legendary:boolean;mythical:boolean;prevo:number|null;chain:number}
export type CollectionStatus='favorite'|'played'|'completed'|'wishlist'|'playing';
export type Collection=Record<string,CollectionStatus[]>;
