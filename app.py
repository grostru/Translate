import streamlit as st
import requests

st.title("🌍 Simple Translator")

text = st.text_area("Enter text to translate")
language = st.text_input("Target language (e.g., Spanish, French)")

if st.button("Translate"):
    response = requests.post(
        "https://translate-pmjdrxqbeaihhdahgbpyhk.streamlit.app/chain/invoke",  # 👈 Usa aquí la URL donde tienes desplegada tu API
        json={"input": {"text": text, "language": language}}
    )

    if response.status_code == 200:
        result = response.json()
        st.success(result.get("output"))
    else:
        st.error("Translation failed.")
