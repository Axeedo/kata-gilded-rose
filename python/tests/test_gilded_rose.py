from gilded_rose import GildedRose, Item, main
from helpers import readfile, get_output


def test_default_item():
    default_item = Item("default", sell_in=10, quality=20)
    items = [default_item]
    shop = GildedRose(items)

    shop.update_quality()

    assert default_item.sell_in == 9
    assert default_item.quality == 19


def test_golden_master():
    original = readfile("golden-master/expected-output.txt").splitlines()
    current = get_output(main).splitlines()

    for i in range(0, len(original)):
        assert original[i] == current[i]


def test_conjured_degradation():
    conjured_item = Item("Conjured Mana Cake", sell_in=10, quality=20)
    items = [conjured_item]
    shop = GildedRose(items)

    shop.update_quality()

    assert conjured_item.sell_in == 9
    assert conjured_item.quality == 18
