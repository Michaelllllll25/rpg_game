from character import Character

def test_character_attributes():
    c = Character("Michael", 400, 300, 200, ["fire", "water"], ["hammer", "sword"], 500)
    assert c.name == "Michael"
    assert c.hp == 400
    assert c.vb == 300
    assert c.atk == 200
    assert c.magic == ["fire", "water"]
    assert c.items == ["hammer", "sword"]
    assert c.wallet == 500

# test methods
def test_get_hp():
    c = Character("Michael", 400, 300, 200, ["fire", "water"], ["hammer", "sword"], 500)
    assert c.get_hp() == 400


def test_get_vb():
    c = Character("Michael", 400, 300, 200, ["fire", "water"], ["hammer", "sword"], 500)
    assert c.get_vb() == 300



