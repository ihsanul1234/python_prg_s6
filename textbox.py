from breezypythongui import EasyFrame
class TextFieldDemo(EasyFrame):
	def __init__(self):
		EasyFrame.__init__(self,title="Text FIeld Demo") 
		self.addLabel(text="Input",row=0,column=0)
		self.inputField=self.addTextField(text="",row=0,column=1)
		self.addLabel(text="output",row=1,column=0)
		self.outputField=self.addTextField(text="",row=1,column=1)
		self.addButton(text="convert",row=2,column=0,columnspan=2,command=self.convert)
		#the event handling method for the button
	def convert(self):
		text=self.inputField.getText()
		result=text.upper()
		self.outputField.setText(result)
TextFieldDemo().mainloop()
