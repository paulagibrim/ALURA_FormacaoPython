import forca as fc
import advinhacao as adv


def escolhe_jogo():
	print("Escolha aqui seu jogo:")
	print("[ 1 ] Jogo da adivinhação")
	print("[ 2 ] Jogo da forca")

	select = int(input("Digite sua escolha: "))
	return select


def seleciona_jogo(s):
	if s == 1:
		adv.jogar()
	elif s == 2:
		fc.jogar()


def main():
	print("******** BEM VINDO(A) A ABA DE JOGOS **********")
	selecao = escolhe_jogo()
	seleciona_jogo(selecao)
	print("***************** FIM DE JOGO *****************")


if __name__ == "__main__":
	main()
