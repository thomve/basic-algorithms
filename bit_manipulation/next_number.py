def get_next(n: int) -> int:
    c: int = n
    c0: int = 0
    c1: int = 0
    while (c & 1) == 0 and c != 0:
        c0 += 1
        c >>= 1

    while (c & 1) == 1:
        c1 += 1
        c >>= 1

    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1
    
    p: int = c0 + c1

    n |= (1 << p)
    n &= ~((1 << p) - 1)
    n |= (1 << (c1 - 1)) - 1

    return n

def get_previous(n: int) -> int:
    temp: int = n
    c0: int = 0
    c1: int = 0

    while (temp & 1) == 1:
        c1 += 1
        temp >>= 1
    
    if temp == 0:
        return -1
    
    while (temp & 1) == 0 and temp != 0:
        c0 += 1
        temp >>= 1

    p: int = c0 + c1
    n &= ((~0) << (p + 1))
    mask: int = (1 << (c1 + 1)) - 1
    n |= mask << (c0 - 1)

    return n

def test_bit_manipulation_functions():
    # Test cases for get_next function
    print(bin(get_next(0b1111)))
    assert get_next(5) == 6
    assert get_next(10) == 12
    assert get_next(0b1010) == 0b1100
    assert get_next(0b1111) == 0b10111

    # Test cases for get_previous function
    assert get_previous(6) == 5
    assert get_previous(12) == 10
    assert get_previous(0b1100) == 0b1010
    assert get_previous(0b10111) == 0b1111

    print("All test cases passed!")

test_bit_manipulation_functions()