import unittest
from plugin.widgets.high_light import HighLight
from plugin.tests.fake_vim import TestWithFakeVim

class TestHighLight(TestWithFakeVim):

	def test_name_with_all_properties(self):
		light = HighLight(fg='1', bg='2', styles=[HighLight.Bold, HighLight.UnderLine, HighLight.Inverse]) 

		self.assertEqual(light.name(), 'etui_hl_fg1_bg2_bold_inverse_underline')

	def test_name_with_default_properties(self):
		light = HighLight(styles=[HighLight.Bold]) 

		self.assertEqual(light.name(), 'etui_hl_bold')

	def test_properties_with_all_properties(self):
		light = HighLight(fg='1', bg='2', styles=[HighLight.Bold, HighLight.UnderLine, HighLight.Inverse]) 

		self.assertEqual(light.properties(), 'ctermfg=1 guifg=1 ctermbg=2 guibg=2 cterm=bold,inverse,underline')

	def test_properties_with_default_properties(self):
		light = HighLight(styles=[HighLight.Bold]) 

		self.assertEqual(light.properties(), 'cterm=bold')

	def test_change_to_with_all_properties(self):
		light = HighLight(fg='1', bg='2', styles=[HighLight.Bold, HighLight.UnderLine, HighLight.Inverse]) 

		light = light.change_to(fg='2')

		self.assertEqual(light.name(), 'etui_hl_fg2_bg2_bold_inverse_underline')
		self.assertEqual(light.properties(), 'ctermfg=2 guifg=2 ctermbg=2 guibg=2 cterm=bold,inverse,underline')

	def test_change_to_with_default_properties(self):
		light = HighLight(styles=[HighLight.Bold]) 

		light = light.change_to(fg='2')

		self.assertEqual(light.name(), 'etui_hl_fg2_bold')
		self.assertEqual(light.properties(), 'ctermfg=2 guifg=2 cterm=bold')