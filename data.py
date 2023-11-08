experience = {
    "Company" : ["IQVIA", "TIEM ADV", "TIEM ADV"],
    "Company Image" : ["files/Iqvia-logo-color.svg.png", "files/tiem_adv.png", "files/tiem_adv.png"],
    "Company Link" : ["https://www.iqvia.com/", "https://www.tiem.gr/", "https://www.tiem.gr/"],
    "Year" : ["July 2023 - Oct 2023", "Jan 2022 - Feb 2023", "Sept 2020 - March 2021"],
    "Job Title" : ["Intern, Data Analyst", "Project Manager", "Intern, Project Manager"],
    "Job Description" : ["Pre-processing, manipulating and analyzing large-scale datasets using Python and libraries such as pandas and NumPy. Designing and creating interactive data visualizations and dashboards using Matplotlib, Seaborn, Plotly Dash. Development of interactive web applications using Python frameworks such as Streamlit, for data visualization and reporting. Development of automated data analysis procedures. Development of automated data analysis procedures.", "Daily communication with the clients. Managing and filtering the requirements of the clients. Research methodologies based on client needs and requirements. Transfer of clients’ requests to the creative department for the correct execution of the project. Close cooperation with the creative department during each project. Strategic planning and brand development. Supervision of each project during its implementation.", "Daily communication with the clients. Managing and filtering the requirements of the clients. Research methodologies based on client needs and requirements. Transfer of clients’ requests to the creative department for the correct execution of the project. Close cooperation with the creative department during each project. Strategic planning and brand development. Supervision of each project during its implementation."]
}

education = {
    "Title" : ["MSc, Information Systems", "BSc, Organizations Management, Marketing and Tourism"],
    "University" : ["University of Macedonia", "International Hellenic University"],
    "Year" : ["March 2022 - present", "Oct 2015 - Aug 2021"]
}

languages = {
    "Language" : ["English", "Greek"],
    "Level" : ["Proficient", "Native"]
}

"""skills = {
    "Microsoft Office" : ["Excel" , "Word", "PowerPoint"],
    "Programming Languages" : ["Python", "Java", "SQL"],
    "Visualization Tools" : ["Power BI", "Tableau", "Python libraries (Matplotlib, Seaborn, Plotly)"],
    "Machine Learning" : ["scikit-learn package"],
    "Databases" : ["SQL"]
}"""

certifications = {
    "Instructor" : ["Datacamp", "Datacamp", "Datacamp", "Datacamp", "Datacamp", "Datacamp", 
                    "Datacamp", "Datacamp", "Datacamp", "Datacamp", "Datacamp", "Datacamp", 
                    "LinkedIn Learning", "LinkedIn Learning", "LinkedIn Learning", "LinkedIn Learning", 
                    "LinkedIn Learning", "LinkedIn Learning", "LinkedIn Learning","LinkedIn Learning"],
    
    "Title" : ["Tableau Fundamentals", "Introduction to Python", "Intermediate Python", 
               "Data Manipulation with pandas", "Joining Data with pandas", 
               "Introduction to Data Visualization with Seaborn", "Introduction to Statistics in Python", 
               "Machine Learning with scikit-learn", "Introduction to SQL", "Intermediate SQL", 
               "Joining Data in SQL", "Supervised Learning with scikit-learn", "Statistics Foundations 1: The Basics", 
               "Statistics Foundations 2: Probability", "Python for Data Visualization", "Python Data Analysis", 
               "Introduction to Career Skills in Data Analytics", "Advanced Pandas", "Processing Text with Python Essential Training", 
               "Machine Learning with Python: Logistic Regression"],
    
    "Hours" : ["24 Hours", "4 Hours", "4 Hours", "4 Hours", "4 Hours", "4 Hours", "4 Hours", 
               "4 Hours", "4 Hours", "4 Hours", "4 Hours", "4 Hours", "4 Hours", "4 Hours", 
               "4 Hours", "4 Hours", "4 Hours", "4 Hours", "4 Hours", "4 Hours"]
}


certificates = {
    "datacamp":{
        "Title" : ["Tableau Fundamentals", "Introduction to Python", "Intermediate Python", 
               "Data Manipulation with pandas", "Joining Data with pandas", 
               "Introduction to Data Visualization with Seaborn", "Introduction to Statistics in Python", 
               "Machine Learning with scikit-learn", "Introduction to SQL", "Intermediate SQL", 
               "Joining Data in SQL", "Supervised Learning with scikit-learn"],
        "Hours": ["24 Hours", "4 Hours", "4 Hours", "4 Hours", "4 Hours", "4 Hours", "4 Hours", 
                "4 Hours", "4 Hours", "4 Hours", "4 Hours", "4 Hours"]
                },
    "linkedin":{
        "Title" : ["Statistics Foundations 1: The Basics", 
               "Statistics Foundations 2: Probability", "Python for Data Visualization", "Python Data Analysis", 
               "Introduction to Career Skills in Data Analytics", "Advanced Pandas", "Processing Text with Python Essential Training", 
               "Machine Learning with Python: Logistic Regression"],
        "Hours": ["4 Hours", "4 Hours", "4 Hours", "4 Hours", "4 Hours", "4 Hours", "4 Hours", 
               "4 Hours", "4 Hours"]
    }
}

linkedin_certificates = {}

datacamp_list = len(certificates['datacamp']["Title"])
linkedin_list = len(certificates['linkedin']["Title"])

cert_list = len(certifications["Title"])

#CV in PDF
with open("files/Stylianos Moschotoglou - CV.pdf", "rb") as pdf_file:
    pdf = pdf_file.read()