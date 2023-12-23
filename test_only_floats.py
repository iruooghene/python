import only_floats

def test_only_floats():

	assert only_floats.only_floats(12.3,3.4) == 2

	assert only_floats.only_floats(12.3,4) == 1

	assert only_floats.only_floats(12,3) == 0