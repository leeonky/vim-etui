import threading

class Lock(object):
	def __init__(self, locker = None):
		self.locker = locker or threading.Lock()

	def synchronized(self, proc):
		try:
			self.locker.acquire()
			return proc()
		finally:
			self.locker.release()

