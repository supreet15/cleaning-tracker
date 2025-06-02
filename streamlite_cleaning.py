import streamlit as st

# Set app title
st.title("🧽 Cleaning Tracker")

# Tabs for daily, weekly, monthly
tabs = st.tabs(["🗓️ Daily Tasks", "📅 Weekly Tasks", "🗓️ Monthly Tasks"])

# Sample tasks
daily_tasks = [
    "Make beds", "Tidy living room", "Do dishes",
    "Wipe kitchen counters", "Sweep kitchen floor", "Quick bathroom wipe-down"
]

weekly_tasks = [
    "Mop floors", "Vacuum rugs/carpets", "Deep clean bathrooms",
    "Change bedsheets", "Take out trash/recycling", "Dust furniture & shelves"
]

monthly_tasks = [
    "Clean fridge", "Wash windows", "Deep clean kitchen appliances",
    "Wipe down walls & baseboards", "Clean inside cabinets & drawers"
]

# Daily Tasks tab
with tabs[0]:
    st.header("Daily Checklist")
    for task in daily_tasks:
        st.checkbox(task, key=f"daily-{task}")

# Weekly Tasks tab
with tabs[1]:
    st.header("Weekly Checklist")
    for task in weekly_tasks:
        st.checkbox(task, key=f"weekly-{task}")

# Monthly Tasks tab
with tabs[2]:
    st.header("Monthly Checklist")
    for task in monthly_tasks:
        st.checkbox(task, key=f"monthly-{task}")
