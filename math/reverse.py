"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""
def reverse(x: int):
    new_int = 0
    copy = abs(x)
    while copy > 0:
        ending = copy % 10
        new_int = new_int * 10 + ending
        copy = copy // 10
    
    if x < 0:
        new_int = -1 * new_int
    
    if (new_int > ((2**31) - 1)) or (new_int < -2**31):
        return 0

    return new_int