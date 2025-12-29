import streamlit as st
import mtk

st.title("This is title")

st.write("This is a paragraph")

if st.button("Want to see a balloons?"):
    st.balloons()

number1 = st.number_input(
    "Insert the first number", value=None, placeholder="Type a number..."
)

number2 = st.number_input(
    "Insert the second number", value=None, placeholder="Type a number..."
)

if st.button("Add"):
    result = mtk.add(number1, number2)
    st.write(f"The Result: {result}")
if st.button("Subtract"):
    result = mtk.sub(number1, number2)
    st.write(f"The Result: {result}")
if st.button("Multiply"):
    result = mtk.mul(number1, number2)
    st.write(f"The Result: {result}")
if st.button("Division"):
    result = mtk.div(number1, number2)
    st.write(f"The Result: {result}")