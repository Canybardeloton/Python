left_number = 2
right_number = 5.0
symbol = "*"
result = 0

("+", "-", "*", "/")

if isinstance(left_number, int) == False :
	print("left_number is not an integer")
elif isinstance(right_number, int) == False :
	print("rigth_number is not an integer")
else :
	print("left_number and right_number are integers")

match symbol :
	case "+" :
		print(left_number + right_number)
	case "-" :
		print(left_number - right_number)
	case "*" :
		print(left_number * right_number)
	case "/" :
		if right_number != 0 :
			result = left_number / right_number
			print(result)
		else :
			print("Error : division is not allowed")
