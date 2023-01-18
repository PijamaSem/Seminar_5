# Задача №38
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

data = 'абв вба абвгд ыбва фываыб'
bad_text='абв'
print('Исходный данные:',data)
new_data = []
for word in data.split():
    if bad_text not in word:
        new_data.append(word)
print(f"Слова из текста не содержащие '{bad_text}':",new_data)
