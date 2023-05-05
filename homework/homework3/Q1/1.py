numbers_dict = {
    'twenty': '20',
    'nineteen': '19',
    'eighteen': '18',
    'seventeen': '17',
    'sixteen': '16',
    'fifteen': '15',
    'fourteen': '14',
    'thirteen': '13',
    'twelve': '12',
    'eleven': '11',
    'ten': '10',
    'nine': '9',
    'eight': '8',
    'seven': '7',
    'six': '6',
    'five': '5',
    'four': '4',
    'three': '3',
    'two': '2',
    'one': '1'
}

with open("Q1/Zen.txt","r",encoding="utf-8") as file:
    text = file.read()
    for word, number in numbers_dict.items():
        text = text.replace(word, number)
    with open('Q1/Zen_numbers.txt', 'w',encoding="utf-8") as new_file:
        new_file.write(text)
 