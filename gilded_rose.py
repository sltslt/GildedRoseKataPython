# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):
    normal_rate=1
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def range_normal_quality(self, item: Item):
        if item.quality > 50:
            item.quality = 50
        if item.quality < 0:
            item.quality = 0
    def update_sell_in(self, item: Item):
        item.sell_in = item.sell_in - 1
    def update_normal_quality(self, item: Item, rate):
        if item.sell_in>0:
            item.quality = item.quality - rate
        else:
            item.quality = item.quality - 2 * rate
    def update_normal_item(self, item: Item):
        self.update_normal_quality(item, self.normal_rate)
        self.update_sell_in(item)
        self.range_normal_quality(item)
    def update_conjured(self, item: Item):
        self.update_normal_quality(item, 2 * self.normal_rate)
        self.update_sell_in(item)
        self.range_normal_quality(item)
    def update_sulfuras(self, item: Item):
        item.quality = 80
        item.sell_in = item.sell_in
    def update_brie(self, item: Item):
        item.quality = item.quality + self.normal_rate
        self.update_sell_in(item)
        self.range_normal_quality(item)
    def update_backstage(self, item: Item):
        item.quality += self.normal_rate
        if item.sell_in <= 10:
            item.quality += self.normal_rate
        if item.sell_in <= 5:
            item.quality += self.normal_rate
        self.update_sell_in(item)
        if item.sell_in < 0:
            item.quality = 0
        self.range_normal_quality(item)


    def update_quality(self):
        for item in self.items:
            if item.name == "Conjured Mana Cake":
                self.update_conjured(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage(item)
            elif item.name == "Aged Brie":
                self.update_brie(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self.update_sulfuras(item)
            else:
                self.update_normal_item(item)

    # def update_quality(self):
    #     for item in self.items:
    #         if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
    #             if item.quality > 0:
    #                 if item.name != "Sulfuras, Hand of Ragnaros":
    #                     item.quality = item.quality - 1
    #         else:
    #             if item.quality < 50:
    #                 item.quality = item.quality + 1
    #                 if item.name == "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.sell_in < 11:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #                     if item.sell_in < 6:
    #                         if item.quality < 50:
    #                             item.quality = item.quality + 1
    #         if item.name != "Sulfuras, Hand of Ragnaros":
    #             item.sell_in = item.sell_in - 1
    #         if item.sell_in < 0:
    #             if item.name != "Aged Brie":
    #                 if item.name != "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.quality > 0:
    #                         if item.name != "Sulfuras, Hand of Ragnaros":
    #                             item.quality = item.quality - 1
    #                 else:
    #                     item.quality = item.quality - item.quality
    #             else:
    #                 if item.quality < 50:
    #                     item.quality = item.quality + 1
    #
    #
