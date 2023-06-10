import csv
import streamlit as st
import base64

# Function to save the data of people receiving medicine
def save_data(name, medicine_name, price):
    with open("charity_fund_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, medicine_name, price])

# Function to download the CSV file
def download_csv():
    with open("charity_fund_data.csv", "r") as file:
        csv_data = file.read()
    b64 = base64.b64encode(csv_data.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="charity_fund_data.csv">Download CSV File</a>'
    return href

# Function to display the Streamlit app
def main():
    st.title("Monthly Charity Fund for Poor People")
    st.markdown("Enter the details of the medicine distribution:")

    # Input fields for the distributor
    name = st.text_input("Distributor Name")
    medicine_name = st.text_input("Medicine Name")
    price = st.number_input("Price")

    # Save data when the "Add" button is clicked
    if st.button("Add"):
        save_data(name, medicine_name, price)
        st.success("Data saved successfully!")

    # Display the data table for verification and checking records
    st.markdown("## Records")
    with open("charity_fund_data.csv", "r") as file:
        reader = csv.reader(file)
        data = list(reader)
        st.table(data)

    # Download the CSV file when the "Download" button is clicked
    if st.button("Download CSV"):
        href = download_csv()
        st.markdown(href, unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == "__main__":
    main()
