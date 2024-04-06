# calculate salary,weekly working hours given in a list
work_hours=[int(x) for x in input('enter hours per day').split()]
wage=int(input('enter hourly wage'))
total=sum(work_hours)
salary = total*wage
print('salry is',salary)