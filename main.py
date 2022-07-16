import streamlit as st

params = st.experimental_get_query_params()

st.title("Trial redirect")
st.text(f"Just checking. Param: {params[param][0]}")
