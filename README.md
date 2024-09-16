# Checklist Flask Betinha 777

- [x]  Cadastro e login:
- nome, e-mail, senha, e data de nascimento, saldo.
- O login deve ser feito com o e-mail e senha.
- [x]  Criação de eventos:
- [] autenticação dos eventos
- **título** de até 50 caracteres, uma **descrição** curta de até 150 caracteres sobre esse evento
- **valor de cota:** no mínimo 1 real e 0 centavos.
- **Período de recebimento de aposta** é dado como a data e hora do início e data e hora de fim.
- datas têm que constar: dia, mês, e ano.
- [ ]  Verificação de saldo
- Verificar se o cliente tem os fundos necessários, caso tenha, o valor deve ser retirado da conta e não voltar mais, caso não tenha, exibir uma mensagem

### Moderação

- [ ]  Usuário moderador
- [ ]  Evento aprovado pelo moderador

Após a data limite do evento, o moderador deve informar ao sistema se:

- Evento ocorreu(SIM)
- Evento não ocorreu(NÃO)

Após isso, o sistema deve de maneira proporcional aos valores apostados:

- Remover os valores das wallets de quem perdeu
- Depositar o dinheiro para quem ganhou.

