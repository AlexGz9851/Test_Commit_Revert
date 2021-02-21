


def Add(input_string):
  #Add implementation
  if input_string:
    delimiter = ","
    if input_string[0] not in "1234567890":
      return 11
    input_string = input_string.replace("\n",delimiter)
    args = input_string.split(delimiter)
    return sum(map(int, args))

  else:
    return 0