# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # def test_foo(self):
    #     items = [Item("foo", 0, 0)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEqual("foo", items[0].name)

    def test_normal(self):
        name = "+5 Dexterity Vest"
        gr = GildedRose([Item(name, 0, 19),Item(name, 2, 19)])
        gr.update_quality()
        self.assertEqual(-1,gr.items[0].sell_in)
        self.assertEqual(17, gr.items[0].quality)

        self.assertEqual(1, gr.items[1].sell_in)
        self.assertEqual(18, gr.items[1].quality)

    def test_sulfuras(self):
        name = "Sulfuras, Hand of Ragnaros"
        gr = GildedRose([Item(name, 10, 80), Item(name, 0,80)])
        gr.update_quality()
        self.assertEqual(10, gr.items[0].sell_in)
        self.assertEqual(80, gr.items[0].quality)

        self.assertEqual(0, gr.items[1].sell_in)
        self.assertEqual(80, gr.items[1].quality)
    def test_conjured(self):
        name = "Conjured Mana Cake"
        gr = GildedRose([Item(name, 10, 20),Item(name, 0, 10)])
        gr.update_quality()
        self.assertEqual(9,gr.items[0].sell_in)
        self.assertEqual(18, gr.items[0].quality)

        self.assertEqual(-1, gr.items[1].sell_in)
        self.assertEqual(6, gr.items[1].quality)

    def test_brie_item(self):
        name = "Aged Brie"
        gr = GildedRose([Item(name, 10, 50), Item(name, 0, 10), Item(name, 12, 32)])
        gr.update_quality()
        self.assertEqual(9, gr.items[0].sell_in)
        self.assertEqual(50, gr.items[0].quality)

        self.assertEqual(-1, gr.items[1].sell_in)
        self.assertEqual(11, gr.items[1].quality)

        self.assertEqual(11, gr.items[2].sell_in)
        self.assertEqual(33, gr.items[2].quality)

    def test_backstage_pass_item(self):
        name = "Backstage passes to a TAFKAL80ETC concert"
        gr = GildedRose([Item(name, 10, 32), Item(name, 0, 10), Item(name, 12, 32), Item(name, 4, 32), Item(name, 4, 50)])
        gr.update_quality()
        self.assertEqual(9, gr.items[0].sell_in)
        self.assertEqual(34, gr.items[0].quality)

        self.assertEqual(-1, gr.items[1].sell_in)
        self.assertEqual(0, gr.items[1].quality)

        self.assertEqual(11, gr.items[2].sell_in)
        self.assertEqual(33, gr.items[2].quality)

        self.assertEqual(3, gr.items[3].sell_in)
        self.assertEqual(35, gr.items[3].quality)

        self.assertEqual(3, gr.items[4].sell_in)
        self.assertEqual(50, gr.items[4].quality)





if __name__ == '__main__':
    unittest.main()
