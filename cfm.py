import csv
import streamlit as st
import base64
from reportlab.pdfgen import canvas

# Set page config to wide layout
st.set_page_config(layout="wide")

# Add CSS styling to set the background image and position the input fields
st.markdown(
    """
    <style>
    .container {
        position: relative;
        width: 100%;
        height: 100%;
    }
    .background-image {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
    }
    .form-container {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        z-index: 1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add your image file name in the background image URL
image_file = "images.jpeg"

# Create a container for the background image and the form
container = st.container()

# Add the background image
container.image(
    image_file,
    use_column_width=True,
    output_format="auto",
    caption="",
    clamp=False,
    channels="RGB"
)


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


# Function to download the PDF file
def download_pdf():
    pdf = canvas.Canvas("charity_data.pdf")
    with open("charity_fund_data.csv", "r") as file:
        reader = csv.reader(file)
        y = 700
        for row in reader:
            if row:
                pdf.drawString(50, y, " | ".join(row))
                y -= 20
    pdf.save()

    with open("charity_data.pdf", "rb") as file:
        pdf_data = file.read()
    b64 = base64.b64encode(pdf_data).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="charity_data.pdf">Download PDF File</a>'
    return href


# Function to display the Streamlit app
def main():
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

    # Download PDF file
    download_link = download_pdf()
    st.markdown(download_link, unsafe_allow_html=True)


# Run the Streamlit app
if __name__ == "__main__":
    main()
