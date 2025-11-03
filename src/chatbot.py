# chatbot.py
import streamlit as st

st.set_page_config(page_title="AI Chatbot Assistant", page_icon="🤖")

st.title("🤖 AI Placement Chatbot Assistant")
st.write("Ask me anything about improving your placement chances!")

# Define some simple rule-based responses
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "cgpa" in user_input:
        return "Maintaining a CGPA above 7.5 can improve your placement chances significantly."
    elif "skills" in user_input or "courses" in user_input:
        return "You can take online courses like Python, SQL, and Power BI to boost your employability."
    elif "communication" in user_input:
        return "Try participating in group discussions or mock interviews to strengthen your communication skills."
    elif "internship" in user_input:
        return "Having at least one internship experience gives you practical exposure and improves your profile."
    elif "projects" in user_input:
        return "Build at least 2-3 real-world projects using data science or web development to showcase your skills."
    elif "certification" in user_input:
        return "Certifications in Python, Excel, or Data Analytics are highly valued by recruiters."
    elif "resume" in user_input:
        return "Keep your resume short (1 page), highlight projects, internships, and technical skills."
    elif "placement" in user_input or "improve" in user_input:
        return "Focus on consistent CGPA, practical projects, strong communication, and at least one internship."
    else:
        return "I'm still learning! Try asking about CGPA, skills, projects, internships, or communication tips."

# Chat interface
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

user_input = st.text_input("You:", placeholder="Ask your question here...")

if user_input:
    response = chatbot_response(user_input)
    st.session_state["chat_history"].append(("You", user_input))
    st.session_state["chat_history"].append(("Bot", response))

# Display chat
for speaker, msg in st.session_state["chat_history"]:
    if speaker == "You":
        st.markdown(f"🧑 **{speaker}:** {msg}")
    else:
        st.markdown(f"🤖 **{speaker}:** {msg}")
