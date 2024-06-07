import streamlit as st
import datetime
from services.data_service import load_data, save_data

def habit_tracker(habit_name, habit_id):
    st.subheader(f"Track '{habit_name}'")
    
    today = datetime.date.today()
    date_str = today.strftime('%Y-%m-%d')
    
    habit_data = load_data(f"data/habit_tracking_{habit_id}.json")
    
    # Check if habit_data exists for today, initialize if it doesn't
    if not any(day['date'] == date_str for day in habit_data):
        habit_data.append({
            'date': date_str,
            'status': 'pending'
        })
        save_data(habit_data, f"data/habit_tracking_{habit_id}.json")
    
    # Display habit tracking
    st.subheader("Habit Tracking")
    for day in habit_data:
        st.text(f"Date: {day['date']}, Status: {day['status']}")
    
    # Button to mark habit as completed
    if st.button("Mark as Completed"):
        for day in habit_data:
            if day['date'] == date_str:
                day['status'] = 'completed'
                save_data(habit_data, f"data/habit_tracking_{habit_id}.json")
                st.success("Habit marked as completed!")
                break
