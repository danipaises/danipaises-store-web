# Nintendo Universe — danipaises.com.br/nintendo

O código-fonte está em `Nintendo/` e a distribuição pública em `../nintendo/`. Os diretórios têm capitalização distinta porque o endereço solicitado é `/nintendo`.

Para atualizar a publicação, execute `npm ci` e `npm run build` nesta pasta, valide e envie ao GitHub tanto `Nintendo/` quanto `nintendo/`. O GitHub Pages deve continuar publicando a raiz da branch `main`. A página principal da loja permanece separada.

Museu digital e enciclopédia independente de fãs, em português brasileiro. React, TypeScript e Vite, com páginas estáticas por registro, busca local, coleção persistente, quiz, comparador, Pokédex e PWA.

**O catálogo está em expansão.** Consulte [docs/COBERTURA.md](docs/COBERTURA.md) para as contagens reais e [docs/TESTES.md](docs/TESTES.md) para o que foi verificado. Não é uma enciclopédia exaustiva de todos os lançamentos.

## Abrir a versão pronta

O pacote contém `../nintendo/`, com o build de produção. Com Python 3:

```bash
python3 -m http.server 8080 --directory .. --bind 0.0.0.0
```

No Windows pode ser `py -m http.server 8080 --directory .. --bind 0.0.0.0`. Abra `http://localhost:8080/nintendo/`. No celular na mesma rede, abra `http://IP-DO-COMPUTADOR:8080/nintendo/`. HTTP por IP permite navegar; PWA e service worker normalmente exigem HTTPS ou localhost. Não abra o HTML por `file://`, pois módulos e rotas precisam de servidor HTTP. Não requer Docker, banco de dados, conta ou chave de API.

## Desenvolvimento

Node.js 22.12+ ou 24 LTS e npm. Dependências fixadas no lockfile:

```bash
npm ci
npm run dev
```

A porta padrão é 4173. O servidor aceita rede local; não exponha o servidor de desenvolvimento à internet.

```bash
npm run validate
npm run build
npm test
node scripts/check-build.mjs
npm run coverage
npm run preview
```

Os testes da PWA leem `dist/sw.js`; execute o build antes da primeira rodada. O build gera HTML individual, sitemap, canonical, Open Graph, JSON-LD, download do catálogo e service worker. Para outro domínio, defina `SITE_URL=https://seu-dominio/nintendo` durante o build.

## Recursos

- História em capítulos; linha do tempo filtrável por década, ano, categoria, console e franquia.
- Consoles, revisões e comparação das especificações documentadas.
- Franquias, jogos e personagens com URL própria e fontes.
- Busca universal; biblioteca com filtros, ordenação e paginação sobre dados reais.
- Coleção local com cinco marcações, exportação e importação JSON validada.
- Quiz com assunto, dificuldade, explicações, revisão e recorde local.
- Pokédex importada da PokéAPI, sem chamadas à API durante a navegação.
- Evolução por lançamentos, trajetórias documentadas e revisões de hardware.
- Museu, galeria, referências, modo claro/escuro e suporte a teclado/movimento reduzido.
- PWA: consulte [docs/PWA.md](docs/PWA.md).

## Estrutura

```text
src/components/   páginas e componentes visuais
src/data/         catálogo, fontes, mídia e Pokédex em JSON
src/lib/          consulta, coleção e estado
src/App.tsx       resolução das rotas
src/entry-server.tsx  renderização durante o build
src/main.tsx      hidratação e registro da PWA
src/styles.css    design responsivo
public/media/     fotografias licenciadas locais
public/icons/     ícones originais da PWA
scripts/          build, importação, validação e cobertura
tests/            catálogo, coleção e worker
docs/             arquitetura, dados, mídia, cobertura e testes
../nintendo/      distribuição de produção gerada
```

## Continuar e publicar

Leia [AGENTS.md](AGENTS.md), [ARQUITETURA.md](docs/ARQUITETURA.md), [DADOS.md](docs/DADOS.md) e [MIDIA.md](docs/MIDIA.md). Publique o conteúdo de `../nintendo/` em host estático HTTPS com suporte a `diretorio/index.html` e configure `404.html` como página de erro. Não é necessária reescrita geral para uma SPA. Esta cópia publica pelo repositório GitHub Pages. Não inclui identidade de hospedagem do projeto original.

## Direitos

Projeto independente, sem afiliação, patrocínio ou aprovação da Nintendo. Marcas e produtos pertencem aos titulares correspondentes. Sem ROMs, BIOS ou downloads de jogos. Fotos têm licenças individuais em `media.json`; algumas conservam CC BY-SA 3.0. As fichas sem capas autorizadas usam gráficos próprios identificados. Licenças de software: `docs/licenses/`.
