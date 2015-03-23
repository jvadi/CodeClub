def reverseWord(string):
    result = string[-1].upper()
    for i in range(-2, -len(string)-1, -1):
        result += string[i].lower()
    return result

print(reverseWord("for"))
print(reverseWord("Bar"))
print(reverseWord("wOl"))
print(reverseWord("hOp"))
print(reverseWord("Hip"))
