flag_cupom_desconto = True
flag_pagamento_pix = False

def renderizar_tela():
  print("--- TELA DE PAGAMENTO (Compra-Tudo.com) ---")
  valor_compra = 150.00
  print("Valor do produto: R$", valor_compra)
  if flag_cupom_desconto == True:
   print("[ NOVO CAMPO ]: Digite seu Cupom de Desconto aqui!")
  if flag_pagamento_pix == True:
   print("[ BOTÃO ]: Pagar com PIX ")
  else:
   print("[ BOTÃO ]: Pagar com Cartão de Crédito ")
renderizar_tela()
