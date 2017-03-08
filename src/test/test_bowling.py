
balls = []

def score():
    out = ""
    for ball in balls:
        out += ball
    return out

def bowl(cnt):
    balls.append(cnt)
    return cnt

def _test_frame_1_ball_1():
    expected = '0'
    bowl('0')
    actual = score()
    assert actual == expected

def test_frame_1_ball_2():
    expected = '00'
    bowl('0')
    bowl('0')
    actual = score()
    assert actual == expected

