from string import punctuation

#palindrom = "Koby�a ma ma�y bok!"
palindrom = "Ile Romanowi da�a za �ad Iwona moreli?"

def is_palindrom(palindrom: str) -> bool:
    palindrom_wspak = ""
    palindrom = palindrom.lower()
    for e in reversed(palindrom):
        palindrom_wspak += e
    if palindrom == palindrom_wspak:
        return True
    else:
        return False

def trim_special_chars(text: str) -> str:
    
    for i in punctuation:
        text = text.replace(i, "")
    new_text = text.replace(".","").replace(" ", "").lower()
    return new_text

print(is_palindrom(trim_special_chars(palindrom)))
#print(trim_special_char("Koby�a ma ma�y bok!"))