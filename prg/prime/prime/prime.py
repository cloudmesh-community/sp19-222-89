from flask import jsonify
def prime(n):
	for i in range(2,n):
		if(n%i == 0):
			return(str(n) + " is not a prime number")
	
	result = str(n) + " is a prime number"
	return jsonify(result)
