shifr_k=input("Введите ключ шифра: ")

initinal_str=input("Введите сообщение: ")
cyrillic_alphabet = [
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'
]
shifr_k_numbers=[]
encrypted_str=""
for letter in shifr_k:
    letter_index=cyrillic_alphabet.index(letter)+1
    shifr_k_numbers.append(letter_index)
i=0
for element in initinal_str:
    if element in cyrillic_alphabet:
        letter=element
        letter_index=cyrillic_alphabet.index(letter)+1
        letter_index_encrypted=(letter_index+shifr_k_numbers[i])%33
        if letter_index_encrypted==0:
            letter_index_encrypted=33
        i=i+1
        if i==len(shifr_k_numbers):
            i=0
        letter_encrypted=cyrillic_alphabet[letter_index_encrypted-1]
        encrypted_str=encrypted_str+letter_encrypted
    else:
        encrypted_str=encrypted_str+element
print(encrypted_str)