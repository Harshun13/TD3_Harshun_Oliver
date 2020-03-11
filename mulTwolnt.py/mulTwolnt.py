import sys

def mul ():
	return x*y

if __name__=="__main__":
	if ( len(sys.argv) >  3):
                print("error!! Entrez que 2 variable")

	elif ( len(sys.argv) == 1 ):
		x = input("premier valeur: ")
		y = input("deuxieme valeur: ")
		x = int(x)
		y = int(y)
		print( mul() )
	elif (len(sys.argv) == 2 ):
		print("error!! Entrez encore une valeur")
		y = input("Le deuxieme valeur: ")
		x = int( sys.argv[1] )
		y = int(y)
		print( mul() )
	else:
		x = int( sys.argv[1] )
		y = int( sys.argv[2] )
		print( mul() )




