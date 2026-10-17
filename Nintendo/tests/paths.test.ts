import {test} from 'node:test';
import assert from 'node:assert/strict';
import {publicUrl,appPath} from '../src/lib/paths';
test('links e mídia ficam dentro de /nintendo sem duplicar o prefixo',()=>{assert.equal(publicUrl('/jogos/mario'),'/nintendo/jogos/mario');assert.equal(publicUrl('/media/game-boy.webp'),'/nintendo/media/game-boy.webp');assert.equal(publicUrl('/nintendo/quiz'),'/nintendo/quiz');assert.equal(publicUrl('/'),'/nintendo/')});
test('links externos e âncoras são preservados',()=>{assert.equal(publicUrl('https://nintendo.com/'),'https://nintendo.com/');assert.equal(publicUrl('#historia'),'#historia');assert.equal(publicUrl('//example.test/x'),'//example.test/x')});
test('roteador reconhece /nintendo, suas páginas e barras finais',()=>{assert.equal(appPath('/nintendo'),'/');assert.equal(appPath('/nintendo/'),'/');assert.equal(appPath('/nintendo/jogos/mario/'),'/jogos/mario/');assert.equal(appPath('/nintendoland'),'/nintendoland')});
