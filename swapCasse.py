def swapCasse(text):
    result=""
    for character in text:
        if "A"<= character<="Z":
            result+=chr(ord(character)+32)
        elif "a"<=character<="z":
            result+=chr(ord(character)-32)
        else:
          result+=character
    return result
print(swapCasse("KUmArRiShI"))
