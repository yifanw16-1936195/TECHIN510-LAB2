import streamlit as st
import datetime
import pytz

st.title('World Clock App')
page = st.sidebar.selectbox("Choose your page", ["World Clock", "UNIX Timestamp Converter"])

if page == "World Clock":
    st.header("World Clock")
    timezones = {'New York': 'America/New_York', 'London': 'Europe/London', 
                 'Berlin': 'Europe/Berlin', 'Tokyo': 'Asia/Tokyo', 
                 'Sydney': 'Australia/Sydney', 'Mumbai': 'Asia/Kolkata'}
    selected_cities = st.multiselect('Select cities', options=list(timezones.keys()), default=['New York', 'London'])
    for city in selected_cities:
        tz = pytz.timezone(timezones[city])
        city_time = datetime.datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
        st.write(f"The current time in {city} is: {city_time}")

elif page == "UNIX Timestamp Converter":
    st.header("UNIX Timestamp Converter")
    unix_input = st.number_input("Enter UNIX timestamp:", step=1, format="%d")
    if unix_input:
        dt_object = datetime.datetime.fromtimestamp(unix_input, tz=pytz.UTC)
        st.write("Human-readable time (UTC):", dt_object.strftime('%Y-%m-%d %H:%M:%S %Z'))