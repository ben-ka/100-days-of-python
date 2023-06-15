import random
def Generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password=""
    password_list =[]
    nr_letters= random.randint(4,7)
    nr_symbols = random.randint(1,3)
    nr_numbers = 10 - nr_letters -nr_symbols
    for letter in range(nr_letters):
        password_list.append(random.choice(letters))
    for symbol in range(nr_symbols):
        password_list.append(random.choice(symbols))
    for number in range(nr_numbers):
        password_list.append(random.choice(numbers)) 
    random.shuffle(password_list)
    shuffled_pass = ''.join(password_list)
    for char in shuffled_pass:
        password+=char
    return str(password)