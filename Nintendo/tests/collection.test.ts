import {test} from 'node:test';
import assert from 'node:assert/strict';
import {parseCollection,toggleStatus,exportCollection} from '../src/lib/collection';
const ids=new Set(['mario','zelda']);
test('exportação/importação preservam marcações válidas e removem duplicatas',()=>{const data={mario:['favorite','played'] as const};assert.deepEqual(parseCollection(exportCollection({mario:[...data.mario]}),ids),data);assert.deepEqual(parseCollection('{"version":1,"games":{"mario":["favorite","favorite"]}}',ids),{mario:['favorite']})});
test('marcação é reversível e não altera o objeto original',()=>{const original={mario:['favorite'] as ('favorite')[]};const next=toggleStatus(original,'mario','played');assert.deepEqual(original,{mario:['favorite']});assert.deepEqual(next,{mario:['favorite','played']});assert.deepEqual(toggleStatus(original,'mario','favorite'),{})});
test('importação rejeita JSON inválido e arquivos muito grandes',()=>{assert.throws(()=>parseCollection('{bad',ids),/JSON válido/);assert.throws(()=>parseCollection(' '.repeat(2_000_001),ids),/2 MB/)});
test('importação rejeita versões, estrutura, status e jogos desconhecidos',()=>{for(const invalid of [null,[],{version:2,games:{}},{version:1,games:[]},{version:1,games:{fake:['favorite']}},{version:1,games:{mario:['admin']}},{version:1,games:{mario:'favorite'}}])assert.throws(()=>parseCollection(JSON.stringify(invalid),ids))});
test('importação rejeita chaves que podem tentar poluir objetos',()=>{assert.throws(()=>parseCollection('{"version":1,"games":{"__proto__":["favorite"]}}',ids));assert.throws(()=>parseCollection('{"version":1,"games":{"constructor":["favorite"]}}',ids))});
