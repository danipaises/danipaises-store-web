# Arquitetura e decisão técnica

## Escolha

React + TypeScript + Vite, com geração estática de todas as rotas do acervo e hidratação no navegador. O conteúdo público não exige conta, escrita centralizada, banco ou renderização por requisição; a coleção local foi solicitada explicitamente.

| Alternativa | Vantagem | Decisão |
|---|---|---|
| React/Vite com geração estática | Build portátil, dados versionados e HTML por registro | Adotada |
| Next.js com export estático | Convenções integradas de rotas e metadados | Viável; nesta entrega não há benefício decisivo que justifique a estrutura adicional |
| Backend e SSR | Edição simultânea, contas e atualizações centralizadas | Adiar até existir necessidade editorial/operacional |

Documentação consultada: [Vite — implantação estática](https://vite.dev/guide/static-deploy.html), [React — renderToString](https://react.dev/reference/react-dom/server/renderToString), [React — geração estática](https://react.dev/reference/react-dom/static/prerender), [Next — export estático](https://nextjs.org/docs/app/guides/static-exports), [MDN — cache PWA](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Caching).

`renderToString` é adequado aqui porque os dados editoriais da renderização são locais e síncronos. Não há Suspense ou requisição pendente no build. A Pokédex carrega em chunk separado no cliente; seu HTML estático contém a introdução e os filtros. Se houver dados assíncronos na geração futura, migrar para a API `prerender` apropriada.

## Fluxo

1. JSON em `src/data` passa pela validação de IDs e referências.
2. Vite compila cliente e entrada de renderização.
3. `scripts/prerender.mjs` percorre `getRoutes()`, gerando HTML, metadados, canonical, Open Graph, JSON-LD, sitemap e worker.
4. O cliente hidrata o HTML correspondente. Desenvolvimento e fallback offline usam renderização inicial quando necessário.
5. Navegação utiliza links HTML nativos. Filtros por URL são lidos após montagem para não gerar incompatibilidade de hidratação.
6. O worker mantém shell e dados locais; fotografias usam cache após visualização.

## Dados, pesquisa e expansão

JSON atende ao volume desta entrega e dispensa credenciais. React, catálogo, referências e Pokédex são separados em chunks. A busca normaliza acentos e compara termos reais em títulos, anos, franquias, plataformas, gêneros e créditos disponíveis.

Para dezenas de milhares de registros, criar índice pré-calculado, dividir dados por franquia/plataforma e carregar sob demanda. Edição por várias pessoas pode exigir CMS/banco com histórico editorial, preservando geração estática pública. Não adicionar serviço pago ou login sem necessidade.

## Coleção

Chave `nintendo-universe:collection:v1`, schema versionado. IDs apontam para listas de marcações independentes. Importação valida tamanho, versão, IDs e estados e combina os dados sem apagar a coleção existente. O evento `storage` atualiza outras abas. Falhas de armazenamento são exibidas. Não há sincronização entre dispositivos ou envio da coleção ao servidor.

## Acessibilidade e SEO

HTML semântico, um h1 por página, links nativos, labels, foco visível, aria-live, textos alternativos e controles nativos. Menu móvel controla foco e torna o fundo inerte. Movimento reduzido desativa transições. Não se afirma certificação WCAG: ainda é necessária auditoria com tecnologias assistivas. Não são inventados campos para schema detalhado de VideoGame.

## Segurança

Sem endpoints privados ou segredos no cliente. Conteúdo textual é escapado pelo React, sem HTML externo injetado. Importações não aceitam IDs desconhecidos. Servir por HTTPS, preservar lockfile e não versionar credenciais. A coleta/importação não é executada pelo visitante.
