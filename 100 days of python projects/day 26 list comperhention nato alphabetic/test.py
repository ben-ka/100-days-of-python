# import random
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# student_scores = {name: random.randint(1,100) for name in names}
# print(student_scores)
# passed_students = {student:grade for (student, grade) in student_scores.items() if grade >= 55}


import pandas                    
dict = {
    'students' : ['ben','tom','muly'],
    'scores' : [95,83,13]
}                                                                                                           
student_df = pandas.DataFrame(dict)
for (index,row) in student_df.iterrows():
    if row.scores >60:
        print(row.scores)    





# new_list = [name.upper() for name in names if len(name) >=5]                              
# print(new_list)

