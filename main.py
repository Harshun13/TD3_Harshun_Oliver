from addTwoInt import add
a = input("Pour additionner appuyer y ou pour sortir appuyer q"+ " ")
while((a=="y") or (a=="q")):
	if (a=="y"):
		a = input("Entrez le premier valeur: ")
		b = input("Entrez le deuxieme valeur: ")
		a = int(a) 
		b = int(b)
		print(add(a,b))
	elif (a=="q"):
		break
	else:
		print("error!!")

		
