email_tmpl = """
Olá, %(nome)s
Tem interesse em comprar %(produto)s?
    
Este produto é ótimo para resolver
%(texto)s
    
Clique agora em %(link)s
    
Apenas %(quantidade)d disponiveis!
    
Preço promocional R$%(preco).2f
"""

clientes = ["Maria", "Joao", "Bruno"]

for cliente in clientes:
    print(email_tmpl % {
        "nome": cliente, 
        "produto":"caneta", 
        "texto": "Escrever muito bem", 
        "link": "https://canetalegais.com", 
        "quantidade": 1, 
        "preco": 50.5,
        }
    )

#------------------- New Style --------------------
msg = "Olá, %s você é o  player n %03d e você tem %.3f pontos."
msg % ("Fabio", 2, 987,3)

#------------------- New Style --------------------

msg = "Olá, {} você é o  player n {:03d} e você tem {:.3f} pontos."
msg.format("Fabio", 2, 987.3)

"{:^20}".format("Fabio") #Centraliza o texto no total de 20 char
"{:<20}".format("Fabio") #Posiciona o texto a esquerda no total de 20 char
"{:>20}".format("Fabio") #Posiciona o texto a direita no total de 20 char
"{:-^20}".format("Fabio") #Centraliza o texto no total de 20 char e preenche os espaços em branco com o simbolo antes do ˆ

msg = "Olá, {nome} você é o  player n {numero:03d} e você tem {pontos:.3f} pontos."
msg.format(numero=2, pontos=987.3, nome="Fabio")

# Concatenação %s -> Logging
# str.format {} -> mensagens longas, e-mail
# f-strings -> restante, msg, print, error
# Imprimir emoji print("\U000CODIGO") -> unicode.explorer.com
# Imprimir emoji print("\N{panda face}") -> unicode.explorer.com