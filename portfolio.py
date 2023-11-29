import streamlit as st
import info
import pandas as pd
from PIL import Image
import base64

def who_am_i_section():
    st.header("Who Am I?")
    st.write(info.who_am_i)
    st.write("---")

def career_goals_section():
    st.header("Career Goals")

    st.subheader("Long-term Aspirations")
    st.write(info.career_goals["long_term_aspirations"])

    st.subheader("Roadmap and Timeline")
    for item in info.career_goals["roadmap_timeline"]:
        st.write("- " + item)

    st.subheader("Budget")
    for item in info.career_goals["budget"]:
        st.write("- " + item)

    st.subheader("Key Steps")
    for step in info.career_goals["key_steps"]:
        st.write("- " + step)

    st.write("---")
def get_base64_encoded_pdf(pdf_file_path):
    with open(pdf_file_path, "rb") as pdf_file:
        return base64.b64encode(pdf_file.read()).decode('utf-8')

# About Me Section
def about_me_section():
    st.header("About Me")
    
    # Create two columns: one for the image and one for the text
    col1, col2 = st.columns([1, 2])  # Adjust the ratio based on your preference

    # Load and rotate the image
    image = Image.open(info.profile_picture)
    rotated_image = image.rotate(-90, expand=True)

    # Display the image in the first column
    with col1:
        col1.image(rotated_image, width=200)

    # Display the text in the second column
    with col2:
        col2.write(info.about_me)
        col2.write(info.about_me1)

    st.write('---')

# Sidebar Links Section
def links_section():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link = f'<a href="{info.my_linkedin_url}"><img src="{info.linkedin_image_url}" alt="LinkedIn" width="75" height="75"></a>'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)
    st.sidebar.text("Checkout my work")
    github_link = f'<a href="{info.my_github_url}"><img src="{info.github_image_url}" alt="Github" width="65" height="65"></a>'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)
    st.sidebar.text("Or email me!")
    email_html = f'<a href="mailto:{info.my_email_address}"><img src="{info.email_image_url}" alt="Email" width="75" height="75"></a>'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)

    # Resume download
    st.sidebar.header("Resume")
    with open(info.resume_file_path, 'rb') as file:
        st.sidebar.download_button(
            label="Download Resume",
            data=file,
            file_name=info.resume_download_name,
            mime='application/octet-stream'
        )

    # View Resume button
    if st.sidebar.button('View Resume'):
        base64_pdf = get_base64_encoded_pdf(info.resume_file_path)
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
        st.sidebar.markdown(pdf_display, unsafe_allow_html=True)

# Call the sections to display them
about_me_section()
who_am_i_section()
links_section()
career_goals_section()
# ... rest of your Streamlit app code ...

# info.py file content needs to be updated with the actual paths and file names:
# info.resume_file_path = 'path/to/Liu_Yichuan_Resume.pdf'
# info.resume_download_name = 'Resume_Yichuan_Liu.pdf'


# Education
def education_section(education_data, course_data,education_data1):
    st.header("Education")
    st.subheader(f"**{education_data['Institution']}**")
    st.write(f"**Degree:** {education_data['Degree']}")
    st.write(f"**Graduation Date:** {education_data['Graduation Date']}")
    st.write(f"**GPA:** {education_data['GPA']}")

    st.write("**Relevant Coursework:**")
    coursework = pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code": "Course Code",
        "names": "Course Names",
        "semester_taken": "Semester Taken",
        "skills": "What I Learned"},
        hide_index=True
    )

    st.subheader(f"**{education_data1['Institution']}**")
    st.write(f"**Degree:** {education_data1['Degree']}")
    st.write(f"**Graduation Date:** {education_data1['Graduation Date']}")
    st.write(f"**GPA:** {education_data1['GPA']}")
    
    st.write("---")


education_section(info.education_data, info.course_data, info.education_data1)

def experience_section(experience_data):
    st.header("Professional Experience")
    for job_title, (job_description, image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        
        if image is not None:
            expander.image(image, width=250)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")

experience_section(info.experience_data)


# Skills
def skills_section(programming_data, spoken_data):
    st.header("Skills")
    st.subheader("Programming Languages")
    for skill, percentage in programming_data.items():
        st.write(f"{skill} {info.programming_icons.get(skill, '')}")
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.write(f"{spoken} {info.spoken_icons.get(spoken, '')}: {proficiency}")
skills_section(info.programming_data, info.spoken_data)

#Activities

def activities_section(leadership_data, activity_data):
    st.header("Activities")
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])

    with tab1:
        st.subheader("Leadership")
        for title, (details, image) in leadership_data.items():
            expander = st.expander(f"{title}")
            
            if image is not None:
                expander.image(image, width=250)
            for bullet in details:
                expander.write(bullet)

    with tab2:
        st.subheader("Community Service")
        for title, details in activity_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)

st.write("---")
activities_section(info.leadership_data, info.activity_data)


# Projects
def project_section(projects_data,s1,s2,s3,s4,s5,s6,s7,s8,p1,p2,p3):
    st.header("Projects")
    for project_name, project_description in projects_data.items():
        expander = st.expander(f"{project_name}")
        expander.write(project_description)
    expander = st.expander(f"{s1}")
    expander.subheader("Objective and Motivation")
    expander.write(s2)
    expander.subheader("Technical Setup")
    expander.subheader("Materials:")
    for s in s3:
        expander.write("-"+s)
    expander.subheader("The Ultrasonic Sensor")
    expander.write(p1)
    expander.subheader("Arduino UNO")
    expander.write(p2)
    expander.subheader("The Buzzer")
    expander.write(p3)
    expander.subheader("Implementation process")
    for t,i in s4:
        expander.image(i)
        expander.write(t)
    expander.subheader("Programming the Arduino")
    expander.image("code.png")
    for c in s5:
        expander.write(c)
    expander.subheader("Connecting to battery")
    expander.write("Now use the battery clip to connect the Arduino with the 9V battery. Now the sensor is portable. For adjusting the distanece connect with Arduino and set it up. Here is the final result:")
    expander.image("final.jpg")
    expander.subheader("Learning Outcomes")
    expander.subheader("Technical Skills")
    for c in s6:
        expander.write(c)
    expander.subheader("Essential Skills")
    for c in s7:
        expander.write(c)
    expander.subheader("Conclusion")
    expander.write(s8)
    expander.write("source:https://www.geeksforgeeks.org/distance-measurement-using-ultrasonic-sensor-and-arduino/")

    st.write("---")
    
project_section(info.projects_data,info.s1,info.s2,info.s3,info.s4,info.s5,info.s6,info.s7,info.s8,info.p1,info.p2,info.p3)