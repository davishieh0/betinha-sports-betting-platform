from flask import Flask, render_template, request, redirect, session, flash, url_for

class Usuario:
    def __init__(self, nome, email, senha, data_nascimento, saldo, moderador="N"):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.data_nascimento = data_nascimento
        self.saldo = saldo
        self.moderador = moderador

usuario_master = Usuario('Betinha','betinha777@gmail.com','Betinha123',None,99999999,'S')

usuario_login = {usuario_master.email: usuario_master}
#Definindo o email e infos para o login
lista_users=[usuario_master]

class Evento:
    def __init__(self, titulo, valor_cota,hora_inicio,hora_fim):
        self.titulo = titulo
        self.valor_cota = valor_cota
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim

lista_eventos = []
lista_eventos_aprovados = []

app = Flask(__name__)
app.secret_key = 'betinhaPapaGrana'  # Necessário para usar sessões e flashes

@app.route('/')
def index():
    return render_template('index.html',lista=lista_eventos)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route('/criar_user',methods=['POST', ])
def criar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    data_nascimento = request.form['data_nascimento']
    saldo = request.form['saldo']

     
    if not nome or not email or not senha or not data_nascimento or not saldo:
        flash('Todos os campos são obrigatórios!')
        return redirect(url_for('cadastro'))
    
    usuario = Usuario(nome,email,senha,data_nascimento,saldo)
    lista_users.append(usuario)
    usuario_login[email] = usuario  # Adiciona ao dicionário de login

    return redirect('/')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima = proxima)

@app.route('/autenticar',methods=['POST', ]) 
def autenticar():
    email = request.form['email']
    senha = request.form['senha']
    proxima_pagina = request.form['proxima']
    if email in usuario_login:
        if senha == usuario_login[email].senha:
            #Parte mais chata de entender 
            session['usuario'] = email
            flash(f'{email} foi logado com sucesso!')
            return redirect((proxima_pagina))
    else:
        flash(f'Email ou senha incorretos')
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session['usuario'] = None
    flash('Deslogado com sucesso!')
    return redirect(url_for('index'))


@app.route('/novo_evento')
def novo_evento():
    if 'usuario' not in session or session ['usuario'] == None:
        return redirect (url_for('login',proxima=url_for('novo_evento')))
    return render_template('novo_evento.html')


@app.route('/criar_evento',methods=['POST', ])
def criar_evento():
    titulo = request.form['titulo']
    valor_cota = request.form['valor_cota']
    hora_inicio = request.form['hora_inicio']
    hora_fim = request.form['hora_fim']

    evento = Evento(titulo,valor_cota,hora_inicio,hora_fim)
    lista_eventos.append(evento)

    return redirect (url_for('index'))

app.run(debug=True)

