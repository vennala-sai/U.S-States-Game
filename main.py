import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
cont = True
res = []
while cont:
    inp = screen.textinput("Guess the State", "What's another state's name?").capitalize()
    r = data[data["state"] == inp]

    if inp == "Exit":
        cont = False
    elif r.empty:  # Check if the DataFrame is empty (state not found)
        cont = False  # End the game if the state is not found
    else:
        pet = turtle.Turtle()
        pet.hideturtle()
        pet.penup()
        pet.setposition(int(r.x), int(r.y))
        pet.write(inp)
    res.append(inp)
l = data["state"].tolist()
res.sort()
if res[len(res) -1] == "Exit":
    res.remove("Exit")
f = []
for state in l:
    if state not in res:
        f.append(state)
# x = []
# y = []
# for state in f:
#     r = data[data["state"] == inp]
#     x.append(r.x)
#     y.append(r.y)
# d = {
#     "states": f,
#     "x": x,
#     "y": y
# }
z = pandas.DataFrame(f)
z.to_csv("missed_states.csv")

