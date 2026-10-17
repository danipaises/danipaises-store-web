# Imagens e atribuições

Pesquisa e verificação: **17 de outubro de 2026**.

As fotografias utilizadas foram localizadas no Wikimedia Commons. Os metadados de cada arquivo foram conferidos na API oficial do Commons para identificar autor, origem e licença; páginas de descrição e históricos de arquivos também foram consultados, especialmente nos materiais com atribuição ou compartilhamento pela mesma licença. Uma fotografia publicada em um site oficial não foi considerada livre apenas por sua origem.

Os arquivos estão armazenados em `public/media/` e são servidos pelo próprio site. Não há hotlink de imagens nem necessidade de conta, token ou chamada à API em tempo de execução. O manifesto `src/data/media.json` informa o caminho local, o texto alternativo, a autoria, a licença, os links de origem e a alteração técnica realizada. Os links de fonte apontam para a página do arquivo, onde também é possível consultar seu histórico e recuperar o original.

## Transformações

As fotografias foram reduzidas proporcionalmente para, no máximo, 1.200 pixels no maior lado e convertidas para WebP com qualidade 86. A foto de Game & Watch Ball conserva sua resolução original de 640 × 480 pixels. As transparências dos originais PNG foram preservadas. Não foram inventadas imagens históricas, acrescentados elementos às fotografias, removidas marcas ou alteradas telas para representar jogos.

As versões de SNES, Wii U e Game Boy Advance SP conservam a licença **CC BY-SA 3.0**, incluindo a exigência de compartilhar adaptações sob a mesma licença. As demais seguem a licença individual declarada no manifesto. A escolha de uma fotografia em domínio público não elimina direitos de marca sobre o produto retratado. O projeto é independente, sem afiliação à Nintendo ou aos fotógrafos.

Para exibir uma imagem, mantenha uma atribuição legível na página individual ou no painel de créditos acessível junto à imagem: autor, nome e link da licença, link da fonte e informação de redimensionamento/conversão. Um modelo adequado é: “Foto: Evan-Amos · CC BY-SA 3.0 · Wikimedia Commons. Redimensionada e convertida para WebP.”

## Recuperar os arquivos

A distribuição já contém as imagens otimizadas. O script opcional de recuperação exige Node.js, `curl`, Python 3 e Pillow:

```sh
python3 -m pip install Pillow
node scripts/download-media.mjs
```

O script preserva arquivos já existentes. Para recuperar todos novamente, use `node scripts/download-media.mjs --force`. No Windows, pode ser necessário definir a variável `PYTHON` para o caminho do interpretador instalado. Os originais são baixados para uma pasta temporária e removidos depois da conversão. O script aceita somente as URLs HTTPS de `upload.wikimedia.org` aprovadas no manifesto; falhas de rede interrompem a execução com erro em vez de produzir imagens quebradas. Respeite respostas 429 e aguarde antes de repetir uma operação.

## Adicionar material

1. Localize o arquivo original e leia as condições de uso daquela imagem específica.
2. Registre autor, licença, link da licença e página de origem. Para materiais oficiais sem autorização clara de reutilização, use um substituto visual original até obter permissão.
3. Salve uma versão otimizada em `public/media/` e acrescente o registro a `src/data/media.json` com `entityId` correspondente ao catálogo.
4. Verifique imagem, texto alternativo, dimensão e atribuição na interface, em modo claro e escuro.
5. Não remova avisos de atribuição ou de compartilhamento pela mesma licença quando criar derivados.

## Limites editoriais

As fotografias mostram exemplares físicos e modelos específicos, não necessariamente a unidade de lançamento de cada mercado. A foto de Hanafuda é uma fotografia de exposição de 2006, não uma fotografia de 1889. A imagem da sede é de 2015 e não deve ilustrar a fundação sem uma legenda contextual. Os cards sem mídia aprovada devem usar ilustrações originais identificadas como substitutas; capas e artes protegidas não foram copiados indiscriminadamente.

O catálogo não dispõe ainda de fotografia individual para todas as revisões de hardware nem de capas, screenshots e artes licenciadas para cada jogo e personagem. Essa ausência deve permanecer explícita no relatório de cobertura.

## Catálogo de créditos

Esta edição contém **20 fotografias locais**: 18 de consoles/sistemas e 2 históricas.

| Arquivo local | Autor | Licença | Fonte |
| --- | --- | --- | --- |
| `/media/game-boy.webp` | Evan-Amos (fotografia original); versão PNG descrita na fonte | [Domínio público](https://commons.wikimedia.org/wiki/File:Game-Boy-FL.png#Licensing) | [Commons](https://commons.wikimedia.org/wiki/File:Game-Boy-FL.png) |
| `/media/nes.webp` | Evan-Amos | [Domínio público](https://commons.wikimedia.org/wiki/File:NES-Console-Set.png#Licensing) | [Commons](https://commons.wikimedia.org/wiki/File:NES-Console-Set.png) |
| `/media/snes.webp` | Evan-Amos | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0) | [Commons](https://commons.wikimedia.org/wiki/File:SNES-Mod1-Console-Set.png) |
| `/media/nintendo-64.webp` | Evan-Amos | [Domínio público](https://commons.wikimedia.org/wiki/File:N64-Console-Set.png#Licensing) | [Commons](https://commons.wikimedia.org/wiki/File:N64-Console-Set.png) |
| `/media/gamecube.webp` | Evan-Amos | [Domínio público](https://commons.wikimedia.org/wiki/File:GameCube-Console-Set.png#Licensing) | [Commons](https://commons.wikimedia.org/wiki/File:GameCube-Console-Set.png) |
| `/media/wii.webp` | Evan-Amos | [Domínio público](https://commons.wikimedia.org/wiki/File:Wii-Console.png#Licensing) | [Commons](https://commons.wikimedia.org/wiki/File:Wii-Console.png) |
| `/media/wii-u.webp` | Takimata; edição: Tokyoship | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0) | [Commons](https://commons.wikimedia.org/wiki/File:Wii_U_Console_and_Gamepad.png) |
| `/media/nintendo-ds.webp` | Evan-Amos | [Domínio público](https://commons.wikimedia.org/wiki/File:Nintendo-DS-Fat-Blue.png#Licensing) | [Commons](https://commons.wikimedia.org/wiki/File:Nintendo-DS-Fat-Blue.png) |
| `/media/nintendo-ds-lite.webp` | Evan-Amos | [Domínio público](https://commons.wikimedia.org/wiki/File:Nintendo-DS-Lite-Black-Open.png#Licensing) | [Commons](https://commons.wikimedia.org/wiki/File:Nintendo-DS-Lite-Black-Open.png) |
| `/media/nintendo-3ds.webp` | Evan-Amos | [Domínio público](https://commons.wikimedia.org/wiki/File:Nintendo-3DS-AquaOpen.png#Licensing) | [Commons](https://commons.wikimedia.org/wiki/File:Nintendo-3DS-AquaOpen.png) |
| `/media/nintendo-switch.webp` | Evan-Amos; edição: Gunnar.offel | [Domínio público](https://commons.wikimedia.org/wiki/File:Nintendo-Switch-wJoyCons-BlRd-Standing-FL.png#Licensing) | [Commons](https://commons.wikimedia.org/wiki/File:Nintendo-Switch-wJoyCons-BlRd-Standing-FL.png) |
| `/media/nintendo-switch-2.webp` | AOMAF2024 | [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.en) | [Commons](https://commons.wikimedia.org/wiki/File:Nintendo_Switch_2_console_in_handheld_mode.png) |
| `/media/game-and-watch.webp` | Joshua Murphy (Jawesome98) | [Domínio público](https://commons.wikimedia.org/wiki/File:Game_%26_Watch_Ball.jpg#Licensing) | [Commons](https://commons.wikimedia.org/wiki/File:Game_%26_Watch_Ball.jpg) |
| `/media/game-boy-advance.webp` | Evan-Amos | [Domínio público](https://commons.wikimedia.org/wiki/File:Nintendo-Game-Boy-Advance-Purple-FL.png#Licensing) | [Commons](https://commons.wikimedia.org/wiki/File:Nintendo-Game-Boy-Advance-Purple-FL.png) |
| `/media/game-boy-advance-sp.webp` | Evan-Amos | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0) | [Commons](https://commons.wikimedia.org/wiki/File:Game-Boy-Advance-SP-Mk1-Blue.png) |
| `/media/virtual-boy.webp` | Evan-Amos | [Domínio público](https://commons.wikimedia.org/wiki/File:Virtual-Boy-Set.png#Licensing) | [Commons](https://commons.wikimedia.org/wiki/File:Virtual-Boy-Set.png) |
| `/media/color-tv-game.webp` | Chapuisat (Flickr) | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0) | [Commons](https://commons.wikimedia.org/wiki/File:Nintendo_Color_TV_game_6.jpg) |
| `/media/hanafuda.webp` | fuzzcat | [CC BY 2.0](https://creativecommons.org/licenses/by/2.0) | [Commons](https://commons.wikimedia.org/wiki/File:Nintendo_Hanafuda.jpg) |
| `/media/sede-nintendo.webp` | Tokumeigakarinoaoshima | [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.en) | [Commons](https://commons.wikimedia.org/wiki/File:Nintendo_Co.,_Ltd._headquarters_taken_from_the_Kintetsu_train.JPG) |
| `/media/game-boy-color.webp` | Evan-Amos; edição: Gunnar.offel | [Domínio público](https://commons.wikimedia.org/wiki/File:Nintendo-Game-Boy-Color-FL.png#Licensing) | [Commons](https://commons.wikimedia.org/wiki/File:Nintendo-Game-Boy-Color-FL.png) |

## Verificação dos arquivos

Em 17/10/2026, todos os 20 caminhos do manifesto foram conferidos e as 20 imagens abriram e passaram pela verificação de decodificação do Pillow. Nenhum arquivo ultrapassa 1.200 pixels no maior lado. Os IDs e caminhos são únicos. O conjunto ocupa 1.383.504 bytes (aproximadamente 1,32 MiB). A folha de contato foi inspecionada visualmente para confirmar a correspondência entre objetos e legendas. A integração de créditos, carregamento no navegador e cache offline deve ser coberta pelos testes do site.
