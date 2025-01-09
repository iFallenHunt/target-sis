# Monthly revenue by state
revenue = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Others": 19849.53,
}

# Calculation of total revenue
total_revenue = sum(revenue.values())

# Calculation of the percentage for each state
percentages = {
    state: (value / total_revenue) * 100
    for state, value in revenue.items()
}

# Displaying the results
print("Percentage of revenue by state:")
for state, percentage in percentages.items():
    print(f"{state}: {percentage:.2f}%")