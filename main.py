from datetime import datetime

# getting first sunday
def get_first_sunday(year, month):
    for day in range(1, 8):
        if datetime(year, month, day).weekday() == 6:
            return day
    return None

# print(get_first_sunday(2025, 3))

# extracting needed expences from all data
def expenses_to_first_sundays(expenses):
    data = []
    
    for year_month, days in expenses.items():
        year, month = map(int, year_month.split('-'))
        first_sunday = get_first_sunday(year, month)
        if first_sunday is None:
            continue
        
        for day, categories in days.items():
            # taking all days till first sunday
            if int(day) <= first_sunday:
                for category, amounts in categories.items():
                    data.extend(amounts)
    
    return data

# not optimized, sorted func
def solution1(expenses):
    relevant_expenses = expenses_to_first_sundays(expenses)
    if not relevant_expenses:
        return None
    
    relevant_expenses.sort()
    
    # checking odd or even
    n = len(relevant_expenses)
    if n % 2 == 1:
        return relevant_expenses[n // 2]
    else:
        return (relevant_expenses[n // 2 - 1] + relevant_expenses[n // 2]) / 2