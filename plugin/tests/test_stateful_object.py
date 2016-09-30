from mock import patch
from mock import MagicMock
import unittest
from plugin.widgets.stateful_object import StatefulObject

class TestStatefulObject(unittest.TestCase):

	def test_create_with_name(self):
		obj = StatefulObject('test')
		self.assertEqual(obj, StatefulObject.get('test'))

	def test_create_set_with_name(self):
		obj = object()
		StatefulObject.set('new_obj', obj)
		self.assertEqual(obj, StatefulObject.get('new_obj'))

	def test_delete(self):
		obj = StatefulObject('test')
		StatefulObject.delete('test')
		self.assertEqual(None, StatefulObject.get('test'))

	def test_invoke(self):
		class Test(StatefulObject):
			def __init__(self):
				super(Test, self).__init__('test')

		obj = Test();
		obj.fun = MagicMock(return_value=4)

		self.assertEqual(4, StatefulObject.invoke('test', 'fun', 1, 2))
		obj.fun.assert_called_with(1, 2)

	def test_invoke(self):
		StatefulObject.delete('test')
		self.assertEqual(None, StatefulObject.invoke('test', 'fun'))
