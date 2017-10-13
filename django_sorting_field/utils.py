import json

import six


def clean_order_json(value):
        value = "[]" if value is None else value

        try:
            return json.loads(value)
        except ValueError:
            return []


def iterate_in_order(items, order):
    # In case our order is still in json format
    if isinstance(order, six.string_types):
        order = clean_order_json(order)

    items_by_id = {item.id: item for item in items}

    # Return items that are ordered first
    for entry in order:
        if entry not in items_by_id:
            continue
        yield items_by_id.pop(entry)

    # Return the rest
    for identifier, item in items_by_id.iteritems():
        yield item


def sort_by_order(items, order):
    return [item for item in iterate_in_order(items, order)]
