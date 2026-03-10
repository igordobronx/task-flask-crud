import pytest
import requests

BASE_URL = "http://127.0.0.1:5000"
tasks = []

#teste pra criar
def test_create_task():
    new_task_data = {
        "title": "nova tarefa",
        "description": "descricao da nova tarefa"
    } 
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200 #usa assert para validar se o codigo é 200 (pytest)
    response_json = response.json()
    assert "mensagem" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])

#teste pra ler
def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get_task(): #pega tarefa especifica
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json['id']

#patch / put
def test_update_task():
     if tasks:
        task_id = tasks[0]
        payload = {
            "completed": True,
            "description": "nova descricao",
            "title": "titulo atualizado"
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
        response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        #nova requisicao a tarefa especifica
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert response_json["title"] == payload["title"]
        assert response_json["description"] == payload["description"]

def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        response.status_code == 200

        #quando eu deletar a tarefa, ela obrigatoriamente deve nao existir(retornar 404 no get) pois foi deletada
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404
