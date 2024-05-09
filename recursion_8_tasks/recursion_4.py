def is_palindrome(s: str) -> bool:
    s = s.replace(' ', '').lower()
    return is_palindrome_prepare_string(s, len(s))

def is_palindrome_prepare_string(s: str, length: int) -> bool:
    if s[length-1] != s[-length]:
        return False
    if length <= 1:
        return True
    length -= 1
    return is_palindrome_prepare_string(s, length)

# strings = ['топот', 'топор', 'а роза упала на лапу Азора', 'мама мыла раму', '1001001', '1009002']
# for s in strings:
#     print(is_palindrome(s))
