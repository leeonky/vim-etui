from libs.extended_lock import Lock

statefull_object_list = {}
statefull_object_list_locker = Lock()

class StatefulObject(object):
	def __init__(self, name):
		def set_object():
			statefull_object_list[name] = self
		statefull_object_list_locker.synchronized(set_object);

	@staticmethod
	def get(name):
		def get_object():
			return statefull_object_list.get(name, None)
		return statefull_object_list_locker.synchronized(get_object)

	@staticmethod
	def delete(name):
		def delete_object():
			statefull_object_list.pop(name, None)
		return statefull_object_list_locker.synchronized(delete_object)

	@staticmethod
	def invoke(name, symbol, *args):
		try:
			obj = StatefulObject.get(name);
			method = getattr(obj, symbol);
			return method(*args)
		except:
			return None
