from collective.behavior.size.interfaces import ISize
from plone.directives import form
from rwproperty import getproperty
from rwproperty import setproperty
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

    @getproperty
    def weight(self):
        return getattr(self.context, 'weight', 0.0)

    @setproperty
    def weight(self, value):
        """Setting weight

        :param value: Weight in gram.
        :type value: float
        """
        if isinstance(value, float):
            # Set weight
            setattr(self.context, 'weight', value)
        else:
            raise ValueError('Not Float')

    @getproperty
    def width(self):
        return getattr(self.context, 'width', 0.0)

    @setproperty
    def width(self, value):
        """Setting width

        :param value: Weight in gram.
        :type value: float
        """
        if isinstance(value, float):
            # Set width
            setattr(self.context, 'width', value)
        else:
            raise ValueError('Not Float')

    @getproperty
    def height(self):
        return getattr(self.context, 'height', 0.0)

    @setproperty
    def height(self, value):
        """Setting height

        :param value: Weight in gram.
        :type value: float
        """
        if isinstance(value, float):
            # Set height
            setattr(self.context, 'height', value)
        else:
            raise ValueError('Not Float')

    @getproperty
    def depth(self):
        return getattr(self.context, 'depth', 0.0)

    @setproperty
    def depth(self, value):
        """Setting depth

        :param value: Weight in gram.
        :type value: float
        """
        if isinstance(value, float):
            # Set depth
            setattr(self.context, 'depth', value)
        else:
            raise ValueError('Not Float')

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
