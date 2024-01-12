# Kenzie Buster
A linguagem utilizada é o Python e o framework Django. O Banco de dados utilizado é o sqlite3.    
Essa API tem o intuito de fazer uma gestão de vendas de filmes. A aplicação gerencia usuários, filmes e compras, incluindo autenticação e permissões de rotas para diferentes tipos de usuário.   

| Rotas                        | Verbo HTTP | Objetivo                         |
|------------------------------|------------|----------------------------------|
| /api/users/                  | POST       | Criação de usuário               |
| /api/users/login/            | POST       | Autenticação do usuário          |
| /api/users/<int:user_id>/    | GET        | Busca de usuário por ID          |
| /api/users/<int:user_id>/    | PATCH      | Atualizar usuário                |
| /api/movies/                 | POST       | Criação de filme                 |
| /api/movies/                 | GET        | Listagem de filme                |
| /api/movies/<int:movie_id>/  | GET        | Busca de filme por ID            |
| /api/movies/<int:movie_id>/  | DELETE     | Deleção de filme                 |
| /api/movies/<int:movie_id>/orders/ | POST  | Criação de pedido   

## Configuração do Ambiente Virtual (Opcional, mas recomendado)
### Crie um ambiente virtual
```python -m venv venv```

### Ative o ambiente virtual
#### No Windows
```venv\Scripts\activate```
#### No Linux/Mac
```source venv/bin/activate```


## Instalar o Django:
```pip install django```

## Instalação das Dependencias
```pip install -r requirements.txt```

## Migrações e Aplicações
### Execute as migrações
```python manage.py makemigrations```
```python manage.py migrate```

### Inicie o servidor de desenvolvimento
```python manage.py runserver```


## Preparando ambiente para execução dos testes

1. Verifique se os pacotes **pytest**, **pytest-testdox** e/ou **pytest-django** estão instalados globalmente em seu sistema:
```shell
pip list
```

2. Caso eles apareçam na listagem, rode os comandos abaixo para realizar a desinstalação:

```shell
pip uninstall pytest pytest-testdox pytest-django -y
```

3. Após isso, crie seu ambiente virtual:
```shell
python -m venv venv
```

4. Ative seu ambiente virtual:

```shell
# Linux e Mac:
source venv/bin/activate

# Windows (PowerShell):
.\venv\Scripts\activate

# Windows (GitBash):
source venv/Scripts/activate
```

5. Instale as bibliotecas necessárias:

```shell
pip install pytest-testdox pytest-django
```

## Execução dos testes:


- Tarefa 1:
```python
pytest --testdox -vvs tests/tarefas/t1/
```

- Tarefa 2:
```python
pytest --testdox -vvs tests/tarefas/t2/
```

- Tarefa 3:
```python
pytest --testdox -vvs tests/tarefas/t3/
```

- Tarefa 4:
```python
pytest --testdox -vvs tests/tarefas/t4/
```
---

Você também pode rodar cada método de teste isoladamente:

```shell
pytest --testdox -vvs caminho/para/o/arquivo/de/teste::NomeDaClasse::nome_do_metodo_de_teste
```

**Exemplo**: executar somente "test_user_login_without_required_fields".

```shell
pytest --testdox -vvs tests/tarefas/t2/users/t2_user_views_test.py::UserLoginViewsT2Test::test_user_login_without_required_fields
```
--- 

Para executar todos os testes:
```shell
pytest --testdox -vvs
```