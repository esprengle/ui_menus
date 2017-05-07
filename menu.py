import ui

'''MenuBar is a ui.View that implements right_bar_buttons and left_bar_buttons.  Add ui.Buttons, or other Views, they will get height-resized and added in the appropriate location.  Use None for simple placeholder(gap)

'''
class MenuBar(ui.View):
	def __init__(self,*args,**kwargs):
		ui.View.__init__(self,*args,**kwargs)
		self.height=44
		self.margin=32
		self.ymargin=6
		self.placeholder_width=20
		self._right_button_items=[]
		self._left_button_items=[]
		self._title=None
	def layout(self):
		def a():
			x=self.margin
			for b in self._left_button_items:
				if b:
					b.x=x
					x+=b.width+self.margin
				else:
					x+=self.placeholder_width
			x=self.width
			for b in self._right_button_items:
				x-=self.margin
				if b:
					x-=b.width
					b.x=x
				else:
					x-=self.placeholder_width	
			if self._title:
				self._title.size_to_fit()
				self._title.x=self.bounds.center().x-self._title.width/2.
		ui.animate(a,0.5)
	@property
	def title(self):
		return self._title
	@title.setter
	def title(self,item):		
		if self._title:
			self.remove_subview(self._title)
		self._title=item
		item.height=self.height-self.ymargin
		item.y=self.ymargin/2
		self.add_subview(item)
		item.x=self.bounds.center().x-item.width/2.
		item.flex='lr'
		self.layout() # maybe needed?
	@property
	def right_button_items(self):
		return self._right_button_items
	@right_button_items.setter
	def right_button_items(self,items):
		rbset=set(self._right_button_items)
		lbset=set(self._left_button_items)
		iset=set(items)
		# first, check for old views no longer needed
		for b in rbset-iset-lbset:
			if b:
				self.remove_subview(b)
		#then, check for views to add
		for b in iset-rbset:
			if b:
				self.add_subview(b)
				b.height=self.height-self.ymargin
				b.y=self.ymargin/2
		# set, and reverse items, so right is right
		self._right_button_items=items
		self._right_button_items.reverse()
		self.layout()
	@property
	def left_button_items(self):
		return self._left_button_items
	@left_button_items.setter
	def left_button_items(self,items):
		rbset=set(self._right_button_items)
		lbset=set(self._left_button_items)
		iset=set(items)
		# first, check for old views no longer needed
		for b in lbset-iset-rbset:
			if b:
				self.remove_subview(b)
		#add new views
		for b in iset-lbset:
			if b:
				self.add_subview(b)
				b.height=self.height-self.ymargin
				b.y=self.ymargin/2
		self._left_button_items=items
		self.layout()
if __name__=='__main__':
	b2=ui.Button(image=ui.Image.named('iow:grid_32'))
	b=ui.Button(image=ui.Image.named('iow:alert_32'))
	b3=ui.Button(image=ui.Image.named('iob:archive_32'))
	ti=ui.Label('Project/1/kitchen')
	m=MenuBar()
	
	m.width=500
	t=ui.TextField(frame=(0,0,32,150))
	t.flex='w'
	t.width=150
	m.left_button_items=[None,t,b,None,b2]
	m.right_button_items=[b3,None]
	m.title=ti
	v=ui.View()
	v.present('panel')
	v.add_subview(m)
	m.width=v.width
	v.flex='w'
	m.flex='w'
