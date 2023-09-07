import turtle
import pandas

FONT = ('Arial', 12, 'normal')


screen = turtle.Screen()
screen.addshape('blank_states_img.gif')
screen.title('game of states')
turtle.shape('blank_states_img.gif')

data = pandas.read_csv('50_states.csv')
state_names = []
score = 0
while len(data):
    entry = screen.textinput(f'{score}/50 solved', 'Enter state name:').title()
    if entry == 'Exit':
        break
    if entry in data.state.to_list():
        score += 1
        state = data[data.state == entry]
        data = data.drop(state.index)
        name = turtle.Turtle()
        name.hideturtle()
        name.penup()
        name.goto(int(state.x), int(state.y))
        name.write(entry, font=FONT)

        state_names.append(name)

for s in data.state:
    print(s)