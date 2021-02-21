


def Add(input_string):
  #Add implementation
  if input_string:
    args = input_string.split(",")
    args = map(int, args)
    result = 0
    for i in args:
      result += i
    return result

  else:
    return 0