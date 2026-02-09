#Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data_entrada = input("Digite a adata no formado dd/mm/aaaa: ")
data_saida = data_entrada.split("/")
print(data_saida)