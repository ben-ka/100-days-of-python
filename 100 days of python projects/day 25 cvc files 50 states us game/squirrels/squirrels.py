import pandas
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
squirrel_count = {
    'fur colors':{'Gray':0,'Cinnamon':0,'Black':0}
}
color_list = data['Primary Fur Color'].tolist()
for squirrel in color_list:
    if pandas.notnull(squirrel) and squirrel.isalpha():
        squirrel_count['fur colors'][squirrel]+=1
squirrel_data = pandas.DataFrame(squirrel_count)
squirrel_data.to_csv('squirrel_count.csv')


