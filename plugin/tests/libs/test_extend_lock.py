import unittest
from mock import MagicMock
from plugin.widgets.libs.extended_lock import Lock

class TestExtendedLock(unittest.TestCase):

	def setUp(self):
		class FakeLock(object):
			pass
		self.fake_lock = FakeLock()
		self.fake_lock.acquire = MagicMock()
		self.fake_lock.release = MagicMock()
		self.lock = Lock(self.fake_lock)

	def test_should_call_lock_and_release_and_return_value(self):
		return_object = object()
		fun = MagicMock(return_value = return_object)

		self.assertEqual(self.lock.synchronized(fun), return_object)
		self.fake_lock.acquire.assert_called_with()
		self.fake_lock.release.assert_called_with()

	def test_should_call_release_even_raise_error(self):
		def fun():
			raise Exception()
		try:
			self.lock.synchronized(fun)
			self.fail('fail')
		except:
			self.fake_lock.acquire.assert_called_with()
			self.fake_lock.release.assert_called_with()

