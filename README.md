# Projeto de Extração de Texto de Notícias

Este projeto tem como objetivo extrair o texto de notícias de URLs armazenadas em um banco de dados MySQL, utilizando ferramentas como `requests`, `BeautifulSoup`, e `Playwright`. O processo é automatizado para ser executado periodicamente, utilizando o `schedule` para executar a tarefa a cada 5 horas.

## Funcionalidades

- Conexão com o banco de dados MySQL para buscar URLs de notícias que ainda não possuem texto extraído.
- Extração do conteúdo das páginas de notícias utilizando `requests`, `BeautifulSoup` ou `Playwright`.
- Atualização do banco de dados com o texto extraído das notícias.
- Execução periódica do processo a cada 5 horas, utilizando a biblioteca `schedule`.

## Tecnologias Utilizadas

- **Python 3.x**
- **MySQL** para banco de dados.
- **requests** para requisições HTTP.
- **BeautifulSoup** para extração de conteúdo HTML.
- **Playwright** para extração de conteúdo de páginas dinâmicas.
- **schedule** para agendar a execução periódica do processo.
- **python-dotenv** para gerenciar as variáveis de ambiente a partir de um arquivo `.env`.

## Instalação

1. Inicie o ambiente:

   ```bash
   uv venv
   .venv\Scripts\activate
   ```

2. Instale os módulos:

   ```bash
   uv add
   ```

3. Rode o projeto:
   ```bash
   python app.py
   ```
