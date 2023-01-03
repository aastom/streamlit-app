import streamlit
import pandas

streamlit.header("Breakfast Menu")
streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach & Rocket Smoothie")
streamlit.text("🐔 Hard-Boiled Free-Range Egg")

streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")

fruits = pandas.read_csv(
    "https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt"
)

# Let's put a pick list here, so they can pick the fruit they want to include
fruits = fruits.set_index("Fruit")
fruits_selected = streamlit.multiselect(
    "Pick some fruits:", list(fruits.index), ["Avocado", "Strawberries"]
)
fruits_to_show = fruits.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

# New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

streamlit.dataframe(fruityvice_normalized)