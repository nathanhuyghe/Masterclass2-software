import streamlit as st

# Titel
st.title("Mijn Eerste Streamlit App")

# Tekst
st.write("Welkom bij mijn app!")

# Slider
x = st.slider("Kies een getal", 0, 100)
st.write(f"Het kwadraat van {x} is {x**2}")