import turtle
import pandas

WIDTH = 700
HEIGHT = 500

screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.title('U.S. STATES GAME')
#screen.addshape('blank_states_img.gif') another option


data = pandas.read_csv('50_states.csv')
states = data['state'].tolist()
state_location_dict = {}

for state in states:
    x_cor = int(data['x'][data['state'] == state])
    y_cor = int(data['y'][data['state'] == state])
    state_location_dict[state] = (x_cor,y_cor)


screen.bgpic('blank_states_img.gif')  

ben = turtle.Turtle()
score = 0

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f'{score}/50 states correct',prompt='enter a U.S. country').title()
    if answer_state == 'Exit':
        break
    if answer_state in state_location_dict:
        score+=1
        ben.penup()
        ben.hideturtle()
        ben.goto(state_location_dict[answer_state])
        ben.write(answer_state,False,'center',('arial',8,'normal'))
        state_location_dict.pop(answer_state)

    if score == 50:
        ben.home()
        ben.write('You Won',False,'center',('arial',35,'normal'))
        game_is_on = False
    


def get_coor(x,y):
    print(x,y)
turtle.onscreenclick(get_coor)
states_to_learn = [state for state in state_location_dict]
states_to_print = pandas.DataFrame(states_to_learn)
states_to_print.to_csv('states_to_learn.csv')



