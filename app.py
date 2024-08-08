from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# URL da Random User API
API_URL = 'https://randomuser.me/api/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/colaboradores')
def employees():
    # Obtendo o número da página a partir dos parâmetros da URL
    page = int(request.args.get('page', 1))
    results_per_page = 20

    # Fazendo a requisição GET à API
    response = requests.get(API_URL, params={'results': 100})
    data = response.json()

    # Extraindo a lista de usuários
    users = data.get('results', [])

    # Paginação
    start = (page - 1) * results_per_page
    end = start + results_per_page
    paginated_users = users[start:end]

    total_pages = (len(users) + results_per_page - 1) // results_per_page 

    # Passando os dados para o template
    return render_template(
        'employees.html',
        users=paginated_users,
        page=page,
        total_pages=total_pages
    )

if __name__ == '__main__':
    app.run(debug=True)
