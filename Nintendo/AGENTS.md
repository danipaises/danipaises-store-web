# Continuidade do Nintendo Universe

Enciclopédia independente em português brasileiro. Não apresentar como oficial, afiliada ou completa. Medir cobertura e lacunas nos dados. Respeitar fontes, licenças e a instrução de executar/testar além de planejar.

## Antes de editar

Leia README, docs/ARQUITETURA.md, DADOS.md, COBERTURA.md, MIDIA.md e TESTES.md. Preserve IDs públicos, referências, créditos e o prefixo público /nintendo. Esta cópia pertence ao repositório principal da loja e publica pela integração Cloudflare Workers conectada ao GitHub.

## Conteúdo

- Fonte por registro; priorizar portais oficiais, museus e entrevistas.
- Não preencher campos ausentes por adivinhação. Diferenciar basic/deep e estreia/port/remake.
- Não tratar anunciado como lançado sem confirmação. Registrar corte temporal e diferenças regionais.
- Distinguir propriedade, parceria, publicação e presença num console.
- Usar nomes de plataformas de consoles.json para vínculos.
- Manter autoria/licenças de fotos, inclusive CC BY-SA. Gráficos substitutos continuam identificados.
- Não adicionar ROMs, BIOS ou downloads protegidos.

## Implementação e validação

React/TypeScript/Vite com geração estática. Preservar busca real, coleção local sem conta e dados versionados. Não adicionar servidor ou serviços com credenciais sem necessidade. Não injetar HTML externo não confiável.

Antes da entrega: `npm run validate`, `npm run build`, `npm test`, `node scripts/check-build.mjs`, `npm run coverage`. O build precede os testes PWA. Faça QA de alterações visuais no navegador: home, navegação, filtros, ficha, coleção, quiz, tela pequena e tema. Documente limites; não invente Lighthouse, certificação WCAG ou teste em dispositivo físico. Repetir apenas checks afetados por correções.

## Publicação

Manter código em Nintendo e build em nintendo; executar npm run build dentro de Nintendo e enviar ambos na mesma alteração. Preservar arquivos da loja fora dessas pastas. Não copiar configuração Sites para esta cópia. Nunca gravar tokens em arquivos/Git. Não limpar coleções do usuário para testes. Usar dados descartáveis em ambiente de QA. A coleção pessoal não é enviada ao servidor.
