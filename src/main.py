from flask import Flask, render_template, request, jsonify
from APIService import ApiService
from Endereco import Endereco

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/procurar-cep', methods=['POST'])
def procurar_cep():
    cep = request.form['cep']
    service = ApiService()
    endereco = service.procurar_cep(cep)

    if endereco:
        return jsonify({
            'logradouro': endereco['logradouro'],
            'bairro': endereco['bairro'],
            'cidade': endereco['localidade'],
            'estado': endereco['uf']
        })
    else:
        return jsonify({'error': 'CEP não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)