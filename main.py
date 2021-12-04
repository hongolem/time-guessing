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

def on_logo_touched():
    global Guess1
    Guess1 = control.millis()
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_logo_released():
    global Guess1, Guess2, Result, Time
    Guess2 = control.millis()
    Result = Guess2 - Guess1
    led.plot_bar_graph(Result, Time)
    basic.pause(500)
    if led.point(4, 0):
        victory()
    basic.pause(2000)
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_released)

def victory():
    music.play_melody("C D E F", 120)
    basic.show_icon(IconNames.YES)
