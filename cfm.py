import streamlit as st
import csv

def save_data(distributor_name, medicine_name, price):
    with open("charity_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([distributor_name, medicine_name, price])

def main():
    st.title("Monthly Charity Fund for Poor People")
    st.markdown("Please enter the following details:")
    
    distributor_name = st.text_input("Distributor Name")
    medicine_name = st.text_input("Medicine Name")
    price = st.number_input("Price")
    
    if st.button("Submit"):
        if not distributor_name or not medicine_name or not price:
            st.error("Please fill in all fields.")
        else:
            save_data(distributor_name, medicine_name, price)
            st.success("Data saved successfully!")

if __name__ == "__main__":
    main()
