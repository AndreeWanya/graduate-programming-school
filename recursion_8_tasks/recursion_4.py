def is_palindrome(s: str) -> bool:
    s = s.replace(' ', '').lower()
    if s[0] != s[-1]:
        return False
    if len(s) <= 1:
        return True
    return is_palindrome(s[1: -1])

# strings = ['топот', 'топор', 'а роза упала на лапу Азора', 'мама мыла раму', '1001001', '1009002']
# for s in strings:
#     print(is_palindrome(s))
