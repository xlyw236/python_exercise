#
# Example file for working with classes
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

 
class myClass():
  def method1(self):
    print "A"
    
  def method2(self, someString):
    print "B" 
    
class anotherClass(myClass):
  def method2(self):
    print "C"
    
  def method1(self):
    myClass.method1(self);
    print "D"

def main():   
  c = myClass()
  c.method1()
  c.method2("This is a string")
  c2 = anotherClass()
  c2.method1()

if __name__=="__main__":
  main()