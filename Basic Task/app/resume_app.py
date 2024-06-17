import streamlit as st

# Set page configuration
st.set_page_config(page_title="Neha Sakhawat's Digital Resume", page_icon="📄", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #000000;
        padding: 20px;
        font-family: 'Arial', sans-serif;
    }
    .title {
        font-size: 48px;
        font-weight: bold;
        color: #39ff14; /* Neon green color */
        text-align: center;
        margin-bottom: 5px;
    }
    .subtitle {
        font-size: 24px;
        font-weight: bold;
        color: #39ff14; /* Neon green color */
        text-align: center;
        margin-top: 5px;
        margin-bottom: 20px;
    }
    .section-header {
        font-size: 20px;
        font-weight: bold;
        color: #39ff14; /* Neon green color */
        text-align: center;
        margin-top: 20px;
        margin-bottom: 10px;
        border-bottom: 2px solid #39ff14; /* Neon green color */
        padding-bottom: 5px;
    }
    .info-item {
        font-size: 16px;
        color: #c0c0c0; /* Metallic color */
        text-align: left;
        line-height: 1.6;
        margin-bottom: 10px;
    }
    .contact-info {
        font-size: 16px;
        color: #c0c0c0; /* Metallic color */
        text-align: left;
        line-height: 1.6;
        margin-bottom: 20px;
    }
    .skills-bar {
        width: 100%;
        max-width: 300px;
        background-color: #333333;
        border-radius: 5px;
        margin-bottom: 10px;
        margin: 0 auto;
    }
    .skills-bar-inner {
        height: 24px;
        border-radius: 5px;
    }
    .problem-solving {
        width: 92%;
        background-color: #39ff14; /* Neon green color */
    }
    .adaptability {
        width: 98%;
        background-color: #39ff14; /* Neon green color */
    }
    </style>
""", unsafe_allow_html=True)

# Title and Introduction
st.markdown('<h1 class="title">Neha Sakhawat\'s Digital Resume</h1>', unsafe_allow_html=True)
st.markdown("""
<div class="info-item">
Welcome to my professional digital resume. I am an enthusiastic and motivated individual with a strong background in Computer Science.
</div>
""", unsafe_allow_html=True)

# Contact Information
st.markdown('<div class="section-header">Contact Information</div>', unsafe_allow_html=True)
st.markdown('<div class="contact-info">LinkedIn: <a href="https://www.linkedin.com/in/neha-s-2135b8284" style="color:#39ff14;">www.linkedin.com/in/neha-s-2135b8284</a><br>Email: neeha9012@gmail.com<br>Mobile: +92 347 0436193<br>GitHub: <a href="https://github.com/Neha9012" style="color:#39ff14;">github.com/Neha9012</a></div>', unsafe_allow_html=True)

# Education
st.markdown('<div class="section-header">Education</div>', unsafe_allow_html=True)
st.markdown("""
    <ul class="info-item">
        <li><strong>Fazaia College of Education for Women</strong><br>Bachelor of Science in Computer Science, 4th Semester<br>GPA: 3.31<br>June 2022 - August 2026<br>Lahore, Pakistan</li>
        <li><strong>IT Academy PAF Base Lahore Cantt</strong><br>Diploma in Information Technology (DIT), Grade: A+<br>January 2021 – February 2022<br>Lahore, Pakistan</li>
    </ul>
""", unsafe_allow_html=True)

# Skills Summary with Bars (Adjusted to remove Soft Skills)
st.markdown('<div class="section-header">Skills Summary</div>', unsafe_allow_html=True)
st.markdown("""
    <ul class="info-item">
        <li><strong>Languages:</strong> Python, C++, CSS, HTML</li>
        <li><strong>Frameworks:</strong> Pandas, Numpy, Scikit-Learn, Matplotlib</li>
        <li><strong>Tools:</strong> Excel, PowerPoint, MS Word</li>
        <li><strong>Platforms:</strong> VS Code, Jupyter Notebook, Visual Studio, .NET</li>
    </ul>
""", unsafe_allow_html=True)

# Experience
st.markdown('<div class="section-header">Work Experience</div>', unsafe_allow_html=True)
st.markdown("""
    <ul class="info-item">
        <li><strong>Coding Mentor, TeacherOn.com</strong><br>January 2023 - 2024<br>
            <ul>
                <li>Guided mentees through coding challenges with tailored support.</li>
                <li>Shared industry insights for enhanced coding proficiency.</li>
                <li>Conducted hands-on sessions to reinforce coding skills.</li>
                <li>Offered constructive feedback for continual improvement.</li>
                <li>Personalized mentorship for individual coding growth.</li>
            </ul>
        </li>
    </ul>
""", unsafe_allow_html=True)

# Projects
st.markdown('<div class="section-header">Projects</div>', unsafe_allow_html=True)
st.markdown("""
    <ul class="info-item">
        <li><strong>Technotalks: Where Tech Conversations Flourish</strong><br>February 2023<br>
            <ul>
                <li>Developed user-friendly frontend for Technotalks Guest Post Website.</li>
                <li>Integrated secure user authentication for guest authors.</li>
                <li>Implemented responsive design for seamless access across devices.</li>
                <li>Ensured cross-browser compatibility for universal accessibility.</li>
                <li>Conducted usability testing to refine and optimize user experience.</li>
            </ul>
        </li>
        <li><strong>Face Detection Attendance Tracking System</strong><br>October 2023<br>
            <ul>
                <li>Developed Python script using OpenCV for automated employee entrance tracking.</li>
                <li>Utilized webcam for real-time face detection at office entrance.</li>
                <li>Script captured date, time, and employee photo upon face detection.</li>
                <li>Automated attendance recording streamlined management process.</li>
                <li>Enhanced accuracy, reduced workload, and improved security.</li>
            </ul>
        </li>
        <li><strong>Student Portal Frontend Development</strong><br>August 2023<br>
            <ul>
                <li>Developed user-friendly frontend interface for student portal.</li>
                <li>Implemented responsive design using HTML, CSS, and JavaScript.</li>
                <li>Collaborated with backend team to integrate frontend with backend services.</li>
                <li>Conducted usability testing to ensure intuitive navigation.</li>
                <li>Achieved seamless cross-browser compatibility for enhanced accessibility.</li>
            </ul>
        </li>
        <li><strong>Network Traffic Anomaly Detection with Python</strong><br>June 2024<br>
            <ul>
                <li>Implemented network traffic anomaly detection using Isolation Forests and PCA.</li>
                <li>Leveraged machine learning algorithms for enhanced network security.</li>
                <li>Analyzed network traffic data to identify patterns and detect anomalies.</li>
                <li>Utilized Python for data processing, model training, and anomaly detection.</li>
                <li>Improved network security by identifying potential threats in real-time.</li>
            </ul>
        </li>
    </ul>
""", unsafe_allow_html=True)

# Certificates (Adjusted to remove Soft Skills)
st.markdown('<div class="section-header">Certificates</div>', unsafe_allow_html=True)
st.markdown("""
    <ul class="info-item">
        <li>Google Data Analytics Certification (March 2023): Accreditation for expertise in data analytics conferred by Google.</li>
        <li>Huawei Certification in Artificial Intelligence (March 2023): Accreditation in AI technologies awarded by Huawei.</li>
        <li>AI Provisional Certification, Prime Minister Youth Development Program (March 2023): Certification in AI through a government youth development initiative.</li>
        <li>Crash Course on Python, Google (March 2023): Certificate of completion for an intensive Python programming course.</li>
        <li>Huawei Talent Python Certification (March 2023): Certification demonstrating proficiency in Python programming endorsed by Huawei.</li>
        <li>Certificate in Information Technology (DIT) (March 2023): Formal recognition of competency in Information Technology skills.</li>
        <li>Cyber Security, Network Academy (March 2023): Certification verifying skills in cybersecurity acquired through a network academy.</li>
        <li>Cybersecurity Certifications (Various Dates): Assorted certifications attesting to proficiency in various cybersecurity technologies and methodologies, including network security, ethical hacking, and risk management.</li>
        <li>AI Mathematics (March 2023): Accreditation focusing on mathematical concepts and applications within Artificial Intelligence.</li>
        <li>AI Google Essentials Certificate (June 2024): Certification covering essential concepts and applications in artificial intelligence provided by Google.</li>
    </ul>
""", unsafe_allow_html=True)
