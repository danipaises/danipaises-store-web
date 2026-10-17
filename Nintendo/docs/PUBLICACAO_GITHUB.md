# Publicação no repositório da loja

- Código completo: Nintendo/.
- Build estático: nintendo/.
- URL: https://danipaises.com.br/nintendo/.
- Origem: projeto Nintendo Universe entregue em 17/10/2026.
- A página principal da loja, CNAME e arquivos originais foram preservados.
- .nojekyll evita transformação dos arquivos estáticos pelo Jekyll.

Dentro de Nintendo: npm ci, npm run build, npm run validate, npm test e node scripts/check-build.mjs. O build escreve ../nintendo. Enviar código e distribuição na mesma alteração.

Nesta migração passaram 19 testes, validação do acervo e verificação de 23.096 referências internas do build. A instalação da PWA em aparelho físico permanece pendente. Não há necessidade de chave de API para abrir o site.

O código usa /nintendo em links, mídia, formulário de busca, roteador e registro do worker. O escopo do worker e seu cache ficam restritos a /nintendo/, sem interceptar a loja na raiz. Manifest, canonical e sitemap foram ajustados.

Nintendo e nintendo são diretórios diferentes nesta hospedagem sensível a capitalização. Para editar ambos, use um sistema de arquivos que preserve essa distinção. Os dados e relatórios editoriais originais permanecem disponíveis em docs/.
