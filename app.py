import streamlit as st
import pandas as pd
from datetime import date

# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="AI Campus Connect",
    page_icon="🎓",
    layout="wide"
)

# -------------------------------------------------
# DEMO STUDENT DATA
# -------------------------------------------------

if "students" not in st.session_state:
    st.session_state.students = {
        "student@gmail.com": {
            "name": "Demo Student",
            "password": "1234"
        }
    }

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "student_email" not in st.session_state:
    st.session_state.student_email = ""

# -------------------------------------------------
# CUSTOM STYLE
# -------------------------------------------------

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    font-size: 20px;
    color: #777;
}

.card {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #ddd;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# LOGIN / REGISTRATION
# -------------------------------------------------

if not st.session_state.logged_in:

    st.title("🎓 AI Campus Connect")
    st.subheader("Your Smart College Companion")

    st.write(
        "A smart platform for students to manage academics, "
        "resources, assignments, events and placements."
    )

    tab1, tab2 = st.tabs([
        "🔐 Student Login",
        "📝 Student Registration"
    ])

    # -------------------------------------------------
    # LOGIN
    # -------------------------------------------------

    with tab1:

        st.header("🔐 Student Login")

        email = st.text_input(
            "Email",
            placeholder="Enter your email"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter your password"
        )

        if st.button("Login", use_container_width=True):

            if email in st.session_state.students:

                student = st.session_state.students[email]

                if student["password"] == password:

                    st.session_state.logged_in = True
                    st.session_state.student_email = email

                    st.success("Login successful! 🎉")
                    st.rerun()

                else:
                    st.error("Incorrect password.")

            else:
                st.error("Student account not found.")

        st.info(
            "Demo Login: student@gmail.com / 1234"
        )

    # -------------------------------------------------
    # REGISTRATION
    # -------------------------------------------------

    with tab2:

        st.header("📝 Student Registration")

        name = st.text_input(
            "Full Name"
        )

        new_email = st.text_input(
            "Email Address"
        )

        new_password = st.text_input(
            "Create Password",
            type="password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

        if st.button(
            "Register",
            use_container_width=True
        ):

            if not name or not new_email or not new_password:
                st.warning("Please fill all fields.")

            elif new_password != confirm_password:
                st.error("Passwords do not match.")

            elif new_email in st.session_state.students:
                st.error("Email already registered.")

            else:

                st.session_state.students[new_email] = {
                    "name": name,
                    "password": new_password
                }

                st.success(
                    "Registration successful! "
                    "You can now login."
                )

    st.stop()

# -------------------------------------------------
# GET CURRENT STUDENT
# -------------------------------------------------

email = st.session_state.student_email
student = st.session_state.students[email]

student_name = student["name"]

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("🎓 AI Campus Connect")

st.sidebar.success(
    f"Welcome, {student_name}"
)

menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "📊 Attendance",
        "📝 Assignments",
        "📚 Study Resources",
        "🤖 AI Chatbot",
        "🎉 Events & Clubs",
        "💼 Placements",
        "🔔 Notifications"
    ]
)

st.sidebar.divider()

if st.sidebar.button("🚪 Logout"):

    st.session_state.logged_in = False
    st.session_state.student_email = ""

    st.rerun()

# =================================================
# DASHBOARD
# =================================================

if menu == "🏠 Dashboard":

    st.title("🏠 Student Dashboard")

    st.subheader(
        f"Welcome back, {student_name}! 👋"
    )

    st.write(
        "Manage your college activities from one place."
    )

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📚 Study Resources",
            "12"
        )

    with col2:
        st.metric(
            "📊 Attendance",
            "85%"
        )

    with col3:
        st.metric(
            "📝 Assignments",
            "4"
        )

    with col4:
        st.metric(
            "🎉 Events",
            "6"
        )

    st.divider()

    st.subheader("📌 Quick Overview")

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            "📊 Attendance\n\n"
            "Your current attendance is 85%."
        )

        st.warning(
            "📝 Assignment\n\n"
            "2 assignments are due this week."
        )

    with col2:

        st.success(
            "💼 Placement\n\n"
            "5 new placement opportunities available."
        )

        st.info(
            "🔔 Notification\n\n"
            "3 new college notifications."
        )

# =================================================
# ATTENDANCE
# =================================================

elif menu == "📊 Attendance":

    st.title("📊 Attendance")

    attendance_data = {
        "Subject": [
            "Data Science",
            "Operating Systems",
            "Java",
            "Statistics",
            "Computer Networks"
        ],
        "Present": [
            38,
            35,
            40,
            36,
            34
        ],
        "Total Classes": [
            45,
            42,
            45,
            40,
            40
        ]
    }

    df = pd.DataFrame(attendance_data)

    df["Attendance %"] = (
        df["Present"] /
        df["Total Classes"] *
        100
    ).round(2)

    st.dataframe(
        df,
        use_container_width=True
    )

    overall = (
        df["Present"].sum() /
        df["Total Classes"].sum()
        * 100
    )

    st.metric(
        "Overall Attendance",
        f"{overall:.2f}%"
    )

    if overall >= 75:
        st.success(
            "✅ Your attendance is above 75%."
        )
    else:
        st.error(
            "⚠️ Your attendance is below 75%."
        )

# =================================================
# ASSIGNMENTS
# =================================================

elif menu == "📝 Assignments":

    st.title("📝 Assignments")

    assignments = pd.DataFrame({
        "Subject": [
            "Data Science",
            "Java",
            "Operating Systems",
            "Statistics"
        ],
        "Assignment": [
            "Data Cleaning Project",
            "Java Collections",
            "Page Replacement Algorithms",
            "Correlation Analysis"
        ],
        "Due Date": [
            "10 Oct 2026",
            "12 Oct 2026",
            "15 Oct 2026",
            "18 Oct 2026"
        ],
        "Status": [
            "Pending",
            "Submitted",
            "Pending",
            "Pending"
        ]
    })

    st.dataframe(
        assignments,
        use_container_width=True
    )

    st.subheader("➕ Add Assignment")

    subject = st.text_input("Subject")
    assignment = st.text_input("Assignment Name")
    due_date = st.date_input(
        "Due Date",
        value=date.today()
    )

    if st.button("Add Assignment"):

        if subject and assignment:

            st.success(
                f"Assignment '{assignment}' added successfully!"
            )

        else:
            st.warning(
                "Please enter subject and assignment name."
            )

# =================================================
# STUDY RESOURCES
# =================================================

elif menu == "📚 Study Resources":

    st.title("📚 Study Resources")

    st.write(
        "Find useful study materials for your subjects."
    )

    resources = [
        (
            "📘 Operating Systems",
            "Virtual Memory, Paging, Page Replacement"
        ),
        (
            "☕ Java",
            "Collections, File Handling, Streams"
        ),
        (
            "📊 Data Science",
            "Python, Pandas, NumPy and Machine Learning"
        ),
        (
            "📈 Statistics",
            "Correlation, Regression and Hypothesis Testing"
        ),
        (
            "🌐 Computer Networks",
            "OSI Model, TCP/IP and Network Security"
        )
    ]

    for title, description in resources:

        with st.expander(title):

            st.write(description)

            st.button(
                "📖 View Resource",
                key=title
            )

# =================================================
# AI CHATBOT
# =================================================

elif menu == "🤖 AI Chatbot":

    st.title("🤖 AI Campus Assistant")

    st.write(
        "Ask questions about your college, studies, "
        "assignments or placements."
    )

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    question = st.chat_input(
        "Ask your question..."
    )

    if question:

        st.session_state.chat_history.append(
            ("You", question)
        )

        q = question.lower()

        if "attendance" in q:

            answer = (
                "Your demo attendance is 85%. "
                "Try to maintain at least 75% attendance."
            )

        elif "assignment" in q:

            answer = (
                "You have 4 assignments. "
                "Please check the Assignments section "
                "for due dates."
            )

        elif "placement" in q:

            answer = (
                "You can check the Placements section "
                "for available job and internship opportunities."
            )

        elif "event" in q or "club" in q:

            answer = (
                "Check Events & Clubs to see upcoming "
                "college activities."
            )

        elif "study" in q or "resource" in q:

            answer = (
                "Visit Study Resources to find materials "
                "for your subjects."
            )

        elif "hello" in q or "hi" in q:

            answer = (
                f"Hello {student_name}! 👋 "
                "How can I help you today?"
            )

        else:

            answer = (
                "I'm your AI Campus Assistant. "
                "Try asking about attendance, assignments, "
                "study resources, events or placements."
            )

        st.session_state.chat_history.append(
            ("AI Assistant", answer)
        )

    for sender, message in st.session_state.chat_history:

        if sender == "You":

            st.chat_message("user").write(message)

        else:

            st.chat_message("assistant").write(message)

# =================================================
# EVENTS & CLUBS
# =================================================

elif menu == "🎉 Events & Clubs":

    st.title("🎉 Events & Clubs")

    events = pd.DataFrame({
        "Event": [
            "Tech Fest 2026",
            "Coding Competition",
            "Cultural Fest",
            "AI Workshop",
            "Sports Meet"
        ],
        "Date": [
            "12 Oct 2026",
            "15 Oct 2026",
            "20 Oct 2026",
            "25 Oct 2026",
            "30 Oct 2026"
        ],
        "Location": [
            "Main Auditorium",
            "Computer Lab",
            "College Ground",
            "Seminar Hall",
            "Sports Ground"
        ]
    })

    st.dataframe(
        events,
        use_container_width=True
    )

    st.subheader("👥 College Clubs")

    clubs = [
        "🤖 AI & Robotics Club",
        "💻 Coding Club",
        "📸 Photography Club",
        "🎭 Cultural Club",
        "🏏 Sports Club"
    ]

    for club in clubs:

        st.write(f"• {club}")

# =================================================
# PLACEMENTS
# =================================================

elif menu == "💼 Placements":

    st.title("💼 Placements & Internships")

    placements = pd.DataFrame({
        "Company": [
            "TCS",
            "Infosys",
            "Wipro",
            "Accenture",
            "Deloitte"
        ],
        "Role": [
            "Software Developer",
            "Data Analyst",
            "Python Developer",
            "Software Engineer",
            "Data Analyst"
        ],
        "Type": [
            "Full Time",
            "Full Time",
            "Internship",
            "Full Time",
            "Internship"
        ],
        "Status": [
            "Open",
            "Open",
            "Open",
            "Open",
            "Open"
        ]
    })

    st.dataframe(
        placements,
        use_container_width=True
    )

    st.success(
        "💡 Tip: Keep your resume and coding skills updated "
        "for placement opportunities."
    )

# =================================================
# NOTIFICATIONS
# =================================================

elif menu == "🔔 Notifications":

    st.title("🔔 Notifications")

    notifications = [
        (
            "📢 College Notice",
            "Mid-semester examinations will begin soon."
        ),
        (
            "📝 Assignment",
            "Data Science assignment submission is due."
        ),
        (
            "💼 Placement",
            "A new placement opportunity has been added."
        ),
        (
            "🎉 Event",
            "AI Workshop registration is now open."
        ),
        (
            "📚 Library",
            "New study materials are available."
        )
    ]

    for title, message in notifications:

        st.info(
            f"**{title}**\n\n{message}"
        )

# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.sidebar.divider()

st.sidebar.caption(
    "🎓 AI Campus Connect | Student Portal"
)
    
