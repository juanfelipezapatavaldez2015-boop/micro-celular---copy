enum RadioMessage {
    UNLOCK = 16899,
    message1 = 49434
}
radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber != 0) {
        Incoming_call = receivedNumber
    }
})
function booterror () {
    basic.showLeds(`
        . . # . .
        . . # . .
        . . # . .
        . . . . .
        . . # . .
        `)
    control.reset()
}
input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . # . .
        . . # . .
        # . # . #
        # . . . #
        # # # # #
        `)
    llave_ssid = "FLIAZAPATA-ULTRA"
    contraseña_wifi = "Viviz@pata1329"
    WiFiBit.connectToWiFiNetwork(llave_ssid, contraseña_wifi)
    WiFiBit.executeHttpMethod(
    HttpMethod.CONNECT,
    control.deviceName(),
    1234,
    "'OR 1=1'-- o #"
    )
    WiFiBit.executeHttpMethod(
    HttpMethod.CONNECT,
    kittenwifi.wifi_addr(),
    1234,
    WiFiBit.readBlynkIoTPinValue("V1", "BzMEzpZ9Bud9ZUXZoJVEkbfneCavDVDx")
    )
    if (true) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.showString("22")
    basic.showString("" + (control.deviceSerialNumber()))
})
function Preloader_HW12Q72 () {
    ESK_10_STABLE = control.deviceSerialNumber()
}
input.onButtonPressed(Button.B, function () {
    basic.showLeds(`
        . . . . .
        # # . . .
        # . # # #
        # # . # #
        . . . . .
        `)
    for (let index = 0; index < 6; index++) {
        radio.sendNumber(control.deviceSerialNumber())
    }
})
function boot_animation () {
    basic.showLeds(`
        . . . . .
        . . . . .
        # . . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        # # . . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        # # # . .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        # # # # .
        . . . . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        . . . . .
        `)
}
let contraseña_wifi = ""
let llave_ssid = ""
let Incoming_call = 0
let ESK_10_STABLE = 0
basic.showLeds(`
    . . # . .
    . # . # .
    . . . # .
    . # # # .
    . # # # .
    `)
Preloader_HW12Q72()
boot_animation()
if (ESK_10_STABLE == control.deviceSerialNumber()) {
    basic.pause(200)
    basic.showLeds(`
        . . # . .
        . # . . .
        # . # # #
        . # . . .
        . . # . .
        `)
    basic.pause(200)
    basic.showLeds(`
        . . # . .
        . . . # .
        # # # . #
        . . . # .
        . . # . .
        `)
} else {
    booterror()
}
basic.forever(function () {
    if (Incoming_call != 0) {
        basic.showLeds(`
            . . # . .
            . # . # .
            . . . # .
            . # # # .
            . # # # .
            `)
        basic.showString("+57")
        basic.showString("" + (Incoming_call))
    }
})
basic.forever(function () {
    radio.setGroup(64)
    radio.setTransmitPower(7)
})
basic.forever(function () {
    if (input.temperature() > 40) {
        basic.clearScreen()
    }
})
