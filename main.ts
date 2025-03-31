function linefinder() {
    if (JoyCar.linefinder(SensorLCRSelection.Left) && (JoyCar.linefinder(SensorLCRSelection.Center) && JoyCar.linefinder(SensorLCRSelection.Right))) {
        JoyCar.drive(FRLRDirection.Forward, 10)
    }
    
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    linefinder()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    JoyCar.stop(StopIntensity.Intense)
})
