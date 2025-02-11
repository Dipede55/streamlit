import streamlit as st
import pandas as pd 
import plotly.express as pd
import os
print(os.path.exists("style.css"))  # Should print True if the file exists

st.set_page_config(layout= 'wide', initial_sidebar_state= 'expanded') 
#Expands the app layout to use the full width of the screen
#Expands the sidebar by default when the app loads.
with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html= True)
st.sidebar.header('Menu')
st.sidebar.subheader('Money income')

st.title("♉ My fianace dashboard ☻")
st.write()
#input income
income = st.number_input("Income (thousand): ", min_value = 0, value = 7000, step = 1)

# Expense Goods
goods = ["Rent", "Merch", "Debt", "Foods", "Drinks", "Petrol", "Shopping", "Others"]
expense_data = {}
for good in goods:
   expense_data[good] = st.number_input(f"{good} expense (thousand)", min_value = 0, value = 0, step = 10, key = good)
# Convert to DataFrame
df = pd.DataFrame()

