from collective.behavior.size import _
from zope.interface import Attribute
from zope.interface import Interface
from zope.schema import Float


class ISize(Interface):
    """Interface for Size behavior."""

    weight = Float(
        title=_(u'Weight'),
        description=_(u'Weight in gram.'),
        min=0.0,
        required=False)

    width = Float(
        title=_(u'Width'),
        description=_(u'Width in centimeter.'),
        min=0.0,
        required=False)

    height = Float(
        title=_(u'Height'),
        description=_(u'Height in centimeter.'),
        min=0.0,
        required=False)

    depth = Float(
        title=_(u'Depth'),
        description=_(u'Depth in centimeter.'),
        min=0.0,
        required=False)

    dimension = Attribute('Dimemsion in the cube of meter.')

    def calculated_weight(rate):  # pragma: no cover
        """Return calculated weight for shipping."""
