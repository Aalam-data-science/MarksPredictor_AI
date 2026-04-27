# 🚀 AI-Powered Academic Performance Predictor
### Built for Parul University Engineering Students

This is a professional-grade Decision Support System (DSS) designed to help students calculate their required marks in End-Sem exams to achieve a target SGPA.

## ✨ Key Features
- [cite_start]**Multi-Branch Support:** Accurate subject lists for AI&DS, CSE, ME, Civil, and more[cite: 14, 15, 42, 92].
- [cite_start]**Smart Prediction Engine:** Accounts for Mid-Sem (40), Internal (20), and Practical (30) components[cite: 11, 15, 117].
- **AI Study Planner:** Categorizes subjects into **Critical**, **Moderate**, and **Safe** zones based on difficulty.
- **Interactive UI:** Built using Streamlit for real-time "What-If" analysis.

## 📁 File Structure
- `app.py`: The main Streamlit dashboard.
- [cite_start]`engine/`: Logic for grade points and reverse-prediction[cite: 1, 11].
- [cite_start]`data/`: Master JSON containing branch-wise subjects and credits[cite: 9, 15, 26].
- `utils/`: Helper functions for UI formatting.

## 🛠️ Installation
1. Clone the repo: `git clone <your-repo-link>`
2. Install dependencies: `pip install streamlit`
3. Run the app: `streamlit run app.py`
