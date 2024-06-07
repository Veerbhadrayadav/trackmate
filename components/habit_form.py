import streamlit as st

def habit_form(default_data=None):
    if default_data is None:
        default_data = {
            "habit_name": "",
            "description": ""
        }
    
    st.subheader("Habit Details")
    habit_name = st.text_input("Habit Name", default_data["habit_name"])
    description = st.text_area("Description", default_data["description"])
    
    return {
        "habit_name": habit_name,
        "description": description
    }
