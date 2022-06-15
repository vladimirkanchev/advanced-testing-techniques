def addthis(x, y):
  print(f"This is x: {x} and the x-type is {type(x)}")
  print(f"This is y: {y} and the y-type is {type(y)}")
  result = x+y
  print(f"This is the result: {result}")
  return result

print(addthis(1,2))
