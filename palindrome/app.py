def is_palindrome(text):
    text = text.lower().replace(" ", "")
    palindrome = [c for c in text]
    palindrome.reverse()
    palindrome = "".join(palindrome)

    return text == palindrome


print("Race Car : ", is_palindrome("Race Car"))
print("Iceman : ", is_palindrome("Iceman"))