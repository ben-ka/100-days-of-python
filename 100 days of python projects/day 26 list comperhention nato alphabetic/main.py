import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

data_dict = {row.letter:row.code for (index,row) in data.iterrows()}
is_on = True
while is_on:
    word = input('Enter word: ').upper()
    letters = word.strip('')
    try:
        nato_letters = [data_dict[letter] for letter in letters]
    except KeyError:
        print('Invalid word. Only letters in the Alphabet please')
    else:
        print(nato_letters)
        is_on = False
