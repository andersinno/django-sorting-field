import json

from django import forms
from django.utils.encoding import force_text

from .utils import clean_order_json, sort_by_order
from .widgets import SortingWidget


class SortedItem(object):

    def __init__(self, identifier, label):
        self.id = identifier
        self.label = label


class SortingFormField(forms.CharField):

    def __init__(self, *args, **kwargs):
        kwargs.update({
            "widget": SortingWidget(),
            "required": False,
        })
        self.items = []
        super(SortingFormField, self).__init__(*args, **kwargs)

    def populate(self, items):
        self.items = [SortedItem(item.pk, force_text(item)) for item in items]

    def prepare_value(self, value):
        value = clean_order_json(value)
        return sort_by_order(self.items, value)

    def to_python(self, value):
        value = clean_order_json(value)
        return json.dumps(value)
