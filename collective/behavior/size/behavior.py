from collective.behavior.size.interfaces import ISize
from plone.directives import form
from zope.interface import alsoProvides
from zope.interface import implements
import logging

logger = logging.getLogger(__name__)


alsoProvides(ISize, form.IFormFieldProvider)


class Size(object):
    """
    """
    implements(ISize)

    def __init__(self, context):
        self.context = context

    def _set_size(self, attr, value):
        """Setting weight

        :param attr: Name of attribute.
        :type attr: str

        :param value: Weight in gram.
        :type value: float
        """
        if value is not None:
            try:
                setattr(self.context, attr, float(value))
            except ValueError:
                logger.warn('The value should be float, but not.')

    @property
    def weight(self):
        return getattr(self.context, 'weight', 0.0)

    @weight.setter
    def weight(self, value):
        """Setting weight

        :param value: Weight in gram.
        :type value: float
        """
        self._set_size('weight', value)

    @property
    def width(self):
        return getattr(self.context, 'width', 0.0)

    @width.setter
    def width(self, value):
        """Setting width

        :param value: Weight in gram.
        :type value: float
        """
        self._set_size('width', value)

    @property
    def height(self):
        return getattr(self.context, 'height', 0.0)

    @height.setter
    def height(self, value):
        """Setting height

        :param value: Weight in gram.
        :type value: float
        """
        self._set_size('height', value)

    @property
    def depth(self):
        return getattr(self.context, 'depth', 0.0)

    @depth.setter
    def depth(self, value):
        """Setting depth

        :param value: Weight in gram.
        :type value: float
        """
        self._set_size('depth', value)

    @property
    def dimension(self):
        """Dimemsion in the cube of meter.

        :rtype: float
        """
        return self.width * self.height * self.depth / 10.0 ** 6

    def calculated_weight(self, rate=None):
        """Returns calculated weight based on rate in kg.

        :param rate: kg / m **3
        :param type: float

        :rtype: float
        """
        weight_in_kg = self.weight / 1000.0
        if rate and isinstance(rate, float) and rate > 0.0:
            dimension_weight = self.dimension * rate
            if dimension_weight > weight_in_kg:
                return dimension_weight
        return weight_in_kg
