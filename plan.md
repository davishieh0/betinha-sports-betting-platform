/novo eventos -> /login -> /autenticar -> url(/novo eventos)

variável próxima atribui o url
envio via request.form
redirect proxima


Passo a passo fluxo de url's

1. determinar caminho

/novo_evento -> /login -> /autenticar -> /novo_evento

2. fluxo:
## /novo_evento
```py
@app.route('/novo_evento')
def novo_evento():
    if 'usuario' not in session or session ['usuario'] == None:
        return redirect (url_for('login',proxima=url_for('novo_evento')))
    return render_template('novo_evento.html')

```
## /login
```py
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima = proxima)

```

## login.html
```html
 <input type="hidden" name="proxima" value="{{proxima}}">
 ```

 ## /autenticar
 ```py
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
 ```
