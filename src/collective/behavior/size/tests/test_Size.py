import mock
import unittest


class TestSize(unittest.TestCase):

    def test_subclass(self):
        from collective.behavior.size.behavior import Size
        self.assertTrue(issubclass(Size, object))

    def create_instance(self, context=mock.Mock()):
        from collective.behavior.size.behavior import Size
        return Size(context)

    def test_instance(self):
        instance = self.create_instance()
        from collective.behavior.size.behavior import Size
        self.assertIsInstance(instance, Size)

    def test_instance_provides_ISize(self):
        instance = self.create_instance()
        from collective.behavior.size.interfaces import ISize
        self.assertTrue(ISize.providedBy(instance))

    def test_instance__verifyObject(self):
        instance = self.create_instance()
        instance.context.width = 0.0
        instance.context.height = 0.0
        instance.context.depth = 0.0
        from collective.behavior.size.interfaces import ISize
        from zope.interface.verify import verifyObject
        self.assertTrue(verifyObject(ISize, instance))

    def test__set_size_positive(self):
        instance = self.create_instance()
        instance._set_size('aaa', 2.0)
        self.assertEqual(instance.context.aaa, 2.0)

    def test__set_size__None(self):
        instance = self.create_instance()
        instance.context.weight = 2.0
        instance._set_size('weight', None)
        self.assertEqual(instance.context.weight, 2.0)

    def test__set_size__ValueError(self):
        instance = self.create_instance()
        instance.context.weight = 2.0
        instance._set_size('weight', 'AAA')
        self.assertEqual(instance.context.weight, 2.0)

    def test__set_size_positive_attribute(self):
        instance = self.create_instance()
        instance.context.weight = 2.0
        instance._set_size('weight', 3.0)
        self.assertEqual(instance.context.weight, 3.0)

    def test_weight_set(self):
        instance = self.create_instance()
        instance._set_size = mock.Mock()
        instance.weight = 2.0
        instance._set_size.called_with('weight', 2.0)

    def test_width(self):
        instance = self.create_instance()
        instance.context.width = 2.0
        self.assertEqual(instance.width, 2.0)

    def test_width_set(self):
        instance = self.create_instance()
        instance._set_size = mock.Mock()
        instance.width = 2.0
        instance._set_size.called_with('width', 2.0)

    def test_height(self):
        instance = self.create_instance()
        instance.context.height = 2.0
        self.assertEqual(instance.height, 2.0)

    def test_height_set(self):
        instance = self.create_instance()
        instance._set_size = mock.Mock()
        instance.height = 2.0
        instance._set_size.called_with('height', 2.0)

    def test_depth(self):
        instance = self.create_instance()
        instance.context.depth = 2.0
        self.assertEqual(instance.depth, 2.0)

    def test_depth_set(self):
        instance = self.create_instance()
        instance._set_size = mock.Mock()
        instance.depth = 2.0
        instance._set_size.called_with('height', 2.0)

    def test_dimension_zero(self):
        instance = self.create_instance()
        instance.width = 0.0
        instance.height = 0.0
        instance.depth = 0.0
        self.assertEqual(instance.dimension, 0.0)

    def test_dimension_positive(self):
        instance = self.create_instance()
        instance.width = 100.0
        instance.height = 200.0
        instance.depth = 300.0
        self.assertEqual(instance.dimension, 6.0)

    def test_calculated_weight__rate_None(self):
        instance = self.create_instance()
        instance.weight = 2000.0
        self.assertEqual(instance.calculated_weight(), 2.0)

    def test_calculated_weight__rate_not_float(self):
        instance = self.create_instance()
        instance.weight = 2000.0
        self.assertEqual(instance.calculated_weight(rate='AAA'), 2.0)

    def test_calculated_weight__rate_minus(self):
        instance = self.create_instance()
        instance.weight = 2000.0
        self.assertEqual(instance.calculated_weight(rate=-2.0), 2.0)

    def test_calculated_weight__dimension_weight_negative(self):
        instance = self.create_instance()
        instance.weight = 2000.0
        instance.width = 50.0
        instance.height = 100.0
        instance.depth = 100.0
        self.assertEqual(instance.calculated_weight(rate=1.0), 2.0)

    def test_calculated_weight__dimension_weight_positive(self):
        instance = self.create_instance()
        instance.weight = 2000.0
        instance.width = 400.0
        instance.height = 100.0
        instance.depth = 100.0
        self.assertEqual(instance.calculated_weight(rate=1.0), 4.0)
