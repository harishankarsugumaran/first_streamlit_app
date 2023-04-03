import pandas as pd
import streamlit

streamlit.title("My Parents New Healthy Diner")

streamlit.header("Breakfast Favorites")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# load the data from csv file to a pandas dataframe
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# display the data from csv file in streamlit web app
streamlit.dataframe(my_fruit_list)

# app url : https://harishankarsugumaran-first-streamlit-app-streamlit-app-u3y3yt.streamlit.app/