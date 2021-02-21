


def Add(input_string):
  #Add implementation
  if input_string:
    args = input_string.split(",")
    return sum(map(int, args))

  else:
    return 0