#
# Example file for working with conditional statements
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)
a="aa"
b="bb"
c="cc"
def main():
  x, y = 19999, 100
  if(x < y):
    st= a
  elif (x == y):
    st= b
  elif (x > y):
    st= c
  else:
    st= "x is greater than y"
  print st
  
if __name__ == "__main__":
  main()

