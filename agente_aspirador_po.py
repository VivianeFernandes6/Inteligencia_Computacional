def agente_aspirador_po(local, status):

	SUJO = "sujo"
	LIMPO = "limpo"
	A = "A"
	B = "B"
	ASPIRAR = "aspirar"
	RIGHT = "direita"
	LEFT = "esquerda"
	NoOperacao = "nada"


	if(status == SUJO):
		return ASPIRAR
	elif(local == A):
		return RIGHT
	elif(local == B):
		return LEFT
	else:
		return NoOperacao






print(agente_aspirador_po("B", "sujo"))
print(agente_aspirador_po("A", "limpo"))
