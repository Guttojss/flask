from flask import Flask, request,url_for,render_template,redirect,session
from markupsafe import escape
# app 
app = Flask(__name__,static_folder='static',static_url_path='')
'''
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
    return 'Vá á rota /index.html. Falta fazer : APIs with JSON etc.'

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

# Executando o contexto de teste para gerar URLs
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe')) #dá print na consola (tenho q ir ver)


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

with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'


@app.route('/upload',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['note.txt']
        file.save("note.txt")

@app.route('/')
def index():
    username = request.cookies.get('username')
    return redirect('static/index.html') #Não Funciona
Aparece uma coisa na Consola qnd se dá F5'''

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('logged'))
    return render_template('loggin.html')

@app.route('/logged')
def logged():
    if 'username' in session:
        return render_template('logged.html',name=session['username'])
    return 'You are not logged in'

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))