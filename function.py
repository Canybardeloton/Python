input_salary = input("Please enter your annual salary : ")
annual_salary = int(input_salary)
month_salary = 0
week_salary = 0
hour_salary = 0
hours_input = input("Please enter your working hours : ")
hours_worked = int(hours_input)

def monthly_salary(annual_salary) :
	return (annual_salary / 12)

month_salary = monthly_salary(annual_salary)
print(f"monthly salary : {month_salary}")

def weekly_salary(month_salary) :
	return (month_salary / 4)

week_salary = weekly_salary(month_salary)
print(f"week_salary : {week_salary}")

def	hourly_salary(week_salary, hours_worked) :
	return (week_salary / hours_worked)

hour_salary = hourly_salary(week_salary, hours_worked)
print(f"Your hourly wage is {hour_salary}")
