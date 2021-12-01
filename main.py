Time = 0
Guess = 0

def on_button_pressed_a():
    music.play_tone(262, Time)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Time
    Time = randint(1, 12) * 250
    music.play_tone(262, Time)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global Guess
    Guess = control.millis()
    led.plot_bar_graph(Guess, Time)
    basic.pause(5000)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
