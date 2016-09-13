class ExtendedInt(int):

	@staticmethod
	def _to_alphabet(i):
		if i < 26:
			return '%c' % (ord('a') + i)
		return ExtendedInt._to_alphabet(i/26) + ExtendedInt._to_alphabet(i%26)

	def to_alphabet(self):
		return ExtendedInt._to_alphabet(self)
