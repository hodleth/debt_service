
# use all interest on pricipal to service debt
def sim1(equity_amt, equity_rate, debt_amt, debt_rate, debt_term):

	while debt_amt > 0 and debt_term > 0:

		equity_int_earned = int((equity_amt*equity_rate) - equity_amt)
		debt_amt -= equity_int_earned
		debt_term -= 1

	if debt_amt < 0:
		equity_amt += (-1*debt_amt)
		debt_amt = 0

	return debt_term, equity_amt, debt_amt

# compound principal for n years
# pay interest on debt for n years
# then use sim1 method
def sim2(cp_yrs, equity_amt, equity_rate, debt_amt, debt_rate, debt_term):

	debt_term -= cp_yrs
	while cp_yrs > 0:
		equity_amt *= 1+(equity_rate - debt_rate)
		cp_yrs -= 1

	return sim1(equity_amt, equity_rate, debt_amt, debt_rate, debt_term) 


if __name__ == '__main__':

	equity_amt = 100000
	equity_rate = 1.1

	debt_amt = 200000
	debt_rate = 1.02
	debt_term = 30

	#years_left = sim2()

	years_left = sim2(30, equity_amt, equity_rate, debt_amt, debt_rate, debt_term)
	print(years_left)

	#print(years_left)
	#print("time to service:", debt_term-years_left, "years")