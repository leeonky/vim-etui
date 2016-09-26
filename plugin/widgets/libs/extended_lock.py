import threading

class Lock(object):
	def __init__(self):
		self.locker = threading.Lock()

	def synchronized(self, proc):
		try:
			self.locker.acquire()
			return proc()
		finally:
			self.locker.release()

