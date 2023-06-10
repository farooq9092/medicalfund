import csv
import streamlit as st
import base64
from fpdf import FPDF

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

# Function to convert CSV to PDF
def convert_csv_to_pdf(csv_file_path, pdf_file_path):
    pdf = FPDF()
    pdf.add_page()

    # Set font and size
    pdf.set_font("Arial", size=12)

    # Open CSV file and read data
    with open(csv_file_path, "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    # Add data to PDF table
    for row in data:
        for item in row:
            pdf.cell(40, 10, str(item), 1)
        pdf.ln()

    # Save PDF file
    pdf.output(pdf_file_path)

# Function to display the Streamlit app
def main():
    # Customize main heading color
    st.title("Report Monthly Charity Fund for Poor People")
    st.markdown("<style>.title { color: green; }</style>") unsafe_allow_html=True)
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

    # Download PDF file
    if st.button("Download PDF"):
        csv_file_path = "charity_fund_data.csv"
        pdf_file_path = "charity_fund_data.pdf"
        convert_csv_to_pdf(csv_file_path, pdf_file_path)
        with open(pdf_file_path, "rb") as file:
            b64 = base64.b64encode(file.read()).decode()
            href = f'<a href="data:application/pdf;base64,{b64}" download="charity_data.pdf">Download PDF File</a>'
            st.markdown(href, unsafe_allow_html=True)

# Run the Streamlit app
if __name__ == "__main__":
    main()
