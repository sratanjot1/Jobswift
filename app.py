import os
import streamlit as st
import google.generativeai as palm
from dotenv import load_dotenv

load_dotenv()
# Configure the API with your API key
palm.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Define the model to be used
model_name = 'models/text-bison-001'

#Function to generate resume
def generate_resume(name, experience, skills, projects, education, awards):
    prompt = f"My name is {name}. I have {experience} years of experience in {skills}."
    prompt += "\n\nProjects:\n{projects}\n\nEducation:\n{education}\n\nAwards and Recognition:\n{awards}"
    response = palm.generate_text(model=model_name, prompt=prompt)
    return response.result

#Function to generate cover letter
def generate_cover_letter(company_name, job_title):
    prompt = f"Dear Hiring Manager, \n\nI am writing to express my interest in the {job_title} position at {company_name}."
    response = palm.generate_text(model=model_name, prompt=prompt)
    return response.result

# Function to generate interview preparation questions
def generate_interview_questions (skills):
    prompt = f"Interview Preparation Questions Based on Skills: {skills}"
    response = palm.generate_text(model=model_name, prompt=prompt)
    return response.result

# Main Function

def main():
    st.title("JobSwift: Accelerating Careers With AI-Powered Applications")
    st.markdown("""
    JobSwift is an innovative platform leveraging AI technology to streamline the job application process and empower users in their career advancement journey. Powered by Google's PaLM model (text-bison-001) and integrated with Streamlit's interactive interface, JobSwift offers a range of AI-driven tools to optimize resumes, craft personalized cover letters, and prepare for interviews. Users input their career details, skills, and job preferences, and JobSwift generates tailored application materials tailored to their unique profiles. Whether users are seeking their first job, transitioning to a new career, or aiming for advancement in their current role, JobSwift provides personalized support to accelerate their career aspirations.

    ## Scenario 1: Recent Graduates Entering the Job Market
    JobSwift assists recent graduates in navigating the competitive job market by generating professional resumes and cover letters tailored to entry-level positions in their chosen field. Users input their academic achievements, internships, and relevant skills, and JobSwift generates polished application materials optimized for attracting hiring managers' attention. With JobSwift's support, recent graduates can kickstart their careers with confidence and stand out among other applicants.

    ## Scenario 2: Career Changers Exploring New Opportunities
    JobSwift supports individuals looking to transition into new career paths by providing personalized guidance and resources. Users input their current skills, past experiences, and desired job roles, and JobSwift suggests relevant courses, certifications, and skill enhancement opportunities to facilitate the transition. Additionally, JobSwift generates resumes and cover letters tailored to showcase transferable skills and align with the requirements of target positions, helping career changers successfully pivot into their desired fields.

    ## Scenario 3: Professionals Seeking Career Advancement
    JobSwift aids professionals in advancing their careers by offering tools to enhance their job application materials and interview preparation. Users input their career achievements, leadership experiences, and career goals, and JobSwift generates polished resumes highlighting key accomplishments and skills relevant to leadership positions. Furthermore, JobSwift provides interview preparation materials tailored to leadership roles, including common interview questions, strategies for showcasing leadership qualities, and tips for effective communication. With JobSwift's assistance, professionals can confidently pursue career advancement opportunities and take their careers to the next level.

""")
    option = st.sidebar.selectbox("Select Option", ["Generate Resume", "Generate Cover Letter", "Generate Interview Questions"])
    if option == "Generate Resume":
        st.subheader("Generate Resume")
        name = st.text_input("Enter your name")
        experience = st.number_input("Enter your years of experience", min_value=0, step=1)
        skills = st.text_area("Enter your skills")
        projects = st.text_area("Enter your projects")
        education = st.text_area("Enter your education")
        awards = st.text_area("Enter your awards and recognition")

        if st.button("Generate"):
            if name and experience and skills and projects and education and awards:
                resume = generate_resume(name, experience, skills, projects, education, awards)
                st.write(resume)
            else:
                st.warning("Please fill in all the fields.")

    elif option == "Generate Cover Letter":
        st.subheader("Generate Cover Letter")
        company_name = st.text_input("Enter the company name")
        job_title = st.text_input("Enter the job title")
        if st.button("Generate"):
            if company_name and job_title:
                cover_letter = generate_cover_letter (company_name, job_title) 
                st.write(cover_letter)
            else:
                st.warning("Please fill in all the fields.")

    elif option == "Generate Interview Questions":
        st.subheader("Generate Interview Questions")
        skills = st.text_area("Enter your skills")
        if st.button("Generate"):
            if skills:
                interview_questions = generate_interview_questions(skills)
                st.write(interview_questions)
            else:
                st.warning("Please enter your skills.")

if __name__ == "__main__":
    main()
