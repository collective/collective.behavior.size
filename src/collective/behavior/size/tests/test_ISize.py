import unittest


class TestISize(unittest.TestCase):

    def test_subclass(self):
        from collective.behavior.size.interfaces import ISize
        from zope.interface import Interface
        self.assertTrue(issubclass(ISize, Interface))

    def get_schema(self, name):
        """Get schema by name.

        :param name: Name of schema.
        :type name: str
        """
        from collective.behavior.size.interfaces import ISize
        return ISize.get(name)

    def test_weight__instance(self):
        schema = self.get_schema('weight')
        from zope.schema import Float
        self.assertIsInstance(schema, Float)

    def test_weight__title(self):
        schema = self.get_schema('weight')
        self.assertEqual(schema.title, u'Weight')

    def test_weight__description(self):
        schema = self.get_schema('weight')
        self.assertEqual(
            schema.description, u'Weight in gram.')

    def test_weight__min(self):
        schema = self.get_schema('weight')
        self.assertEqual(schema.min, 0.0)

    def test_weight__required(self):
        schema = self.get_schema('weight')
        self.assertFalse(schema.required)

    def test_width__instance(self):
        schema = self.get_schema('width')
        from zope.schema import Float
        self.assertIsInstance(schema, Float)

    def test_width__title(self):
        schema = self.get_schema('width')
        self.assertEqual(schema.title, u'Width')

    def test_width__description(self):
        schema = self.get_schema('width')
        self.assertEqual(
            schema.description, u'Width in centimeter.')

    def test_width__min(self):
        schema = self.get_schema('width')
        self.assertEqual(schema.min, 0.0)

    def test_width__required(self):
        schema = self.get_schema('width')
        self.assertFalse(schema.required)

    def test_height__instance(self):
        schema = self.get_schema('height')
        from zope.schema import Float
        self.assertIsInstance(schema, Float)

    def test_height__title(self):
        schema = self.get_schema('height')
        self.assertEqual(schema.title, u'Height')

    def test_height__description(self):
        schema = self.get_schema('height')
        self.assertEqual(
            schema.description, u'Height in centimeter.')

    def test_height__min(self):
        schema = self.get_schema('height')
        self.assertEqual(schema.min, 0.0)

    def test_height__required(self):
        schema = self.get_schema('height')
        self.assertFalse(schema.required)

    def test_depth__instance(self):
        schema = self.get_schema('depth')
        from zope.schema import Float
        self.assertIsInstance(schema, Float)

    def test_depth__title(self):
        schema = self.get_schema('depth')
        self.assertEqual(schema.title, u'Depth')

    def test_depth__description(self):
        schema = self.get_schema('depth')
        self.assertEqual(
            schema.description, u'Depth in centimeter.')

    def test_depth__min(self):
        schema = self.get_schema('depth')
        self.assertEqual(schema.min, 0.0)

    def test_depth__required(self):
        schema = self.get_schema('depth')
        self.assertFalse(schema.required)

    def test_dimension__instance(self):
        from zope.interface import Attribute
        schema = self.get_schema('dimension')
        self.assertIsInstance(schema, Attribute)

    def test_dimension__doc(self):
        schema = self.get_schema('dimension')
        self.assertEqual(schema.getDoc(), 'Dimemsion in the cube of meter.')
