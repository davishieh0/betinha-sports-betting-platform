# 🚀 Checklist OBRIGATÓRIO - Antes de Enviar ao GitHub

## 🔴 AÇÕES CRÍTICAS (OBRIGATÓRIAS)

### 1. 🔐 Implementar Hash de Senhas (CRÍTICO!)
**Status**: ❌ NÃO IMPLEMENTADO - VULNERABILIDADE CRÍTICA!

**O que fazer**:
```bash
# 1. Instalar bcrypt
pip install bcrypt==4.0.1

# 2. Adicionar ao app.py (no início, após os imports):
```

```python
import bcrypt

def hash_password(password):
    """Cria um hash da senha usando bcrypt"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password, hashed):
    """Verifica se a senha corresponde ao hash"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
```

**Modificar linha ~174 em app.py**:
```python
# ANTES (INSEGURO)
cursor.execute('INSERT INTO usuarios VALUES (%s, %s, %s, %s, %s, %s)', (None, admin, name, email, password, birth))

# DEPOIS (SEGURO)
hashed_password = hash_password(password)
cursor.execute('INSERT INTO usuarios VALUES (%s, %s, %s, %s, %s, %s)', (None, admin, name, email, hashed_password, birth))
```

### 2. 🔒 Remover Arquivo .env do Repositório
**Status**: ⚠️ ARQUIVO .env PRESENTE - RISCO DE VAZAR CREDENCIAIS!

```bash
# Remover .env do tracking do git
git rm --cached .env

# Verificar se .gitignore está correto
cat .gitignore  # deve conter .env
```

### 3. 📝 Atualizar .env.example
**Status**: ✅ CRIADO, mas precisa verificar

Garantir que `.env.example` não contenha credenciais reais:
```env
# Configurações do Banco de Dados
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=SUA_SENHA_AQUI
DB_NAME=bd_betinha

# Chave secreta da aplicação
SECRET_KEY=GERE_UMA_CHAVE_FORTE_AQUI

# Configurações de Email
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=465
MAIL_USE_TLS=False
MAIL_USE_SSL=True
MAIL_USERNAME=seu_email@gmail.com
MAIL_PASSWORD=sua_senha_de_app_gmail
```

## 🟡 AÇÕES RECOMENDADAS (Fortemente Sugeridas)

### 4. 🗂️ Limpar Arquivos Desnecessários
```bash
# Remover arquivos antigos/desnecessários
git rm betinha.py plan.md templates/cadastro.html templates/novo_evento.html

# Adicionar novos arquivos importantes
git add .gitignore .env.example requirements.txt SECURITY.md
git add app.py templates/ static/
```

### 5. 📚 Atualizar README.md
Adicionar seção de segurança e instalação:

```markdown
## 🔧 Instalação e Configuração

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/betinha-sports-betting-platform.git
cd betinha-sports-betting-platform
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações reais
```

### 4. Configurar banco de dados
```sql
-- Execute os scripts de criação do banco
-- (adicione aqui os scripts SQL necessários)
```

## 🔐 Segurança
- ✅ Credenciais protegidas em variáveis de ambiente
- ✅ Chaves secretas não expostas no código
- ⚠️ Implementar hash de senhas (bcrypt)
- ⚠️ Configurar HTTPS em produção
```

### 6. 🗃️ Criar Script SQL de Setup
Criar arquivo `database/setup.sql` com a estrutura do banco:

```sql
-- Adicione aqui os CREATE TABLE necessários
-- para que outros desenvolvedores possam recriar o banco
```

## 🟢 AÇÕES OPICIONAIS (Melhorias)

### 7. 🔧 Arquivo de Configuração de Desenvolvimento
Criar `config.py`:
```python
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    # Database
    DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME', 'bd_betinha')
    
    # Mail
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', '465'))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'False').lower() == 'true'
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', 'True').lower() == 'true'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
```

### 8. 🧪 Adicionar Arquivo de Teste
Criar `test_basic.py`:
```python
import unittest
from app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```

## 📋 CHECKLIST FINAL

**ANTES DE FAZER git push:**

- [ ] **CRÍTICO**: Hash de senhas implementado
- [ ] **CRÍTICO**: Arquivo .env removido do git (`git rm --cached .env`)
- [ ] **CRÍTICO**: .env.example sem credenciais reais
- [ ] **CRÍTICO**: .gitignore configurado corretamente
- [ ] Arquivos desnecessários removidos
- [ ] requirements.txt atualizado
- [ ] README.md atualizado com instruções
- [ ] SECURITY.md revisado
- [ ] Teste local funcionando

## 🚨 COMANDO PARA COMMIT SEGURO

```bash
# 1. Verificar o que será commitado
git status

# 2. Adicionar arquivos (SEM O .env!)
git add .gitignore .env.example requirements.txt SECURITY.md app.py templates/ static/ README.md

# 3. Remover arquivos sensíveis se necessário
git rm --cached .env

# 4. Commit
git commit -m "feat: implementa segurança e remove credenciais hardcoded

- Adiciona hash de senhas com bcrypt
- Move credenciais para variáveis de ambiente
- Adiciona .gitignore para proteger arquivos sensíveis
- Atualiza documentação de segurança
- Remove arquivos desnecessários"

# 5. Push (APENAS APÓS VERIFICAR TUDO)
git push origin master
```

## ⚠️ LEMBRETE FINAL

**NUNCA faça push sem implementar o hash de senhas!** 
Isso é uma vulnerabilidade crítica que expõe todos os usuários.
