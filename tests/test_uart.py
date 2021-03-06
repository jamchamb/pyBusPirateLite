from pyBusPirateLite.UART import UART


def test_init():
    uart = UART(connect=False)
    assert uart.portname == ''


def test_connect():
    uart = UART(connect=False)
    uart.connect()
    assert uart.portname != ''
    uart.hw_reset()


def test_enter():
    uart = UART(connect=False)
    uart.connect()
    uart.enter()
    assert uart.mode == 'uart'
    uart.hw_reset()


def test_connect_on_init():
    uart = UART()
    assert uart.mode == 'uart'
    uart.hw_reset()


def test_modestring():
    uart = UART()
    assert uart.modestring == 'ART1'
    uart.hw_reset()


def test_echo():
    pass


def test_manual_speed_cfg():
    pass


def test_begin_input():
    pass


def test_end_input():
    pass


def test_enter_bridge_mode():
    pass


def def_set_cfg():
    pass


def test_read_cfg():
    pass
