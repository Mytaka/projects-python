number_of_tickets = int(input('скільки білетів потрібно? '))
users_cost = {}

tickets_counter = 0
while tickets_counter < number_of_tickets:
    user_old = int(input('Скільки вам років? '))
    user_row = int(input('Який ряд? '))

    if user_old <= 3:
        old_cost = 0
    elif user_old <= 13:
        old_cost = 100
    elif user_old >= 14:
        old_cost = 200
    
    cost = old_cost
    if user_row == 1:
        cost = int(old_cost) * 1.2
    
    users_cost[f'Tickets_{tickets_counter+1}'] = cost 
    tickets_counter += 1 

print(users_cost)