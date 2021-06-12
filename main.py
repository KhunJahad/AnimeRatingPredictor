import streamlit as st
import base64
import os

curdir = os.getcwd()

main_bg = curdir + "/images/bg.jpg"
main_bg_ext = "jpg"

st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)


header = st.beta_container()


text_form = st.form(key = 'my_form')


with header:
	st.title('Anime Description Classifier')


with text_form:
	text_input = st.text_input(label='Enter your anime story for getting reviews')
	submit_button = st.form_submit_button(label='Submit')





