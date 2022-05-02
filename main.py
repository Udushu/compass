Degrees = 0

def on_forever():
    global Degrees
    Degrees = input.compass_heading()
    if Degrees < 45:
        basic.show_string("N")
    elif Degrees < 135:
        basic.show_string("E")
    elif Degrees < 225:
        basic.show_string("S")
    elif Degrees < 315:
        basic.show_string("W")
    else:
        basic.show_string("N")
basic.forever(on_forever)
