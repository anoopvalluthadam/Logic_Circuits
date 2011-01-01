class test:
	def __init__(self,name):
		self.name=name
class test1 (test):
	def __init__(self,name):
		test.__init__(self,name)
		self.A=test("anoop")
		print self.A.name
		print self.name

a=test1("Anu")

