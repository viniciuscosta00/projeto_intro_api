from flask import Blueprint, request, jsonify
from controllers.tarefa_controller import TarefaController

tarefas_bp = Blueprint('tarefas', __name__)

@tarefas_bp.route('/tarefas', methods=['GET'])
def get_listar_tarefas():
    return jsonify([tarefa.to_dict() for tarefa in TarefaController.get_listar_tarefas()])

@tarefas_bp.route('/api/cria_tarefas', methods=['POST'])
def criar_tarefa():
    dados = request.get_json()
    id = dados.get_json()