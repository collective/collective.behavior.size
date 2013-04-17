from collective.behavior.size.schema import SizeSchema


class ISize(SizeSchema):
    """Interface for behavior: Size"""

    def dimension():  # pragma: no cover
        """Dimemsion in the cube of meter."""

    def calculated_weight(rate):  # pragma: no cover
        """Return calculated weight for shipping."""
