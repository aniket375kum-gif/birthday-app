import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Surprise!", page_icon="🎉", layout="centered")

# --- Session State Setup ---
if "page" not in st.session_state:
    st.session_state.page = "login"

# ==========================================
# --- Page 1: Login Page ---
# ==========================================
if st.session_state.page == "login":
    st.markdown("""
        <style>
        .main { background-color: #E0E7FF; }
        .login-card {
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            max-width: 400px;
            margin: auto;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='login-card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center; color:#1F2937;'>Welcome Back</h2>", unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("LOGIN", use_container_width=True):
        if username == "admin" and password == "password":
            st.session_state.page = "birthday"
            st.rerun()
        else:
            st.error("Incorrect Username or Password. Try admin/password")

    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# --- Page 2: Happy Birthday Page ---
# ==========================================
elif st.session_state.page == "birthday":
    st.markdown("""
        <style>
        .main { background-color: #FFE4E1; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center; color:#FF1493;'>🎉 Happy Birthday! 🎂</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#6B7280; font-size:18px;'>It's time to celebrate!</p>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎁 CLICK HERE FOR YOUR SURPRISE 🎁", use_container_width=True):
            st.session_state.page = "wish"
            st.rerun()

# ==========================================
# --- Page 3: Birthday Wish Page ---
# ==========================================
elif st.session_state.page == "wish":
    st.markdown("""
        <style>
        .main { background-color: #FFF8DC; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style='text-align:center; padding: 40px;'>
            <h1 style='color:#FF4500; font-family: Comic Sans MS;'>🎉 HAPPY BIRTHDAY! 🎉</h1>
            <p style='font-size:20px; color:#FF4500; font-family: Comic Sans MS;'>
                Wishing you a day filled with joy,<br>
                laughter, and lots of cake!<br><br>
                May this year bring you closer to your goals<br>
                and fill your life with amazing memories.<br><br>
                🎂 🎁 🎈 🎊
            </p>
        </div>
    """, unsafe_allow_html=True)
