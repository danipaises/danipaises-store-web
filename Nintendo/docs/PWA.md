# PWA e offline

O build produz manifest, ícones 192/512 e `sw.js`. Instalação exige navegador compatível, HTTPS/localhost e permissão do host.

## Estratégia

- Pré-cache: páginas de entrada, HTML offline, CSS e todos os chunks com dados e ferramentas.
- Navegação: tenta rede e guarda páginas bem-sucedidas. Offline, usa página visitada ou shell; o cliente identifica a URL e exibe o registro dos dados locais.
- Fotografias: guardadas depois da visualização, sem baixar todas no primeiro acesso.
- Fontes externas: não interceptadas; exigem internet.
- Atualização: assinatura dos assets/dados identifica o cache. São removidos apenas caches antigos com prefixo deste projeto.
- Coleção: localStorage independente do cache. Limpar dados do site remove a coleção; exporte antes.

## Limites e teste

A visita inicial precisa concluir online. Navegadores podem bloquear worker/instalação em frames ou apagar armazenamento por falta de espaço. Host com login pode impor restrições; o build também funciona em outro domínio HTTPS. Não se promete cache antes do carregamento inicial nem todas as fotos offline.

`tests/pwa.test.ts` executa o worker gerado em simulação para verificar precache, atualização, navegação e fotografias em cache. A instalação em dispositivo físico não foi realizada. Consulte TESTES.md para o observado nesta entrega. No teste manual HTTPS: abrir online, concluir cache, visitar foto, desconectar e navegar entre ficha, catálogo, coleção e quiz; reconectar e verificar atualização.
