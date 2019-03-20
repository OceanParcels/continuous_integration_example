def hello_world():
    print('Hello World!')
    return 0


def test_hello_world():
    hw = hello_world()
    assert(hw == 0)
