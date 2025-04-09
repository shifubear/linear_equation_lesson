import streamlit as st

# Define the pages
page_1 = st.Page("example.py", title="Example", icon="🌱")
page_2 = st.Page("demo.py", title="Practice", icon="🌸")

# Set up navigation
pg = st.navigation([page_1, page_2])

# Run the selected page
pg.run()
