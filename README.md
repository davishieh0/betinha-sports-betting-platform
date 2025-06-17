# Plataforma de Apostas

Uma plataforma de apostas esportivas moderna desenvolvida com Flask e Python, proporcionando uma experiência completa para apostadores e administradores.

## 📋 Sobre o Projeto

Betinha 777 é uma aplicação web full-stack que permite aos usuários criar contas, gerenciar saldos e participar de eventos de apostas em tempo real. A plataforma conta com sistema de moderação para garantir a integridade das apostas e um painel administrativo completo.

## 🚀 Tecnologias Utilizadas

- **Backend**: Python 3.x + Flask
- **Banco de Dados**: MySQL
- **Frontend**: HTML5, CSS3, JavaScript
- **Autenticação**: Flask-Login
- **ORM**: SQLAlchemy

## ⚙️ Funcionalidades

### 👤 Sistema de Usuários
- Cadastro completo com validação de dados
- Autenticação segura por email e senha
- Gerenciamento de perfil e saldo
- Sistema de carteira digital

### 🎯 Gestão de Eventos
- Criação de eventos de apostas personalizados
- Configuração de cotas e períodos de apostas
- Sistema de aprovação por moderadores
- Controle de datas limite para apostas

### 🛡️ Sistema de Moderação
- Painel administrativo para moderadores
- Aprovação e validação de eventos
- Resolução de apostas (ganhou/perdeu)
- Distribuição automática de prêmios

### 💰 Gestão Financeira
- Verificação automática de saldo
- Processamento seguro de transações
- Distribuição proporcional de ganhos
- Histórico completo de apostas

## 🏗️ Arquitetura do Sistema

```
betinha/
├── app/
│   ├── models/          # Modelos do banco de dados
│   ├── routes/          # Rotas da aplicação
│   ├── templates/       # Templates HTML
│   ├── static/          # Arquivos estáticos (CSS, JS)
│   └── utils/           # Utilitários e helpers
├── migrations/          # Migrações do banco
├── config.py           # Configurações da aplicação
└── requirements.txt    # Dependências do projeto
```

## 🛠️ Instalação e Configuração

### Pré-requisitos
- Python 3.8+
- MySQL 8.0+
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/davishieh0/betinha.git
cd betinha
```

2. **Crie um ambiente virtual**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Configure o banco de dados**
```bash
# Crie um banco MySQL chamado 'betinha'
mysql -u root -p
CREATE DATABASE betinha;
```

5. **Configure as variáveis de ambiente**
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
export DATABASE_URL=mysql://usuario:senha@localhost/betinha
```

6. **Execute as migrações**
```bash
flask db upgrade
```

7. **Inicie a aplicação**
```bash
flask run
```

## 📊 Modelo de Dados

### Principais Entidades
- **Users**: Gerenciamento de usuários e autenticação
- **Events**: Eventos de apostas e configurações
- **Bets**: Registro de apostas realizadas
- **Transactions**: Histórico de transações financeiras
