def upper(text):
    result=""
    for character in text:
        if "a"<= character<="z":
            result+=chr(ord(character)-32)
        else:
          result+=character
    return result
print(upper("kumar"))