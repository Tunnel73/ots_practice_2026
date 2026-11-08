import turtle


def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)
    num_turns = 5

    if state == "RIGHT1":
        t.forward(10)  # Перемещение

        if x >= 10:
            state = "UP1"
            t.setheading(90)  # Поворот вверх
            return state, turn
        return state, turn
    if state == "UP1":
        t.forward(10)  # Перемещение

        if y >= -1:
            state = "RIGHT2"
            t.setheading(0)  # Поворот вправо
            return state, turn
        return state, turn
    if state == "INIT":

        if True:
            state = "DOWN1"
            t.setheading(270)  # Поворот вниз
            return state, turn
        return state, turn
    if state == "DOWN2":
        t.forward(10)  # Перемещение

        if y <= -30:
            state = "RIGHT3"
            t.setheading(0)  # Поворот вправо
            return state, turn
        return state, turn
    if state == "RIGHT3":
        t.forward(10)  # Перемещение

        if x >= 30:
            state = "UP2"
            t.setheading(90)  # Поворот вверх
            return state, turn
        return state, turn
    if state == "UP2":
        t.forward(10)  # Перемещение

        if y >= -1:
            state = "RIGHT4"
            t.setheading(0)  # Поворот вправо
            return state, turn
        return state, turn
    if state == "RIGHT4":
        t.forward(10)  # Перемещение

        if x >= 40:
            state = "DOWN3"
            t.setheading(270)  # Поворот вниз
            return state, turn
        return state, turn
    if state == "DOWN3":
        t.forward(10)  # Перемещение

        if y <= -30:
            state = "STOP"
            t.setheading(0)  # Поворот вправо
            return state, turn
        return state, turn
    if state == "DOWN1":
        t.forward(10)  # Перемещение

        if y <= -30:
            state = "RIGHT1"
            t.setheading(0)  # Поворот вправо
            return state, turn
        return state, turn
    if state == "RIGHT2":
        t.forward(10)  # Перемещение

        if x >= 20:
            state = "DOWN2"
            t.setheading(270)  # Поворот вниз
            return state, turn
        return state, turn
    return state, turn


def draw():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state
    t = turtle.Turtle()
    t.speed(0)
    turn = 1

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)
    turtle.done()


if  __name__ == "__main__":
    draw()
