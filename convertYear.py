import streamlit as st
st.title ("แอปพลิเคชันแปลงปี พ.ศ เป็น ค.ศ.")

bh_yeaer=st.number_input("Input the year that you want to convert (พ.ศ.)", value=2569)
ce_year=bh_year-543
st.header(f"ปี ค.ศ. คือ : {ce_year}")
