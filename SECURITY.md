# 🔒 Guia de Segurança - Betinha Sports Platform

## ⚠️ PROBLEMAS DE SEGURANÇA CORRIGIDOS

Este documento lista os problemas de segurança que foram identificados e corrigidos no projeto.

### 🚨 Problemas Encontrados e Soluções

#### 1. Credenciais Hardcoded no Código
**Problema**: Senhas e chaves sensíveis estavam expostas diretamente no código fonte.

**Itens expostos**:
- Senha do banco de dados: `otavio2912`
- Chave secreta da aplicação: `shhhhhh`
- Email SMTP: `trabalhobetinha777@gmail.com`
- Senha SMTP: `oabc hsen ryxu evla`

**Solução**: 
- Criação de arquivo `.env` para armazenar configurações sensíveis
- Modificação do código para usar variáveis de ambiente
- Adição do `.env` ao `.gitignore` para não versionar credenciais

#### 2. Chave Secreta Fraca
**Problema**: A chave secreta `'shhhhhh'` é extremamente fraca e previsível.

**Solução**: 
- Uso de variável de ambiente `SECRET_KEY`
- Recomendação para gerar chave forte (32+ caracteres aleatórios)

## 🛠️ Como Configurar Seguramente

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Configurar Variáveis de Ambiente
1. Copie o arquivo `.env.example` para `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edite o arquivo `.env` com suas credenciais reais:
   ```env
   # ALTERE ESTAS CONFIGURAÇÕES!
   DB_PASSWORD=sua_senha_real_do_banco
   SECRET_KEY=gere_uma_chave_forte_aqui
   MAIL_USERNAME=seu_email_real@gmail.com
   MAIL_PASSWORD=sua_senha_de_app_real
   ```

### 3. Gerar Chave Secreta Forte
Use o Python para gerar uma chave forte:
```python
import secrets
print(secrets.token_hex(32))
```

### 4. Configurar Senha de App do Gmail
1. Ative a autenticação em duas etapas na sua conta Google
2. Gere uma "Senha de app" específica para esta aplicação
3. Use esta senha no arquivo `.env`

## 🔐 Recomendações Adicionais de Segurança

### Banco de Dados
- [ ] Altere a senha padrão do MySQL
- [ ] Crie um usuário específico para a aplicação (não use root)
- [ ] Configure permissões mínimas necessárias

### Aplicação
- [ ] Implemente hash de senhas (bcrypt/scrypt)
- [ ] Adicione rate limiting para login
- [ ] Configure HTTPS em produção
- [ ] Implemente logs de segurança

### Servidor
- [ ] Use um servidor web reverso (nginx/Apache)
- [ ] Configure firewall apropriado
- [ ] Mantenha o sistema atualizado
- [ ] Use certificados SSL válidos

## 📋 Checklist de Segurança

- [x] Credenciais removidas do código fonte
- [x] Arquivo `.env` criado para configurações
- [x] `.gitignore` configurado para não versionar `.env`
- [x] Dependências atualizadas em `requirements.txt`
- [ ] Senhas alteradas no arquivo `.env`
- [ ] Chave secreta forte gerada
- [ ] Usuário específico criado no banco de dados
- [ ] Senhas dos usuários com hash implementado

## 🚨 IMPORTANTE

**NUNCA** commite o arquivo `.env` no repositório Git. Ele contém informações sensíveis que podem comprometer a segurança da aplicação.

**SEMPRE** altere todas as senhas padrão antes de colocar a aplicação em produção.
