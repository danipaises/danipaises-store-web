/** Endereço público da enciclopédia, isolado do restante do domínio. */
export const BASE_PATH='/nintendo';
export function publicUrl(value:string|undefined):string|undefined{
 if(!value?.startsWith('/')||value.startsWith('//'))return value;
 if(value===BASE_PATH||value.startsWith(BASE_PATH+'/'))return value;
 return BASE_PATH+value;
}
export function appPath(value:string):string{
 if(value===BASE_PATH)return '/';
 return value.startsWith(BASE_PATH+'/')?value.slice(BASE_PATH.length):value;
}
