let mode = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    mode += 1
    if (mode == 1) {
        linefinder()
    } else if (mode == 0) {
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
        JoyCar.stop(StopIntensity.Intense)
    } else {
        basic.showLeds(`
            # . # . #
            # . # . #
            # . # . #
            # . # . #
            # . # . #
            `)
        JoyCar.brakelight(ToggleSwitch.On)
    }
    
})
function linefinder() {
    if (JoyCar.linefinder(SensorLCRSelection.Left) === true && (JoyCar.linefinder(SensorLCRSelection.Center) === false && JoyCar.linefinder(SensorLCRSelection.Right) === true)) {
        JoyCar.drive(FRLRDirection.Forward, 20)
    } else if (JoyCar.linefinder(SensorLCRSelection.Left) === true && (JoyCar.linefinder(SensorLCRSelection.Center) === true && JoyCar.linefinder(SensorLCRSelection.Right) === false)) {
        JoyCar.drive(FRLRDirection.Right, 10)
    } else if (JoyCar.linefinder(SensorLCRSelection.Left) === false && (JoyCar.linefinder(SensorLCRSelection.Center) === true && JoyCar.linefinder(SensorLCRSelection.Right) === true)) {
        JoyCar.drive(FRLRDirection.Left, 10)
    } else if (JoyCar.linefinder(SensorLCRSelection.Left) === true && (JoyCar.linefinder(SensorLCRSelection.Center) === true && JoyCar.linefinder(SensorLCRSelection.Right) === true)) {
        JoyCar.drive(FRLRDirection.Reverse, 5)
    }
    
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    JoyCar.stop(StopIntensity.Intense)
})
