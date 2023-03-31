# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again."    
# }
# # print(programming_dictionary["Bug"])       # finding value using key

# programming_dictionary["loop"] = "the action of doing something again and again"   # adding an item to a dic
# # print(programming_dictionary)

# empty_dictionary = {}      # empty dictionary


# programming_dictionary["Bug"] = "a moth in your computer"      #chang an existing item
# # print(programming_dictionary)

# #loop through a dictionary giving only a key
# for key in programming_dictionary:
#     print(key)

# for key in programming_dictionary:                   # loop through a dictionary printing the values
#     print(programming_dictionary[key])

# for key in programming_dictionary:                        #doing both
#     print(key + " - "+programming_dictionary[key])














# Scores 91 - 100: Grade = "Outstanding"

# Scores 81 - 90: Grade = "Exceeds Expectations"

# Scores 71 - 80: Grade = "Acceptable"

# Scores 70 or lower: Grade = "Fail"



student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:

    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"

    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"

    elif student_scores[key] >70:
        student_grades[key] ="Acceptable"

    elif student_scores[key] <=70:
        student_grades[key] = "Fail"
    

# # 🚨 Don't change the code below 👇
# print(student_grades)









            # nesting
capitals = {
    "France":"paris",
    "germany":"berlin"                         #normal
}



#nesting a list in a dictionary
travel_log ={
    "France":["Paris","lille","Dijon"],
    "Germany":["Berlin","hamburg"]
}

#nesting a dictionary in a dictionary
travel_log = {
    "France": {"cities_visited" : ["Paris", "lille","Dijon"], "total_visits": 12},
    "Germany":{"cities_visited" : ["Berlin","hamburg"] ,  "total visits":18}
}


#nesting a dictionary in a list

travel_log = [
    {
    "country":"France",
    "cities_visited" : ["Paris", "Lille","Dijon"],
    "total_visits": 12
    },
    {
    "country":"Germany",
    "cities_visited" : ["Berlin","Hamburg","Stuttgart"] , 
    "total_visits":5
    }
]

def add_new_country(country,total_visits , cities_visited ,travel_log):
    travel_log.append(
         {
            "country": country,    
            "total_visits" : total_visits,
            "cities_visited": cities_visited,
        }
    )
       
    
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"],travel_log)

print(travel_log)





  


