import streamlit as st
import pandas as pd

def create_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('charity_fund_data.csv', index=False)

def main():
    st.title("Monthly Charity Fund for Poor People")
    st.markdown("Please enter the following details:")
    
    distributor_name = st.text_input("Name")
    medicine_name = st.text_input("Medicine Name")
    price = st.number_input("Price")
    
    if st.button("Submit"):
        if not distributor_name or not medicine_name or not price:
            st.error("Please fill in all fields.")
        else:
            new_data = {"Distributor Name": [distributor_name], "Medicine Name": [medicine_name], "Price": [price]}
            create_csv(new_data)
            
            st.success("Data saved successfully!")

if __name__ == "__main__":
    main()
