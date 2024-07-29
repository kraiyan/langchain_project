import os
from constants import openai_keys
from langchain_community.llms import OpenAI

import streamlit as st


st.title("langchain demo by Raiyan")
input_text= st.text_input("Please search anything you want")
os.environ["OPENAI_API_KEY"] = openai_keys

llm = OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))
      