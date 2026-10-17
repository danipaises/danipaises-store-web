# Modelo de dados e manutenção

Contratos em `src/types.ts`. IDs são estáveis, em minúsculas com hífens: fazem parte das URLs e coleções. Não reutilizar o ID de um lançamento.

| Arquivo em src/data | Conteúdo |
|---|---|
| games.json | Jogos, plataformas, gêneros, ano, descrição, nível e fontes |
| consoles.json | Sistemas, datas regionais verificadas, specs, modelos e acessórios |
| franchises.json | História e relação da franquia com a Nintendo |
| characters.json | Personagens, estreia e trajetórias documentadas |
| history.json | Eventos e relações com consoles/franquias |
| quiz.json | Quatro opções, índice correto, explicação e fontes |
| media.json | Arquivos locais, autoria, licença e origem das fotos |
| game-sources.json / history-sources.json | Referências por ID |
| pokedex.json / pokedex-meta.json | Espécies e metadados da importação PokéAPI |

## Adicionar jogos

1. Pesquise fonte oficial ou especializada confiável e registre título, URL, instituição, data de consulta e tipo de fonte.
2. Escolha a franquia existente ou cadastre uma nova antes de usar seu ID.
3. Adicione `id`, `title`, `franchise`, `year`, `platforms`, `genres`, `description`, `depth` e `sourceIds`. Plataformas devem usar os nomes amigáveis exatos de `consoles.json`.
4. `year` corresponde à estreia original mais antiga identificada. Diferencie versões, regiões e ports; não use uma data ocidental como estreia mundial sem verificar.
5. `originalTitle`, `developer`, `publisher`, `details` e `relatedIds` são opcionais. Omita o que não foi confirmado. `details` mapeia título em português para texto autoral fonteado.
6. `basic` indica metadados essenciais; `deep` exige contexto e ao menos duas seções substanciais. Repetir a ficha não constitui aprofundamento.
7. Valide, gere cobertura, build e testes. A URL e o HTML são gerados automaticamente.

## Franquias, personagens e história

Preencha origem, história, cor acessível e relação com a Nintendo: propriedade, parceria e publicação não são equivalentes. Personagens usam `debut` para o ano de estreia e `evolution` apenas para mudanças confirmadas. Eventos podem ter `consoleId` e `franchise`. Ordem de lançamento, cronologia narrativa e revisão de hardware são relações distintas. Não transformar estimativas em precisão falsa.

## Mídia e quiz

Siga `MIDIA.md`. Toda fotografia precisa de autor, licença/condição específica, URL da origem, URL da licença e alt. Preserve as condições CC BY-SA. Sem autorização adequada, mantenha substituto identificado. Não copiar capas apenas porque aparecem num portal oficial.

No quiz, `answer` é índice zero a três; alternativas distintas, explicação e fontes são obrigatórias. Categoria e dificuldade precisam corresponder aos filtros.

## Atualizar

`python3 scripts/import-pokedex.py` importa quatro CSVs públicos, usando `curl`, e mantém cópias em `.cache/pokeapi`. Para atualização deliberada, arquive a versão anterior e remova somente esse cache. Não baixa sprites. Registre o corte em `pokedex-meta.json`.

`scripts/build-history-data.py` registra a geração histórica desta entrega. Não executá-lo sobre edições posteriores sem revisar o que será regravado. Jogos são mantidos editorialmente; não há scraping contínuo ou automático no visitante. Termos e licenças continuam exigindo revisão.

Antes de entregar, confira duplicatas, primeiras datas, plataformas, fontes diretas e estado lançado/anunciado. Atualize a cobertura sem alegar completude pela quantidade.
