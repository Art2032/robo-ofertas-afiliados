# Robô de Ofertas Afiliadas

Projeto inicial para organizar e validar ofertas da Shopee e do Mercado Livre usando GitHub Actions.

## Estado atual

Esta é uma primeira versão de infraestrutura. Ela:
- lê produtos cadastrados manualmente em `data/produtos.json`;
- aceita apenas Shopee e Mercado Livre;
- verifica campos obrigatórios, links HTTPS e desconto mínimo cadastrado de 20%;
- evita repetir o mesmo identificador na mesma execução;
- pode ser executada manualmente ou em horários programados pelo GitHub Actions.

**Importante:** esta versão ainda não busca ofertas nas lojas, não confirma preços em tempo real e não publica no Instagram ou Facebook. O desconto é um dado informado no JSON, não uma verificação feita na loja.

## Como cadastrar um produto

Edite `data/produtos.json` e substitua o exemplo por dados reais. Use seu link de afiliado oficial e uma imagem que você tenha autorização para utilizar.

Exemplo de campos:
- `loja`: `Shopee` ou `Mercado Livre`
- `id`: identificador único do produto
- `nome`: nome do produto
- `preco_atual` e `preco_anterior`: valores numéricos
- `desconto_percentual`: desconto informado
- `url_afiliado`: link de afiliado HTTPS
- `imagem_url`: endereço HTTPS de imagem autorizada

## Executar no GitHub

1. Abra a aba **Actions** do repositório.
2. Se necessário, habilite GitHub Actions.
3. Selecione **Verificar ofertas**.
4. Clique em **Run workflow** para testar manualmente.
5. Consulte os logs para ver os produtos validados ou rejeitados.

O agendamento está configurado para 11h17, 14h17, 17h17 e 20h17 UTC (08h17, 11h17, 14h17 e 17h17 no horário de Brasília, UTC-3). O GitHub pode atrasar execuções agendadas.

## Próximas etapas para automação completa

1. Integrar fontes e APIs oficiais/autorizadas para obter ofertas e links de afiliado.
2. Conferir preço e disponibilidade antes de cada publicação.
3. Configurar Meta for Developers, uma Página do Facebook e a conta profissional do Instagram vinculada.
4. Configurar publicação pela API oficial da Meta e armazenar tokens em **GitHub Secrets** (nunca no código).
5. Adicionar controle persistente de duplicatas, histórico e avisos de erro.

A participação em programas de afiliados e o uso das APIs dependem dos requisitos e permissões de cada plataforma. Não use dados de outra pessoa nem informe idade falsa para contornar regras.

## Desenvolvimento

O projeto usa Python 3.12 e, nesta etapa, apenas a biblioteca padrão do Python.
