for quadRes in [14,6,11]:
  for number in range(1,30):
    if (number*number)%29 == quadRes:
      print(quadRes, " is Quadratic Residue, and it's square root is ", number)
