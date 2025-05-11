import streamlit as st

# Define the pages
home_page = st.Page("pages/Home.py", title="Streamlit Demo Project", icon="👋")
plotting_demo_page = st.Page("pages/1_Plotting_Demo.py", title="Plotting Demo", icon="📈")
mapping_demo_page = st.Page("pages/2_Mapping_Demo.py", title="Mapping Demo", icon="🌍")
dataframe_demo_page = st.Page("pages/3_DataFrame_Demo.py", title="DataFrame Demo", icon="📊")

echobot_demo_page = st.Page("pages/4_EchoBot_Demo.py", title="Echo Bot Demo", icon="🤖")
chatbot_demo_page = st.Page("pages/5_ChatBot_Demo.py", title="Chat Bot Demo", icon="🤖")
chatbotasync_demo_page = st.Page("pages/6_ChatBotAsync_Demo.py", title="Chat Bot Async Demo", icon="🤖")

# Set up navigation
pg = st.navigation([home_page, plotting_demo_page, mapping_demo_page, dataframe_demo_page, echobot_demo_page, chatbot_demo_page, chatbotasync_demo_page])

# Run the selected page
pg.run()