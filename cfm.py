import csv
import streamlit as st
import base64

# Set page config to wide layout
st.set_page_config(layout="wide")

# Function to save the data of people receiving medicine
def save_data(name, medicine_name, price):
    with open("charity_fund_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, medicine_name, price])

# Function to calculate the total sum of prices
def calculate_total_sum():
    total_sum = 0
    with open("charity_fund_data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[2].replace('.', '').isdigit():
                total_sum += float(row[2])
    return round(total_sum, 2)

# Function to delete the record of a person
def delete_record(name):
    rows = []
    with open("charity_fund_data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == name:
                continue
            rows.append(row)

    with open("charity_fund_data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Function to download the CSV file
def download_csv():
    with open("charity_fund_data.csv", "r") as file:
        csv_data = file.read()
    b64 = base64.b64encode(csv_data.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="charity_fund_data.csv">Download CSV File</a>'
    return href

# Function to download the TXT file
def download_txt():
    with open("charity_fund_data.csv", "r") as file:
        txt_data = file.read()
    b64 = base64.b64encode(txt_data.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="charity_fund_data.txt">Download TXT File</a>'
    return href

# Function to display the Streamlit app
def main():
    st.title("Monthly Charity Fund for Poor People")
    st.markdown("Enter the details of the medicine distribution:")

    # Input fields for the distributor
    name = st.text_input("Name")
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

    # Calculate and display the total sum of prices
    total_sum = calculate_total_sum()
    st.markdown(f"## Total Sum of Prices: {total_sum}")

    # Delete the record of a person
    delete_name = st.text_input("Enter the name to delete the record")
    if st.button("Delete Record"):
        delete_record(delete_name)
        st.success("Record deleted successfully!")

    # Download the CSV file when the "Download CSV" button is clicked
    if st.button("Download CSV"):
        href = download_csv()
        st.markdown(href, unsafe_allow_html=True)

    # Download the TXT file when the "Download TXT" button is clicked
    if st.button("Download TXT"):
        href = download_txt()
        st.markdown(href, unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == "__main__":
    main()
