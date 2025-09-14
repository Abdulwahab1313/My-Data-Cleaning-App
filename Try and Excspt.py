import streamlit as st
import pandas as pd
from io import BytesIO
st.title(" Welcome to Aw's csv DataCleaning app")
fl= st.file_uploader("pick a file")
if fl:
    see = pd.read_csv(fl)
    pd.set_option("display.max_row", None)
    st.subheader("you can perform any of the following task")
    option = st.radio('pick what youll like to do',["About Columns","Check Dirts","Clean Dirt"])
    if option == "About Columns":
        st.subheader("Below is an information of your column and their Data type")
        st.write(see.columns)
        st.text(see.dtypes)
    elif option == "Check Dirts":
        check_dirt = see.isna().sum()
        st.text(f"you have the following columns as ur dirt \n {check_dirt}")
    elif option == "Clean Dirt":
        clean = see.dropna()
        fs = io.BytesIO()
    with pd.ExcelWriter(fs, engine="openpyxl") as writer:
   		clean.to_excel(writer, index=False)
   		pick = st.radio("Pick what type of Format you'll like to download",["Excel","csv"])
   		if pick == "Excel":
            btn = st.download_button(
				label="click here to download the clean data",
				data=buffer,
				file_name= st.text_input("Enter your desired name") +".xlsx",
				mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
		elif pick == "csv":
            tb2 = clean.to_csv()
            btn = st.download_button(
                label = "click to download the clean csv ",
                data = tb2,
                file_name = st.text_input("Enter your desired name") + ".csv"
            )







