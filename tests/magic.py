from magic import Spell

def test_spell_attributes():
    s = Spell("Fire", 500, 300)
    assert s.name == "Fire"
    assert s.dmg == 500
    assert s.cost == 300
