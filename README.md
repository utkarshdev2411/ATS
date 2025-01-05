# ATS Resume Expert

"ATS Resume Expert" is a Streamlit-based web application designed to analyze resumes against job descriptions using Google's Generative AI. This tool provides detailed feedback on how well a resume matches a job description, including insights on key skills, experience gaps, and formatting improvements.

## Features

1. **Resume Upload**  
   - Upload a PDF resume for analysis.

2. **Job Description Input**  
   - Enter the job description in a text area.

3. **AI-Powered Analysis**  
   - Uses Google's Generative AI to compare the resume and job description.

4. **Feedback Options**  
   - **Tell Me about the Resume**: Provides insights into how well the resume fits the job description.  
   - **How Can I Improve My Resume?**: Suggests actionable improvements for the resume.  
   - **Percentage Matched**: Calculates a compatibility score between the resume and job description.

## Technical Details

- **Streamlit**: Framework for creating the web interface.
- **Google Generative AI**: Powers the resume and job description analysis.
- **Python-Dotenv**: Manages environment variables.
- **PDF2Image**: Converts PDF resumes into images for processing.
- **Pillow (PIL)**: Handles image processing.
- **Base64**: Encodes images for rendering.

## Files

- **app.py**: The main application file containing all logic for PDF processing, AI integration, and the Streamlit app interface.
- **requirements.txt**: Lists all required Python packages.
- **.gitignore**: Defines files and directories to be excluded from Git tracking.

## How to Run

1. Install the required dependencies:  
   ```sh
   pip install -r requirements.txt
Set up your environment variable:
Create a .env file and add your Generative AI API key:

plaintext
Copy code
GENAI_API_KEY=your_api_key_here
Start the Streamlit app:

sh
Copy code
streamlit run app.py
