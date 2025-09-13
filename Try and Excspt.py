import streamlit as st
import pandas as pd
from io import BytesIO
st.title("DataCleaning app")
fl= st.file_uploader("pick a file")
if fl:
    see = pd.read_csv(fl)
    pd.set_option("display.max_row", None)
    st.write("you can perform any of the following task")
    option = st.radio('pick what youll like to do',["About the data","Check Columns","Check Dirts","Clean Dirt"])
    if option == "About the data":
        st.write(see.info())
    elif option == "Check Columns":
        st.write(see.columns)
        dtype = st.radio("about columns", ["about ur data type"])
        if dtype == "about ur data type":
            st.write(see.dtype)
    elif option == "Check_Dirts":
        check_dirt = st.table(see.isna().sum())
        st.write(f"you have the following columns as ur dirt \n {check_dirt}")
    elif option == "Clean Dirt":
        clean = see.dropna()
        tb = clean.to_excel(r"C:\Users\HP\Downloads\test2.xlsx")
        buffer = BytesIO()
        clean.to_excel(buffer, engine ='openpyxl',index = False)
        btn = st.download_button(
            label="download",
            data = buffer,
            file_name = "data.xlsx",
            mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )



