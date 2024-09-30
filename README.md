# Sistema de Gerenciamento de Carros

Primeiramente, uma agradecimento ao adm do PycodeBR, que proporcionou o conhecimento necessário para a criação desse projeto através do Django MASTER. Todos os créditos e direitos reservados a ele.


Um sistema desenvolvido em Django para o gerenciamento de carros, incluindo um front-end para interação do usuário.


## Desenvolvido Em
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" title="Python" alt="Python" width="40" height="40"/>



## Funcionalidades

- Cadastro de carros (marca, modelo, ano, etc...)
- Listagem de carros cadastrados
- Atualização e exclusão de carros
- Interface intuitiva para facilitar a gestão de veículos

## Tecnologias Utilizadas

- **Backend**: Django 4.x
- **Frontend**: HTML, CSS, JavaScript 
- **Banco de Dados**: SQLite (ou MySQL, PostgreSQL, etc.)


## Pré-requisitos

Antes de rodar o projeto, você precisará ter as seguintes ferramentas instaladas:

- [Python 3.12.2](https://www.python.org/downloads/)
- [Django 4.x](https://www.djangoproject.com/download/)
- [Git](https://git-scm.com/)

## Como Rodar o Projeto Localmente

1. Clone o repositório:
    ```bash
    git clone https://github.com/AmrmDev/Gestao-de-Carros
    ```
2. Acesse a pasta do projeto:
    ```bash
    cd Gestao-de-Carros
    ```
3. Crie e ative um ambiente virtual:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # No Windows: .venv\Scripts\activate
    ```
4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
5. Faça as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```
6. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

7. Acesse o projeto no navegador:
    ```
    http://localhost:8000
    ```

## Estrutura do Projeto

- `app/` - Aplicações Django relacionadas ao gerenciamento de carros
- `templates/` - Arquivos HTML do front-end
- `static/` - Arquivos estáticos (CSS, JS, imagens)
- `models.py` - Modelos do banco de dados
- `views.py` - Lógica de controle das páginas
- `urls.py` - Configurações de roteamento

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um [issue](https://github.com/usuario/nome-do-repositorio/issues) ou enviar um pull request.

