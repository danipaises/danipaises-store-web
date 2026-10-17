"""Rebuild researched, editorial historical data. Run from repository root."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'src/data'
def save(name, value):
    (DATA / (name + '.json')).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n')

sources = json.loads((DATA / 'history-sources.json').read_text())
additional = [
 ('h-zelda-history', 'Zelda: histórico oficial dos lançamentos japoneses', 'https://www.nintendo.com/jp/character/zelda/history/index.html'),
 ('h-metroid-archive', 'Metroid Dread Report 4: retrospectiva da saga', 'https://www.nintendo.com/en-gb/News/2021/August/Metroid-Dread-Report-Vol-4-Unravelling-a-saga-35-years-in-the-making-2018281.html'),
 ('h-luigi-debut', 'Iwata Asks: a estreia de Luigi em 1983', 'https://iwataasks.nintendo.com/interviews/wiiu/new-super-luigi-u/0/1/'),
 ('h-waluigi', 'Boas-vindas ao maravilhoso mundo de Waluigi', 'https://www.nintendo.com/pt-br/whatsnew/boas-vindas-ao-maravilhoso-mundo-de-waluigi/'),
 ('h-dkc', 'Donkey Kong Country: arquivo do Super Nintendo', 'https://www.nintendo.com/en-gb/Games/Super-Nintendo/Donkey-Kong-Country-276896.html'),
 ('h-dk-history', 'Conheça o rei das bananas: história de Donkey Kong', 'https://www.nintendo.com/pt-br/whatsnew/conheca-o-rei-das-bananas/'),
 ('h-rosalina', 'Super Mario Galaxy: estreia de Rosalina', 'https://www.nintendo.com/en-gb/Games/Wii/Super-Mario-Galaxy-283322.html'),
 ('h-mario-land', 'Super Mario Land: Sarasaland e Daisy', 'https://www.nintendo.com/en-gb/Games/Game-Boy/Super-Mario-Land-275902.html'),
 ('h-mario-land2', 'Super Mario Land 2: arquivo japonês e Wario', 'https://www.nintendo.com/jp/character/mario/archives/land2/index.html'),
 ('h-kirby-about', 'Kirby: perfil e catálogo histórico oficial', 'https://kirby.nintendo.com/about/'),
 ('h-kirby-copy', 'Iwata Asks: origem das habilidades de cópia', 'https://www.nintendo.com/en-gb/Iwata-Asks/Iwata-Asks-Kirby-s-Adventure-Wii/Iwata-Asks-Kirby-s-Adventure-Wii/2-Programmers-Never-Say-No/2-Programmers-Never-Say-No-230204.html'),
 ('h-kirby-dream-land', 'Kirby’s Dream Land: história e Rei Dedede', 'https://www.nintendo.com/en-gb/Games/Game-Boy/Kirby-s-Dream-Land-275682.html'),
 ('h-wars-official', 'Famicom Wars: arquivo oficial de 1988', 'https://www.nintendo.com/jp/famicom/software/hvc-fw/index.html'),
 ('h-yoshi-eggs', 'Yoshi no Tamago: arquivo oficial de 1991', 'https://www.nintendo.com/jp/famicom/software/fmc-yeg/index.html'),
 ('h-kimishima', 'Mudanças na gestão: nomeação de Tatsumi Kimishima', 'https://www.nintendo.co.jp/ir/pdf/2015/150914e.pdf'),
 ('h-museum-direct', 'Nintendo Museum Direct: abertura em outubro de 2024', 'https://www.nintendo.com/en-gb/News/Nintendo-Direct/2024/Nintendo-Museum-Direct-August-20th-2024-2643142.html'),
]
known = {s['id'] for s in sources}
for sid, title, url in additional:
    if sid not in known:
        sources.append(dict(id=sid,title=title,url=url,publisher='Nintendo',accessed='2026-10-17',type='primary'))
save('history-sources', sources)

history=[]
def event(id,year,title,category,description,sourceIds,content=None,consoleId=None,franchise=None):
    d=dict(id=id,year=year,title=title,category=category,description=description,sourceIds=sourceIds)
    if content: d['content']=content
    if consoleId: d['consoleId']=consoleId
    if franchise: d['franchise']=franchise
    history.append(d)

event('fundacao',1889,'Cartas que iniciaram uma história','Empresa','Fusajiro Yamauchi começa a produzir e vender cartas Hanafuda em Kyoto.',['h-corporate'],[
 'A trajetória da Nintendo começa com um objeto físico de entretenimento: cartas japonesas Hanafuda. O fundador, Fusajiro Yamauchi, trabalhava em Shimogyo-ku, Kyoto. A data se refere ao início dessa atividade; a estrutura societária mudaria ao longo das décadas.',
 'O museu desta enciclopédia parte das cartas porque elas conectam períodos muito diferentes da empresa: impressão, fabricação de brinquedos e, mais tarde, interação eletrônica. Não atribuímos uma tradução definitiva ao nome Nintendo: explicações populares sobre sua etimologia exigem cautela.'
])
event('cartas-ocidentais',1902,'Baralhos ocidentais','Empresa','A produção passa a incluir cartas de estilo ocidental no Japão.',['h-corporate'])
event('marufuku',1947,'Constituição da Marufuku','Empresa','É estabelecida a Marufuku Co., Ltd., antecessora societária da Nintendo atual.',['h-corporate'])
event('hiroshi',1949,'Hiroshi Yamauchi assume a presidência','Empresa','A gestão de Hiroshi Yamauchi atravessaria a transformação das cartas aos videogames.',['h-europe','h-yamauchi'])
event('nome-playing-card',1951,'Nintendo Playing Card','Empresa','A companhia adota o nome Nintendo Playing Card Co., Ltd.',['h-corporate'])
event('plastico',1953,'Cartas de plástico','Inovação','A Nintendo desenvolve a fabricação em massa de cartas plásticas no Japão.',['h-corporate'])
event('disney',1959,'Cartas com personagens Disney','Empresa','A empresa começa a vender baralhos licenciados com personagens Disney.',['h-corporate'])
event('bolsa',1962,'Entrada na bolsa','Empresa','A Nintendo lista ações nas bolsas de Osaka e Kyoto.',['h-corporate'])
event('nome-atual',1963,'Nintendo Co., Ltd.','Empresa','O nome deixa de se restringir às cartas, acompanhando a diversificação.',['h-corporate'])
event('ultra-hand',1966,'Ultra Hand e a era dos brinquedos','Inovação','O braço extensível Ultra Hand representa a inventividade de Gunpei Yokoi.',['h-ultra'],[
 'Muito antes dos consoles, a Nintendo experimentou maneiras de ampliar seu negócio de entretenimento. O Ultra Hand, um braço mecânico extensível, tornou-se um exemplo conhecido desse período e do trabalho de Gunpei Yokoi.',
 'Há numerosas histórias sobre negócios paralelos da empresa. Este acervo evita transformar relatos repetidos, sem documentação suficiente, em uma lista definitiva de empreendimentos. O recorte confirmado enfatiza cartas, brinquedos e produtos eletrônicos.'
])
event('laser-clay',1973,'Laser Clay Shooting System','Inovação','Um sistema de tiro para instalações de lazer amplia a presença da Nintendo no entretenimento eletrônico.',['h-corporate'])
event('color-tv',1977,'Primeiros videogames domésticos','Console','TV Game 6 e TV Game 15 chegam ao Japão como sistemas dedicados.',['h-corporate'],consoleId='color-tv-game')
event('arcades',1978,'Entrada nos arcades de vídeo','Empresa','A Nintendo passa a desenvolver e vender máquinas de videogame para fliperamas.',['h-corporate'])
event('game-watch',1980,'Game & Watch','Console','Jogos portáteis com tela LCD combinam entretenimento e relógio.',['h-europe'],consoleId='game-and-watch')
event('america',1980,'Nintendo of America','Empresa','A subsidiária norte-americana é estabelecida em Nova York.',['h-corporate'])
event('donkey-kong',1981,'Donkey Kong e Jumpman','Jogo','O arcade Donkey Kong apresenta o personagem que passaria a ser conhecido como Mario.',['h-dk-history'],[
 'Donkey Kong liga a história de duas franquias. O gorila protagoniza a máquina de arcade, enquanto o personagem controlado pelo jogador, então chamado Jumpman, é o ponto de partida de Mario.',
 'As aventuras de arcade não têm a mesma estrutura dos futuros Donkey Kong Country. A enciclopédia preserva essa diferença de contexto, em vez de tratar todos os jogos como sequências equivalentes.'
],franchise='donkey-kong')
event('famicom',1983,'Famicom no Japão','Console','O Family Computer inaugura a família que seria conhecida internacionalmente como NES.',['h-nes','h-corporate'],consoleId='nes')
event('luigi',1983,'Mario Bros. apresenta Luigi','Jogo','Mario ganha um irmão e parceiro no arcade Mario Bros.',['h-luigi-debut'],franchise='mario')
event('super-mario',1985,'Super Mario Bros.','Jogo','A aventura de plataforma para Famicom estabelece o Reino Cogumelo como cenário central.',['h-mario40'],franchise='mario')
event('nes-america',1985,'NES chega à América do Norte','Console','A expansão internacional adapta apresentação, marca e distribuição do Famicom.',['h-europe','h-nes'],consoleId='nes')
event('zelda',1986,'A primeira lenda de Hyrule','Jogo','The Legend of Zelda estreia no Famicom Disk System em 21 de fevereiro, no Japão.',['h-zelda-history'],franchise='zelda',consoleId='famicom-disk-system')
event('metroid',1986,'Metroid: exploração interligada','Jogo','Samus Aran inicia sua saga no Famicom Disk System japonês.',['h-metroid-archive'],franchise='metroid')
event('game-boy',1989,'Game Boy','Console','O portátil de cartuchos intercambiáveis leva o catálogo Nintendo a novas situações de uso.',['h-game-boy'],consoleId='game-boy')
event('super-famicom',1990,'Super Famicom','Console','A geração de 16 bits da Nintendo começa no Japão; o Super NES chega depois a outras regiões.',['h-snes'],consoleId='snes')
event('fire-emblem',1990,'Fire Emblem','Jogo','Shadow Dragon & the Blade of Light estreia no Japão com batalhas táticas e personagens persistentes.',['h-fireemblem'],franchise='fire-emblem')
event('kirby',1992,'Kirby’s Dream Land','Jogo','Kirby estreia no Game Boy; a habilidade de copiar poderes seria introduzida no jogo seguinte.',['h-kirby','h-kirby-about'],franchise='kirby')
event('starfox',1993,'Star Fox e os polígonos','Inovação','O chip Super FX ajuda a trazer gráficos poligonais ao Super Nintendo.',['h-starfox'],franchise='star-fox',consoleId='snes')
event('dkc',1994,'Donkey Kong Country','Jogo','A aventura com Donkey Kong e Diddy Kong utiliza gráficos pré-renderizados no Super Nintendo.',['h-dkc'],franchise='donkey-kong')
event('virtual-boy',1995,'Virtual Boy: outra proposta de profundidade','Console','O sistema usa imagens estereoscópicas, em uma experiência distinta dos consoles de televisão.',['h-virtualboy'],[
 'O Virtual Boy deve ser entendido como uma tentativa específica de produzir profundidade estereoscópica. Seu visor e seu suporte físico tornavam a experiência diferente tanto de um Game Boy quanto de um console tradicional.',
 'O sistema teve uma trajetória comercial curta. A entrevista oficial com Shigeru Miyamoto apresenta reflexões sobre a proposta e os limites do produto; não cabe atribuir todas as decisões ou o resultado a uma única pessoa.'
],consoleId='virtual-boy')
event('pokemon',1996,'Pokémon Red e Green','Jogo','Os primeiros jogos Pokémon são lançados para Game Boy no Japão em fevereiro.',['h-pokemon-history'],franchise='pokemon')
event('n64',1996,'Nintendo 64','Console','O console e Super Mario 64 marcam a transição da Nintendo para aventuras tridimensionais.',['h-nintendo-64','h-mario40'],consoleId='nintendo-64')
event('ocarina',1998,'Ocarina of Time','Jogo','A saga Zelda chega ao Nintendo 64 com exploração e combates em três dimensões.',['h-zelda-history'],franchise='zelda')
event('pokemon-company',2000,'The Pokémon Company','Empresa','Pokémon Center Co., Ltd. passa a se chamar The Pokémon Company e amplia a gestão da marca.',['h-pokemon-history'],franchise='pokemon')
event('gba',2001,'Game Boy Advance','Console','A linha Game Boy recebe uma nova geração de hardware e jogos.',['h-game-boy-advance'],consoleId='game-boy-advance')
event('gamecube',2001,'Nintendo GameCube','Console','A Nintendo adota discos ópticos proprietários em seu novo console doméstico.',['h-gamecube'],consoleId='gamecube')
event('animal-crossing',2001,'Uma vida em Animal Crossing','Jogo','Dōbutsu no Mori estreia no Nintendo 64 japonês antes das versões internacionais da série.',['h-animal'],franchise='animal-crossing')
event('iwata-presidente',2002,'Satoru Iwata assume a presidência','Empresa','O desenvolvedor e executivo sucede Hiroshi Yamauchi na liderança da companhia.',['h-europe','h-iwata'])
event('ds',2004,'Nintendo DS: duas telas','Console','A tela sensível ao toque acrescenta novas formas de interação ao catálogo portátil.',['h-nintendo-ds'],consoleId='nintendo-ds')
event('wii',2006,'Wii e os controles de movimento','Console','Wii Remote e Wii Sports tornam gestos uma parte central da experiência.',['h-wii','h-wiisports'],consoleId='wii',franchise='wii-sports')
event('3ds',2011,'Nintendo 3DS','Console','O sucessor do DS oferece imagem estereoscópica sem óculos em modelos compatíveis.',['h-nintendo-3ds'],consoleId='nintendo-3ds')
event('wii-u',2012,'Wii U e o GamePad','Console','Uma tela no controle cria possibilidades de jogo assimétrico e de interação com duas telas.',['h-wii-u'],consoleId='wii-u')
event('dificuldades-wii-u',2014,'Desafios do período Wii U','Empresa','O balanço do exercício registra prejuízo operacional e dificuldades de vendas do Wii U.',['h-fy2014'],[
 'A história da Nintendo também inclui resultados abaixo das expectativas. Na apresentação de maio de 2014, a empresa reconhece os problemas de impulso comercial do Wii U e relata o resultado do exercício encerrado em março.',
 'Os números de um período financeiro não equivalem a uma medida de qualidade de todos os jogos. Este acervo distingue desempenho comercial, recepção crítica e legado de design; valores e vendas só devem ser comparados com datas de corte equivalentes.'
])
event('splatoon',2015,'Splatoon inaugura uma nova franquia','Jogo','As batalhas de tinta estreiam no Wii U com os Inklings.',['h-splatoon'],franchise='splatoon',consoleId='wii-u')
event('iwata-legado',2015,'O legado de Satoru Iwata','Empresa','A morte de Iwata encerra um período marcado por DS, Wii e novas formas de comunicação.',['h-iwata'])
event('kimishima',2015,'Tatsumi Kimishima assume a presidência','Empresa','A Nintendo anuncia a nova gestão em setembro, após a morte de Satoru Iwata.',['h-kimishima'])
event('miitomo',2016,'Miitomo e os dispositivos móveis','Inovação','Miitomo é lançado como aplicativo para dispositivos inteligentes.',['h-corporate'])
event('switch',2017,'Nintendo Switch','Console','O formato híbrido aproxima o uso na televisão e o uso portátil em um mesmo sistema.',['h-switch-compare'],consoleId='switch')
event('starfox2',2017,'Star Fox 2 finalmente lançado','Museu','O projeto de Super Nintendo antes cancelado chega ao público no Nintendo Classic Mini: SNES.',['h-starfox'],[
 'Uma obra cancelada pode voltar à história de outra maneira. Star Fox 2 foi desenvolvido para Super Nintendo, mas não chegou ao mercado naquela época. Seu lançamento no console em miniatura permite comparar ideias de duas fases da franquia.',
 'A entrevista oficial de 2017 reúne participantes do desenvolvimento. Ela é a referência principal desta entrada, evitando depender apenas de relatos de colecionadores ou arquivos distribuídos sem autorização.'
],franchise='star-fox')
event('furukawa',2018,'Shuntaro Furukawa assume a presidência','Empresa','A mudança de liderança é anunciada oficialmente aos investidores.',['h-furukawa'])
event('switch-online',2018,'Nintendo Switch Online','Inovação','A Nintendo inicia seu serviço por assinatura para a família Switch.',['h-corporate'],consoleId='switch')
event('switch-lite',2019,'Nintendo Switch Lite','Console','A família Switch ganha um modelo dedicado ao jogo portátil.',['h-switch-lite'],consoleId='switch-lite')
event('super-nintendo-world',2021,'Super Nintendo World','Empresa','A área temática abre no Universal Studios Japan, ampliando experiências fora dos consoles.',['h-corporate'])
event('switch-oled',2021,'Nintendo Switch – Modelo OLED','Console','Uma revisão da família Switch traz tela OLED e alterações no suporte e na base.',['h-switch-oled'],consoleId='switch-oled')
event('mario-filme',2023,'Super Mario nos cinemas','Empresa','The Super Mario Bros. Movie é lançado como animação produzida em parceria com a Nintendo.',['h-corporate'],franchise='mario')
event('museum',2024,'Nintendo Museum','Museu','A antiga fábrica em Uji abre em 2 de outubro como espaço de história do entretenimento Nintendo.',['h-museum','h-corporate','h-museum-direct'],[
 'O Nintendo Museum fica em Uji, Kyoto, em uma instalação ligada à história industrial da empresa. A exposição aproxima produtos de diferentes épocas e regiões, mostrando que um mesmo nome pode ter embalagens e apresentações distintas.',
 'A instituição combina exposição e experiências interativas. Este Nintendo Universe é um projeto independente: menciona o museu como fonte e marco histórico, sem afirmar vínculo institucional ou reproduzir sua visita como se fosse oficial.'
])
event('switch-2',2025,'Nintendo Switch 2','Console','O sucessor do Switch é lançado em 5 de junho, com Joy-Con 2 e nova capacidade de hardware.',['h-switch2','h-switch2-release'],consoleId='switch-2')
event('bananza',2025,'Donkey Kong Bananza','Jogo','Donkey Kong protagoniza uma aventura 3D de destruição de cenários para Nintendo Switch 2.',['h-bananza'],franchise='donkey-kong',consoleId='switch-2')
event('virtual-boy-classics',2026,'Virtual Boy volta ao catálogo oficial','Museu','Virtual Boy – Nintendo Classics fica disponível em 17 de fevereiro para Switch e Switch 2.',['h-vb2026'],[
 'A retrospectiva oficial da Nintendo Austrália publicada em 2 de março de 2026 confirma a disponibilidade do aplicativo desde 17 de fevereiro. O acesso requer Nintendo Switch Online + Pacote adicional e um dos acessórios específicos.',
 'A notícia distingue os sete jogos disponíveis naquele momento dos títulos anunciados para adição posterior, incluindo projetos antes inéditos. Esta entrada não transforma esse anúncio em confirmação de que todos já foram lançados.'
],consoleId='virtual-boy')
expanded = {
 'hiroshi': [
   'Hiroshi Yamauchi assume a presidência em 1949 e conduz a companhia por décadas de transformação. Sua gestão abrange a diversificação em brinquedos e entretenimento eletrônico, a entrada nos arcades e o estabelecimento dos consoles de cartuchos.',
   'Uma biografia de executivo ajuda a entender decisões, mas não substitui o trabalho coletivo de engenheiros, artistas, programadores e distribuidores. A história da Nintendo reúne tanto liderança empresarial quanto criação de produtos.'
 ],
 'game-watch': [
   'Os Game & Watch combinam um jogo eletrônico dedicado com funções de relógio em um aparelho portátil. A tela LCD utiliza figuras predeterminadas, uma abordagem diferente dos sprites desenhados por consoles de cartuchos.',
   'A família recebe formatos variados. Por isso, Game & Watch deve ser estudado como uma linha de aparelhos e jogos, não como um console único capaz de executar todo o catálogo. Sua proposta mostra como o contexto de uso pode orientar o design.'
 ],
 'famicom': [
   'O Family Computer, ou Famicom, chega ao Japão em 1983. Sua relação com o NES é histórica e técnica, mas as apresentações regionais não são idênticas: nome, aparência, conexão de controles e calendário de distribuição precisam ser registrados conforme a edição.',
   'A comercialização de jogos separados do aparelho possibilita ampliar o catálogo ao longo do tempo. Na enciclopédia, a plataforma relaciona lançamentos, controles e acessórios; compatibilidade entre produtos de regiões diferentes exige verificação específica.'
 ],
 'super-mario': [
   'Super Mario Bros. é lançado para Famicom em 1985. O jogo faz do deslocamento lateral, dos saltos e das transformações os elementos centrais de uma viagem por diferentes fases.',
   'Essa data marca a série Super Mario, mas não o nascimento do personagem: Mario já havia aparecido em Donkey Kong e Mario Bros. A diferença evita misturar o aniversário de um personagem com o aniversário de uma linha de jogos.'
 ],
 'zelda': [
   'A estreia japonesa de The Legend of Zelda ocorre no Famicom Disk System em 21 de fevereiro de 1986. Link busca os fragmentos da Triforce da Sabedoria e enfrenta Ganon para resgatar Zelda.',
   'O histórico oficial de lançamentos apresenta a edição de disquete antes da versão internacional em cartucho. A cronologia narrativa do mundo de Hyrule é uma questão separada: um jogo publicado depois pode retratar uma época anterior.'
 ],
 'game-boy': [
   'O Game Boy chega em 1989 e permite trocar jogos em cartuchos, diferentemente dos aparelhos dedicados Game & Watch. A portabilidade muda onde e quando uma aventura pode ser jogada.',
   'A família Game Boy incluiria revisões de tamanho e tela, seguidas pelo Game Boy Color e pelo Game Boy Advance. Agrupar a família ajuda a navegação, mas não significa que todos os seus jogos funcionem em todos os modelos.'
 ],
 'super-famicom': [
   'O Super Famicom estreia no Japão em 1990. A expansão internacional usa a marca Super Nintendo Entertainment System e acontece em calendários diferentes, motivo pelo qual o ano de uma edição europeia não deve ser aplicado ao lançamento japonês.',
   'O catálogo inclui novos títulos e novas formas de apresentar séries existentes. Super Mario World, F-Zero e outros jogos exploram a geração de 16 bits em propostas diferentes; não existe uma única medida que resuma toda a evolução técnica.'
 ],
 'starfox': [
   'Star Fox utiliza o chip Super FX no cartucho para auxiliar a apresentação de cenas poligonais no Super Nintendo. O jogo demonstra que a capacidade de uma plataforma também pode ser ampliada por componentes incluídos no software físico.',
   'A entrevista oficial documenta a colaboração entre profissionais da Nintendo e da Argonaut. Na Europa, o primeiro jogo foi conhecido como Starwing; nomes diferentes não devem gerar automaticamente dois jogos originais no catálogo.'
 ],
 'pokemon': [
   'Red e Green chegam ao Game Boy no Japão em fevereiro de 1996. Trocar criaturas entre jogadores integra a proposta da franquia, que depois se expande para cartas, animação, filmes e muitos derivados.',
   'As versões internacionais não seguem exatamente o mesmo calendário ou os mesmos nomes das primeiras edições japonesas. O catálogo trata região, versão e relançamento como dados separados e registra os papéis de Nintendo, Game Freak, Creatures e The Pokémon Company.'
 ],
 'n64': [
   'O Nintendo 64 chega em 1996, com Super Mario 64 como um dos exemplos centrais de exploração em três dimensões. Mover o personagem em profundidade e controlar a câmera cria problemas de design diferentes dos encontrados em plataformas laterais.',
   'O sistema conserva cartuchos como mídia de jogos. Seus controles e acessórios fazem parte da experiência histórica, mas as necessidades variam por título; uma entrada de console não deve prometer compatibilidade universal.'
 ],
 'gamecube': [
   'O GameCube estreia em 2001 e utiliza discos ópticos proprietários. O formato compacto do aparelho e o desenho de seu controle ajudam a distinguir a geração anterior ao Wii.',
   'Luigi’s Mansion e outras aventuras ampliam o papel de personagens conhecidos. A biblioteca também inclui projetos de estúdios parceiros e terceiros: estar disponível no GameCube não torna automaticamente um jogo propriedade da Nintendo.'
 ],
 'ds': [
   'O Nintendo DS estreia em 2004 com duas telas e uma tela de toque. Essa configuração permite organizar informações e ações em superfícies diferentes, acrescentando outras possibilidades à entrada tradicional por botões.',
   'O DS Lite, o DSi e o DSi XL são modelos distintos da família. Aplicativos, câmeras e serviços de modelos posteriores não devem ser atribuídos ao primeiro aparelho sem indicação.'
 ],
 'wii': [
   'O Wii chega em 2006 com uma proposta de interação baseada no Wii Remote. Wii Sports apresenta modalidades que relacionam gestos do jogador às ações na tela e usa personagens Mii.',
   'A ideia de controle acessível convive com um catálogo amplo, incluindo jogos que usam botões, apontamento e acessórios. Nunchuk, Wii MotionPlus e controles clássicos têm funções e requisitos próprios; o nome da plataforma não basta para determinar como cada título é jogado.'
 ],
 '3ds': [
   'O Nintendo 3DS estreia em 2011 e combina a herança de duas telas com imagem estereoscópica sem óculos em sua tela superior. A função pode ser ajustada ou desativada nos modelos compatíveis.',
   'A família inclui também o Nintendo 2DS, cuja proposta não usa o efeito 3D. Modelos New possuem diferenças de hardware; requisitos específicos de jogos e aplicativos precisam ser mantidos no nível de cada lançamento.'
 ],
 'wii-u': [
   'O Wii U estreia em 2012 com o GamePad, um controle com tela. O projeto permite apresentar informações ou perspectivas diferentes para quem segura o controle e para quem acompanha a televisão.',
   'O Wii U é um console próprio, e não apenas um acessório do Wii. A existência de compatibilidade com jogos e controles anteriores não elimina diferenças de catálogo, funcionamento e requisitos entre as duas plataformas.'
 ],
 'switch': [
   'O Nintendo Switch chega em 2017 com modos de televisão, mesa e portátil. Os controles Joy-Con destacáveis participam dessa flexibilidade, enquanto cada jogo informa os modos e configurações que oferece.',
   'As revisões Lite e OLED atendem a usos diferentes dentro da família. O Lite é dedicado ao modo portátil; a existência de um mesmo catálogo não significa que acessórios e modos de jogo sejam intercambiáveis sem restrições.'
 ],
 'switch-2': [
   'O Nintendo Switch 2 é lançado em 5 de junho de 2025. O sistema mantém a proposta de alternar contextos de uso e introduz controles Joy-Con 2, com conexão magnética e novas formas de interação em títulos compatíveis.',
   'O catálogo distingue jogos exclusivos, edições para o novo sistema e jogos anteriores compatíveis. Resolução e taxa de quadros dependem da combinação entre jogo, modo, tela e configurações; capacidades máximas não são promessas universais.'
 ]
}
for row in history:
    if row['id'] in expanded:
        row['content'] = expanded[row['id']]
save('history',sorted(history,key=lambda e:e['year']))

franchises=[]
def franchise(id,name,year,color,description,history,ownership,sourceIds,topics=None):
    d=dict(id=id,name=name,year=year,color=color,description=description,history=history,ownership=ownership,sourceIds=sourceIds)
    if topics: d['topics']=[dict(title=t,body=b) for t,b in topics]
    franchises.append(d)

franchise('mario','Super Mario',1981,'#D61932','Do arcade aos mundos 3D, uma família de aventuras, esportes, corridas e RPGs.',[
 'Mario aparece em Donkey Kong, em 1981, antes de Super Mario Bros. inaugurar sua série de plataforma em 1985. O catálogo diferencia a primeira aparição do personagem e o início de cada linha de jogos.',
 'Os jogos de plataforma convivem com Mario Kart, Mario Party, Paper Mario, Mario & Luigi e séries esportivas. Capas, datas e créditos devem ser tratados por edição: um remake é um lançamento distinto, mas não uma história inteiramente nova.',
 'A passagem a Super Mario 64 ampliou o espaço de exploração. Sunshine, Galaxy e Odyssey demonstram propostas diferentes para a aventura 3D, enquanto jogos como New Super Mario Bros. e Wonder mantêm a linguagem lateral.'
],'Franquia Nintendo; desenvolvedoras e parceiros variam entre séries e títulos.',['h-dk-history','h-mario-history','h-mario40'],[
 ('Aventuras e transformações','Cogumelos, flores e outras transformações mudam os movimentos e as possibilidades do personagem. Os poderes pertencem ao contexto de cada jogo; sua presença não deve ser presumida para toda a série.'),
 ('Linhas do universo Mario','O catálogo reúne plataforma 2D e 3D, Mario Kart, Mario Party, Paper Mario, Mario & Luigi, esportes e derivados. A relação de família não substitui a identificação da série de origem.'),
 ('Reino Cogumelo e personagens','Mario, Luigi, Peach, Toad e Bowser formam parte do elenco recorrente. Jogos individuais também introduzem reinos, habitantes e adversários próprios. O perfil de personagem reúne essas relações sem transformar versões em pessoas históricas reais.')])
franchise('zelda','The Legend of Zelda',1986,'#276C50','Exploração, enigmas e lendas de Hyrule em diferentes épocas e estilos.',[
 'O primeiro The Legend of Zelda estreia no Famicom Disk System japonês em 1986. A série combina exploração de territórios, descoberta de itens e desafios que mudam conforme o jogo.',
 'Link e Zelda não devem ser tratados como uma única dupla com idade fixa em todos os títulos. As histórias retratam diferentes épocas e encarnações, com conexões específicas e mundos além de Hyrule.',
 'A ordem de lançamento é verificável por datas de publicação. A cronologia do mundo ficcional é outra camada editorial: relações oficiais precisam ser apresentadas com sua fonte, e interpretações de fãs devem permanecer identificadas como interpretações.'
],'Franquia Nintendo; alguns jogos e derivados são desenvolvidos com estúdios parceiros.',['h-zelda-history','h-zelda-triforce','h-zelda-origin'],[
 ('Triforce','O símbolo reúne Poder, Sabedoria e Coragem. A mitologia oficial associa suas partes a Ganondorf, Zelda e Link, respectivamente, sem exigir que a relíquia desempenhe exatamente o mesmo papel em todos os jogos.'),
 ('Cronologia oficial e lançamento','O catálogo organiza os títulos por lançamento. A ordem narrativa aqui não é uma árvore completa: só relações verificadas são descritas. Ocarina of Time, Majora’s Mask e The Wind Waker têm contextos próprios documentados no histórico oficial.'),
 ('Itens, masmorras e regiões','Armas e ferramentas permitem enfrentar inimigos e resolver obstáculos; o desenho das masmorras muda entre as aventuras. Koholint, Termina e os mares de The Wind Waker mostram que a série ultrapassa um único mapa.')])
franchise('pokemon','Pokémon',1996,'#CFA900','Colecionar, trocar, batalhar e descobrir criaturas em muitas regiões.',[
 'Pokémon Red e Green são lançados no Japão para Game Boy em fevereiro de 1996. As versões Red e Blue chegariam aos Estados Unidos em 1998; datas de regiões diferentes não são intercambiáveis.',
 'A Game Freak concebe e desenvolve a série principal, a Nintendo participa da fabricação e venda dos jogos, e a Creatures trabalha em áreas como cartas e modelos digitais. A The Pokémon Company administra a marca; sua antecessora foi estabelecida pelas três empresas em 1998.',
 'Jogos, cartas, animação e aplicativos são ramos relacionados, mas distintos. O catálogo separa série principal, remakes e derivados. A Pokédex registra tipos e relações de evolução sem substituir as regras específicas de cada versão.'
],'Propriedade e gestão compartilhadas: Nintendo, Game Freak, Creatures e The Pokémon Company têm papéis distintos.',['h-pokemon-history','h-pokemon-company','h-pikachu'],[
 ('Gerações e regiões','As gerações agrupam fases de jogos e criaturas. Uma região é um lugar do mundo ficcional, e um remake pode revisitar uma região antiga com mecânicas de outra fase.'),
 ('Pokédex interativa','A base local permite procurar espécies, filtrar tipos e gerações e visualizar relações de evolução. A origem e a data de extração dos dados estão registradas; formas e mecânicas especiais não devem ser confundidas com novas espécies.'),
 ('Lendários e míticos','As classificações são registradas conforme a base consultada. Raridade no jogo, força em batalha e condição de lendário ou mítico são conceitos diferentes.')])
franchise('kirby','Kirby',1992,'#CC4A82','Um herói capaz de aspirar inimigos e explorar mundos de formas inesperadas.',[
 'Kirby’s Dream Land apresenta o herói no Game Boy em 1992. As habilidades de cópia passam a integrar a série em Kirby’s Adventure, de 1993; o primeiro jogo não deve receber retroativamente essa mecânica.',
 'O catálogo inclui plataforma e experiências alternativas, como pinball, desafios de movimento e corridas. A parceria entre Nintendo e HAL Laboratory é central para a trajetória da franquia.'
],'Franquia associada à Nintendo e à HAL Laboratory; consultar os créditos de cada título.',['h-kirby','h-kirby-about','h-kirby-deluxe','h-kirby-copy'],[
 ('Habilidades de cópia','Aspirar determinados inimigos permite usar poderes diferentes. Disponibilidade, comandos e aprimoramentos variam entre os jogos.'),
 ('Amigos e rivais','Rei Dedede, Meta Knight e Waddle Dees podem ocupar papéis diferentes conforme a aventura. Um personagem que enfrenta Kirby em uma história pode cooperar com ele em outra.')])
franchise('donkey-kong','Donkey Kong',1981,'#84532F','Dos barris do arcade às selvas de Country e às cavernas de Bananza.',[
 'A estreia de Donkey Kong em 1981 é também a estreia de Mario, então chamado Jumpman. O arcade e a família Country representam fases distintas da franquia.',
 'Donkey Kong Country, desenvolvido pela Rare, usa gráficos pré-renderizados no Super Nintendo e apresenta Diddy Kong. A série Land adapta a aventura ao contexto do Game Boy; Donkey Kong 64 explora o espaço 3D.',
 'Jungle Beat, Returns e Tropical Freeze experimentam controles e estruturas diferentes. Bananza leva o personagem a uma aventura de destruição de cenários em Nintendo Switch 2. A gravata característica já aparecia na arte do Donkey Kong de Game Boy, em 1994.'
],'Franquia Nintendo; Rare, Retro Studios e outras equipes participam em títulos específicos.',['h-dk-history','h-dkc','h-bananza'],[
 ('Arcade e aventura','A família de jogos reúne desafios de tela, plataformas laterais, aventura 3D e derivados. O histórico deve evitar reduzir essa diversidade a uma única sequência numerada.'),
 ('A família Kong','Donkey Kong e Diddy são personagens centrais das aventuras Country. As relações de parentesco entre versões receberam descrições diferentes ao longo do tempo; esta base não impõe uma árvore genealógica definitiva.')])
franchise('metroid','Metroid',1986,'#B74722','Exploração de ficção científica, caminhos interligados e novas habilidades.',[
 'Metroid estreia em 1986 e coloca Samus Aran em uma missão no planeta Zebes. Explorar áreas conectadas e retornar com novas capacidades faz parte da identidade da série.',
 'A linha 2D e os jogos Metroid Prime exploram perspectivas diferentes. Metroid: Zero Mission reconta o primeiro jogo; Samus Returns revisita Metroid II. Dread continua a história após Fusion.'
],'Franquia Nintendo; equipes internas e parceiras desenvolvem os diferentes jogos.',['h-metroid-archive','h-metroid-design'])
franchise('animal-crossing','Animal Crossing',2001,'#417B4B','Vida cotidiana, vizinhos e a criação de um lugar próprio.',[
 'A série começa como Dōbutsu no Mori no Nintendo 64 japonês em abril de 2001. As versões posteriores expandem a ideia de viver em uma comunidade de animais.',
 'Em New Leaf, a possibilidade de personalizar o espaço público leva ao papel de prefeito. A entrevista de desenvolvimento mostra como esse conceito nasceu de decisões de design, em vez de ser simplesmente uma troca de cenário.'
],'Franquia Nintendo.',['h-animal','h-isabelle'])
franchise('pikmin','Pikmin',2001,'#69842E','Pequenas criaturas, estratégia e expedições em ambientes gigantes.',[
 'Pikmin nasce no GameCube, com Olimar comandando criaturas de cores e capacidades diferentes. Gerenciar grupos e tarefas transforma um ambiente familiar em território de exploração.',
 'A edição NEW PLAY CONTROL! para Wii adapta a seleção e o comando dos Pikmin ao apontamento do Wii Remote. Revisões de controle devem ser registradas separadamente do lançamento original.'
],'Franquia Nintendo.',['h-pikmin','h-europe'])
franchise('splatoon','Splatoon',2015,'#7047BC','Batalhas de tinta, transformação e cultura urbana.',[
 'Splatoon estreia no Wii U em 2015. As partidas de Turf War colocam a cobertura de território com tinta no centro da disputa.',
 'Inklings alternam entre formas humanoide e de lula, usando a tinta para se movimentar. Essa relação entre mapa, cor e deslocamento distingue a franquia de jogos baseados apenas em eliminar adversários.'
],'Franquia Nintendo.',['h-splatoon'])
franchise('star-fox','Star Fox',1993,'#356A99','Combates espaciais, equipe de pilotos e experimentos com polígonos.',[
 'Star Fox estreia no Super Nintendo utilizando o chip Super FX para gráficos poligonais. A colaboração com a Argonaut é documentada em entrevistas de desenvolvimento.',
 'Star Fox 2 foi cancelado em sua época e recebeu lançamento oficial no Nintendo Classic Mini: SNES em 2017. A existência de um projeto anterior não equivale a um lançamento comercial naquele ano de produção.'
],'Franquia Nintendo; diferentes jogos têm parceiros de desenvolvimento.',['h-starfox'])
franchise('f-zero','F-Zero',1990,'#4263A7','Corridas futuristas de alta velocidade em pistas de ficção científica.',[
 'F-Zero integra o início da geração Super Famicom. A apresentação das pistas e das máquinas ajuda a construir a sensação de velocidade da série.',
 'O catálogo preserva a distinção entre o original, sequências domésticas, jogos portáteis e experiências online. A estreia japonesa de 1990 não deve ser substituída pelo ano de uma edição ocidental.'
],'Franquia Nintendo.',['h-fzero'])
franchise('fire-emblem','Fire Emblem',1990,'#3C5D9A','Batalhas táticas, personagens e decisões com consequências.',[
 'Shadow Dragon & the Blade of Light estreia no Famicom em 20 de abril de 1990, no Japão. A Intelligent Systems é uma parceira central da série.',
 'Os jogos visitam países, épocas e elencos diferentes. Nem toda entrada continua diretamente a aventura anterior. Remakes, títulos para dispositivos móveis e colaborações têm identificação própria no catálogo.'
],'Franquia Nintendo / Intelligent Systems, conforme os créditos oficiais da série.',['h-fireemblem','h-marth'])
franchise('earthbound','EarthBound / Mother',1989,'#AA4D67','RPGs que encontram o extraordinário em ambientes cotidianos.',[
 'Mother nasce no Famicom japonês. O primeiro jogo recebe oficialmente o nome EarthBound Beginnings em sua publicação internacional posterior.',
 'EarthBound acompanha Ness e seus companheiros em cenários contemporâneos, com humor e fenômenos psíquicos. Nome comercial internacional e posição na série precisam ser distinguidos: EarthBound corresponde a Mother 2.'
],'Série com direitos creditados à Nintendo e a Shigesato Itoi; consultar cada edição.',['h-mother','h-earthbound'])
franchise('yoshi','Yoshi',1991,'#3D8C42','O companheiro de Mario também protagoniza aventuras com identidade própria.',[
 'Yoshi aparece em Super Mario World, lançado no Japão em 1990. O ano de 1991 aqui identifica o começo de títulos próprios com seu nome, não a primeira aparição do personagem.',
 'Yoshi’s Island explora outra linguagem visual e outra relação entre personagens, movimentos e exploração. A entrevista oficial com a equipe mostra o processo criativo por trás de Super Mario World e Yoshi’s Island.'
],'Franquia Nintendo, relacionada ao universo Mario.',['h-mario-world','h-yoshi-interview','h-yoshi-eggs'])
franchise('wario','Wario',1994,'#AD8E15','Caça ao tesouro, humor e coleções de microjogos.',[
 'Wario é apresentado como rival em Super Mario Land 2, de 1992. Wario Land: Super Mario Land 3 inicia a linha de aventuras protagonizadas por ele em 1994.',
 'A família Wario reúne propostas distintas: jogos de plataforma e a série de microjogos WarioWare. Seu personagem conserva relações com Mario, mas os catálogos devem permitir explorar as linhas próprias.'
],'Franquia Nintendo; relacionada ao universo Mario.',['h-mario-land2','h-mario-friends','h-europe'])
franchise('smash-bros','Super Smash Bros.',1999,'#B54537','Um encontro de personagens em combates de plataforma.',[
 'O primeiro Super Smash Bros. estreia no Nintendo 64 em 1999, reunindo personagens de diferentes séries Nintendo.',
 'O dano acumulado e o lançamento para fora da arena organizam o combate. Os jogos posteriores ampliam o elenco, incluindo participações licenciadas de outras empresas; presença no jogo não transfere a propriedade de uma franquia à Nintendo.'
],'Série Nintendo com personagens próprios e propriedades de parceiros sob licença.',['h-smash'])
franchise('kid-icarus','Kid Icarus',1986,'#5388B2','Pit enfrenta ameaças mitológicas em aventuras de ação.',[
 'Kid Icarus estreia no Famicom Disk System em 1986 e chega a outras regiões como jogo de NES. Pit é o protagonista ligado à proteção de Angel Land.',
 'A franquia combina referências mitológicas com regras próprias. As descrições deste acervo tratam esse universo como ficção e distinguem a aventura original de suas continuações.'
],'Franquia Nintendo.',['h-kidicarus'])
franchise('advance-wars','Wars / Advance Wars',1988,'#5B7B42','Estratégia por turnos com exércitos, terreno e comandantes.',[
 'A família Wars começa com Famicom Wars no Japão, em 1988. Advance Wars dá nome à fase iniciada no Game Boy Advance, em vez de ser o ponto inicial de toda a família.',
 'As batalhas combinam unidades, captura de instalações e leitura do terreno. O catálogo agrupa os jogos da família sem confundir títulos publicados apenas no Japão com lançamentos internacionais.'
],'Série Nintendo com a Intelligent Systems como desenvolvedora de títulos centrais.',['h-wars-official','h-wars'])
franchise('golden-sun','Golden Sun',2001,'#A67C24','RPG, alquimia, Djinn e enigmas resolvidos com Psynergy.',[
 'Golden Sun estreia no Game Boy Advance e é desenvolvido pela Camelot. A aventura combina combates com exploração e poderes utilizados também fora das batalhas.',
 'The Lost Age continua a história a partir de outro grupo. Os Djinn e a Psynergy conectam progressão de personagens, classes e desafios dos ambientes.'
],'Série publicada pela Nintendo e desenvolvida pela Camelot; não confundir a publicadora com a equipe de criação.',['h-goldensun'])
franchise('xenoblade','Xenoblade Chronicles',2010,'#9F3A46','Mundos de grande escala, grupos de aventureiros e RPGs da Monolith Soft.',[
 'Xenoblade Chronicles estreia no Wii no Japão em 2010 e chega à Europa em 2011. Shulk e a espada Monado são centrais à aventura original.',
 'Os ambientes, combates e relações entre personagens estruturam a experiência. A Monolith Soft é a desenvolvedora; a Nintendo atua como publicadora, e as diferentes entradas merecem registros próprios.'
],'Série Nintendo desenvolvida pela Monolith Soft.',['h-xenoblade'])
franchise('rhythm-heaven','Rhythm Heaven',2006,'#AA8035','Pequenas situações de humor que dependem de ritmo e precisão.',[
 'A série começa no Japão como Rhythm Tengoku para Game Boy Advance. Outros mercados usam nomes como Rhythm Heaven e Rhythm Paradise.',
 'Os minijogos pedem que o jogador reconheça padrões musicais. A entrevista de desenvolvimento documenta a colaboração com o músico Tsunku e a busca por uma interação acessível.'
],'Franquia Nintendo, com colaboração musical documentada de Tsunku.',['h-rhythm'])
franchise('punch-out','Punch-Out!!',1984,'#AC4732','Boxe de observação, esquiva e leitura dos adversários.',[
 'Punch-Out!! aparece nos arcades em 1984. A série combina o tema do boxe com adversários de padrões reconhecíveis e desafios de tempo de resposta.',
 'As versões domésticas reinterpretam a proposta, em vez de serem cópias idênticas da máquina original. O catálogo diferencia o arcade, suas adaptações e os jogos posteriores.'
],'Franquia Nintendo.',['h-punchout'])
franchise('luigis-mansion','Luigi’s Mansion',2001,'#447543','Luigi enfrenta fantasmas com equipamentos do professor E. Gadd.',[
 'Luigi’s Mansion estreia no GameCube em 2001. Luigi deixa o papel habitual de parceiro para investigar uma mansão e procurar Mario.',
 'Exploração, enigmas e captura de fantasmas organizam uma experiência distinta das plataformas Mario. As continuações mudam os locais e os equipamentos, preservando o contraste entre coragem e apreensão do protagonista.'
],'Franquia Nintendo relacionada ao universo Mario; desenvolvedoras variam por título.',['h-luigi','h-mario-friends'])
franchise('wii-sports','Wii Sports',2006,'#307E9B','Movimentos cotidianos transformados em esportes acessíveis.',[
 'Wii Sports acompanha a chegada do Wii em 2006. Tênis, boliche e outras modalidades demonstram a proposta do Wii Remote.',
 'O jogo usa personagens Mii e regras simplificadas. A facilidade de compreender os gestos faz parte de sua identidade, mas não elimina diferenças de controle entre o original, Resort e outras experiências esportivas.'
],'Franquia Nintendo.',['h-wiisports'])
franchise('excitebike','Excitebike',1984,'#A74B2F','Motocross, rampas e o cuidado com a temperatura do motor.',[
 'Excitebike é uma das séries de corrida da Nintendo da era Famicom e NES. Equilibrar a moto e administrar aceleração são partes da experiência.',
 'O catálogo distingue o jogo doméstico da edição VS. de arcade e das revisões posteriores. Um relançamento moderno não deve substituir o ano de origem do título.'
],'Franquia Nintendo.',['h-excitebike','h-europe'])
save('franchises',franchises)

characters=[]
def character(id,name,franchise,debut,description,sourceIds,evolution=None):
    d=dict(id=id,name=name,franchise=franchise,debut=debut,description=description,sourceIds=sourceIds)
    if evolution: d['evolution']=[dict(year=y,title=t,description=b) for y,t,b in evolution]
    characters.append(d)
character('mario','Mario','mario',1981,'Herói do Reino Cogumelo, reconhecido pelo boné vermelho, bigode e habilidade de saltar. Estreia em Donkey Kong como Jumpman.',['h-mario-friends','h-dk-history'],[(1981,'Donkey Kong','Primeira aparição no arcade, em uma apresentação de poucos pixels.'),(1985,'Super Mario Bros.','A aventura lateral organiza o Reino Cogumelo e suas transformações.'),(1996,'Super Mario 64','Movimentação livre em cenários tridimensionais.'),(2017,'Super Mario Odyssey','Cappy amplia as possibilidades de movimento e interação.')])
character('luigi','Luigi','mario',1983,'Irmão de Mario, identificado pela roupa verde. Apesar do receio de fantasmas, protagoniza investigações em Luigi’s Mansion.',['h-luigi-debut','h-mario-friends','h-luigi'],[(1983,'Mario Bros.','Surge como parceiro de Mario.'),(2001,'Luigi’s Mansion','Assume uma aventura própria de exploração e captura de fantasmas.')])
character('peach','Princesa Peach','mario',1985,'Princesa do Reino Cogumelo, amiga de Mario e participante de aventuras e disputas esportivas.',['h-mario40','h-mario-friends'])
character('toad','Toad','mario',1985,'Habitante do Reino Cogumelo e ajudante de Peach. Seu chapéu apresenta pintas vermelhas; outros Toads têm cores variadas.',['h-mario40','h-mario-friends'])
character('bowser','Bowser','mario',1985,'Rei dos Koopas e adversário recorrente de Mario, capaz de usar força e soprar fogo.',['h-mario40','h-mario-friends'])
character('yoshi','Yoshi','yoshi',1990,'Companheiro de Mario que usa a língua para apanhar inimigos e pode produzir ovos para lançar. Estreia em Super Mario World.',['h-mario-world','h-yoshi-interview','h-mario-friends'],[(1990,'Super Mario World','Acompanha Mario na aventura do Super Famicom.'),(1995,'Yoshi’s Island','É protagonista na jornada com Baby Mario e ganha outra linguagem visual.')])
character('daisy','Daisy','mario',1989,'Princesa de Sarasaland, apresentada em Super Mario Land; também participa de esportes e festas do universo Mario.',['h-mario-land','h-mario-friends'])
character('wario','Wario','wario',1992,'Rival autoproclamado de Mario, conhecido pelo boné amarelo, bigode anguloso e interesse em dinheiro.',['h-mario-land2','h-mario-friends'],[(1992,'Super Mario Land 2','Aparece como rival de Mario.'),(1994,'Wario Land','Passa a protagonizar sua própria linha de aventuras.')])
character('waluigi','Waluigi','mario',2000,'Parceiro de Wario e rival declarado de Luigi. Sua primeira participação ocorre em Mario Tennis, no Nintendo 64.',['h-waluigi','h-mario-friends'])
character('rosalina','Rosalina','mario',2007,'Viajante cósmica ligada às Lumas. É apresentada em Super Mario Galaxy.',['h-rosalina','h-mario-friends'])
character('donkey-kong','Donkey Kong','donkey-kong',1981,'Personagem associado à força, barris e bananas. O nome reúne uma história que vai dos arcades à família Country.',['h-dk-history','h-mario-friends'],[(1981,'Donkey Kong','O arcade introduz o nome e o confronto com Jumpman.'),(1994,'Donkey Kong Country','A aventura de plataforma adota sprites pré-renderizados e a parceria com Diddy.'),(2025,'Donkey Kong Bananza','Cenários 3D destrutíveis ampliam as possibilidades de ação.')])
character('diddy-kong','Diddy Kong','donkey-kong',1994,'Ágil parceiro de Donkey Kong, reconhecido pelo boné vermelho e pela camiseta com estrelas. É apresentado em Donkey Kong Country.',['h-dkc','h-mario-friends'])
character('link','Link','zelda',1986,'Nome de heróis de diferentes épocas de Hyrule. Suas encarnações enfrentam perigos e participam de histórias ligadas à Coragem.',['h-zelda-history','h-zelda-triforce'],[(1986,'The Legend of Zelda','A jornada original usa vista superior e exploração de um território aberto.'),(1998,'Ocarina of Time','Uma encarnação é apresentada em uma aventura tridimensional.'),(2017,'Breath of the Wild','Exploração e experimentação ganham outra escala em Hyrule.')])
character('zelda','Zelda','zelda',1986,'Nome de personagens centrais de diferentes épocas da saga. A princesa é associada à Sabedoria e tem papéis distintos conforme o jogo.',['h-zelda-history','h-zelda-triforce'])
character('ganon','Ganon','zelda',1986,'Adversário que aparece desde a aventura original. Ganondorf e suas transformações estão ligados à busca de poder na mitologia da série.',['h-zelda-history','h-zelda-triforce'])
character('impa','Impa','zelda',1986,'Personagem que conecta Link a Zelda na história do primeiro jogo; outras versões assumem papéis diferentes em épocas posteriores.',['h-zelda-history'])
character('marin','Marin','zelda',1993,'Jovem de Koholint que encontra Link após o naufrágio em Link’s Awakening. Seu gosto por cantar marca a aventura.',['h-zelda-history'])
character('midna','Midna','zelda',2006,'Companheira misteriosa de Link em Twilight Princess, ligada ao mundo do crepúsculo e à transformação do herói.',['h-zelda-history'])
character('kirby','Kirby','kirby',1992,'Herói que aspira inimigos e flutua. A habilidade de copiar poderes surge depois de sua estreia em Kirby’s Dream Land.',['h-kirby','h-kirby-about','h-kirby-copy'],[(1992,'Kirby’s Dream Land','A estreia utiliza a tela monocromática do Game Boy.'),(1993,'Kirby’s Adventure','As habilidades de cópia acrescentam novas maneiras de jogar.'),(2022,'Kirby and the Forgotten Land','Uma aventura de plataforma integralmente 3D muda a exploração.')])
character('rei-dedede','Rei Dedede','kirby',1992,'Autoproclamado rei de Dream Land, usa um grande martelo. Pode ser adversário ou aliado de Kirby.',['h-kirby-dream-land','h-dedede'])
character('pikachu','Pikachu','pokemon',1996,'Pokémon do tipo Elétrico, registrado como número 0025 na Pokédex Nacional. Suas bochechas armazenam eletricidade.',['h-pikachu','h-pokemon-history'])
character('samus','Samus Aran','metroid',1986,'Caçadora de recompensas e protagonista de Metroid. Sua armadura adquire recursos que permitem enfrentar ameaças e alcançar novas áreas.',['h-metroid-archive'],[(1986,'Metroid','Investiga o planeta Zebes na aventura original.'),(2004,'Metroid: Zero Mission','A origem recebe uma recriação no Game Boy Advance.'),(2021,'Metroid Dread','A saga 2D continua após os acontecimentos de Fusion.')])
character('marth','Marth','fire-emblem',1990,'Príncipe de Altea e protagonista do primeiro Fire Emblem. Sua trajetória estabelece uma das linhagens de heróis da série.',['h-marth','h-fireemblem'])
character('ness','Ness','earthbound',1994,'Garoto de Onett que parte com companheiros em EarthBound, usando habilidades psíquicas e objetos cotidianos em sua jornada.',['h-earthbound'])
character('pit','Pit','kid-icarus',1986,'Protagonista de Kid Icarus, associado à defesa de Angel Land e à deusa Palutena.',['h-kidicarus'])
character('olimar','Olimar','pikmin',2001,'Explorador espacial que comanda os Pikmin para superar obstáculos e reunir peças de sua nave.',['h-pikmin','h-europe'])
character('isabelle','Isabelle','animal-crossing',2012,'Assistente introduzida em Animal Crossing: New Leaf. Ajuda na administração da cidade e nas tarefas do prefeito.',['h-isabelle','h-animal'])
character('tom-nook','Tom Nook','animal-crossing',2001,'Personagem ligado à loja, às casas e à vida comunitária. Sua função acompanha as mudanças de cada Animal Crossing.',['h-animal'])
character('inkling','Inkling','splatoon',2015,'Habitante de Splatoon que alterna entre forma humanoide e forma de lula, usando tinta para combater e se deslocar.',['h-splatoon'])
save('characters',characters)

quiz=[]
def question(id,category,difficulty,text,options,answer,explanation,sourceIds):
    quiz.append(dict(id=id,category=category,difficulty=difficulty,question=text,options=options,answer=answer,explanation=explanation,sourceIds=sourceIds))
question('fundacao','História','Fácil','Em que ano começou a trajetória da Nintendo?',['1889','1949','1977','1983'],0,'Fusajiro Yamauchi começou a fabricar e vender cartas Hanafuda em Kyoto em 1889.',['h-corporate'])
question('hanafuda','História','Fácil','Qual produto está ligado à origem da Nintendo?',['Televisores','Cartas Hanafuda','Rádios portáteis','Discos de música'],1,'As cartas Hanafuda antecedem em muitas décadas os videogames da empresa.',['h-corporate'])
question('fundador','História','Médio','Quem iniciou a fabricação de cartas da Nintendo em 1889?',['Satoru Iwata','Gunpei Yokoi','Fusajiro Yamauchi','Shigeru Miyamoto'],2,'O fundador foi Fusajiro Yamauchi, em Kyoto.',['h-corporate'])
question('ultra-hand','História','Difícil','Qual produto se associa ao trabalho de Gunpei Yokoi antes dos videogames?',['Wii Balance Board','Super Scope','Rumble Pak','Ultra Hand'],3,'O Ultra Hand é um braço mecânico extensível da fase de brinquedos da Nintendo.',['h-ultra'])
question('museu-local','História','Médio','Em qual cidade fica o Nintendo Museum?',['Uji','Osaka','Tóquio','Nagoya'],0,'O museu ocupa uma instalação histórica da Nintendo em Uji, na região de Kyoto.',['h-museum'])
question('museu-ano','História','Médio','Em que ano o Nintendo Museum abriu?',['2017','2024','2020','2025'],1,'A história corporativa registra a abertura do museu em 2024.',['h-corporate','h-museum'])
question('nso-ano','História','Difícil','Em que ano começou o serviço Nintendo Switch Online?',['2015','2017','2018','2021'],2,'O serviço foi iniciado em 2018, depois do lançamento do console em 2017.',['h-corporate'])
question('mario-debut','Mario','Fácil','Em qual jogo Mario fez sua primeira aparição?',['Super Mario Bros.','Mario Kart','Super Mario Land','Donkey Kong'],3,'Mario estreou em Donkey Kong, em 1981, com o nome Jumpman.',['h-dk-history'])
question('luigi-estreia','Mario','Médio','Qual jogo apresentou Luigi em 1983?',['Mario Bros.','Super Mario 64','Luigi’s Mansion','Super Mario World'],0,'A entrevista oficial sobre New Super Luigi U identifica Mario Bros. como sua estreia.',['h-luigi-debut'])
question('daisy','Mario','Médio','De qual reino Daisy é princesa?',['Hyrule','Sarasaland','Dream Land','Altea'],1,'Daisy é a princesa de Sarasaland, cenário de Super Mario Land.',['h-mario-friends','h-mario-land'])
question('rosalina','Mario','Médio','Em qual aventura Rosalina é apresentada?',['Super Mario Sunshine','Super Mario 3D Land','Super Mario Galaxy','Super Mario Bros. 3'],2,'Rosalina faz sua estreia em Super Mario Galaxy.',['h-rosalina'])
question('waluigi','Mario','Difícil','Qual jogo marcou a estreia de Waluigi?',['Mario Party','Wario Land','Mario Kart 64','Mario Tennis para Nintendo 64'],3,'Waluigi foi apresentado em Mario Tennis, para Nintendo 64.',['h-waluigi'])
question('wario','Mario','Médio','Em qual jogo Wario aparece como um novo rival de Mario?',['Super Mario Land 2: 6 Golden Coins','Super Mario Galaxy','Super Mario Bros.','Mario Bros.'],0,'Wario é o rival de Super Mario Land 2, lançado originalmente em 1992.',['h-mario-land2','h-mario40'])
question('yoshi','Mario','Fácil','Qual jogo apresentou Yoshi?',['Super Mario Sunshine','Super Mario World','Super Mario Land','Super Mario Bros. 2'],1,'Yoshi foi apresentado em Super Mario World, originalmente lançado no Japão em 1990.',['h-mario-world','h-yoshi-interview'])
question('zelda-heroi','Zelda','Fácil','Qual é o nome mais recorrente dos heróis controlados na série Zelda?',['Marth','Ness','Link','Olimar'],2,'Link é o nome dos heróis de diversas épocas da série; não se trata necessariamente da mesma pessoa.',['h-zelda-triforce'])
question('zelda-triforce','Zelda','Fácil','Qual trio representa as partes da Triforce?',['Água, fogo e terra','Tempo, espaço e luz','Força, sorte e velocidade','Poder, Sabedoria e Coragem'],3,'A Triforce é formada pelas partes de Poder, Sabedoria e Coragem.',['h-zelda-triforce'])
question('zelda-original','Zelda','Difícil','Em qual sistema o primeiro Zelda estreou no Japão?',['Famicom Disk System','Nintendo 64','Game Boy','Super Famicom'],0,'The Legend of Zelda foi lançado no Famicom Disk System em 21 de fevereiro de 1986.',['h-zelda-history'])
question('koholint','Zelda','Médio','Qual ilha é o cenário central de Link’s Awakening?',['Delfino','Koholint','Wuhu','Yoshi’s Island'],1,'Link chega a Koholint após um naufrágio em Link’s Awakening.',['h-zelda-history'])
question('termina','Zelda','Médio','Que mundo aparece em Majora’s Mask?',['Sarasaland','Altea','Termina','Hocotate'],2,'A aventura de Majora’s Mask se passa em Termina.',['h-zelda-history'])
question('zelda-ordens','Zelda','Difícil','Qual afirmação distingue corretamente duas maneiras de organizar Zelda?',['Todos os jogos mostram Link na mesma idade.','A ordem narrativa é idêntica à de lançamento.','Teorias de fãs são sempre oficiais.','Datas de lançamento e cronologia narrativa são critérios diferentes.'],3,'A publicação dos jogos é uma ordem histórica; o tempo do mundo ficcional exige outras fontes e relações.',['h-zelda-history','h-zelda-triforce'])
question('pokemon-primeiros','Pokémon','Fácil','Quais versões iniciaram Pokémon no Japão em 1996?',['Red e Green','Gold e Silver','Ruby e Sapphire','X e Y'],0,'Pokémon Red e Green foram os primeiros jogos da franquia no Japão.',['h-pokemon-history'])
question('pokemon-estudio','Pokémon','Médio','Qual empresa concebe e desenvolve a série principal Pokémon?',['Camelot','Game Freak','Retro Studios','Argonaut'],1,'A The Pokémon Company identifica a Game Freak como responsável pela concepção original e desenvolvimento da série.',['h-pokemon-history'])
question('pokemon-companhia','Pokémon','Difícil','Quais empresas estabeleceram a antecessora da The Pokémon Company em 1998?',['Nintendo, Sega e Capcom','HAL, Rare e Camelot','Nintendo, Creatures e Game Freak','Sony, Nintendo e Microsoft'],2,'Pokémon Center Co., Ltd. foi estabelecida pelas três empresas em 1998.',['h-pokemon-history'])
question('pikachu-tipo','Pokémon','Fácil','Qual é o tipo de Pikachu?',['Fogo','Água','Planta','Elétrico'],3,'A Pokédex oficial classifica Pikachu como Elétrico.',['h-pikachu'])
question('pikachu-numero','Pokémon','Médio','Qual é o número de Pikachu na Pokédex Nacional?',['0025','0001','0151','0150'],0,'Pikachu ocupa o número 0025 na Pokédex Nacional.',['h-pikachu'])
question('pokemon-xy','Pokémon','Difícil','Quais jogos principais tiveram o primeiro lançamento mundial simultâneo da série em 2013?',['Ruby e Sapphire','X e Y','Gold e Silver','Red e Blue'],1,'O histórico corporativo registra Pokémon X e Y como o primeiro lançamento mundial simultâneo da série.',['h-pokemon-history'])
question('kirby-primeiro','Kirby','Fácil','Em qual jogo Kirby estreou?',['Kirby Super Star','Kirby Air Ride','Kirby’s Dream Land','Kirby’s Epic Yarn'],2,'Kirby’s Dream Land foi lançado no Game Boy em 1992.',['h-kirby','h-kirby-about'])
question('kirby-copia','Kirby','Médio','Qual jogo introduziu as habilidades de cópia?',['Kirby’s Dream Land','Kirby Air Ride','Kirby’s Dream Course','Kirby’s Adventure'],3,'Kirby’s Adventure, de 1993, acrescentou a habilidade de copiar poderes.',['h-kirby-copy'])
question('dedede','Kirby','Fácil','Qual personagem usa um grande martelo e se declara rei de Dream Land?',['Rei Dedede','Olimar','Fox','Wario'],0,'Rei Dedede é o autoproclamado rei de Dream Land e tem um grande martelo.',['h-dedede'])
question('kirby-colabora','Kirby','Médio','Qual estúdio tem uma ligação central com a série Kirby?',['Argonaut','HAL Laboratory','Camelot','Monolith Soft'],1,'A HAL Laboratory desenvolve jogos de Kirby em parceria com a Nintendo.',['h-kirby','h-kirby-deluxe'])
question('dk-ano','Donkey Kong','Médio','Em que ano surgiu o arcade Donkey Kong?',['1977','1980','1981','1994'],2,'O arcade Donkey Kong foi lançado em 1981.',['h-dk-history'])
question('dk-diddy','Donkey Kong','Fácil','Quem é o parceiro apresentado em Donkey Kong Country?',['Luigi','Meta Knight','Pit','Diddy Kong'],3,'Diddy Kong é apresentado em Donkey Kong Country, de 1994.',['h-dkc'])
question('dk-grafico','Donkey Kong','Médio','Qual técnica marca o visual do Donkey Kong Country original?',['Gráficos pré-renderizados','Vídeo de atores em tela cheia','Somente vetores monocromáticos','Realidade aumentada'],0,'O jogo apresenta personagens e cenários com arte pré-renderizada em um console de 16 bits.',['h-dkc'])
question('dk-gravata','Donkey Kong','Difícil','A gravata de Donkey Kong apareceu em qual arte de caixa antes de Country?',['Donkey Kong 64','Donkey Kong para Game Boy','Donkey Konga','Jungle Beat'],1,'A Nintendo destaca que a gravata já aparecia na arte do Donkey Kong de Game Boy em 1994.',['h-dk-history'])
question('bananza-plataforma','Donkey Kong','Fácil','Para qual console foi lançado Donkey Kong Bananza?',['Nintendo 3DS','Wii U','Nintendo Switch 2','Nintendo GameCube'],2,'Donkey Kong Bananza é uma aventura para Nintendo Switch 2.',['h-bananza'])
question('color-tv','Consoles','Difícil','Qual família inclui os primeiros videogames domésticos da Nintendo de 1977?',['Game & Watch','Game Boy','Nintendo DS','Color TV-Game'],3,'TV Game 6 e TV Game 15 são os sistemas domésticos lançados pela Nintendo em 1977.',['h-corporate'])
question('gameboy-ano','Consoles','Médio','Em que ano o Game Boy original estreou no Japão?',['1989','1983','1996','2001'],0,'O lançamento do Game Boy ocorreu em 1989.',['h-game-boy'])
question('ds-tela','Consoles','Fácil','Qual recurso é central à proposta do Nintendo DS?',['Controle com volante obrigatório','Duas telas, com uma sensível ao toque','Somente jogos em CD','Visor de realidade virtual'],1,'O DS usa duas telas e entrada por toque em uma delas.',['h-nintendo-ds'])
question('wii-controle','Consoles','Fácil','Qual controle está associado à proposta de movimentos do Wii?',['Joy-Con 2','DualShock','Wii Remote','Nintendo 64 Controller'],2,'O Wii Remote é o controle principal ligado à proposta de gestos do Wii.',['h-wii','h-wiisports'])
question('wiiu-controle','Consoles','Médio','Como se chama o controle com tela do Wii U?',['Wii Zapper','Super Scope','Game Boy Player','Wii U GamePad'],3,'O Wii U GamePad incorpora a tela à interação com o console.',['h-wii-u'])
question('switch-lite','Consoles','Médio','Qual modelo Switch foi projetado para o uso portátil dedicado?',['Nintendo Switch Lite','Nintendo Switch – Modelo OLED','Nintendo Switch original','Nintendo Switch 2'],0,'O Switch Lite não oferece o modo de televisão do Switch padrão.',['h-switch-lite','h-switch-compare'])
question('switch2-lancamento','Consoles','Médio','Qual é a data de lançamento do Nintendo Switch 2?',['3 de março de 2017','5 de junho de 2025','18 de novembro de 2012','21 de novembro de 1990'],1,'A data oficial de lançamento do Nintendo Switch 2 é 5 de junho de 2025.',['h-switch2-release'])
question('vb-classics','Consoles','Difícil','Qual aplicativo de clássicos ficou disponível em fevereiro de 2026?',['Sega Dreamcast – Nintendo Classics','Nintendo DS – Nintendo Classics','Virtual Boy – Nintendo Classics','Wii U – Nintendo Classics'],2,'A retrospectiva oficial confirma Virtual Boy – Nintendo Classics disponível a partir de 17 de fevereiro de 2026.',['h-vb2026'])
question('gamecube-midia','Consoles','Médio','Qual mídia física caracteriza o catálogo original do GameCube?',['Fita cassete','Cartucho do Game Boy','Disquete de computador','Disco óptico proprietário'],3,'O GameCube utiliza discos ópticos proprietários, diferentes dos cartuchos do Nintendo 64.',['h-gamecube'])
save('quiz',quiz)

ids={s['id'] for s in sources}
for group in (history,franchises,characters,quiz):
    assert len({x['id'] for x in group})==len(group)
    for row in group:
        assert row['sourceIds'] and all(s in ids for s in row['sourceIds']),row['id']
for q in quiz:
    assert len(q['options'])==4 and 0<=q['answer']<=3
print(json.dumps(dict(history=len(history),franchises=len(franchises),characters=len(characters),quiz=len(quiz),sources=len(sources))))
