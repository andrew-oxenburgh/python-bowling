BOOTLES_LEFT = '''
{} more bottles of beer on the wall,
{} more bottles of beer.
drink it down pass it around,
{} more bottles of beer
'''

ONE_BOTTLE_LEFT = '''
1 more bottle beer on the wall,
1 more bottle of beer.
drink it down pass it around,
1 more bottle of beer
'''


NO_BOTTLES_LEFT = '''
no more bottles of beer on the wall,
no more bottles of beer. 
go to the store and buy some more,
{} bottles of beer on the wall.
'''


def how_many_bottles(cnt):
    res = ""
    NUM_BOTTLES = cnt
    NUM_BOTTLES_EXCLUDING_LAST = NUM_BOTTLES - 1
    if NUM_BOTTLES > 1:
        for i in range(NUM_BOTTLES_EXCLUDING_LAST):
            bottles_left = NUM_BOTTLES - i
            res += BOOTLES_LEFT.format(bottles_left, bottles_left, bottles_left)

    if NUM_BOTTLES > 0:
        res += ONE_BOTTLE_LEFT

    res += NO_BOTTLES_LEFT.format(NUM_BOTTLES)
    return res
