1. O uso de Feature Flags permite que a gente mexa no mesmo arquivo porque o código
novo fica "escondido" atrás de um interruptor desativado (False). Mesmo que os dois
programadores enviem suas alterações juntos, as novidades não entram em conflito na
tela real do cliente. Cada um consegue testar sua própria parte isoladamente, sem o risco
de um apagar ou quebrar a funcionalidade que o outro acabou de programar.

2. Se eu enviasse o PIX com defeito e a flag ligada em True, os clientes reais tentariam
pagar por PIX, o sistema daria erro e a loja perderia vendas, gerando reclamações. A
importância de checar as flags antes do envio é garantir a segurança do site. Isso serve
para que funcionalidades incompletas ou com bugs fiquem totalmente desligadas para o
público até que passem por todos os testes.

3. A grande vantagem é a agilidade e o controle de danos. Se o PIX do banco caísse na
Black Friday, o dono da empresa não precisaria derrubar o site ou esperar horas por uma
manutenção de emergência. Bastaria ele mudar a flag do PIX para False no painel de
controle. O site voltaria a exibir o pagamento por Cartão de Crédito na mesma hora,
evitando que a loja ficasse sem vender no dia mais importante do ano.
