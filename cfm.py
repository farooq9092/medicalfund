import streamlit as st
import pandas as pd
import base64
import requests

# Function to download the CSV file from GitHub
def download_csv():
    csv_url = "https://raw.githubusercontent.com/farooq9092/cmf/main/charity_fund_data.csv"
    response = requests.get(csv_url)
    content = response.content.decode("utf-8")
    df = pd.read_csv(pd.compat.StringIO(content))
    return df

# Function to save the updated data to the CSV file on GitHub
def save_data(df):
    csv_file_path = "charity_fund_data.csv"
    csv_data = df.to_csv(index=False)
    b64 = base64.b64encode(csv_data.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{csv_file_path}">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)

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
            # Download the current CSV file from GitHub
            df = download_csv()
            
            # Add the new data to the DataFrame
            new_data = {"Distributor Name": distributor_name, "Medicine Name": medicine_name, "Price": price}
            df = df.append(new_data, ignore_index=True)
            
            # Save the updated DataFrame back to the CSV file on GitHub
            save_data(df)
            
            st.success("Data saved successfully!")

if __name__ == "__main__":
    main()
