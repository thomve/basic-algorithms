def min_product(a: int, b: int) -> int:
    smaller = a if a < b else b
    bigger = b if a < b else a
    return min_product_helper(smaller, bigger)

def min_product_helper(smaller: int, bigger: int) -> int:
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger
    s = smaller >> 1
    half_prod = min_product_helper(s, bigger)
    if smaller % 2 == 0:
        return half_prod + half_prod
    else:
        return half_prod + half_prod + bigger
    

print(min_product(8, 7)) # 56
print(min_product(6, 8)) # 48