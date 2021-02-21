


def Add(input_string):
  #Add implementation
  if input_string:
    args = input_string.split(",")
    args = map(int, args)
    return sum(args)

  else:
    return 0