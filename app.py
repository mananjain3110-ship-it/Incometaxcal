import streamlit as st

# -------------------------------
# Tax Calculation Function
# -------------------------------
def calculate_tax(income):
    taxable_income = income - 50000  # Standard Deduction
    
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
# Streamlit UI
# -------------------------------
st.title("Income Tax Calculator (India - New Regime)")

income = st.number_input("Enter Annual Income (₹)", min_value=0)

if st.button("Calculate Tax"):
    tax = calculate_tax(income)
    
    st.subheader("Result")
    st.write(f"Taxable Income after deduction: ₹ {income - 50000:,.2f}")
    st.write(f"Total Tax Payable: ₹ {tax:,.2f}")

    if tax == 0:
        st.success("No tax liability ✅")