"""
You write down a secret number and ask your friend to guess what the number is. 
When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located 
in the wrong position. 
Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. 
Note that both secret and guess may contain duplicate digits.
"""
def get_hint(secret: str, guess: str) -> str:
    bulls = 0
    cows = 0

    secret_count = {}
    guess_count = {}

    for s_digit, g_digit in zip(secret, guess):
        if s_digit == g_digit:
            bulls += 1
        else:
            secret_count[s_digit] = secret_count.get(s_digit, 0) + 1
            guess_count[g_digit] = guess_count.get(g_digit, 0) + 1

    for digit in guess_count:
        if digit in secret_count:
            cows += min(secret_count[digit], guess_count[digit])

    return f"{bulls}A{cows}B"