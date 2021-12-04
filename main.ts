let Time = 0
let Guess1 = 0
let Guess2 = 0
let Result = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.playTone(262, Time)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    Time = randint(1, 12) * 250
    music.playTone(262, Time)
})
input.onLogoEvent(TouchButtonEvent.Touched, function on_logo_touched() {
    
    Guess1 = control.millis()
})
input.onLogoEvent(TouchButtonEvent.Released, function on_logo_released() {
    
    Guess2 = control.millis()
    Result = Guess2 - Guess1
    led.plotBarGraph(Result, Time)
    basic.pause(500)
    if (led.point(4, 0)) {
        victory()
    }
    
    basic.pause(2000)
    basic.clearScreen()
})
function victory() {
    music.playMelody("C D E F", 120)
    basic.showIcon(IconNames.Yes)
}

