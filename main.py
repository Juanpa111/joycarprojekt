def linefinder():
    if JoyCar.linefinder(SensorLCRSelection.LEFT) and ( not JoyCar.linefinder(SensorLCRSelection.CENTER) and JoyCar.linefinder(SensorLCRSelection.RIGHT)):
        JoyCar.drive(FRLRDirection.FORWARD, 10)

    elif JoyCar.linefinder(SensorLCRSelection.LEFT) and (JoyCar.linefinder(SensorLCRSelection.CENTER) and JoyCar.linefinder(SensorLCRSelection.RIGHT)):
        JoyCar.drive(FRLRDirection.RIGHT, 5)
    

def on_button_pressed_a():
    linefinder()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    JoyCar.stop(StopIntensity.INTENSE)
input.on_button_pressed(Button.B, on_button_pressed_b)
