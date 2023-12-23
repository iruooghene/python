import zeroed_code

def test_zeroed_code():

	assert zeroed_code.zeroed_code([2,5,7,8,9]) == ([0,5,7,8,0])

	assert zeroed_code.zeroed_code([5,6,7,8,9,3]) == ([0,6,7,8,9,0])
	
	

	