def only_floats(a,b):

	if type(a) == type(float(1.0)) and type(b) == type(float(1.0)):
		return 2

	if type(a) == type(float(1.0)) and type(b) != type(float(1.0)):
		return 1
	
	if type(a) != type(float(1.0)) and type(b) != type(float(1.0)):
		return 0
	