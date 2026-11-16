import streamlit as st

st.title("🧾 แอปคำนวณส่วนลดและ VAT 7%")
fullprice = st.number_input("กรอกราคาเต็มของสินค้า (บาท):", min_value=0.0 , value=0.0)
discountpercent = st.numberinput("กรอกส่วนลด (%):", min_value=0.0 , value =0.0)
discount = fullprice * (discountpercent / 100)
discountedprice = fullprice - discount
vat = price discountedprice * 0.07
netprice = discountedprice + vat
st.title(f"• ส่วนลด ({discountpercent:.2f}%): **{discount:.2f}** %")
st.title(f"•  ราคาหลังหักส่วนลด: **{discountedprice:.2f}** บาท")
st.title(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {netprice:.2f} บาท")
st.divider()
st.write("นายคุณานนท์ นนทศิลา เลขที่ 13  ม.4/5")
