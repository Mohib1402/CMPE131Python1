def calculate_apr(principal, interest_rate, years):

	try:
		principal =float(principal)
		interest_rate = float(interest_rate)
		years = int(years)
		for i in range(years):
			principal =  principal * (1 + interest_rate)
			return f'{principal}'

	except ValueError:
		return False;
