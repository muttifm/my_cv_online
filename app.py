from pathlib import Path
import streamlit as st
from PIL import Image


## Directories
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


## General
PAGE_TITLE = "Digital CV | Mehrdad Touraji"
PAGE_ICON = ":wave:"
NAME = "Mehrdad Touraji"
DESCRIPTION = """
Intraday Management Specialist, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "mehrdad.touraji@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/mehrdad-touraji-6a7bb3234/",
    "GitHub": "https://github.com/muttifm",
}

PROJECTS = {
    "🏆 Successfully developed and implemented end-to-end data pipelines, ensuring seamless data flow and processing.",
    "🏆 Led the design and optimization of data models, enabling efficient data storage and retrieval.",
    "🏆 Leveraged cloud technologies to architect scalable and cost-effective data solutions.","",
    "🏆 Collaborated cross-functionally to deliver innovative products and drive business growth through data insights."
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


## Asset Transfer
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


## Section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width = 550)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


## Social Media
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


## Experince and Qualifictions
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Versatile professional adept in data engineering, software development, and problem-solving across diverse domains.
- ✔️ Mastery in Python, Kotlin, and JavaScript, harnessing their full potential to deliver robust and scalable solutions.
- ✔️ Cloud Maestro proficient in leveraging cloud technologies to architect and optimize data pipelines.
- ✔️ Database Wrangler skilled in managing databases, designing efficient data models, and ensuring data integrity.
- ✔️ Pipeline Architect experienced in designing and implementing end-to-end data pipelines for seamless data flow.
- ✔️ Committed to driving insights and innovation through the power of data, enabling data-driven decision-making.
"""
)


## Skills
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 💻 Expertise in data engineering, software development, and agile methodologies for efficient product development.
- 📊 Proficient in data analysis, machine learning, and statistical modeling to extract actionable insights.
- 🔧 Strong problem-solving skills with a focus on delivering high-quality, scalable, and maintainable solutions.
- ☁️ Extensive experience with cloud platforms, including AWS and Azure, for scalable and secure data processing.
- 🗄️ Deep understanding of databases, data modeling, and optimization techniques to ensure data accuracy and performance.
"""
)


## Working Experience
st.write('\n')
st.subheader("Work History")
st.write("---")

## 1
st.write("🚧", "**Intraday Management Specialist | Trade Republic Bank GmbH**")
st.write("07/2020 - Present")
st.write(
    """
- ► Led product development initiatives, collaborating with stakeholders to define requirements and deliver high-quality solutions.
- ► Leveraged user feedback and market research to drive product enhancements, resulting in increased user adoption and revenue growth.
- ► Acted as a bridge between business stakeholders and development teams, ensuring clear communication and alignment of goals.
"""
)

## 2
st.write('\n')
st.write("🚧", "**Quality Analyst | Majorel GmbH**")
st.write("07/2020 - 12/2021")
st.write(
    """
- ► Managed product quality assurance processes, implementing effective testing strategies to enhance product performance and reliability.
- ► Worked closely with development teams to prioritize and resolve product issues, ensuring timely delivery of bug fixes and feature improvements.
- ► Contributed to product roadmap planning, leveraging data insights and user feedback to drive continuous product enhancements.
"""
)

## 3
st.write('\n')
st.write("🚧", "**Subject Matter Expert | Arvato CRM Solutions**")
st.write("08/2019 - 07/2020")
st.write(
    """
- ► Collaborated with cross-functional teams to define product requirements and validate solutions, ensuring alignment with customer needs and market trends.
- ► Conducted market research and competitor analysis to identify product gaps and opportunities for innovation.
- ► Provided subject matter expertise in product demonstrations and client presentations, influencing decision-making and driving successful product adoption.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write({project})

