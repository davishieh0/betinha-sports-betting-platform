# 🎲 Betinha Sports Betting Platform

Uma plataforma completa de apostas esportivas desenvolvida com Flask e Python, oferecendo um ambiente seguro e intuitivo para apostadores e administradores.

## 📋 Sobre o Projeto

**Betinha Sports Betting Platform** é uma aplicação web full-stack que permite aos usuários participar de eventos de apostas esportivas de forma segura e organizada. A plataforma conta com sistema robusto de autenticação, gestão financeira, moderação de eventos e interface responsiva.

### 🏆 Principais Características

- **🔐 Autenticação Segura**: Sistema de login com hash bcrypt
- **💰 Gestão Financeira**: Carteira digital com depósitos e saques
- **🎯 Eventos Dinâmicos**: Criação e aprovação de eventos de apostas
- **👥 Sistema de Moderação**: Painel administrativo completo
- **📧 Notificações**: Sistema de email integrado
- **🛡️ Segurança Avançada**: Proteção de dados e credenciais

## 🚀 Tecnologias Utilizadas

### Backend
- **Python 3.x** - Linguagem principal
- **Flask 2.3.3** - Framework web
- **MySQL** - Banco de dados relacional
- **bcrypt** - Hash seguro de senhas
- **Flask-Mail** - Sistema de emails

### Frontend
- **HTML5** - Estrutura das páginas
- **CSS3** - Estilização responsiva
- **JavaScript** - Interatividade do cliente

### Segurança
- **python-dotenv** - Gestão de variáveis de ambiente
- **Hash bcrypt** - Proteção de senhas
- **Validação de entrada** - Prevenção de ataques
- **Sessões seguras** - Controle de autenticação

## ⚙️ Funcionalidades Completas

### 👤 Sistema de Usuários
- **Cadastro Completo**: Validação de dados e verificação de email
- **Login Seguro**: Autenticação com hash bcrypt
- **Gestão de Perfil**: Edição de informações pessoais
- **Controle de Sessão**: Logout seguro e gestão de sessões

### 💳 Sistema Financeiro
- **Carteira Digital**: Saldo em tempo real
- **Depósitos**: Sistema de recarga de créditos
- **Saques**: Processamento com taxas progressivas
- **Histórico**: Rastreamento completo de transações
- **Limite Diário**: Controle de saques por segurança

### 🎯 Gestão de Eventos
- **Criação de Eventos**: Interface intuitiva para novos eventos
- **Categorização**: Organização por modalidades esportivas
- **Sistema de Cotas**: Cálculo automático de odds
- **Período de Apostas**: Controle de datas limite
- **Status Dinâmico**: Acompanhamento em tempo real

### 🛡️ Sistema de Moderação
- **Painel Administrativo**: Interface completa para moderadores
- **Aprovação de Eventos**: Validação antes da publicação
- **Resolução de Apostas**: Definição de resultados
- **Distribuição Automática**: Pagamento proporcional de prêmios
- **Auditoria**: Logs de todas as ações administrativas

### 📊 Funcionalidades Avançadas
- **Busca Inteligente**: Filtros por categoria e status
- **Resultados**: Visualização de eventos finalizados
- **Estatísticas**: Dashboards de desempenho
- **Notificações**: Alertas por email
- **Responsividade**: Interface adaptável a dispositivos

## 🏗️ Arquitetura do Sistema

```
betinha-sports-betting-platform/
├── app.py                     # Aplicação principal Flask
├── requirements.txt           # Dependências Python
├── .env.example              # Modelo de configurações
├── .gitignore                # Arquivos ignorados pelo Git
├── static/                   # Arquivos estáticos
│   ├── css/                  # Folhas de estilo
│   ├── js/                   # Scripts JavaScript
│   └── assets/               # Imagens e ícones
├── templates/                # Templates HTML
│   ├── base.html            # Template base
│   ├── index.html           # Página inicial
│   ├── login.html           # Página de login
│   ├── register.html        # Página de cadastro
│   ├── home.html            # Dashboard principal
│   ├── betEvent.html        # Interface de apostas
│   ├── myWallet.html        # Carteira do usuário
│   ├── newEvent.html        # Criação de eventos
│   ├── approveEvent.html    # Aprovação de eventos
│   └── ...                  # Outros templates
└── docs/                    # Documentação
    ├── SECURITY.md          # Guia de segurança
    └── ...                  # Outros documentos
```

## 🔧 Instalação e Configuração

### Pré-requisitos
- Python 3.8+ instalado
- MySQL Server configurado
- Git para controle de versão

### 1. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/betinha-sports-betting-platform.git
cd betinha-sports-betting-platform
```

### 2. Configurar Ambiente Virtual
```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar Variáveis de Ambiente
```bash
# Copiar arquivo de exemplo
cp .env.example .env

# Editar .env com suas configurações:
nano .env
```

**Configuração do arquivo `.env`:**
```env
# Banco de Dados
DB_HOST=127.0.0.1
DB_USER=seu_usuario_mysql
DB_PASSWORD=sua_senha_mysql
DB_NAME=bd_betinha

# Segurança
SECRET_KEY=sua_chave_secreta_muito_forte_aqui

# Email (opcional)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=465
MAIL_USE_SSL=True
MAIL_USERNAME=seu_email@gmail.com
MAIL_PASSWORD=sua_senha_de_app_gmail
```

### 5. Configurar Banco de Dados
```sql
-- Criar banco de dados
CREATE DATABASE bd_betinha CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Usar o banco
USE bd_betinha;

-- Criar tabelas (adicione aqui os scripts de criação das tabelas)
-- Tabela usuarios, carteira, eventos, apostas, etc.
```

### 6. Executar Aplicação
```bash
python app.py
```

A aplicação estará disponível em: `http://localhost:5000`

## 🔐 Configuração de Segurança

### Geração de Chave Secreta
```python
import secrets
print(secrets.token_hex(32))
```

### Configuração de Email Gmail
1. Ative a autenticação em duas etapas
2. Gere uma "Senha de app" específica
3. Use essa senha no arquivo `.env`

### Hash de Senhas
O sistema utiliza bcrypt para hash seguro de senhas com salt automático.

## 📚 Guias de Uso

### Para Usuários
1. **Cadastro**: Acesse `/register` e complete seus dados
2. **Login**: Entre com email e senha em `/login`
3. **Depositar**: Use a interface para adicionar créditos
4. **Apostar**: Navegue pelos eventos disponíveis
5. **Acompanhar**: Verifique resultados e ganhos

### Para Administradores
1. **Login Admin**: Acesse com conta administrativa
2. **Moderar Eventos**: Aprove/reprove eventos criados
3. **Finalizar Apostas**: Defina resultados dos eventos
4. **Monitorar**: Acompanhe atividades da plataforma

---
