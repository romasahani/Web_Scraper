import streamlit as st
import requests
from bs4 import BeautifulSoup
import webbrowser

st.set_page_config(page_title="Web Scraper", page_icon=":globe_with_meridians:")



st.markdown("<h1 style= 'text-align:center;'>Web Scraper</h1>", unsafe_allow_html=True)
with st.form("Search"):
    keyword = st.text_input("Enter your keyword")
    search=st.form_submit_button("Search")

placeholder=st.empty()
if search:

    page=requests.get(f"https://unsplash.com/s/photos/{keyword}")
    soup=BeautifulSoup(page.content )
    rows=soup.find_all("div", class_="d95fI")
    col1, col2 = placeholder.columns(2)
    for row in rows:
        figures=row.find_all("figure")
        for i in range(2):
            img=figures[i].find("img", class_="ApbSI z1piP vkrMA")
            list=img["srcset"].split("?")
            if i==0:
                col1.image(list[0])
            else:
                col2.image(list[0])



