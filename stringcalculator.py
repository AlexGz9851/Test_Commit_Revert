


def Add(input_string):
  #Add implementation
  if input_string:
    input_string = input_string.replace("\n",",")
    args = input_string.split(",")
    return sum(map(int, args))

  else:
    return 0