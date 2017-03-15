def funct_reversi():
	val = [(x*y,x,y) for x in range(100,1000) for y in range(100,1000) if str(x*y) == str(x*y)[::-1]]
	print("{} x {} = {}".format(max(val)[2], max(val)[1], max(val)[0]))


def main():
	funct_reversi()

if __name__ == "__main__":
	main()