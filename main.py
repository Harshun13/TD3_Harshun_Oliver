from addTwoInt import add
from mulTwoInt import mul

print("Choisi entre A ou M ")
z = input()
while ((z == "A") or (z == "M")):
	if (z =="A"):
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
	elif (z=="M"):
		b = input("Pour multipliyer appuyer y ou pour sortir appuyer q"+ " ")
		while((b=="y") or (b=="q")):
			if (b=="y"):
				d=input("valeur svp: ")
				e=input("valeur svp: ")
				d=int(d)
				e=int(e)
				print(mul(d,e))
			elif (b=="q"):
				break
			else: 
				print("error!!")
	else:
		print("Rechoisi entre A ou M")
	
