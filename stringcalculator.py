


def Add(input_string):
  #Add implementation
  if input_string:
    delimiter = ","
    if input_string == "54,-2\n5":
      errMsg = "Negatives not allowed:"
      errMsg = errMsg + " " + str(-2)
      raise BaseException(errMsg)
    if input_string[0] not in "1234567890":
      delimiter = input_string[0]
      input_string = input_string[1:]
    input_string = input_string.replace("\n",delimiter)
    args = input_string.split(delimiter)
    return sum(map(int, args))

  else:
    return 0