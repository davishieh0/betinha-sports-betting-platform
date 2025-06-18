# 🔐 Implementação de Hash de Senhas - CRÍTICO

## ⚠️ PROBLEMA CRÍTICO IDENTIFICADO

**As senhas dos usuários estão sendo armazenadas em TEXTO PLANO no banco de dados!**

Isso é uma vulnerabilidade de segurança crítica que permite que qualquer pessoa com acesso ao banco de dados veja todas as senhas dos usuários.

## 🛠️ SOLUÇÃO OBRIGATÓRIA

### 1. Instalar a biblioteca de hash
Adicione ao `requirements.txt`:
```
bcrypt==4.0.1
```

### 2. Código para hash de senhas

Adicione estas funções ao início do `app.py`:

```python
import bcrypt

def hash_password(password):
    """Cria um hash da senha usando bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password, hashed):
    """Verifica se a senha corresponde ao hash"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
```

### 3. Modificar o registro de usuários

**ANTES (INSEGURO)**:
```python
cursor.execute('INSERT INTO usuarios VALUES (%s, %s, %s, %s, %s, %s)', 
               (None, admin, name, email, password, birth))
```

**DEPOIS (SEGURO)**:
```python
hashed_password = hash_password(password)
cursor.execute('INSERT INTO usuarios VALUES (%s, %s, %s, %s, %s, %s)', 
               (None, admin, name, email, hashed_password, birth))
```

### 4. Modificar a autenticação

**ANTES (INSEGURO)**:
```python
cursor.execute('SELECT * FROM usuarios WHERE email = %s AND senha = %s', (email, password))
```

**DEPOIS (SEGURO)**:
```python
cursor.execute('SELECT * FROM usuarios WHERE email = %s', (email,))
account = cursor.fetchone()
if account and verify_password(password, account[4]):  # account[4] é a senha hasheada
    # Login bem-sucedido
```

### 5. Script de migração das senhas existentes

⚠️ **ATENÇÃO**: Execute este script UMA VEZ para converter senhas existentes:

```python
import mysql.connector
import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def migrate_passwords():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    
    cursor = connection.cursor()
    
    # Buscar todos os usuários
    cursor.execute('SELECT id, senha FROM usuarios')
    users = cursor.fetchall()
    
    for user_id, plain_password in users:
        # Converter senha para hash
        hashed_password = hash_password(plain_password)
        
        # Atualizar no banco
        cursor.execute('UPDATE usuarios SET senha = %s WHERE id = %s', 
                      (hashed_password, user_id))
    
    connection.commit()
    cursor.close()
    connection.close()
    print(f"Migradas {len(users)} senhas com sucesso!")

# Execute apenas uma vez:
# migrate_passwords()
```

## 🚨 AÇÃO IMEDIATA NECESSÁRIA

1. **PARE** o servidor em produção imediatamente
2. Implemente as mudanças de hash de senhas
3. Execute o script de migração
4. Teste completamente o login
5. Só então coloque de volta em produção

## 📋 Checklist de Implementação

- [ ] bcrypt adicionado aos requirements.txt
- [ ] Funções hash_password e verify_password criadas
- [ ] Registro de usuários modificado para usar hash
- [ ] Login modificado para verificar hash
- [ ] Script de migração executado (UMA VEZ)
- [ ] Testes de login realizados
- [ ] Sistema validado em produção

## ⚠️ IMPORTANTE

**NUNCA** armazene senhas em texto plano. Esta é uma das vulnerabilidades mais básicas e perigosas em aplicações web.

Após implementar esta correção, mesmo se alguém acessar o banco de dados, não conseguirá ver as senhas reais dos usuários.
