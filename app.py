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
    "🏆 Applying Advanced LookML Concepts in Looker": "https://www.cloudskillsboost.google/public_profiles/ee8343cc-a3ce-412c-b33e-de8209ff9645/badges/3060629?utm_medium=social&utm_source=linkedin&utm_campaign=ql-social-share",
    "🏆 RevOps Certified (Hotspot)": "https://app-eu1.hubspot.com/academy/achievements/48ct57xg/en/1/mehrdad-touraji/revenue-operations",
    "🏆 Database Objects, Virtual Warehouse creation and configuration, loading and querying": "https://www.credly.com/badges/4a841404-472b-4f55-b6ee-24d344195bad/linked_in_profile",
    "🏆 Data Science with Python": "https://www.linkedin.com/posts/mehrdad-touraji-6a7bb3234_im-happy-to-share-that-ive-obtained-a-new-activity-7008126054481436672-wWe2/?utm_source=share&utm_medium=member_desktop",
    "🏆 AWS Cloud Practioner": "https://www.linkedin.com/posts/mehrdad-touraji-6a7bb3234_validate-or-obtain-understanding-of-cloud-activity-7005602814936686592-WWy-/?utm_source=share&utm_medium=member_desktop",
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
- ✔️ Led product strategy and development, collaborating with cross-functional teams to deliver customer-centric solutions.
- ✔️ Utilized agile methodologies to drive iterative product enhancements, resulting in improved user experience and increased customer satisfaction.
- ✔️ Applied data-driven insights to make informed product decisions, aligning business objectives with user needs.
- ✔️  Demonstrated strong leadership skills in guiding product development lifecycles, ensuring timely delivery and meeting strategic goals.
"""
)


## Skills
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Proficient in product management tools and methodologies, including agile frameworks (Scrum/Kanban) and product roadmap planning.
- 📊 Skilled in data-driven decision-making, utilizing analytics and user research to inform product strategy and feature prioritization.
- 📚 Strong understanding of software development lifecycle (SDLC), user experience (UX) design principles, and market analysis.
- 🗄️ Experience working with databases, data modeling, and integrating data-driven insights into product development.
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
    st.write(f"[{project}]({link})")

