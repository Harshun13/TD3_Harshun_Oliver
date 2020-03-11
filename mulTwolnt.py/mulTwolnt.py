import sys

def add (x,y):
	return x+y

if __name__=="__main__":
	if (len(sys.argv) > 3):
		print("error!! Affichez 2 variable")
	elif (len(sys.argv) < 3):
		print("error!! Affichez 2 varaible")
	else:
		x = int( sys.argv[1] )
		y = int( sys.argv[2] )
		print(add(x,y))


