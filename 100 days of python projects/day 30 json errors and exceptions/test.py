# types of errors

# # file not found
# with open ('file.txt') as file:
#     file.read()

## key error
# dictionary = {'key1':'value1'}
# print(dictionary['key2'])

## index error
# list = [3,5,6]
# big = list[3]

# # type error

# text = 'abc'
# print(text+5)

## how to catch exceptions



try:
    file = open('a_file.txt')
    dictionary = {'key1' : 'value1'}
    print(dictionary['rgtbytb'])


except FileNotFoundError :
    file = open('a_file.txt','w')
    file.write('something')

except KeyError as error_msg:
    print(f'the key {error_msg} does not exist')

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print('file was closed')

# # raising your own errors

# finally:
#     raise TypeError('i made up an error')


# when to raise an error

height = float(input('height: '))
weight = int(input('weight: '))

if height > 3:
    raise ValueError('The height is too large')

bmi = weight / height ** 2
print(bmi)