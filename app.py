import streamlit as st
st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px; 
}

.card {
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #ddd;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)
from streamlit_mic_recorder import speech_to_text

st.set_page_config(
    page_title="AI Placement Coach",
    page_icon="🎯",
    layout="wide"
)
if "interview_number" not in st.session_state:
    st.session_state.interview_number = 0
if "interview_feedback" not in st.session_state:
    st.session_state.interview_feedback = None
if "interview_history" not in st.session_state:
    st.session_state.interview_history = []

st.markdown(
    '<div class="main-title">🔭 FutureLens AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your AI-powered direction system</div>',
    unsafe_allow_html=True
)


st.sidebar.title("Navigation")

option = st.sidebar.radio(
    "Choose a section",
    [
        "🏠 Dashboard",
        "📄 Resume Analyzer",
        "💼 Job Match",
        "🧠 AI Study Assistant",
        "🎤 Mock Interview",
        "💻 Coding Interview",
        "📊 Performance Report",
        "🗺️ Placement Roadmap"
    ]
)

if option == "🏠 Dashboard":

    st.title("🎯Dashboard ")

    st.write(
        "Your AI-powered placement preparation dashboard."
    )

    st.divider()

    # --------------------------------
    # Interview Statistics
    # --------------------------------

    interview_count = 0

    if "interview_history" in st.session_state:
        interview_count = len(
            st.session_state.interview_history
        )

    # --------------------------------
    # Resume Status
    # --------------------------------

    resume_status = "Not Analyzed"

    if "resume_analysis" in st.session_state:
        resume_status = "Analyzed ✅"

    # --------------------------------
    # Job Match Status
    # --------------------------------

    job_status = "Not Checked"

    if "job_match_result" in st.session_state:
        job_status = "Checked ✅"

    # --------------------------------
    # RAG Status
    # --------------------------------

    rag_status = "Not Used"

    if "chat_history" in st.session_state:
        if len(st.session_state.chat_history) > 0:
            rag_status = "Active ✅"

    # --------------------------------
    # Dashboard Cards
    # --------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📄 Resume",
            resume_status
        )

    with col2:

        st.metric(
            "💼 Job Match",
            job_status
        )

    with col3:

        st.metric(
            "🧠 Study Assistant",
            rag_status
        )

    st.divider()

    col4, col5, col6 = st.columns(3)

    with col4:

        st.metric(
            "🎤 Interview Questions",
            interview_count
        )

    with col5:

        coding_status = "Available ✅"

        st.metric(
            "💻 Coding Practice",
            coding_status
        )

    with col6:

        # --------------------------------
# Smart Placement Readiness Score
# --------------------------------

        score = 0

    # Resume = 20 points
    if resume_status == "Analyzed ✅":
        score += 20


    # Job Match = 20 points
    if job_status == "Checked ✅":
        score += 20


    # RAG Study = 20 points
    if rag_status == "Active ✅":
        score += 20


    # Interview performance = 20 points
    if interview_count > 0:

        score += 10

        if "interview_history" in st.session_state:

            completed = len(
                st.session_state.interview_history
            )

            if completed >= 3:
                score += 10


    # Coding practice = 20 points
    if "coding_problem" in st.session_state:

        score += 10

        if "coding_evaluation" in st.session_state:
            score += 10

            st.metric(
                "🎯 Readiness",
                f"{score}%"
            )

        st.divider()

        # --------------------------------
        # Preparation Progress
        # --------------------------------
        # --------------------------------
    # Performance Chart
    # --------------------------------

    st.subheader("📊 Preparation Overview")

    chart_data = {
        "Resume": 100 if resume_status == "Analyzed ✅" else 0,
        "Job Match": 100 if job_status == "Checked ✅" else 0,
        "RAG Study": 100 if rag_status == "Active ✅" else 0,
        "Interview": 100 if interview_count > 0 else 0,
        "Coding": 100 if "coding_problem" in st.session_state else 0
    }

    st.bar_chart(chart_data)
    st.subheader("🚀 Placement Preparation")

    st.progress(
            score / 100
        )

    if score < 40:

            st.info(
                "Start by analyzing your resume "
                "and practicing interview questions."
            )

    elif score < 80:

            st.info(
                "Good progress! Continue practicing "
                "RAG study, interviews and coding."
            )

    else:

            st.success(
                "Excellent progress! Keep practicing "
                "and prepare for real interviews."
            )

    st.divider()

    st.subheader("📌 Recommended Next Steps")

    if score < 40:

            st.write(
                "1. 📄 Analyze your resume"
            )

            st.write(
                "2. 💼 Check your resume against a job"
            )

            st.write(
                "3. 🎤 Practice a mock interview"
            )

    elif score < 80:

            st.write(
                "1. 🧠 Study using the RAG assistant"
            )

            st.write(
                "2. 💻 Practice coding problems"
            )

            st.write(
                "3. 🎤 Complete more mock interviews"
            )

    else:

        st.write(
            "1. 🎯 Practice advanced interview questions"
        )

        st.write(
            "2. 💻 Solve more coding problems"
        )

        st.write(
            "3. 📄 Keep improving your resume"
        )

elif option == "📄 Resume Analyzer":
    st.header("📄 Resume Analyzer")

    st.write("Upload your resume and let AI analyze it.")

    uploaded_file = st.file_uploader(
        "Upload your resume",
        type=["pdf"]
    )

    if uploaded_file is not None:

        from pypdf import PdfReader
        import ollama

        reader = PdfReader(uploaded_file)

        resume_text = ""

        for page in reader.pages:
            text = page.extract_text()

            if text:
                resume_text += text + "\n"

        st.success("Resume uploaded successfully!")

        with st.expander("📄 View Extracted Resume"):
            st.text_area(
                "Resume Content",
                resume_text,
                height=300
            )

        if st.button("🤖 Analyze My Resume"):

            with st.spinner("AI is analyzing your resume..."):

                prompt = f"""
You are an expert placement coach.

Analyze the following resume.

Give the result in these sections:

1. Skills Found
2. Projects Found
3. Education
4. Strengths
5. Weaknesses
6. Missing Skills
7. Suggestions for Placement Preparation

Keep the explanation simple and useful for a college student.

Resume:
{resume_text}
"""

                response = ollama.chat(
                    model="llama3.2",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                answer = response["message"]["content"]
                st.session_state.resume_analysis = answer

            st.subheader("🤖 AI Resume Analysis")

            st.markdown(answer)

elif option == "💼 Job Match":
    st.header("💼 Job Match")

    st.write("Compare your resume with a job description.")

    resume_file = st.file_uploader(
        "Upload your Resume",
        type=["pdf"],
        key="resume_match"
    )

    jd_file = st.file_uploader(
        "Upload Job Description",
        type=["pdf"],
        key="jd_match"
    )

    if resume_file is not None and jd_file is not None:

        from pypdf import PdfReader
        import ollama

        # Extract Resume
        resume_reader = PdfReader(resume_file)

        resume_text = ""

        for page in resume_reader.pages:
            text = page.extract_text()

            if text:
                resume_text += text + "\n"

        # Extract Job Description
        jd_reader = PdfReader(jd_file)

        jd_text = ""

        for page in jd_reader.pages:
            text = page.extract_text()

            if text:
                jd_text += text + "\n"

        st.success("Resume and Job Description uploaded!")

        if st.button("🔍 Check Job Match"):

            with st.spinner("AI is comparing your resume with the job..."):

                prompt = f"""
You are an expert placement and recruitment assistant.

Compare the student's resume with the job description.

Give the result in exactly these sections:

1. Match Score
Give a percentage from 0 to 100.

2. Matching Skills
List the skills present in both the resume and job description.

3. Missing Skills
List important skills required by the job but missing from the resume.

4. Matching Projects
Identify projects from the resume that are relevant to the job.

5. Resume Improvement Suggestions
Give practical suggestions.

6. Preparation Plan
Tell the student what they should learn or practice before applying.

Keep the explanation simple and suitable for a college student.

STUDENT RESUME:
{resume_text}

JOB DESCRIPTION:
{jd_text}
"""

                response = ollama.chat(
                    model="llama3.2",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                answer = response["message"]["content"]
                st.session_state.job_match_result = answer

            st.subheader("🤖 Job Match Result")

            st.markdown(answer)

elif option == "🧠 AI Study Assistant":
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.header("🧠 AI Study Assistant")

    st.write(
        "Upload your study material and ask questions from it using RAG."
    )

    uploaded_file = st.file_uploader(
        "Upload Study PDF",
        type=["pdf"],
        key="study_pdf"
    )

    if uploaded_file is not None:

        from pypdf import PdfReader
        from modules.rag import add_document

        reader = PdfReader(uploaded_file)

        study_text = ""

        for page in reader.pages:

            text = page.extract_text()

            if text:
                study_text += text + "\n"

        st.success("Study PDF uploaded successfully!")

        with st.expander("📄 View Extracted Text"):

            st.text_area(
                "Study Material",
                study_text,
                height=300
            )

        if st.button("📚 Add to Knowledge Base"):

            with st.spinner("Processing study material..."):

                chunks_added = add_document(
                    study_text,
                    uploaded_file.name
                )

            st.success(
                f"Study material added successfully! "
                f"{chunks_added} chunks stored in ChromaDB."
            )
            st.subheader("💬 Ask Your Study Material")

        question = st.text_input(
            "Ask a question from your PDF"
        )

        if st.button("🔍 Ask AI"):

            if question.strip() == "":
                st.warning("Please enter a question.")

            else:

                from modules.rag import search_documents
                import ollama

                with st.spinner("Searching your study material..."):

                    relevant_chunks = search_documents(
                        question,
                        number_of_results=3
                    )

                    context = "\n\n".join(
                        relevant_chunks
                    )

                prompt = f"""
You are an AI study assistant.

Answer the student's question using ONLY the
information provided in the study material below.

If the answer is not present in the material,
say:

"I could not find this information in your uploaded material."

Study Material:
{context}

Student Question:
{question}
"""

                with st.spinner("AI is preparing the answer..."):

                    response = ollama.chat(
                        model="llama3.2",
                        messages=[
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ]
                    )

                    answer = response["message"]["content"]

                st.session_state.chat_history.append(
                {
                    "question": question,
                    "answer": answer
                }
                                        )

                st.subheader("💬 Chat History")

                for chat in st.session_state.chat_history:

                    st.markdown(
                        f"**👤 You:** {chat['question']}"
                    )

                    st.markdown(
                        f"**🤖 AI:** {chat['answer']}"
                    )

                    st.divider()
                st.subheader("📚 Sources Used")

                for i, chunk in enumerate(relevant_chunks):

                 with st.expander(f"Source {i + 1}"):

                          st.write(chunk)

elif option == "🎤 Mock Interview":

    st.header("🎤 AI Mock Interview")

    st.write(
        "Practice placement interviews with your AI interviewer."
    )

    import ollama

    # -----------------------------
    # Initialize session variables
    # -----------------------------

    if "interview_number" not in st.session_state:
        st.session_state.interview_number = 0

    if "interview_question" not in st.session_state:
        st.session_state.interview_question = None

    if "interview_feedback" not in st.session_state:
        st.session_state.interview_feedback = None

    if "interview_history" not in st.session_state:
        st.session_state.interview_history = []

    # -----------------------------
    # Interview Type
    # -----------------------------

    interview_type = st.selectbox(
        "Choose Interview Type",
        [
            "HR Interview",
            "Technical Interview",
            "Mixed Interview"
        ]
    )

    # -----------------------------
    # Start Interview
    # -----------------------------

    if st.button("🎤 Start Interview"):

        st.session_state.interview_number = 1
        st.session_state.interview_question = None
        st.session_state.interview_feedback = None
        st.session_state.interview_history = []

        prompt = f"""
You are an experienced placement interviewer.

Conduct a {interview_type} for a college student.

Generate ONE interview question.

Rules:
- Ask only one question.
- Do not provide the answer.
- Keep it suitable for an entry-level job.
- Make it realistic.
- This is Question 1.

Return only the interview question.
"""

        with st.spinner(
            "🤖 AI interviewer is preparing the question..."
        ):

            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

        st.session_state.interview_question = (
            response["message"]["content"].strip()
        )

        st.rerun()

    # -----------------------------
    # Display Question
    # -----------------------------

    if st.session_state.interview_question:

        st.subheader(
            f"🤖 Question {st.session_state.interview_number}"
        )

    st.info(
                st.session_state.interview_question
            )
    import streamlit.components.v1 as components

    question = st.session_state.interview_question

    components.html(
    f"""
    <script>
        const question = {question!r};

        const speech = new SpeechSynthesisUtterance(question);
        speech.lang = "en-US";
        speech.rate = 0.9;

        window.speechSynthesis.cancel();
        window.speechSynthesis.speak(speech);
    </script>
    """,
    height=10
)

        # -----------------------------
        # Student Answer
        # -----------------------------

    answer = st.text_area(
    "👤 Your Answer",
    height=150,
    key=f"answer_{st.session_state.interview_number}"
)
    st.write("🎙️ Speak your answer")

    audio_value = st.audio_input(
        "Record your answer"
    )

    if audio_value:
        st.audio(audio_value)
        st.success("✅ Audio recorded successfully!")
        # -----------------------------
        # Evaluate Answer
        # -----------------------------

    if st.button(
            "📊 Evaluate My Answer",
            key=f"evaluate_{st.session_state.interview_number}"
        ):

            if answer.strip() == "":

                st.warning(
                    "Please enter your answer."
                )

            else:

                evaluation_prompt = f"""
You are a professional placement interviewer.

Evaluate the student's answer.

Give feedback using exactly these sections:

1. Score out of 10
2. What was good
3. What can be improved
4. Better answer approach
5. Communication feedback

Keep the feedback simple and useful for a college student.

Interview Question:
{st.session_state.interview_question}

Student Answer:
{answer}
"""

                with st.spinner(
                    "🤖 AI is evaluating your answer..."
                ):

                    response = ollama.chat(
                        model="llama3.2",
                        messages=[
                            {
                                "role": "user",
                                "content": evaluation_prompt
                            }
                        ]
                    )

                feedback = (
                    response["message"]["content"].strip()
                )

                st.session_state.interview_feedback = feedback

                st.session_state.interview_history.append(
                    {
                        "question":
                            st.session_state.interview_question,

                        "answer":
                            answer,

                        "feedback":
                            feedback
                    }
                )

                st.rerun()

    # -----------------------------
    # Display Feedback
    # -----------------------------

    if st.session_state.interview_feedback:

        st.subheader("📊 AI Feedback")

        st.markdown(
            st.session_state.interview_feedback
        )

        # -----------------------------
        # Next Question
        # -----------------------------

        if st.button(
            "➡️ Next Question",
            key=f"next_{st.session_state.interview_number}"
        ):

            st.session_state.interview_number += 1

            st.session_state.interview_feedback = None

            previous_questions = [
                item["question"]
                for item in st.session_state.interview_history
            ]

            previous_questions_text = "\n".join(
                [
                    f"- {q}"
                    for q in previous_questions
                ]
            )

            next_prompt = f"""
You are an experienced placement interviewer.

Generate ONE completely NEW interview question.

Interview type:
{interview_type}

Previous questions:
{previous_questions_text}

Rules:
- Do not repeat any previous question.
- Do not rephrase a previous question.
- Ask a completely different question.
- Ask only ONE question.
- Do not provide the answer.
- Keep it suitable for a college student.
- Return ONLY the question.
"""

            with st.spinner(
                "🤖 Preparing your next question..."
            ):

                response = ollama.chat(
                    model="llama3.2",
                    messages=[
                        {
                            "role": "user",
                            "content": next_prompt
                        }
                    ]
                )

            new_question = (
                response["message"]["content"].strip()
            )

            st.session_state.interview_question = new_question

            st.rerun()

    # -----------------------------
    # Interview History
    # -----------------------------

    if st.session_state.interview_history:

        st.divider()

        st.subheader("📚 Interview History")

        for i, item in enumerate(
            st.session_state.interview_history,
            start=1
        ):

            with st.expander(
                f"Question {i}"
            ):

                st.write("🤖 Question:")
                st.write(item["question"])

                st.write("👤 Your Answer:")
                st.write(item["answer"])

                st.write("📊 AI Feedback:")
                st.write(item["feedback"])

elif option == "💻 Coding Interview":

    st.header("💻 AI Coding Interview")

    st.write(
        "Practice coding problems with an AI interviewer."
    )

    import ollama

    # -----------------------------
    # Programming language
    # -----------------------------

    language = st.selectbox(
        "Choose Programming Language",
        [
            "Java",
            "Python",
            "C",
            "JavaScript"
        ]
    )

    # -----------------------------
    # Difficulty
    # -----------------------------

    difficulty = st.selectbox(
        "Choose Difficulty",
        [
            "Easy",
            "Medium",
            "Hard"
        ]
    )

    # -----------------------------
    # Generate Problem
    # -----------------------------

    if st.button("💻 Generate Coding Problem"):

        coding_prompt = f"""
You are a technical coding interviewer.

Create ONE coding interview problem.

Programming Language:
{language}

Difficulty:
{difficulty}

Give the problem using exactly these sections:

1. Problem
2. Input
3. Output
4. Example
5. Constraints

Rules:
- Do not provide the solution.
- Do not provide code.
- Keep it suitable for a college placement interview.
"""

        with st.spinner("🤖 Generating coding problem..."):

            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "user",
                        "content": coding_prompt
                    }
                ]
            )

        st.session_state.coding_problem = (
            response["message"]["content"]
        )

        # Clear previous evaluation
        if "coding_evaluation" in st.session_state:
            del st.session_state.coding_evaluation

        st.rerun()

    # -----------------------------
    # Display Coding Problem
    # -----------------------------

    if "coding_problem" in st.session_state:

        st.subheader("💻 Coding Problem")

        st.markdown(
            st.session_state.coding_problem
        )

        # -----------------------------
        # Code Editor
        # -----------------------------

        code = st.text_area(
            "⌨️ Write Your Code",
            height=300,
            placeholder="Write your solution here..."
        )

        # -----------------------------
        # Evaluate Code
        # -----------------------------

        if st.button("📊 Evaluate Code"):

            if code.strip() == "":

                st.warning(
                    "Please write your code first."
                )

            else:

                evaluation_prompt = f"""
You are an expert coding interviewer.

Evaluate the student's solution.

Programming Language:
{language}

Coding Problem:
{st.session_state.coding_problem}

Student Code:
{code}

Give feedback using exactly these sections:

1. Correctness
2. Score out of 10
3. Logic Explanation
4. Errors or Issues
5. Time Complexity
6. Space Complexity
7. Suggestions for Improvement

Rules:
- Do not rewrite the complete solution.
- Explain simply.
- Focus on helping a college student improve.
"""

                with st.spinner(
                    "🤖 AI is evaluating your code..."
                ):

                    response = ollama.chat(
                        model="llama3.2",
                        messages=[
                            {
                                "role": "user",
                                "content": evaluation_prompt
                            }
                        ]
                    )

                    # IMPORTANT:
                    # response is used INSIDE the same block
                    coding_feedback = (
                        response["message"]["content"]
                    )

                # Save evaluation
                st.session_state.coding_evaluation = (
                    coding_feedback
                )

                st.subheader(
                    "📊 Coding Evaluation"
                )

                st.markdown(
                    coding_feedback
                )

        # -----------------------------
        # Show Previous Evaluation
        # -----------------------------

        if "coding_evaluation" in st.session_state:

            st.divider()

            st.subheader(
                "📊 Latest Coding Evaluation"
            )

            st.markdown(
                st.session_state.coding_evaluation
            )
elif option == "📊 Performance Report":

    st.header("📊 Performance Report")

    st.write(
        "Review your AI interview performance."
    )

    # Check whether interview data exists
    if "interview_history" not in st.session_state:

        st.info(
            "Complete a mock interview first "
            "to generate your performance report."
        )

    elif len(st.session_state.interview_history) == 0:

        st.info(
            "Complete a mock interview first "
            "to generate your performance report."
        )

    else:

        import ollama
        import re

        history = st.session_state.interview_history

        # -----------------------------
        # Prepare interview data
        # -----------------------------

        interview_data = ""

        for i, item in enumerate(
            history,
            start=1
        ):

            interview_data += f"""
Question {i}:
{item["question"]}

Student Answer:
{item["answer"]}

AI Feedback:
{item["feedback"]}

-------------------------
"""

        # -----------------------------
        # Generate report
        # -----------------------------

        if st.button("📊 Generate Performance Report"):

            report_prompt = f"""
You are an expert placement coach.

Analyze the student's complete mock interview.

Interview Data:

{interview_data}

Create a placement performance report.

Use exactly these sections:

1. Overall Performance
Give an overall score out of 10.

2. Strengths
List the student's main strengths.

3. Weaknesses
List the important weaknesses.

4. Communication
Evaluate communication quality.

5. Technical Knowledge
Evaluate technical knowledge if applicable.

6. Areas to Improve
Give specific improvement areas.

7. Placement Preparation Plan
Give a practical preparation plan.

Keep the report simple and useful for a college student.
"""

            with st.spinner(
                "🤖 Generating performance report..."
            ):

                response = ollama.chat(
                    model="llama3.2",
                    messages=[
                        {
                            "role": "user",
                            "content": report_prompt
                        }
                    ]
                )

            report = response["message"]["content"]

            st.session_state.performance_report = report

        # -----------------------------
        # Display report
        # -----------------------------

        if "performance_report" in st.session_state:

            st.subheader(
                "🎯 Placement Performance Report"
            )

            st.markdown(
                st.session_state.performance_report
            )
            st.download_button(
    "📥 Download Performance Report",
    data=st.session_state.performance_report,
    file_name="placement_performance_report.txt",
    mime="text/plain"
)

            st.success(
                "Keep practicing and improve your weak areas!"
            )
elif option == "🗺️ Placement Roadmap":

    st.header("🗺️ Personalized Placement Roadmap")

    st.write(
        "Generate a personalized placement preparation plan using your AI results."
    )

    import ollama

    resume_analysis = st.session_state.get(
        "resume_analysis",
        "Resume analysis not completed."
    )

    job_match = st.session_state.get(
        "job_match_result",
        "Job matching not completed."
    )

    interview_history = st.session_state.get(
        "interview_history",
        []
    )

    coding_evaluation = st.session_state.get(
        "coding_evaluation",
        "Coding evaluation not completed."
    )

    interview_summary = ""

    for i, item in enumerate(
        interview_history,
        start=1
    ):

        interview_summary += f"""
Interview Question {i}:
{item["question"]}

Student Answer:
{item["answer"]}

Feedback:
{item["feedback"]}

-------------------------
"""

    if st.button("🚀 Generate My Placement Roadmap"):

        roadmap_prompt = f"""
You are an expert college placement coach.

Create a personalized placement preparation roadmap
for a college student.

Use the student's available AI results.

RESUME ANALYSIS:
{resume_analysis}

JOB MATCH RESULT:
{job_match}

MOCK INTERVIEW PERFORMANCE:
{interview_summary}

CODING EVALUATION:
{coding_evaluation}

Create a practical 4-week roadmap.

Use exactly these sections:

1. Current Level
Briefly explain the student's current preparation level.

2. Main Weak Areas
List the most important weaknesses.

3. Week 1
Give specific topics and practice tasks.

4. Week 2
Give specific topics and practice tasks.

5. Week 3
Give specific topics and practice tasks.

6. Week 4
Give specific topics and practice tasks.

7. Daily Routine
Create a simple daily placement preparation routine.

8. Priority Skills
List the top 5 skills the student should focus on.

9. Project Improvement
Suggest improvements to the student's projects.

10. Final Placement Tips
Give practical placement advice.

Keep everything simple and suitable for a college student.
Do not give unrealistic advice.
"""

        with st.spinner(
            "🤖 AI is creating your personalized roadmap..."
        ):

            response = ollama.chat(
                model="llama3.2",
                messages=[
                    {
                        "role": "user",
                        "content": roadmap_prompt
                    }
                ]
            )

        roadmap = response["message"]["content"]

        st.session_state.placement_roadmap = roadmap

    if "placement_roadmap" in st.session_state:

        st.subheader("🎯 Your Personalized Roadmap")

        st.markdown(
            st.session_state.placement_roadmap
        )
        st.download_button(
    "📥 Download Placement Roadmap",
    data=st.session_state.placement_roadmap,
    file_name="placement_roadmap.txt",
    mime="text/plain"
)

        st.success(
            "Your personalized placement roadmap is ready!"
        )