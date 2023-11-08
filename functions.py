from data import *
import streamlit as st

def get_experience(data, value):
    st.write(f"###### {data['Job Title'][value]}")
    st.image(f"{data['Company Image'][value]}", width=150)
    st.write(f" *{data['Year'][value]}*")
    with st.expander('Description', expanded=True):
        st.write(f" {data['Job Description'][value]}")

def get_education(data, value):
    st.write(f"###### {data['Title'][value]}")
    st.write(f" {data['University'][value]}")
    st.write(f" *{data['Year'][value]}*")

def get_languages(data, value):
    st.write(f"###### {data['Language'][value]}")
    st.write(f" *{data['Level'][value]}*")


def get_certificates(data, platform, value):
    st.write(f"###### {data[platform]['Title'][value]}")
    st.write(f"*{data[platform]['Hours'][value]}*")

