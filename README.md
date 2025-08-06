# Portal da Transparência - AI

## Índice

- [Descrição](#descrição)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Descrição

O projeto consiste em estruturar, de maneira inteligente e técnica, pesquisa a ser realizada no Portal da Transparência.
Essa pesquisa ocorrerá utilizando a API do Portal da Transparência bem como do SIORG. A primeira necessária é a API-KEY, que estará em um arquivo `.env`.

[https://api.siorg.economia.gov.br/openapi.yaml](https://api.siorg.economia.gov.br/openapi.yaml)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/your-repo/portal-transparencia-ai.git
   cd portal-transparencia-ai
   ```

2. **Instale as dependências usando UV:**

   ```bash
   uv install
   ```

3. **Configure a API-KEY:**
   Crie um arquivo `.env` na raiz do projeto e adicione a sua API-KEY:

   ```plaintext
   PORTAL_API_KEY=your_api_key_here
   ```

4. **Execute o projeto:**

   ```bash
   uv run
   ```

## Uso

### Consulta de Pessoa Física

Para consultar uma pessoa física, utilize o comando abaixo, substituindo `{CPF}` pelo CPF desejado:

```bash
python src/main.py --cpf {CPF}
```

### Consulta de Pessoa Jurídica

Para consultar uma pessoa jurídica, utilize o comando abaixo, substituindo `{CNPJ}` pelo CNPJ desejado:

```bash
python src/main.py --cnpj {CNPJ}
```

## Contribuição

Contribuições são bem-vindas! Para contribuir com este projeto, siga os passos abaixo:

1. **Faça um Fork do repositório:**

   ```bash
   git clone https://github.com/your-repo/portal-transparencia-ai.git
   cd portal-transparencia-ai
   ```

2. **Crie uma nova branch:**

   ```bash
   git checkout -b feature/nome-da-sua-feature
   ```

3. **Faça suas alterações e faça commit:**

   ```bash
   git commit -m "Adicione uma descrição clara das suas alterações"
   ```

4. **Faça push para a sua branch:**

   ```bash
   git push origin feature/nome-da-sua-feature
   ```

5. **Abra um Pull Request:**
   - Vá até o repositório original no GitHub.
   - Clique em "New Pull Request".
   - Selecione a sua branch e descreva as suas alterações.

### Código de Conduta

Por favor, leia o [Código de Conduta](CODE_OF_CONDUCT.md) antes de contribuir.

### Relatórios de Bugs

Se você encontrar um bug, por favor, abra um issue no repositório do GitHub. Inclua detalhes sobre o problema, como passos para reproduzir, ambiente, etc.

````
graph TD
    A["Início: CPF da Pessoa Física"] --> B["Passo 1: Consulta /api-de-dados/pessoa-fisica com parâmetro cpf={CPF}"]
    B --> C{"Resultados Booleanos Obtidos"}

    C -->|servidor = true| D["Passo 2: Detalhamento de Servidor"]
    D --> D1["Viagens: /api-de-dados/viagens-por-cpf com CPF"]
    D --> D2["Remuneração: /api-de-dados/servidores/remuneracao com CPF e mesAno"]
    D --> D3["Vínculos e Cargos: /api-de-dados/servidores com CPF → Obter idServidor → /api-de-dados/servidores/{id}"]
    D --> D4["PEP: /api-de-dados/peps com CPF"]

    C -->|"favorecido... = true (ex: favorecidoNovoBolsaFamilia)"| E["Passo 2: Detalhamento de Benefícios"]
    E --> E1["Benefícios: /api-de-dados/novo-bolsa-familia-sacado-por-nis ou /api-de-dados/bpc-por-cpf-ou-nis com CPF/NIS"]

    C -->|"sancionado... = true (ex: sancionadoCEAF)"| F["Passo 2: Detalhamento de Sanções"]
    F --> F1["Sanções: /api-de-dados/ceaf com CPF"]

    C -->|portadorCPGF = true| G["Passo 2: Detalhamento de Gastos com Cartão"]
    G --> G1["Gastos: /api-de-dados/cartoes com cpfPortador={CPF}"]

    C --> H["Fim: Dossiê Completo com Vínculos, Remuneração, Benefícios, Sanções e Despesas"]
    ````

graph TD
    A["Início: CNPJ da Pessoa Jurídica"] --> B["Passo 1: Consulta /api-de-dados/pessoa-juridica com parâmetro cnpj={CNPJ}"]
    B --> C{"Resultados Booleanos Obtidos"}

    C -->|possuiContratacao = true| D["Passo 2: Detalhamento de Contratos"]
    D --> D1["Listar Contratos: /api-de-dados/contratos/cpf-cnpj com CNPJ → Obter IDs"]
    D1 --> D2["Detalhar Contrato por ID: /api-de-dados/contratos/itens-contratados"]
    D1 --> D3["/api-de-dados/contratos/termo-aditivo"]
    D1 --> D4["/api-de-dados/contratos/documentos-relacionados"]

    C -->|favorecidoDespesas = true| E["Passo 2: Detalhamento de Despesas Diretas"]
    E --> E1["Despesas: /api-de-dados/despesas/documentos-por-favorecido com codigoPessoa={CNPJ}"]

    C -->|"sancionado... = true (ex: sancionadoCEIS)"| F["Passo 2: Detalhamento de Sanções"]
    F --> F1["Sanções: /api-de-dados/ceis ou /api-de-dados/cnep com CNPJ"]

    C -->|emitiuNFe = true| G["Passo 2: Detalhamento de Notas Fiscais"]
    G --> G1["Notas Fiscais: /api-de-dados/notas-fiscais com cnpjEmitente={CNPJ}"]

    C --> H["Fim: Rastreamento Completo de Contratos, Despesas, Sanções e Notas Fiscais"]
`
