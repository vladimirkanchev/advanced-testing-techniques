def addthis(x, y):
  print(f"This is x: {x} and the x-type is {type(x)}")
  print(f"This is y: {y} and the y-type is {type(y)}")
  try:
    result = x+y
  except TypeError as exception:
    print(f"The wrong type passed in {exception}")
    result = int(x)+int(y)
    
  print(f"This is the result: {result}")
  return result

print(addthis("one",2))
