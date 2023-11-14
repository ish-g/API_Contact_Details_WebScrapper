import pandas as pd
import numpy as np
import requests
import streamlit as st

# website for API
# https://rapidapi.com/letscrape-6bRBa3QguO5/api/website-contacts-scraper/

st.set_page_config(layout='wide', page_title='Contact info')
st.sidebar.header('Sidebar')
u = st.sidebar.text_input('Enter the website name here')
st.title('Welcome to Contact WebScrapping')
btn = st.sidebar.button("Enter")

if btn:
    url = "https://website-contacts-scraper.p.rapidapi.com/scrape-contacts"

    querystring = {"query": f'{u}', "match_email_domain": "true"}

    headers = {
        "X-RapidAPI-Key": "b407de9ac8msh71113ab5dfa39a8p1f9530jsnb17e56999818",
        "X-RapidAPI-Host": "website-contacts-scraper.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    soup = response.json()

    df = pd.DataFrame(soup['data'])
    df['emails'] = [[i['value'] for i in df['emails'][0]]]
    df['phone_numbers'] = [[i['value'] for i in df['phone_numbers'][0]]]

    st.subheader(df['domain'][0].capitalize())

    st.write("Email", df['emails'][0])

    st.write('Phone Numbers', df['phone_numbers'][0])

    st.write('Facebook', df['facebook'][0])

    st.write('Instagram', df['instagram'][0])

    st.write("Twitter", df['twitter'][0])

    st.write('Linkedin', df['linkedin'][0])

    st.write("Youtube", df['youtube'][0])

    st.write("Pinterest", df['pinterest'][0])
