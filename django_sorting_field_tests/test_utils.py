from django_sorting_field.utils import sort_by_order


class DummyItem(object):

    def __init__(self, item_id):
        self.id = item_id


def test_sort_by_order_none():
    items = [
        DummyItem(0),
        DummyItem(1),
        DummyItem(2),
    ]
    sorted_items = sort_by_order(items, None)
    assert sorted_items[0].id == 0
    assert sorted_items[1].id == 1
    assert sorted_items[2].id == 2
