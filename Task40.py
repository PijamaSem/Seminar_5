#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def cooding(text):
    count = 0
    char = text[0]
    prev_char = char
    new_text = ''
    for char in text:
        #print(char)
        if char == prev_char:
            count +=1
            prev_char = char
        else:
            new_text +=str(count)
            new_text +=prev_char
            count=1
            prev_char = char
    new_text += str(count)
    new_text += prev_char
    print(new_text)
    return new_text

def encoding(text):
    index =0
    new_text=''
    while index < (len(text)-1):
        key = text[index]
        char = text[index+1]
        new_text += char*int(key)
        index+=2
    print(new_text)
    return new_text


text = 'AAABBBBCCCCC'
print(f'Иcходный текст: {text}')
data = cooding(text)
encoding(data)