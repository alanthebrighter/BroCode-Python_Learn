
def weekdays(number):
  match number:
    case 1:
      print("Sunday")
    case 2:
      print("Monday")
    case 3:
      print("Tuesday")
    case 4:
      print("Wednesday")
    case 5:
      print("Thursday")
    case 6:
      print("Friday")
    case 7:
      print("Saturday")
    case _:
      print("Not valid!")

for n in range(7):
  weekdays(n+1)



