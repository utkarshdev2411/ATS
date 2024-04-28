from dotenv import load_dotenv

load_dotenv()
import base64 # type: ignore
import io # type: ignore
import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai



genai.configure(api_key=os.getenv("GENAI_API_KEY"))



def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input, pdf_content[0], prompt])
    return response.text


#convert pdf to image
def convert_pdf_to_image(pdf_path):
    if pdf_path is not None:
        images = pdf2image.convert_from_bytes(pdf_path.read())
        
        first_page = images[0]  # get the first page

        # convert PIL image to byte array
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts=[
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode('utf-8')
            }

        ]
        return pdf_parts
    else:
         raise FileNotFoundError("File not found")
    
## Streamlit App
st.set_page_config(page_title="ATS Resume Expert", page_icon="🔮")
st.header("🔮 ATS Resume Expert")
input_text = st.text_area("Job Description",key="input", height=250)
uploaded_file = st.file_uploader("Upload a resume(PDF)...", type=["pdf"])

if uploaded_file is not None:
   st.write("Resume uploaded successfully")

submit1=st.button("Tell Me about the resume")

submit2=st.button("How can I improve my resume?")

# submit3=st.button("What are the keywords that are Missing")

submit3=st.button("Percentage Matched")


input_prompt1 = """
 Analyze the following resume and corresponding job description to assess the candidate's fit for the role. Identify the candidate's key skills and experience that directly align with the job requirements. Additionally, highlight any relevant certifications, achievements, or projects that demonstrate their capabilities.

Next, evaluate the candidate's experience level and identify any potential gaps compared to the desired qualifications. Are there specific skills or areas of knowledge that may require additional training or experience?

Finally, based on your analysis, provide a score (e.g., 1-5) indicating the overall fit between the candidate's profile and the job description. Briefly explain the rationale behind your score.*
"""

input_prompt3 = """
You are a highly specialized ATS scanner with expertise in data science and resume parsing. Analyze the provided resume and corresponding job description.

Matching Score:** Calculate a percentage score (0-100%) reflecting the overall match between the candidate's profile and the job requirements. This score should consider factors like:

Keyword Match: Identify and quantify the match between skills, experience, and qualifications listed in the resume and job description. give in a PARAGRAPH manner that is more clear to understand. Only give the 10-15 most important keywords.

Missing Keywords: Identify and list the top 5-10 most critical skills or qualifications mentioned in the job description that are missing from the candidate's resume. Make it crisp.

Work Experience: Evaluate the relevance and depth of the candidate's experience compared to the desired years of experience and specific job duties.



Final Thoughts:** Briefly summarize your assessment, including:

Key strengths of the candidate based on the resume-job description match.
Reasons for any significant gaps in the matching score.
Recommendation for further consideration based on the overall analysis (e.g., proceed to interview, needs additional information, not a strong fit).
"""

input_prompt2 = """
Skills: Identify the skills that are missing in regards to the description. Provide a list of skills that the candidate should consider adding to their resume to better align with the job requirements.

Experience: Evaluate the candidate's work experience and identify any gaps or areas that require further elaboration. Suggest specific examples or projects that could enhance the resume and demonstrate the candidate's qualifications.

Formatting: Review the resume's structure, layout, and overall presentation. Provide recommendations on how the candidate can improve the visual appeal and readability of their resume.
"""


if submit1:
    if uploaded_file is not None:
        pdf_content=convert_pdf_to_image(uploaded_file)
        response=get_gemini_response(input_text,pdf_content,input_prompt1)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.write("Please upload a resume first")

elif submit3:
    if uploaded_file is not None:
        pdf_content=convert_pdf_to_image(uploaded_file)
        response=get_gemini_response(input_text,pdf_content,input_prompt3)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.write("Please upload a resume first")    
elif submit2:
    if uploaded_file is not None:
        pdf_content=convert_pdf_to_image(uploaded_file)
        response=get_gemini_response(input_text,pdf_content,input_prompt2)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.write("Please upload a resume first")            