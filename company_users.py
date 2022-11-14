
companies ={} # dictionary of companies
command = input().split(' -> ')

while command[0] != 'End':
    company = command[0]
    employee_id = command[1]
    if company not in companies:
        companies[company] = []
    if employee_id not in companies[company]:
        companies[company].append(employee_id)
    command = input().split(' -> ')
    
for company, employee_id in companies.items():
    print(company)
    for id in employee_id:
        print(f'-- {id}')
        
