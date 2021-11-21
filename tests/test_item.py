from item import Item

def test_item_attributes():
    i = Item("Sword", "Weapon", "Deals damage", 100)
    assert i.name == "Sword"
    assert i.type == "Weapon"
    assert i.description == "Deals damage"
    assert i.value == 100

