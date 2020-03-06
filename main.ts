input.onButtonPressed(Button.B, function () {
    led.plot(4, 0)
    motor.wheels(motor.Dir.CCW, 2823)
    led.unplot(4, 0)
})
input.onButtonPressed(Button.A, function () {
    led.plot(1, 1)
    motor.servo(30)
    basic.pause(500)
    motor.servo(155)
    led.unplot(1, 1)
})
led.plot(2, 2)
