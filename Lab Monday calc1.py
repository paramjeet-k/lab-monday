from tabulate import tabulate

def calculate_depreciation(method, cost, salvage, life, units_produced=None, total_units=None):
    depreciation_per_year = []
    
    if method == 1:  # Straight-Line Method
        annual_depreciation = (cost - salvage) / life
        depreciation_per_year = [annual_depreciation] * life
    elif method == 2:  # Declining Balance Method
        book_value = cost
        rate = 2 / life
        for year in range(1, life + 1):
            depreciation = book_value * rate
            # Ensure depreciation does not exceed book value - salvage value
            depreciation = min(depreciation, book_value - salvage)
            depreciation_per_year.append(depreciation)
            book_value -= depreciation
    elif method == 3 and units_produced and total_units:  # Units of Production Method
        annual_depreciation = (cost - salvage) * (units_produced / total_units)
        depreciation_per_year = [annual_depreciation] * life
    elif method == 4:  # Sum-of-the-Years-Digits Method
        years = list(range(1, life + 1))
        total = sum(years)
        annual_depreciation = (cost - salvage) * (life / total)
        depreciation_per_year = [annual_depreciation] * life
    elif method == 5:  # Double Declining Balance Method
        book_value = cost
        rate = 2 / life
        for year in range(1, life + 1):
            depreciation = book_value * rate
            # Ensure depreciation does not exceed book value - salvage value
            depreciation = min(depreciation, book_value - salvage)
            depreciation_per_year.append(depreciation)
            book_value -= depreciation
    else:
        return "Invalid input"
    
    # Calculate depreciation per month (for each year)
    depreciation_per_month = [dep / 12 for dep in depreciation_per_year]
    
    return depreciation_per_year, depreciation_per_month

# Example usage:
print("Depreciation Calculator")

# User selects method by entering a number
print("Select Depreciation Method:")
print("1: Straight-Line")
print("2: Declining Balance")
print("3: Units of Production")
print("4: Sum-of-the-Years-Digits")
print("5: Double Declining Balance")

method = int(input("Enter the number corresponding to the chosen depreciation method: "))
cost = float(input("Enter the machinery cost: "))
salvage = float(input("Enter the salvage value: "))
life = int(input("Enter the useful life of the asset (in years): "))

# For Units of Production, additional inputs are needed
if method == 3:
    units_produced = float(input("Enter the units produced this year: "))
    total_units = float(input("Enter the total estimated units to be produced over the asset's life: "))
    depreciation_per_year, depreciation_per_month = calculate_depreciation(method, cost, salvage, life, units_produced, total_units)
else:
    depreciation_per_year, depreciation_per_month = calculate_depreciation(method, cost, salvage, life)

# Prepare data for table
years = [f"Year {i+1}" for i in range(life)]
table = []
for i in range(life):
    table.append([years[i], depreciation_per_year[i], depreciation_per_month[i]])

# Display results in tabular format
print("\nDepreciation Table:")
headers = ["Year", "Depreciation per Year (INR)", "Depreciation per Month (INR)"]
print(tabulate(table, headers=headers, tablefmt="grid"))