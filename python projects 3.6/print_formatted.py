def print_formatted(number):
  width = len(bin(number)[2:])
  rjustify = lambda x: x.rjust(width, ' ')
  for i in range(1, number + 1):
    # print(str(i).rjust(width, ' '), oct(i)[2:].rjust(width, ' '), hex(i)[2:].upper().rjust(width, ' '), bin(i)[2:].rjust(width, ' '))
    print(
      rjustify(str(i)), 
      rjustify(oct(i)[2:]), 
      rjustify(hex(i)[2:].upper()), 
      rjustify(bin(i)[2:])
    )
print_formatted(17)