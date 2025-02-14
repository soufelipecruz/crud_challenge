# crud_challenge

## Sobre o Projeto
Este projeto é uma aplicaçao web simples de lista de tarefas (**To-Do List**) construida com **Flask**, **SQLAlchemy** e **SQLite** no backend, e uma intrface simples HTML no frontend. Ele permite criar, visualizar, atualizar e excluir.

## tecnologias utilizadas
- **Python** (Flask para o backend)
- **Flask-SQLAlchemy** (para gerenciamento do banco de dados SQLite)
- **HTML + CSS** (para interface básica do usuário)

## funcionalidades
A aplicação segue o modelo **CRUD**:

1. **Criar (Creat)**: Permite adicionar uma nova tarefa com um nome e uma descrição.
2. **Ler (Read)**: Lista todas as tarefas salvas no banco de dados.
3. **Atualizar (Update)**: Permite modificar o nome e a descrição de uma tarefa existente.
4. **Deletar (Delete)**: Remove uma tarefa do banco de dados.

## estrutura do projeto

```
📂 projeto-todo
│── 📄 app.py              
│── 📄 banco_dados.db      
│── 📂 templates
│   └── 📄 index.html     
│── 📄 requirements.txt   
│── 📄 README.md           
```

---

##  como executar o projeto

### instalar as dependencias
Crie um ambiente virtual e instale as bibliotecas necessárias:

```sh
pip install flask flask_sqlalchemy
```

### executar o servidor
Inicie a aplicação Flask:

```sh
python app.py
```

O servidor será iniciado na porta **5153** e poderá ser acessado via:

```
http://127.0.0.1:5153/
```

---

## backend - flask
O backend é responsável por gerenciar o banco de dados e processar as requisições da interface.

### **banco de dados (sqlite + SQLAlchemy)**
O banco de dados é um SQLite gerenciado pelo QLAlchemy. O modelo de dados é definido na classe `Tarefas`:

```python
class Tarefas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
```
- `id`: Identificador único de cada tarefa.
- `nome`: Nome da tarefa.
- `descricao`: Descrição detalhada da tarefa.

### **rotas da API**
Abaixo estão as rotas do Flask para gerenciar as tarefas:

#### **para visualizar todas as tarefas (Read)**
```python
@app.route('/')
def index():
    tasks = Tarefas.query.all()
    return render_template('index.html', tasks=tasks)
```
- Busca todas as tarefas no banco e as exibe na página inicial.

#### **para adicionar uma nova tarefa (Create)**
```python
@app.route('/create', methods=['POST'])
def create_tarefa():
    nome = request.form['nome']
    descricao = request.form['descricao']
    new_task = Tarefas(nome=nome, descricao=descricao)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')
```
- Recebe os dados do formulário HTML e adiciona uma nova tarefa no banco.

#### **para atualizar uma tarefa existente (update)**
```python
@app.route('/update/<int:tarefa_id>', methods=['POST'])
def update_tarefa(tarefa_id):
    task = Tarefas.query.get(tarefa_id)
    if task:
        task.nome = request.form['nome']
        task.descricao = request.form['descricao']
        db.session.commit()
    return redirect('/')
```
- busc a tarefa pelo ID e atualiza os campos `nome` e `descricao`.

#### ** excluir uma tarefa (delete)**
```python
@app.route('/delete/<int:tarefa_id>', methods=['POST'])
def delete_tarefa(tarefa_id):
    task = Tarefas.query.get(tarefa_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect('/')
```
- Remove uma tarefa específica do banco de dados.

---

## frontend -> HTML + CSS
O frontend é um simples arquivo **index.html** dentro da pasta `templates/`, que exibe a lista de tarefas e permite adicionar, editar e excluir tarefas.

### **interface principal e única**
```html
<form action="/create" method="POST">
    <label for="nome">Nome da tarefa:</label>
    <input type="text" name="nome" required>
    <label for="descricao">Descrição da tarefa:</label>
    <input type="text" name="descricao" required>
    <button type="submit">Criar tarefa</button>
</form>
```
- Formulário para adicionar uma nova tarefa.

### **lista de tarefas**
```html
<ul>
    {% for task in tasks %}
        <li>
            <form action="/update/{{task.id}}" method="POST">
                <input type="text" name="nome" value="{{task.nome}}">
                <input type="text" name="descricao" value="{{task.descricao}}">
                <button type="submit">Atualizar</button>
            </form>
            <form action="/delete/{{task.id}}" method="POST">
                <button type="submit">Deletar</button>
            </form>
        </li>
    {% endfor %}
</ul>
```
- Vai exibir a lista de tarefas.
- Para permitir atualizar ou excluir cada tarefa.






