let Time = 0
let Guess = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.playTone(262, Time)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Time = randint(1, 12) * 250
    music.playTone(262, Time)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    Guess = control.millis()
    led.plotBarGraph(Guess, Time)
    basic.pause(5000)
})
