Django Sorting Field
====================

* This package implements a Django form field + widget for drag & drog sorting of items
* Sorting any item with a field called ``id`` is supported
* The drag and drop feature has been implemented with `html5sortable <https://lukasoppermann.github.io/html5sortable/index.html>`_.

Known limitations
-----------------

* Refreshing the items on the widget not (yet?) supported out of the box
* No tests

Example of the widget
---------------------

.. image:: readme-media/example.gif

Usage
-----

The sort order field should be implemented on the model containing the sorted objects.
This allows ordering of different instances of the same item set differently.

Let's say you have image CarouselPlugin, Carousel, and Picture models, and you wish to be able to
sort the same Carousel instance differently on each CarouselPlugin.

You also have a CMSPlugin object for the carousel.

.. code-block:: python

	class Carousel(models.Model):
		pass


	class Picture(models.Model):
		carousel = models.ForeignKey(Carousel, related_name="pictures")
		image = SomeImageField()
		name = models.CharField()


	class CarouselPlugin(CMSPlugin):
		carousel = models.ForeignKey(Carousel, related_name="x")


	class CMSCarouselPlugin(CMSPluginBase):
		model = CarouselPlugin

		def render(self, context, instance, placeholder):
			context.update({
				"pictures": self.instance.carousel.pictures.all(),
			})
			return context


Achieving the wanted behavior can be done in the following steps:

Add a (nullable) TextField to the model containing the order information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

	class CarouselPlugin(CMSPlugin):
		carousel = models.ForeignKey(Carousel, related_name="x")
		carousel_order = models.TextField(null=True)


Add the SortingFormField to the CMS Plugin and populate it
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

	from django_sorting_field.fields import SortingFormField

	class CarouselPluginForm(forms.ModelForm):
		carousel_order = SortingFormField()

		def __init__(self, *args, **kwargs):
			super(CarouselPluginForm, self).__init__(*args, **kwargs)
			self.fields["carousel_order"].populate(
				items=self.instance.carousel.pictures.all(),
			)

	class CMSCarouselPlugin(CMSPluginBase):
		model = CarouselPlugin
		form = CarouselPluginForm

		def render(self, context, instance, placeholder):
			context.update({
				"pictures": self.instance.carousel.pictures.all(),
			})
			return context

Finally, sort the items passed to the context data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

	from django_sorting_field.utils import sort_by_order

		class CMSCarouselPlugin(CMSPluginBase):
		model = CarouselPlugin
		form = CarouselPluginForm

		def render(self, context, instance, placeholder):
			context.update({
				"pictures": sort_by_order(
					self.instance.carousel.pictures.all(),
					self.instance.carousel_order
				),
			})
			return context
