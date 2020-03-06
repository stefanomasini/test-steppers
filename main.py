def button_pressed_b():
    led.plot(4, 0)
    motor.wheels(motor.Dir.CCW, 2823)
    led.unplot(4, 0)
input.on_button_pressed(Button.B, button_pressed_b)
def button_pressed_a():
    led.plot(1, 1)
    motor.servo(30)
    basic.pause(500)
    motor.servo(155)
    led.unplot(1, 1)
input.on_button_pressed(Button.A, button_pressed_a)
led.plot(2, 2)