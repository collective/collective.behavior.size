from collective.behavior.size import _
from plone.supermodel.model import Schema
from zope import schema
from zope.interface import Attribute


class ISize(Schema):
    """Interface for Size behavior."""

    weight = schema.Float(
        title=_(u'Weight'),
        description=_(u'Weight in gram.'),
        min=0.0,
        required=False)

    width = schema.Float(
        title=_(u'Width'),
        description=_(u'Width in centimeter.'),
        min=0.0,
        required=False)

    height = schema.Float(
        title=_(u'Height'),
        description=_(u'Height in centimeter.'),
        min=0.0,
        required=False)

    depth = schema.Float(
        title=_(u'Depth'),
        description=_(u'Depth in centimeter.'),
        min=0.0,
        required=False)

    dimension = Attribute('Dimemsion in the cube of meter.')

    def calculated_weight(rate):  # pragma: no cover
        """Return calculated weight for shipping."""
