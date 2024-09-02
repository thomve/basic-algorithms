def update_bits(n: int, m: int, i: int, j: int) -> int:

    if i > j or i < 0 or j >= 32:
        return 0
    
    all_ones = ~0
    left = all_ones << (j + 1)
    right = (1 << i) - 1
    mask = left | right
    
    n_cleared = n & mask
    m_shifted = m << i
    
    return n_cleared | m_shifted

def test_update_bits():
    n1 = 0b10000000000
    m1 = 0b10011
    expected1 = 0b10001001100
    assert update_bits(n1, m1, 2, 6) == expected1

    n2 = 0b11111111111
    m2 = 0b101
    expected2 = 0b11111111101
    assert update_bits(n2, m2, 0, 2) == expected2

    n3 = 0b11111111111
    m3 = 0b111
    expected3 = 0b11111111111
    assert update_bits(n3, m3, 3, 5) == expected3

    n4 = 0b11111111111
    m4 = 0b0
    expected4 = 0b11111111110
    assert update_bits(n4, m4, 0, 0) == expected4

    n5 = 0b11111111111
    m5 = 0b1001
    expected5 = 0b11111001111
    assert update_bits(n5, m5, 3, 6) == expected5

    print("All test cases pass")

test_update_bits()