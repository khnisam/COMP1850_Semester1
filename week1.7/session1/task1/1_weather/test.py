from weather import comfort_level

def test_cold():
    assert comfort_level(0) == "Cold"
    assert comfort_level(7.5) == "Cold"
    assert comfort_level(14) == "Cold"

def test_hot():
    assert comfort_level(25) == "Hot"
    assert comfort_level(50) == "Hot"
    assert comfort_level(99) == "Hot"

def test_ok():
    assert comfort_level(15) == "OK"
    assert comfort_level(20) == "OK"
    assert comfort_level(25) == "OK"