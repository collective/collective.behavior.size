from collective.behavior.size import _
from zope.interface import Attribute
from zope.interface import Interface
from zope.schema import Float


class ISize(Interface):
    """Interface for Size behavior."""

    weight = Float(
        title=_(u'Weight'),
        description=_(u'Weight in gram.'),
        min=0.0)

    width = Float(
        title=_(u'Weight'),
        description=_(u'Weight in centimeter.'))

    height = Float(
        title=_(u'Height'),
        description=_(u'Height in centimeter.'))

    depth = Float(
        title=_(u'Depth'),
        description=_(u'Depth in centimeter.'))

    size = Attribute('Sum of sizes')

    def sub_size(value):
        """Decrease size by value and return the result."""

    def add_size(value):
        """Add size by value and return the result."""
