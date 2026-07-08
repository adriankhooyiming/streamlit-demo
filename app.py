import streamlit as st
from PIL import Image

# App title
st.title("Edited Demo Line")

# Header and subheader
st.header("Welcome!")
st.subheader("This is my Python web app")

# Display text and markdown
st.text("This is plain text.")
st.markdown("**This is bold markdown text.**")

# Display status messages
st.success("Operation successful!")
st.info("Here is some information.")
st.warning("This is a warning.")
st.error("An error occurred.")

# Image display
img = Image.open("dog.jpg")
st.image(img, width=200)

# Dynamic checkboxes generated from a list
st.subheader("Select your skills")

skills = ["Python", "HTML", "Data Analysis", "AI", "Robotics", "You have nothing?!"]
selected_skills = []  # empty list to collect selected skills

# Loop through the list to create one checkbox per skill
for skill in skills:
    if st.checkbox(skill):            # creates a checkbox with the skill name
        selected_skills.append(skill)  # add to selected list if ticked

# Display results based on what was selected
if len(selected_skills) > 0:
    st.success(f"You selected {len(selected_skills)} skill(s):")
    for s in selected_skills:
        st.write(f"  - {s}")

    # Calculate and display a percentage
    percentage = round(len(selected_skills) / len(skills) * 100)
    st.metric("Skills coverage", f"{percentage}%")
else:
    st.warning("Please select at least one skill.")

if "You have nothing?!" in selected_skills:
    st.warning("It can't be. Look at the skills more carefully.")
   
# Radio button
gender = st.radio("Select Gender:", ['Male', 'Female'])
st.success(f"Selected: {gender}")
if gender == "Male":
    st.write("You have chosen Male")
else:
    st.write("You have chosen Female")

# Selectbox
hobby = st.selectbox("Select a Hobby:", ['Dancing', 'Reading', 'Sports', 'Something else'])
st.write("Your hobby is:", hobby)

# Slider
level = st.slider("Choose a level", 1, 8)
st.write(f"Selected level: {level}")

# Text input
name = st.text_input("Enter your name", "")
if st.button("Submit"):
   st.success(f"Hello, {name.title()}!")
