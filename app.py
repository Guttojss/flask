
from flask import Flask, request,url_for,render_template
from markupsafe import escape
# app 
app = Flask(__name__,static_folder='static',static_url_path='')

# Definindo a função para fazer o login
def show_info():  # erro
    return f'Logged as Desconhecido!'

    # Definindo a função para mostrar o formulário de login
def check_info(info):
    if(info == 'rodrigo'):
        return f'Logged as {info}'
    else :
        return show_info()

# Página inicial
@app.route('/')
def pag():
    return 'Vá á rota /index.html'

# Página de projectos
@app.route('/projects/')
def projects():
    return 'The project page'

# Página de About
@app.route('/about')
def about():
    return 'The about page'

# Rota de hello
@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'
'''
# Executando o contexto de teste para gerar URLs
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe')) #dá print na consola (tenho q ir ver)
'''

# Rota de exibição de postagem
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'

# Rota de exibição de subcaminho
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {escape(subpath)}'

# Rota de login (GET e POST)
@app.route('/login/<info>', methods=['GET', 'POST'])
def login(info):
    if request.method == 'GET':
        return check_info(info)
        
