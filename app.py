import streamlit as st
import json
from engine.predictor import predict_needed_marks

# Page Configuration
st.set_page_config(page_title="AI Grade Predictor Pro", layout="wide")

# 1. Load Master Data
with open('data/subjects_config.json', 'r') as f:
    config = json.load(f)

st.title("🚀 Advanced Academic Performance Predictor")
st.markdown("---")

# 2. Sidebar - Global Settings
st.sidebar.header("🎯 Goal Settings")
branch_list = list(config['branches'].keys())
selected_branch = st.sidebar.selectbox("Select Your Department", branch_list)
target_sgpa = st.sidebar.slider("Target SGPA", 5.0, 10.0, 8.5, 0.1)

# 3. Dynamic Subject Selection based on Branch
branch_subjects = config['branches'][selected_branch]
mid_sem_input = {}

col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader(f"📝 {selected_branch} - Mid-Sem Entry")
    st.info("Enter your Mid-Sem marks (Out of 40) for the subjects below:")
    
    for sub_name in branch_subjects:
        sub_info = config['subjects_master'].get(sub_name)
        if sub_info:
            # Only ask for marks if the subject has a Mid-Sem component
            if sub_info['max_marks'] >= 100:
                mid_sem_input[sub_name] = st.number_input(
                    f"{sub_name}", 
                    min_value=0.0, 
                    max_value=40.0, 
                    value=25.0,
                    key=sub_name 
                )

with col2:
    st.subheader("📊 Strategic Action Plan")
    if st.button("Generate My Strategy"):
        # Calling the Prediction Engine
        predictions = predict_needed_marks(target_sgpa, mid_sem_input, config['subjects_master'], config['defaults'])
        
        st.write(f"### Required Marks to Reach {target_sgpa} SGPA")
        
        # Displaying Results & Automated Study Plan
        for sub, target_str in predictions.items():
            if sub in branch_subjects:
                # Extracting numerical value for logic
                try:
                    val = float(str(target_str).split(' / ')[0]) if '/' in str(target_str) else 20.0
                except:
                    val = 24.0
                
                with st.expander(f"📌 {sub} | Target: {target_str}"):
                    if val > 55:
                        st.error(f"🔴 **STATUS: CRITICAL**")
                        st.write(f"**Target:** You need {val} marks out of 60. This requires extreme focus.")
                        st.write("- **Action:** Solve the last 5 years of University Question Papers.")
                        st.write("- **Study Time:** Minimum 3+ hours daily.")
                    elif val > 45:
                        st.warning(f"🟡 **STATUS: MODERATE**")
                        st.write(f"**Target:** You need {val} marks. This is achievable with steady effort.")
                        st.write("- **Action:** Prioritize numerical problems and high-weightage chapters.")
                        st.write("- **Study Time:** 1.5 to 2 hours daily.")
                    elif val > 30:
                        st.success(f"🟢 **STATUS: SAFE**")
                        st.write(f"**Target:** You need {val} marks. You are in a strong position.")
                        st.write("- **Action:** Focus on maintaining your current grasp; avoid silly mistakes.")
                        st.write("- **Study Time:** 45 minutes of revision daily.")
                    else:
                        st.success(f"🟢 **STATUS: SAFE**")

st.markdown("---")
st.caption("Powered by Data Science | Developed for Parul University Engineering Students")