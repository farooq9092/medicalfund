import csv
import streamlit as st

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

# Display the Streamlit app
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

    # Provide external download links
    if st.button("Download CSV"):
        st.markdown("Download CSV file from the link below:")
        csv_link = "https://your-cloud-storage-service.com/charity_data.csv"
        st.markdown(f"[Download CSV](csv_link)")
    if st.button("Download TXT"):
        st.markdown("Download TXT file from the link below:")
        txt_link = "https://your-cloud-storage-service.com/charity_data.txt"
        st.markdown(f"[Download TXT](txt_link)")

# Run the Streamlit app
if __name__ == "__main__":
    main()
