import streamlit as st

# Header
st.title ("Welcome to my profile")
st.write ("This is my first apllication that I've made using Python")

st.divider()

# Profile Info
st.header("Personal Info ไทย")
st.write("**ชื่อ-นามสกุล:** นายคุณานนท์ นนทศิลา")
st.write("**ชั้น ม.4/5** เลขที่ 13")
st.write("**โรงเรียน:** ยุพราชวิทยาลัย")

# Button
if st.button("My feelings when creating this Application for the first time")
  st.success(f"Wow! This is very fun and easy!")
