import streamlit as st

st.title("Niklas hat Geburtstag!")
 
st.write("""Wie viele Jahre wird Niklas wohl alt? """)

age = st.number_input(label='', min_value=0)

if age != 4:
    st.write("Das ist leider nicht richtig. Versuch es noch einmal.")
else:
    st.write("Hurra! Niklas ist schon VIER Jahre alt! Wir wünschen ihm alles Gute!")