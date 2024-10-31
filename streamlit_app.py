import streamlit as st


profilePicturePath = 'data/profile.jpg'

# Basic configuration
st.set_page_config(page_title="My Portfolio", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Projects", "Skills", "Contact"])

# Home Section
if page == "Home":
    st.title("Welcome to My Portfolio")
    # Display Profile Picture
    st.image(profilePicturePath)  # Adjust width as needed
    st.write("Hi, I'm [Your Name], a [Your Profession].")
    st.write("This is a simple portfolio built with Streamlit.")

# About Me Section
elif page == "About Me":
    st.header("About Me")
    # Display Profile Picture
    st.image(profilePicturePath)  # Adjust width as needed
    st.write("Here's a little background about me...")
    # Add more content, images, or profile information here

# Projects Section
elif page == "Projects":
    st.header("Projects")
    st.write("Here are some projects I've worked on.")
    project_data = [
        {"name": "Project 1", "description": "A brief description of Project 1.", "link": "http://example.com"},
        {"name": "Project 2", "description": "A brief description of Project 2.", "link": "http://example.com"},
    ]
    for project in project_data:
        st.subheader(project["name"])
        st.write(project["description"])
        st.markdown(f"[Learn more]({project['link']})")

# Skills Section
elif page == "Skills":
    st.header("Skills")
    st.write("Here's a breakdown of my skills.")
    skills = {
        "Programming Languages": ["Python", "JavaScript", "SQL"],
        "Frameworks": ["Streamlit", "Django", "Flask"],
    }
    for skill, items in skills.items():
        st.subheader(skill)
        st.write(", ".join(items))

# Contact Section
elif page == "Contact":
    st.header("Contact Me")
    st.write("Let's get in touch!")
    st.write("[LinkedIn](https://linkedin.com/in/yourprofile) | [GitHub](https://github.com/yourprofile) | [Email](mailto:your-email@example.com)")
