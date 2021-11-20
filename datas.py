#!/usr/bin/env python3


from time import sleep

print("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++ WORDLIST ++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			""")

with open('datas_saved.txt', 'w') as arquivo:
	data_inicial = int(input("Ano inicial: "))
	data_final = int(input("Ano final: "))
	data_final = data_final + 1
	num = data_inicial

	while(num != data_final):
		for i in range(1, 13):
			for n in range(1, 32):
				arquivo.write(f"{n}/{i}/{num}\n")
				arquivo.write("")
		num = num + 1

		if (num == data_final):
			break
print("Processando", end="")
sleep(0.2)
print("*", end=" ")
sleep(0.2)
print("*", end=" ")
sleep(0.2)
print("*", end=" ")
sleep(0.2)
print("*", end=" ")
sleep(0.2)
print("*")
print("*********")
print("concluído")
print("*********")
print("ARQUIVO = datas_saved.txt")
