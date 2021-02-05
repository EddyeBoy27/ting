# Boas vindas ao repositório do projeto TING(Trybe is not Google)!

## O que foi desenvolvido

A `Trybe` lhe convida para implementar um programa que simule o algoritmo de indexação de documentos similar ao do google. Ou seja, um programa que permita anexar arquivos de texto e posteriormente opere funções de busca sobre tais arquivos

> Com a quantidade de informações disponíveis na Web, encontrar o que você precisa seria quase impossível sem nenhuma ajuda para classificá-las. Os sistemas de classificação do Google organizam centenas de bilhões de páginas da Web, no índice da pesquisa, para fornecer os resultados mais úteis e relevantes em uma fração de segundo. Além disso tudo, a a Google também precisa se preocupar em apresentar os resultados de uma maneira que ajude você a encontrar o que está procurando com mais facilidade ainda.

#### Analisar palavras

> Compreender o significado da sua pesquisa é crucial para retornarmos boas respostas. Por isso, para encontrar páginas com informações relevantes, nosso primeiro passo é analisar o significado das palavras na consulta de pesquisa. Desenvolvemos modelos linguísticos para decifrar as sequências de palavras que precisamos procurar no índice.

Não iremos nos apegar a análise de significados ou busca por sinônimos. Nosso objetivo será identificar ocorrências de termos em arquivos _TXT_. Neste contexto, devemos criar um programa que permita anexar arquivos de texto e posteriormente operar funções de busca sobre tais arquivos.

Sendo assim o programa deverá possuir dois módulos:

- Modo gerenciamento de arquivos;

- Modo de buscas.

---

## Desenvolvimento e testes

Este repositório já contém um _template_ com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Há também o diretório `statics` que contém os arquivos necessários para realização de testes, caso julgue necessário, sinta-se à vontade para criar novos arquivos ou editar o conteúdo dos arquivos existentes. Veja abaixo:

```md
.
├── statics
│   ├── arquivo_teste.txt
│   ├── novo_paradigma_globalizado.txt
│   └── novo_paradigma_globalizado-min.txt
├── tests
├── ting_file_management
│   ├── file_management.py
│   └── file_process.py
├── ting_word_searches
│   └── word_search.py
├── README.md
├── requirements.txt
└── setup.cfg
```

Apesar do projeto já possuir uma estrutura base, você quem deve implementar tanto as funções quanto os testes (_extra_). Novos arquivos podem ser criados conforme a necessidade.

Para executar os testes, lembre-se de primeiro **criar e ativar o ambiente virtual**, além de também instalar as dependências do projeto. Isso pode ser feito através dos comandos:

```bash
$ python3 -m venv .venv

$ source .venv/bin/activate

$ python3 -m pip install -r requirements.txt
```

O arquivo `requirements.txt` contém todos as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`. Com as dependências já instaladas, para executar os testes basta usar o comando:

```bash
$ python3 -m pytest
```

Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse artigo: https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1

Para verificar se você está seguindo o guia de estilo do Python corretamente, execute o comando:

```bash
$ python3 -m flake8
```

---

## Requisitos obrigatórios:

### Pacote `ting_file_management`

#### 1 - Deve haver uma função `txt_importer` dentro do módulo `file_management` capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador. Todas as mensagens de erro devem ir para a `stderr`.

**Exemplo simples de um arquivo txt a ser importado:**

```md
Acima de tudo,
é fundamental ressaltar que a adoção de políticas descentralizadoras nos obriga
à análise do levantamento das variáveis envolvidas.
```

Ao importar um arquivo, ele será adicionado a uma fila. Com isso, ele deve ganhar um identificador (`posicao`) que representa a posição dele na fila. Ou seja, se importarmos o arquivo `teste1.txt`, ele ficará na posição 1 da fila, assim consecutivamente nos demais arquivos.

##### As seguintes verificações serão feitas:

- Caso o arquivo TXT não exista, deve ser exibida a mensagem: "`Arquivo {path_file} não encontrado`";

- Retorno das informações igual ao exemplo abaixo;

- Caso a extensão do arquivo seja diferente de `.txt`, deve ser exibida uma mensagem: "`Formato inválido`".

#### 2 - Deve haver uma função `process` dentro do módulo `file_process` capaz de ler o arquivo carregado na função anterior e efetuar o preprocessamento do conteúdo.

> Observação: ao processar um novo arquivo na fila, o módulo deve ser capaz de retornar informações relacionadas ao arquivo, sendo elas: `nome do arquivo`, `quantidade de linhas` e a `posição do arquivo` dentro da estrutura. 

**Exemplo de retorno**:

```python
{
    "nome_do_arquivo": "arquivo_teste.txt", # Nome do arquivo recém adicionado
    "qtd_linhas": 3,                        # Quantidade de linhas existentes no arquivo
    "posicao": 1                            # Posição do arquivo dentre os demais arquivos adicionados (iniciando em 1)
}
```

##### As seguintes verificações serão feitas:

- Por padrão deve-se ignorar arquivos com o mesmo nome;

- Não deve haver limites de linhas a serem analisadas;

- Em caso de erros, a importação deve ser interrompida e a posição deve ficar disponível para uma nova inserção;

- O exemplo de saída acima deve ser emitido após cada nova inserção válida, via `stdout`.

#### 3 - Deve haver uma função `remove` dentro do módulo `file_process` capaz de remover o primeiro arquivo processado

> Observação: ao remover um arquivo da fila, o módulo deve ser capaz de decrementar a quantidade de arquivos da estrutura.

##### As seguintes verificações serão feitas:

- Por padrão deve-se ignorar a operação caso não hajam arquivos;

- Em caso de erros, a remoção deve ser interrompida e os itens não devem ser alterados, mantendo a imutabilidade da estrutura;

- Em caso de sucesso de remoção, deve ser emitido a mensagem: "`Arquivo {path_file} removido com sucesso`".

#### 4 - Deve haver uma função `file_metadata` dentro do módulo `file_process` capaz de apresentar as informações superficiais dos arquivos processados.

##### As seguintes verificações serão feitas:

- Baseado na posição informada, deve ser apresentado as informações relacionadas ao arquivo, parecido com o apresentado abaixo;

- Em caso da posição não existir, deve ser exibida uma mensagem de erro: "`Posição inválida`" na `stderr`.

**Exemplo de retorno**:

```python
{
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 3,
    "posicao": 1
}
```

### Pacote `ting_word_searches`

#### 5 - Deve haver uma função `exists_word` dentro do módulo `word_search`, que valide a existência da palavra em todos os arquivos processados. Para cada palavra encontrada, deve-se listar sua linha conforme apresentação abaixo.

##### As seguintes verificações serão feitas:

- A busca deve ser _case insensitive_ e deve retornar uma lista no formato:

```json
[{
  "palavra": "de",
  "arquivo": "arquivo_teste.txt",
  "ocorrencias": [
    {
      "linha": 1
    },
    {
      "linha": 2
    }
  ]
}]
```

- Caso a palavra não seja encontrada em nenhum arquivo, deve-se retornar uma lista vazia.

#### 6 - Deve haver uma função `search_by_word` dentro do módulo `word_search`, que busque a palavra em todos os arquivos processados. Para cada palavra encontrada, deve-se listar sua linha, o conteúdo e o arquivo da ocorrência.

##### As seguintes verificações serão feitas:

- A busca deve ser _case insensitive_ e deve retornar uma lista no formato:

```json
[{
  "palavra": "de",
  "arquivo": "arquivo_teste.txt",
  "ocorrencias": [
    {
      "linha": 1,
      "conteudo": "Acima de tudo,"
    },
    {
      "linha": 2,
      "conteudo": "é fundamental ressaltar que a adoção de políticas descentralizadoras nos obriga"
    }
  ]
}]
```

- Caso a palavra não seja encontrada em nenhum arquivo, deve-se retornar uma lista vazia.

---
