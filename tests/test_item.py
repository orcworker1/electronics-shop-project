"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest
def test_calculate_total_price():
    item1 = Item('mac',20000,10)
    item2 = Item('apple',10000,4)
    total_price = item1.calculate_total_price()
    assert total_price == 20000 * 10
    total_price = item2.calculate_total_price()
    assert total_price == 10000 * 4

def test_append_list():
    item1 = Item('apple',10000,10)
    assert item1.name == 'apple'
    assert item1.price == 10000
    assert item1.quantity == 10

def test_apply_discount():
    item1 = Item('apple',10000,10)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0         