import streamlit as st
import streamlit.components.v1 as components
from functions import *
from linkedin_badge import *
from data import pdf


# Set page settings
st.set_page_config(
    page_title="Stylianos Moschotoglou - CV",
    layout="centered"
)

# Set header
st.write("### Stylianos Moschotoglou")
st.markdown("Python Developer - Data Analyst")

# Download button for pdf version
st.download_button(
    label="Download CV",
    data=pdf,
    file_name='Stylianos Moschotoglou - CV.pdf')




tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Experience', 'Education', 'Languages', 'Skills', 'Certifications', 'Contact'])




# Experience Section
with tab1:
    st.markdown("#### Experience")

    get_experience(experience, 0)
    st.write("---")
    get_experience(experience, 1)
    st.write("---")
    get_experience(experience, 2)




# Education Section
with tab2:
    st.markdown("#### Education")

    get_education(education, 0)
    st.write("---")
    get_education(education, 1)





# Languages Section
with tab3:
    st.markdown("#### Languages")

    col3, col4 = st.columns(2)

    with col3:
        get_languages(languages, 0)

    with col4:
        get_languages(languages, 1)





# Skills section
with tab4:
    st.markdown("#### Skills")

    # Programming Languages
    st.write("###### Programming Languages")
    st.write("")
    col5, col6, col7 = st.columns(3)

    with col5:
        # Python
        st.image('https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png',
                width=50,
        )
    with col6:    
        # SQL
        st.image('https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png',
                    width=50,
        )
    with col7:
        # Java
        st.image('https://upload.wikimedia.org/wikipedia/en/3/30/Java_programming_language_logo.svg',
                    width=40,
        )

    st.write("")

    # Visualization Tools
    st.write("###### Visualization Tools")  
    st.write("")
    col8, col9 = st.columns(2)

    with col8:
        # Tableau
        st.image('https://upload.wikimedia.org/wikipedia/commons/4/4b/Tableau_Logo.png',
                    width=160,
        )    
    with col9:
        # Power BI
        st.image('https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg',
                    width=40,
        ) 
        




# Certifications Section
with tab5:
    
    with st.expander("Datacamp Certifications"):
        st.image("files/datacamp.png", width=250)
        
        for i in range(datacamp_list):
            get_certificates(certificates, 'datacamp', i)
    
    with st.expander("LinkedIn Learning Certifications"):
        st.image("files/LinkedIn_Learning_Logo.png", width=250)

        for i in range(linkedin_list):
            get_certificates(certificates, 'linkedin', i)




# Contact Section
with tab6:
    st.markdown("#### Contact Information")
    col10, col11 = st.columns(2)

    with col10:
        st.markdown("""
                    **Personal Information**
                    \n - E: smoschotoglou@outlook.com  
                    \n - T: +30 697 579 1008
                    \n **GitHub**
                    \n - https://github.com/ste-mos              

    """)
    
    with col11:
        components.html("""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="stylianos-moschotoglou" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://gr.linkedin.com/in/stylianos-moschotoglou?trk=profile-badge"></div>
              """, height=310)
