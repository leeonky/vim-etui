class HighLight(object):
	Bold = 'bold'
	UnderLine = 'underline'
	Inverse = 'inverse'
	def __init__(self, fg=None, bg=None, styles=[]):
		self._name = None
		self._properties = None
		self.fg = fg
		self.bg = bg
		self.styles = sorted(styles)

	def name(self):
		if self._name is None:
			sub_names = []
			if self.fg:
				sub_names.append('fg%s' % self.fg)
			if self.bg:
				sub_names.append('bg%s' % self.bg)
			self._name = 'etui_hl_' + '_'.join(sub_names + self.styles)
		return self._name

	def properties(self):
		if self._properties is None:
			properties = []
			if self.fg:
				properties.append('ctermfg=%s guifg=%s' % (self.fg, self.fg))
			if self.bg:
				properties.append('ctermbg=%s guibg=%s' % (self.bg, self.bg))
			if len(self.styles)>0:
				properties.append('cterm=%s' % ','.join(self.styles))
			self._properties = ' '.join(properties)
		return self._properties
	
	def change_to(self, fg=None, bg=None, styles=None):
		if styles is None:
			styles = self.styles
		return HighLight(fg=(fg or self.fg), bg=(bg or self.bg), styles=styles)

	def none_high_light(self):
		return self.fg is None and self.bg is None and self.styles==[]

	def change_to_reset(self):
		return HighLight();

	def add_styles(self, *styles):
		return self.change_to(styles=sorted(set(self.styles + list(styles))))

	def remove_styles(self, *styles):
		return self.change_to(styles=sorted(set(self.styles) - set(styles)))
