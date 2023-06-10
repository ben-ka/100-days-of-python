import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

data_dict = {row.letter:row.code for (index,row) in data.iterrows()}

word = input('insert word: ').upper()
letters = word.strip('')
nato_letters = [data_dict[letter] for letter in letters]
print(nato_letters)