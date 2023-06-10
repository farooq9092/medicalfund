import csv
import streamlit as st
import base64

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
    href = f'<a href="data:file/csv;base64,{b64}" download="charity_data.csv">Download CSV File</a>'
    return href

# Function to display the Streamlit app
def main():
    # Add background image using CSS
    st.markdown(
        """
        <style>
            body {
                background-image: url('data:image/jpeg;base64,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');
                background-size: cover;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Customize main heading color
    st.title("Monthly Charity Fund for Poor People")
    st.markdown("<style>.title { color: green; }</style>", unsafe_allow_html=True)
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

    # Calculate and display the total sum of prices
    total_sum = calculate_total_sum()
    st.markdown(f"## Total Sum of Prices: {total_sum}")

    # Delete the record of a person
    delete_name = st.text_input("Enter the name to delete the record")
    if st.button("Delete Record"):
        delete_record(delete_name)
        st.success("Record deleted successfully!")

    # Download CSV file
    download_link = download_csv()
    st.markdown(download_link, unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == "__main__":
    main()
