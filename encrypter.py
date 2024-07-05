alpha=int(input("Введите коэффициент альфа: "))
beta=int(input("Введите коэффициент бета: "))
initinal_str=input("Введите сообщение: ")
cyrillic_alphabet = [
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'
]
encrypted_str=""
for element in initinal_str:
    if element in cyrillic_alphabet:
        letter=element
        letter_index=cyrillic_alphabet.index(letter)+1
        letter_index_encrypted=(letter_index*alpha+beta)%33
        letter_encrypted=cyrillic_alphabet[letter_index_encrypted-1]
        encrypted_str=encrypted_str+letter_encrypted
    else:
        encrypted_str=encrypted_str+element
print(encrypted_str)
