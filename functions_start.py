#
# Example file for working with functions
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def func1():
  print "I am a function"
  return 1;



def func2(arg1, arg2):
  print arg1, " ", arg2



def cube(x):
  return x*x*x
  
def power(num=1111111, x=5):
  result = 1;
  for i in range(x):
    result = result * num  
  return result

print power()