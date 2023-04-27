original_letter = open('starting_letter.txt')
content = original_letter.read()
original_letter.close()
with open('names.txt') as names:
    for line in names:
        name = line.strip()
        with open(f'ready_to_deliver/letter_for_{name}.txt','w') as file:
            new_content = content.replace('[name]',f'{name}')
            file.write(new_content)
            