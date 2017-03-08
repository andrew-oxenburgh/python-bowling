from src import bottles_of_beer

RES_0_BOTTLE = '''
no more bottles of beer on the wall,
no more bottles of beer. 
go to the store and buy some more,
0 bottles of beer on the wall.
'''

def test_0_bottle():
    actual = bottles_of_beer.how_many_bottles(0)
    expected = RES_0_BOTTLE
    assert actual == expected

RES_1_BOTTLE = '''
1 more bottle beer on the wall,
1 more bottle of beer.
drink it down pass it around,
1 more bottle of beer

no more bottles of beer on the wall,
no more bottles of beer. 
go to the store and buy some more,
1 bottles of beer on the wall.
'''
def test_1_bottle():
    actual = bottles_of_beer.how_many_bottles(1)
    expected = RES_1_BOTTLE
    assert actual == expected

RES_2_BOTTLES = '''
2 more bottles of beer on the wall,
2 more bottles of beer.
drink it down pass it around,
2 more bottles of beer

1 more bottle beer on the wall,
1 more bottle of beer.
drink it down pass it around,
1 more bottle of beer

no more bottles of beer on the wall,
no more bottles of beer. 
go to the store and buy some more,
2 bottles of beer on the wall.
'''
def test_2_bottle():
    actual = bottles_of_beer.how_many_bottles(2)
    expected = RES_2_BOTTLES
    assert actual == expected