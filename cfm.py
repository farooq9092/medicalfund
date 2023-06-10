import streamlit as st
import pandas as pd
import base64

# Function to read the CSV file
def read_csv(file):
    df = pd.read_csv(file)
    return df

# Function to save the updated data to a new CSV file
def save_data(df, csv_file_path):
    csv_data = df.to_csv(index=False)
    b64 = base64.b64encode(csv_data.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{csv_file_path}">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)

def main():
    st.title("Monthly Charity Fund for Poor People")
    st.markdown("Please upload two CSV files:")
    
    # File upload
    csv_file1 = st.file_uploader("Upload CSV File 1", type=["csv"])
    csv_file2 = st.file_uploader("Upload CSV File 2", type=["csv"])
    
    if csv_file1 is not None and csv_file2 is not None:
        # Read the CSV files
        df1 = read_csv(csv_file1)
        df2 = read_csv(csv_file2)
        
        st.markdown("---")
        st.subheader("CSV File 1")
        st.write(df1)
        
        st.markdown("---")
        st.subheader("CSV File 2")
        st.write(df2)
        
        # Perform operations on CSV File 1
        st.markdown("---")
        st.subheader("Operations on CSV File 1")
        # Add your code here to perform operations on df1
        
        # Perform operations on CSV File 2
        st.markdown("---")
        st.subheader("Operations on CSV File 2")
        # Add your code here to perform operations on df2
        
        # Save the updated data
        st.markdown("---")
        if st.button("Save CSV File 1"):
            # Save CSV File 1
            save_data(df1, "file1.csv")
            st.success("CSV File 1 saved successfully!")
        
        if st.button("Save CSV File 2"):
            # Save CSV File 2
            save_data(df2, "file2.csv")
            st.success("CSV File 2 saved successfully!")

if __name__ == "__main__":
    main()
