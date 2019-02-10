import json
import urllib.request

def converter(currency, value):
	req=urllib.request.Request('http://data.fixer.io/api/latest?access_key=5379d7cd801d1babe62148df3c4e85f8&callback=convert', headers ={'User-Agent': 'howCode Currency Bot'})
	data=urllib.request.urlopen(req).read()
	data = data.decode('utf-8')
	data = json.loads(data[8:len(data)-1])

	value = value*data['rates'][currency]/data['rates']['KZT']

	return value

from kivy.app import App
from kivy.config import Config 

from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget


from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

Config.set('graphics','resizable','0');
Config.set('graphics','width','640');
Config.set('graphics','height','480');
    
class CurrencyConverterApp(App):

	def clear_txt(self, instance):
		self.txtkzt.text = "0"
		self.txtusd.text = "0"
		self.txteur.text = "0"
		self.txtrub.text = "0"
		
	def update_text(self, instance):
		self.eur = converter('EUR', float(self.txtkzt.text))
		self.usd = converter('USD', float(self.txtkzt.text))
		self.rub = converter('RUB', float(self.txtkzt.text))

		self.txteur.text = str(round(self.eur,2))
		self.txtusd.text = str(round(self.usd,2))
		self.txtrub.text = str(round(self.rub,2))
		
	def build(self):
		self.txt = "0"
		bl=BoxLayout(orientation = 'vertical',padding = [30,30,30,30])
		gl1 = GridLayout(rows = 1, spacing = 40, size_hint = (.25, .25) )
		gl2 = GridLayout(rows = 1, spacing = 40, size_hint = (.25, .25) )
		gl3 = GridLayout(rows = 1, spacing = 40, size_hint = (.25, .25) )
		gl4 = GridLayout(rows = 1, spacing = 40, size_hint = (.25, .25) )

		self.txtkzt = TextInput( text = "1", font_size = 30, size_hint = (None,None),size = (180,70))
		self.lblkzt = Label(text = 'KZT', font_size = 30, halign = 'justify', size_hint = (.3,.3)) 
		self.btnkzt = Button(text='convert', size_hint=(None, None), size=(80, 50),pos = (480*.25,640*.25 -100), on_press = self.update_text)
		self.btnclear = Button(text='clear', size_hint=(None, None), size=(80, 50),pos = (480*.25,640*.25), on_release = self.clear_txt)

		self.txteur = TextInput(multiline=False, text = "0", font_size = 30, size_hint = (None,None), size = (180,75))
		self.lbleur = Label(text = "EUR", font_size = 30, halign= "right", size_hint = (.3,.3))
		
		self.txtusd = TextInput( text = "0", font_size = 30, size_hint = (None,None), size = (180,75))
		self.lblusd = Label(text = "USD", font_size = 30, valign = "center", halign= "right", size_hint = (1,.2))

		self.txtrub = TextInput( text = "0", font_size = 30, size_hint = (None,None), size = (180,75))
		self.lblrub = Label(text = "RUB", font_size = 30, valign = "center", halign= "center", size_hint = (1,.2))
		
		gl1.add_widget (self.lblkzt)
		gl1.add_widget (self.txtkzt)
		gl1.add_widget (self.btnkzt)
		gl1.add_widget(self.btnclear)
			
		gl2.add_widget( self.lbleur)
		gl2.add_widget( self.txteur)
	
		gl3.add_widget( self.lblusd)
		gl3.add_widget( self.txtusd)
	
		gl4.add_widget(self.lblrub)
		gl4.add_widget(self.txtrub)
		
		bl.add_widget(gl1)
		bl.add_widget(gl2)
		bl.add_widget(gl3)
		bl.add_widget(gl4)
		
		return bl;

	def btn_press(self,instance):
		print("Button clicked")		
		
if __name__=="__main__":
	CurrencyConverterApp().run()