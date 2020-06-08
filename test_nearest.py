from nearest import nearest_square

def test_nerest_square_5():
    assert(nearest_square(5)) == 4

def test_nearest_squaare_12():
    assert(nearest_square(-12) == 0)