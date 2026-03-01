import streamlit as st

st.set_page_config(page_title="Render Test", page_icon="🚀")

st.title("🚀 Streamlit on Render Test")
st.markdown("**Deployment successful!** Your app is live.")

# Sidebar for interactivity
st.sidebar.header("Controls")
name = st.sidebar.text_input("Your name", "Mehmet Can")
slider_val = st.sidebar.slider("Pick a number", 1, 10, 5)

# Main content
col1, col2 = st.columns(2)
with col1:
    st.metric("Your Score", f"{slider_val * 10}%")
with col2:
    st.metric("Status", "✅ Live", delta="Deployed")

if st.button("🎉 Say Hello"):
    st.balloons()
    st.success(f"Hello, {name}! Render deployment works perfectly.")

st.info("Made for İzmir dev testing. Free tier sleeps after 15min inactivity.")
