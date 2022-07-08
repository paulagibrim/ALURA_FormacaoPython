def jogar():
	print("******** BEM VINDO(A) AO JOGO DA FORCA ********")

	palavra_secreta = "banana"
	isForca = False
	isCerto = False

	# enquanto não enforcou, e não acertou
	while not isForca and not isCerto:
		chute = input("Qual letra?")

		index = 0
		for letra in palavra_secreta:
			if letra.lower() == chute.lower().strip():
				print("Letra {} na posição {}".format(letra, index))
			index += 1








if __name__ == "__main__":
	jogar()
