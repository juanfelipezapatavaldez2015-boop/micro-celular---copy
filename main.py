input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . # . .
        . . # . .
        # . # . #
        # . . . #
        # # # # #
        `)
    kittenwifi.ntp_get(kittenwifi.NtpTimeType.SS)
    kittenwifi.wifi_join("FLIAZAPATA-ULTRA", "Viviz@pata1329")
    kittenwifi.rest_header(kittenwifi.HeaderType.ContentType, "application/json")
    kittenwifi.rest_header(kittenwifi.HeaderType.ContentType, "processor mediatek")
    kittenwifi.rest_header(kittenwifi.HeaderType.UserAgent, "Mozilla 5.0")
    kittenwifi.mqtt_subscribe("/hello", 0)
    kittenwifi.rest_request("GET", "www.google.com")
    kittenwifi.rest_request("GET", "/api/test?apple=1")
    kittenwifi.mqtt_publish(
    "/Api",
    "token_auth_3af892",
    1
    )
    kittenwifi.wifi_init_pw(kittenwifi.SerialPorts.PORT1)
    kittenwifi.mqtt_sethost_auth(
    "iot.kittenbot.cn",
    "node01",
    "I:MICRO",
    "1253"
    )
    kittenwifi.mqtt_sethost_auth_port(
    "iot.kittenbot.cn",
    1883,
    "I:MICRO",
    "MICRO:CELL",
    "1253"
    )
    kittenwifi.mqtt_sethost_port("iot.kittenbot.cn", 1883, "I:MICRO")
    kittenwifi.mqtt_sethost_auth(
    "iot.kittenbot.cn",
    "I:MICRO",
    "MICRO:CELL",
    "1253"
    )
    kittenwifi.rest_host("iot.kittenbot.cn", 80, 443)
    kittenwifi.ntp_get(kittenwifi.NtpTimeType.s1970)
    kittenwifi.mqtt_sethost("iot.kittenbot.cn", "node01")
    kittenwifi.mqtt_sethost("iot.kittenbot.cn", "node01")
    kittenwifi.mqtt_sethost("iot.kittenbot.cn", "node01")
    kittenwifi.mqtt_sethost("iot.kittenbot.cn", "node01")
    kittenwifi.rest_request("GET", "/api/test?apple=1")
    kittenwifi.udp_comm("192.168.18.1", 1)
    kittenwifi.udp_comm("192.168.18.1", 1)
    kittenwifi.udp_send("Wifi port1")
    kittenwifi.wifi_init_pw(kittenwifi.SerialPorts.PORT1)
    kittenwifi.wifi_init_pw(kittenwifi.SerialPorts.PORT2)
    kittenwifi.wifi_init_pw(kittenwifi.SerialPorts.PORT3)
    kittenwifi.wifi_init_pw(kittenwifi.SerialPorts.PORT4)
    kittenwifi.udp_comm("192.168.18.1", 1)
    kittenwifi.udp_send("Micro:bit connected")
    kittenwifi.wifi_changename("MICRO:CELL")
    kittenwifi.wifi_init_pw(kittenwifi.SerialPorts.PORT1)
    kittenwifi.mqtt_publish(
    "/Api",
    "token_auth_3af892",
    1,
    1
    )
    if (true) {
        basic.showIcon(IconNames.Yes)
    } else {
        basic.showIcon(IconNames.No)
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.showLeds(`
        . . # . .
        # . # . #
        # . . . #
        # . . . #
        . # # # .
        `)
    basic.showLeds(`
        . # . . .
        . . # . .
        . # # # .
        . # # . .
        . # # # .
        `)
    basic.pause(1000)
})
radio.onReceivedString(function (receivedString) {
    for (let index = 0; index < 4; index++) {
        radio.setFrequencyBand(53)
        radio.setTransmitPower(7)
        radio.setGroup(1)
        radio.setTransmitSerialNumber(true)
        radio.sendNumber(12)
        radio.sendValue("Sim Card", 0)
        radio.sendValue("Movistar", 12)
        radio.sendString("telefono movil")
    }
    if (true) {
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . #
            # . . . #
            # # # # #
            `)
    } else {
        basic.showLeds(`
            . . # . .
            . # . # .
            # . # . #
            # . # . #
            # # # # #
            `)
    }
})
timeanddate.setDate(3, 1, 2026)
timeanddate.setTime(11, 30, 0, timeanddate.MornNight.AM)
basic.showLeds(`
    . # . . .
    . . # . .
    . # # # .
    . # # . .
    . # # # .
    `)
music.play(music.stringPlayable("C F D F - G F C5 ", 151), music.PlaybackMode.UntilDone)
basic.pause(200)
basic.showLeds(`
    . . # . .
    . # . . .
    # . # # #
    . # . . .
    . . # . .
    `)
basic.pause(1000)
basic.showLeds(`
    . . # . .
    . . . # .
    # # # . #
    . . . # .
    . . # . .
    `)
