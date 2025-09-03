from flask import Blueprint, request, jsonify
from controllers.tarefa_controller import TarefaController

tarefas_bp = Blueprint('tarefas', __name__)

@tarefas_bp.route('/api/tarefas', methods=['GET'])
def get_listar_tarefas():
    return jsonify([tarefa.to_dict() for tarefa in TarefaController.get_listar_tarefas()])

@tarefas_bp.route('/api/criar_tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()
    id = dados.get_json()
    titulo = dados.get('titulo')
    concluida = dados.get('concluida', False)
    nova_tarefa = TarefaController.criar_tarefa(id, {id}, {'titulo': titulo}, concluida)
    return jsonify(nova_tarefa.to_dict()), 201
