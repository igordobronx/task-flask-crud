from flask import Flask, request, jsonify
from models.task import Task
# __name__ __main__
app = Flask(__name__)

#CRUD
#CREATE, READ, UPDATE, DELETE

tasks = []
task_id_control = 1
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control #declara a variavel no metodo
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"mensagem": "tarefa criada com sucesso"}) #o servidor deve retornar json ou YAML

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    
    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)


@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"message": "nao foi possivel encontrar a ativdade"}), 404

@app.route('/user/<username>') #para criacao de variaveis, deixe-as no entre de <>
def show_user(username):
    print(username)
    print(type(username))
    return username
#olhar documentacao do flask sobre conversão de variáveis
#https://flask.palletsprojects.com/en/stable/quickstart/#variable-rules


@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)

    if task == None:
        return jsonify({"message":  "n foi posivel encontrar a atividade"}), 404

    data = request.get_json() #atualizando os dados
    task.title = data['title']
    task.completed = data['completed']
    task.description = data['description']
    print(task)
    return jsonify({"message": "tarefa atualizada com sucesso"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    for t in tasks:
        if t.id == id:
            task = t
            break
    
    if not tasks:
        return jsonify({"message": "nao foi possivel encontrar a atividade"}), 404

    tasks.remove(task)
    return jsonify({"message": "tarefa deletada com sucesso"})



#para executar agora (nao usar para clientes reais):
if __name__ == "__main__":
    app.run(debug=True)