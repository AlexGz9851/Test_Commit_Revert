
def checkNeg(args):
  errMsg = "Negatives not allowed:"
  err = False
  for i in args:
    if i< 0:
      err = True
      errMsg = errMsg + " " + str(-2)
      raise BaseException(errMsg)


def Add(input_string):
  #Add implementation
  if input_string:
    delimiter = ","
    if input_string[0] not in "1234567890":
      delimiter = input_string[0]
      input_string = input_string[1:]
    input_string = input_string.replace("\n",delimiter)
    args = input_string.split(delimiter)
    args = map(int, args)
    checkNeg(args)
    return sum(args)

  else:
    return 0