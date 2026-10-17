# Relatório de testes — 17/10/2026

## Resultado desta entrega

| Verificação | Resultado | Evidência |
|---|---|---|
| TypeScript estrito | PASS | `tsc --noEmit` durante o build |
| Build Vite cliente e renderização estática | PASS | 611 rotas de conteúdo; 613 HTML incluindo offline e 404 |
| Integridade do acervo | PASS | 509 jogos, 32 consoles/modelos, 25 franquias, 29 personagens, 58 eventos, 44 questões, 20 imagens, 1.025 espécies; IDs e referências validados |
| Testes automatizados | PASS | 15 testes, 0 falhas |
| Referências internas do build | PASS | 23.096 ocorrências href/src verificadas; destinos locais existentes |
| Texto alternativo | PASS | 90 referências de imagens nos HTML possuem alt |
| Fotografias locais | PASS | 20 arquivos decodificados, caminhos válidos e créditos/licenças registrados |

## Testes automatizados

- Rotas individuais únicas, títulos e vínculo entre jogos e plataformas.
- Busca com normalização de acentos, múltiplos termos e gêneros.
- Corte histórico, perguntas com quatro opções distintas e fontes.
- Coleção: exportar/importar, reversibilidade, imutabilidade e rejeição de JSON inválido, versão incorreta, IDs/status desconhecidos, excesso de tamanho e chaves problemáticas.
- PWA: manifest e ícones; precache de interface e chunks; remoção restrita dos caches antigos; navegação offline com página visitada ou shell; fotografia já vista disponível em cache.

Os testes PWA executam o worker gerado num ambiente simulado; não equivalem a instalação real em um telefone.

## Interface observada no navegador

Executada na prévia de desenvolvimento:

- Home em desktop com fotografia real, navegação e dados do catálogo.
- Biblioteca, busca “Metroid” (17 resultados), combinação com Zelda (zero), limpeza e plataforma Wii.
- Ficha de Super Mario Bros.; marcações Favorito e Já joguei persistiram após recarregar; jogo visível na coleção.
- Quiz Kirby: rodada de quatro questões concluída, feedback e placar apresentados; resposta correta/errada e revisão disponíveis.
- Pokédex: busca Pikachu, tipo Elétrico, geração, altura, peso e relações Pichu/Raichu visíveis.
- Linha do tempo: década de 1980 e ano 1989; evento Game Boy e referências exibidos.
- Comparador: troca do primeiro console para Wii atualizou a comparação.
- Layout móvel em frame de largura 390 px (375 px úteis com scrollbar): home e menu abertos; navegação para biblioteca confirmada. Sem rolagem horizontal no documento observado.

Uma leitura inicial após navegação encontrou a tela anterior porque a navegação ainda estava concluindo; a confirmação foi feita com estado atualizado. Não foi tratado como defeito do produto.

## Correções realizadas

- Inicialização de desenvolvimento tentava hidratar um contêiner sem HTML; o cliente agora cria a raiz quando não existe conteúdo renderizado.
- Erro de variável no relatório do script de geração corrigido.
- Título móvel deixou de unir palavras ao esconder uma quebra de linha.
- Removida regra responsiva que ocultava o quarto console do catálogo.
- Menu móvel recebeu fechamento, controle de foco e fundo inerte.
- Divisão de código em chunks eliminou o aviso de bundle único acima de 500 kB.

## Desempenho e limites de verificação

Build final: maior chunk JavaScript aproximadamente 263,5 kB (33,9 kB gzip). React: 223 kB (69,2 kB gzip); interface: 206,8 kB (57,3 kB gzip); referências: 112,7 kB (13,5 kB gzip). CSS: 73,2 kB (14,5 kB gzip). A Pokédex é separada: 156,4 kB (21,3 kB gzip). Esses são tamanhos medidos dos arquivos, não notas de Lighthouse. Fotografias locais somam aproximadamente 1,32 MiB e usam carregamento tardio, exceto o destaque inicial.

Ao mudar a prévia supervisionada para servir o build, a infraestrutura recusou iniciar com `bwrap: Can't mount proc ... Operation not permitted`. A prévia de produção não foi substituída por outro servidor. A configuração de desenvolvimento foi restaurada, e a validação de build, dados, links e testes automatizados continuou. Portanto, a hidratação do build final em navegador, instalação real da PWA e navegação offline em dispositivo físico permanecem sem verificação direta.

Não foram executados Lighthouse, auditoria completa de WCAG com leitor de tela, navegadores Safari/Firefox físicos, testes de carga nem seleção de arquivo/importação pela interface de um aparelho real. A validação de importação/exportação foi testada na lógica de produção. Não se afirma certificação de acessibilidade ou compatibilidade universal.

Os erros de metadados da extensão do navegador observados na prévia são externos ao aplicativo. O aviso de hidratação inicial do app foi corrigido no código; não foi afirmada uma nova sessão de produção sem erros porque a prévia de produção ficou indisponível.

## Reproduzir

```bash
npm ci
npm run validate
npm run build
npm test
node scripts/check-build.mjs
npm run coverage
npm run preview
```

Para validar instalação/offline no domínio HTTPS, seguir `PWA.md`. Repetir apenas os testes afetados por novas mudanças e registrar os limites restantes.
