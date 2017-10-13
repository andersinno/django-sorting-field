from django.forms.widgets import Widget
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe


class SortingWidget(Widget):
    template_name = 'sorting/widgets/sorting_widget.html'

    class Media:
        css = {
            "all": ("sorting/css/sorting_widget.css",)
        }
        js = (
            "sorting/js/html.sortable.min.js",
            "sorting/js/sorting_widget.js",
        )

    def render(self, name, value, attrs=None):
        context = attrs
        context.update({
            "items": value,
            "name": name,
        })
        html = render_to_string(self.template_name, context)
        return mark_safe(html)
