shifr_k=input("Введите ключ шифра: ")
cyrillic_alphabet = [
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я'
]
shifr_k_numbers=[]
for letter in shifr_k:
    letter_index=cyrillic_alphabet.index(letter)+1
    shifr_k_numbers.append(letter_index)
print(shifr_k)
print(shifr_k_numbers)
