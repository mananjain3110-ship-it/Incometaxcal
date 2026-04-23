import matplotlib.pyplot as plt

# -------------------------------
# Old Regime Tax Calculation
# -------------------------------
def old_tax(income, deductions):
    taxable_income = income - deductions - 50000
    
    tax = 0
    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = (250000 * 0.05) + (taxable_income - 500000) * 0.20
    else:
        tax = (250000 * 0.05) + (500000 * 0.20) + (taxable_income - 1000000) * 0.30
    
    return max(tax, 0)


# -------------------------------
# New Regime Tax Calculation
# -------------------------------
def new_tax(income):
    taxable_income = income - 50000
    
    tax = 0
    if taxable_income <= 300000:
        tax = 0
    elif taxable_income <= 600000:
        tax = (taxable_income - 300000) * 0.05
    elif taxable_income <= 900000:
        tax = (300000 * 0.05) + (taxable_income - 600000) * 0.10
    elif taxable_income <= 1200000:
        tax = (300000 * 0.05) + (300000 * 0.10) + (taxable_income - 900000) * 0.15
    elif taxable_income <= 1500000:
        tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (taxable_income - 1200000) * 0.20
    else:
        tax = (300000 * 0.05) + (300000 * 0.10) + (300000 * 0.15) + (300000 * 0.20) + (taxable_income - 1500000) * 0.30
    
    return max(tax, 0)


# -------------------------------
# Input
# -------------------------------
income = float(input("Enter Annual Income: "))
deductions = float(input("Enter Total Deductions (Old Regime): "))


# -------------------------------
# Calculation
# -------------------------------
old_regime_tax = old_tax(income, deductions)
new_regime_tax = new_tax(income)


# -------------------------------
# Output
# -------------------------------
print("\n------ Tax Comparison ------")
print(f"Old Regime Tax: ₹ {old_regime_tax:,.2f}")
print(f"New Regime Tax: ₹ {new_regime_tax:,.2f}")

if old_regime_tax < new_regime_tax:
    print("Old Regime is Better ✅")
elif new_regime_tax < old_regime_tax:
    print("New Regime is Better ✅")
else:
    print("Both Regimes are Equal")


# -------------------------------
# 📊 Bar Chart (Comparison)
# -------------------------------
regimes = ['Old Regime', 'New Regime']
tax_values = [old_regime_tax, new_regime_tax]

plt.figure()
plt.bar(regimes, tax_values)
plt.title("Tax Comparison (Old vs New)")
plt.xlabel("Regime")
plt.ylabel("Tax Amount (₹)")
plt.show()


# -------------------------------
# 📊 Histogram (Tax Distribution)
# -------------------------------
plt.figure()
plt.hist(tax_values, bins=5)
plt.title("Tax Distribution")
plt.xlabel("Tax Amount (₹)")
plt.ylabel("Frequency")
plt.show()