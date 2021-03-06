def calculate_apr():
	try:
		principal =float(input("Enter P: "))
		interest_rate = float(input("Enter I: "))
		years = int(input("Enter Y: "))
		for i in range(years):
			principal =  principal * (1 + interest_rate)
			return f'{principal}'

	except ValueError:
		return False;
