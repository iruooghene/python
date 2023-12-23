import Discount 

def test_discount():

	assert Discount.discount(200,0.15) == 170 

	assert Discount.discount(150,0.15) == 127.5