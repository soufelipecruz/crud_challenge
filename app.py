from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco_dados.db'
db = SQLAlchemy(app)

class Tarefas(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50), nullable = False)
    descricao = db.Column(db.Text, nullable = False)

# Read
@app.route('/')
def index():
    tasks = Tarefas.query.all()
    return render_template('index.html', tasks=tasks)

#Create
@app.route('/create', methods=['POST'])
def create_tarefa():
    nome = request.form['nome']
    descricao = request.form['descricao']
    new_task = Tarefas(nome= nome, descricao = descricao)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

# Delete
@app.route('/delete/<int:tarefa_id>', methods=['POST'])
def delete_tarefa(tarefa_id):
    task = Tarefas.query.get(tarefa_id)

    if task: 
        db.session.delete(task)
        db.session.commit()
    return redirect('/')
    
# update 
@app.route('/update/<int:tarefa_id>', methods=['POST'])
def update_tarefa(tarefa_id):
    task = Tarefas.query.get(tarefa_id)

    if task:
        task.nome = request.form['nome']
        task.descricao = request.form['descricao']
        db.session.commit()
    return redirect('/')



if __name__ == '__main__':
    with app.app_context():
        db.create_all()


    app.run(debug=True, port=5153)