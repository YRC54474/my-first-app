import streamlit as st

st.markdown("# :red[ 🩺  BMI Calculator]")
st.write("Input your weight and height")

weight = st.number_input("Input your weight (kg):", min_value=1.0, value=1.0)
height_cm = st.number_input("Input your height (cm):", min_value=1.0, value=1.0)

if st.button("▶️ Calculate your BMI value"):
  height_m = height_cm / 100
  bmi = weight / (height_m ** 2)

  st.write("---")
  st.header(f"Your BMI value is: **{bmi:.2f}**")

  if bmi < 18.5:
    st.warning("⚠️ You have less than average weight (Thin)")
  elif 18.5 <= bmi < 23.0:
    st.success("🎉 Your weight is average (Healthy)")
  elif 23.0 <= bmi < 25.0:
    st.info("💡 You're starting to have more than average weight")
  else:
    st.error("🚨 You're fat. You should excerise more often")

st.divider()
st.write("นายคุณานนท์ นนทศิลา เลขที่ 20 ม.4/5")
    

