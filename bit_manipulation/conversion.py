def bit_swap_required(a: int, b: int) -> int:
    count: int = 0
    c: int = a ^ b
    while c != 0:
        count += c & 1
        c >>= 1
    return count

print(bit_swap_required(29, 15))