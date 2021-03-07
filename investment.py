def calculate_apr(principal, interest_rate, years):
	if principal >= 0 and interest_rate >= 0 and years >= 0
		p = principal
		i = interest_rate
		y = years
		if((isinstance(p,float) or isinstance(p, int)) and (isinstance(i,float) or isinstance(i, int)) and isinstance(y, int))
			for i in range(years):
				principal =  principal * (1 + interest_rate)
			return f'{principal}'

	else:
		return False;
