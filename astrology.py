import streamlit as st
import pyaztro

date=st.date_input("Enter Date Of Birth", value=None, min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None,  disabled=False)
#st.write(date)
m=date.month
d=date.day
#st.write(m)
signs = ""
if m == 12:
    signs = "sagittarius" if d < 22 else "capricorn"
elif m == 1:
    signs = "capricorn" if d < 20 else "aquarius"
elif m == 2:
    signs = "aquarius" if d < 19 else "pisces"
elif m == 3:
    signs = "pisces" if d < 21 else "aries"
elif m == 4:
    signs = "aries" if d < 20 else "taurus"
elif m == 5:
    signs = "taurus" if d < 21 else "gemini"
elif m == 6:
    signs = "gemini" if d < 21 else "cancer"
elif m == 7:
    signs = "cancer" if d < 23 else "leo"
elif m == 8:
    signs = "leo" if d < 23 else "virgo"
elif m == 9:
    signs = "virgo" if d < 23 else "libra"
elif m == 10:
    signs = "libra" if d < 23 else "scorpio"
else:
    signs = "scorpio" if m < 22 else "sagittarius"
st.write("Sign is: "+signs.title())
horoscope = pyaztro.Aztro(sign=signs)
st.write(horoscope.description)