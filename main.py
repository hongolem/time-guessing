Time = 0
Guess1 = 0
Guess2 = 0
Result = 0

def on_button_pressed_a():
    music.play_tone(262, Time)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global Time
    Time = randint(1, 12) * 250
    music.play_tone(262, Time)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global Guess1
    Guess1 = control.millis()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_logo_released():
    global Guess2, Result
    Guess2 = control.millis()
    Result = Guess2 - Guess1
    led.plot_bar_graph(Result, Time)
    basic.pause(5000)
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_released)