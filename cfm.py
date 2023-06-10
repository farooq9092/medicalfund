import streamlit as st
import pandas as pd
import requests

GITHUB_API = 'https://api.github.com'
OWNER = 'farooq9092'
REPO = 'cmf'
BRANCH = 'main'
FILE_PATH = 'charity_fund_data.csv'

def create_csv(data):
    df = pd.DataFrame(data)
    csv_data = df.to_csv(index=False)
    headers = {
        'Authorization': 'Bearer YOUR_GITHUB_ACCESS_TOKEN',
        'Accept': 'application/vnd.github.v3+json'
    }
    url = f'{GITHUB_API}/repos/{OWNER}/{REPO}/contents/{FILE_PATH}'
    payload = {
        'message': 'Create CSV file',
        'content': csv_data,
        'branch': BRANCH
    }
    response = requests.put(url, headers=headers, json=payload)
    if response.status_code == 201:
        st.success("CSV file created successfully!")
    else:
        st.error("Failed to create CSV file.")

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

if __name__ == "__main__":
    main()
