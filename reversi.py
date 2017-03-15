def reversi():	
	product = 0
	num1 = 0
	num2 = 0
	for x in range(100,1000):
		for y in range(100,1000):
			if str(x*y) == str(x*y)[::-1]:
				if (x*y) > product:
					product = x*y
					num1 = x
					num2 = y 
	print("{} x {} = {}".format(num1,num2,product))
 # "abc x def = ghiihg"


def main():
	reversi()


if __name__ == "__main__":
	main()
