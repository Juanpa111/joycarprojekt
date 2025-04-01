mode = 0

def on_button_pressed_a():
    global mode
    mode += 1
    if mode == 1:
        linefinder()
    elif mode == 0:
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
        JoyCar.stop(StopIntensity.INTENSE)
    else:
        basic.show_leds("""
            # . # . #
            # . # . #
            # . # . #
            # . # . #
            # . # . #
            """)
        JoyCar.brakelight(ToggleSwitch.ON)
input.on_button_pressed(Button.A, on_button_pressed_a)

def linefinder():
    if JoyCar.linefinder(SensorLCRSelection.LEFT) is True and (JoyCar.linefinder(SensorLCRSelection.CENTER) is False and (JoyCar.linefinder(SensorLCRSelection.RIGHT) is True)):
        JoyCar.drive(FRLRDirection.FORWARD, 20)
    elif JoyCar.linefinder(SensorLCRSelection.LEFT) is True and (JoyCar.linefinder(SensorLCRSelection.CENTER) is True and (JoyCar.linefinder(SensorLCRSelection.RIGHT) is False)):
        JoyCar.drive(FRLRDirection.RIGHT, 10)
    elif JoyCar.linefinder(SensorLCRSelection.LEFT) is False and (JoyCar.linefinder(SensorLCRSelection.CENTER) is True and ( JoyCar.linefinder(SensorLCRSelection.RIGHT) is True)):
        JoyCar.drive(FRLRDirection.LEFT, 10)
    elif JoyCar.linefinder(SensorLCRSelection.LEFT) is True and (JoyCar.linefinder(SensorLCRSelection.CENTER) is True and ( JoyCar.linefinder(SensorLCRSelection.RIGHT) is True)):
        JoyCar.drive(FRLRDirection.REVERSE, 5)
def on_button_pressed_b():
    JoyCar.stop(StopIntensity.INTENSE)
input.on_button_pressed(Button.B, on_button_pressed_b)

