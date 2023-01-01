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
- ✔️ 4 Years expereince extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and GSheet
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


## Skills
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, LookML 
- 📊 Data Visulization: Tableau , Plotly, Seasborn
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: MySQL, RDS , PostgreSQL
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
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Utilised intuitive technology that eliminates mundane tasks and speeds resolutions of issues for better business outcomes
- ► Redesigning data model through iterations, testing, 
"""
)

## 2
st.write('\n')
st.write("🚧", "**Quality Analyst | Majorel GmbH**")
st.write("01/2018 - 02/2022")
st.write(
    """
- ► Built data models and maps to generate meaningful insights from customer data, boosting successful productivity eﬀorts by 12%
- ► Modeled targets likely to renew, and presented analysis to leadership, which led to a YoY revenue increase of €300K
- ► Studied large amounts of data to drive strong understanding of data lifecycle management and data governance and even stronger understanding of data management concepts
"""
)

## 3
st.write('\n')
st.write("🚧", "**Subject Matter Expert | Arvato CRM Solutions**")
st.write("04/2015 - 01/2018")
st.write(
    """
- ► Devised KPIs across mutli-international world-wide markets in collaboration with cross-functional teams to support Product Managers in clustering and prioritization of requirements
- ► Review product changes in the acceptance phase to drive operational analysis of the platform
- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")

