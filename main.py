from datetime import datetime

# test data
expenses_data = {
    "2023-01": {
        "01": {
            "food": [ 22.11, 43, 11.72, 2.2, 36.29, 2.5, 19 ],
            "fuel": [ 210.22 ]
        },
        "09": {
            "food": [ 11.9 ],
            "fuel": [ 190.22 ]
        }
    },
    "2023-03": {
        "07": {
            "food": [ 20, 11.9, 30.20, 11.9 ]
        },
        "04": {
            "food": [ 10.20, 11.50, 2.5 ],
            "fuel": []
        }
    },
    "2023-04": {}
};

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

# algotytm to find k-element(mediana)
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + len(mid):
        return pivot
    else:
        return quickselect(right, k - len(left) - len(mid))

# quick select
def solution2(expenses):
    """
    Zalety:
    - Mniejsza złożoność czasowa dla dużych danych.
    - Mniejsze zużycie pamięci niż np. kolejki priorytetowe.
    
    Wady:
    - Złożoność czasowa: O(n^2) w najgorszym przypadku, ale średnio działa w czasie O(n Log n) i działa lepiej niż algorytm oparty na kolejce priorytetowej.
    - Podobnie jak quicksort, jest szybki w praktyce, ale ma słabą wydajność w najgorszym przypadku.
    """
    relevant_expenses = expenses_to_first_sundays(expenses)
    if not relevant_expenses:
        return None
    
    # checking odd or even
    n = len(relevant_expenses)
    if n % 2 == 1:
        return quickselect(relevant_expenses, n // 2)
    else:
        return (quickselect(relevant_expenses, n // 2 - 1) + quickselect(relevant_expenses, n // 2)) / 2

# print(solution1(expenses_data)) 
# 11.72
# print(solution2(expenses_data))
# 11.72