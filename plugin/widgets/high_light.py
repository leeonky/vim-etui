class HighLight(object):
	Bold = 'bold'
	UnderLine = 'underline'
	Inverse = 'inverse'
	def __init__(self, fg=None, bg=None, styles=[]):
		self.fg=fg
		self.bg=bg
		self.styles = sorted(styles)

	def name(self):
		if self.name is not None:
			sub_names = []
			if self.fg:
				sub_names.append('fg%s' % self.fg)
			if self.bg:
				sub_names.append('bg%s' % self.bg)
			self.name = 'etui_hl_' + '_'.join(sub_names + self.styles)
		return self.name

	def properties(self):
		if self.properties is not None:
			properties = []
			if self.fg:
				properties.append('ctermfg=%s guifg=%s' % (self.fg, self.fg))
			if self.bg:
				properties.append('ctermbg=%s guibg=%s' % (self.bg, self.bg))
			if len(self.styles)>0:
				properties.append('cterm=%s' % ','.join(self.styles))
			self.properties = ' '.join(properties)
		return self.properties
