"""
Streamlit Frontend for Sentiment Analysis
NeuralAICodeCraft - Interactive UI for NLP Project
"""

import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import time
import json

# Page configuration
st.set_page_config(
    page_title="Sentiment Analysis App | NeuralAICodeCraft",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0A0A0F 0%, #1A1A2E 100%);
    }
    .main-header {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, #8B5CF6, #06B6D4);
        border-radius: 20px;
        margin-bottom: 2rem;
    }
    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 2.5rem;
    }
    .main-header h2 {
        color: white;
        margin: 0;
        font-size: 1.5rem;
        opacity: 0.9;
    }
    .main-header p {
        color: white;
        margin-top: 0.5rem;
        opacity: 0.8;
    }
    .sentiment-positive {
        padding: 1rem;
        border-radius: 10px;
        background: rgba(34, 197, 94, 0.2);
        border-left: 4px solid #22C55E;
        margin: 1rem 0;
    }
    .sentiment-negative {
        padding: 1rem;
        border-radius: 10px;
        background: rgba(239, 68, 68, 0.2);
        border-left: 4px solid #EF4444;
        margin: 1rem 0;
    }
    .stButton > button {
        background: linear-gradient(135deg, #8B5CF6, #06B6D4);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        transition: all 0.3s ease;
    }
</style>
""", unsafe_allow_html=True)

# API Configuration
API_URL = "http://localhost:8000"

# Initialize session state
if 'history' not in st.session_state:
    st.session_state.history = []
if 'batch_results' not in st.session_state:
    st.session_state.batch_results = None

# ============================================
# HEADER
# ============================================

st.markdown("""
<div class="main-header">
    <h1>🧠 NeuralAICodeCraft</h1>
    <h2>Sentiment Analysis Project</h2>
    <p>Logistic Regression vs Naive Bayes | Real-time NLP Predictions</p>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🧠 NeuralAICodeCraft")
    st.markdown("---")
    st.markdown("## 📊 Navigation")
    
    page = st.radio(
        "",
        ["🔍 Single Review", "⚖️ Compare Models", "📊 Batch Analysis", "📈 History", "ℹ️ About"]
    )
    
    st.markdown("---")
    st.markdown("### 🚀 Quick Stats")
    
    # Check API health
    try:
        response = requests.get(f"{API_URL}/health", timeout=2)
        if response.status_code == 200:
            st.success("✅ API Connected")
            st.info("Models ready: Logistic Regression + Naive Bayes")
        else:
            st.error("❌ API Not Connected")
    except:
        st.error("❌ API Not Connected")
        st.info("Make sure backend is running: `python main.py`")
    
    st.markdown("---")
    st.markdown("### 📚 Resources")
    st.markdown("[📺 YouTube Channel](https://youtube.com/@NeuralAIC)")
    st.markdown("[💻 GitHub Repo](https://github.com/SaurabhPandey69/YouTube_NeuralAICodeCraft)")

# ============================================
# PAGE 1: SINGLE REVIEW
# ============================================

if page == "🔍 Single Review":
    st.markdown("## 🔍 Analyze a Single Review")
    st.markdown("Enter any text below and our AI models will analyze the sentiment.")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        text_input = st.text_area(
            "Enter your review here:",
            height=150,
            placeholder="e.g., This movie is absolutely amazing and wonderful!"
        )
    
    with col2:
        model_choice = st.selectbox(
            "Select Model:",
            ["both", "logistic", "naivebayes"],
            help="Choose which model to use for analysis"
        )
        
        analyze_button = st.button("🚀 Analyze Sentiment", type="primary", use_container_width=True)
    
    if analyze_button and text_input:
        with st.spinner("Analyzing sentiment..."):
            try:
                response = requests.post(
                    f"{API_URL}/predict",
                    json={"text": text_input, "model": model_choice}
                )
                
                if response.status_code == 200:
                    results = response.json()
                    
                    # Store in history
                    st.session_state.history.append({
                        'timestamp': datetime.now(),
                        'text': text_input,
                        'results': results
                    })
                    
                    # Display results
                    for result in results:
                        if result['sentiment'] == 'POSITIVE':
                            st.markdown(f"""
                            <div class="sentiment-positive">
                                <h3>✅ {result['model']}</h3>
                                <h2>Sentiment: {result['sentiment']}</h2>
                                <p>Confidence: {result['confidence']:.2%}</p>
                                <p>Probability Distribution:</p>
                                <ul>
                                    <li>Positive: {result['probabilities']['positive']:.2%}</li>
                                    <li>Negative: {result['probabilities']['negative']:.2%}</li>
                                </ul>
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.markdown(f"""
                            <div class="sentiment-negative">
                                <h3>❌ {result['model']}</h3>
                                <h2>Sentiment: {result['sentiment']}</h2>
                                <p>Confidence: {result['confidence']:.2%}</p>
                                <p>Probability Distribution:</p>
                                <ul>
                                    <li>Positive: {result['probabilities']['positive']:.2%}</li>
                                    <li>Negative: {result['probabilities']['negative']:.2%}</li>
                                </ul>
                            </div>
                            """, unsafe_allow_html=True)
                        
                        # Gauge chart
                        fig = go.Figure(go.Indicator(
                            mode="gauge+number",
                            value=result['confidence'] * 100,
                            title={'text': f"{result['model']} Confidence"},
                            domain={'x': [0, 1], 'y': [0, 1]},
                            gauge={
                                'axis': {'range': [None, 100]},
                                'bar': {'color': "#8B5CF6"},
                                'steps': [
                                    {'range': [0, 50], 'color': "rgba(239, 68, 68, 0.3)"},
                                    {'range': [50, 75], 'color': "rgba(234, 179, 8, 0.3)"},
                                    {'range': [75, 100], 'color': "rgba(34, 197, 94, 0.3)"}
                                ]
                            }
                        ))
                        fig.update_layout(height=300)
                        st.plotly_chart(fig, use_container_width=True)
                    
                else:
                    st.error(f"Error: {response.status_code}")
            
            except Exception as e:
                st.error(f"Error connecting to API: {str(e)}")
    
    elif analyze_button and not text_input:
        st.warning("Please enter some text to analyze.")

# ============================================
# PAGE 2: COMPARE MODELS
# ============================================

elif page == "⚖️ Compare Models":
    st.markdown("## ⚖️ Compare Logistic Regression vs Naive Bayes")
    st.markdown("Enter a review and see how both models perform side by side.")
    
    text_input = st.text_area(
        "Enter a review to compare both models:",
        height=100,
        placeholder="e.g., This product is fantastic! Best purchase ever!"
    )
    
    if st.button("🔬 Compare Models", type="primary") and text_input:
        with st.spinner("Analyzing with both models..."):
            try:
                response = requests.post(
                    f"{API_URL}/predict",
                    json={"text": text_input, "model": "both"}
                )
                
                if response.status_code == 200:
                    results = response.json()
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        logistic_result = results[0]
                        color = "green" if logistic_result['sentiment'] == 'POSITIVE' else "red"
                        st.markdown(f"""
                        <div style="background: rgba(139, 92, 246, 0.15); padding: 1.5rem; border-radius: 15px; border: 1px solid #8B5CF6;">
                            <h3 style="color: #8B5CF6; text-align: center;">🔬 Logistic Regression</h3>
                            <h2 style="color: {color}; text-align: center;">{logistic_result['sentiment']}</h2>
                            <p style="text-align: center;">Confidence: <strong>{logistic_result['confidence']:.2%}</strong></p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col2:
                        nb_result = results[1]
                        color = "green" if nb_result['sentiment'] == 'POSITIVE' else "red"
                        st.markdown(f"""
                        <div style="background: rgba(6, 182, 212, 0.15); padding: 1.5rem; border-radius: 15px; border: 1px solid #06B6D4;">
                            <h3 style="color: #06B6D4; text-align: center;">🌊 Naive Bayes</h3>
                            <h2 style="color: {color}; text-align: center;">{nb_result['sentiment']}</h2>
                            <p style="text-align: center;">Confidence: <strong>{nb_result['confidence']:.2%}</strong></p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Comparison Chart
                    fig = go.Figure(data=[
                        go.Bar(name='Logistic Regression', x=['Confidence'], y=[logistic_result['confidence']*100], marker_color='#8B5CF6'),
                        go.Bar(name='Naive Bayes', x=['Confidence'], y=[nb_result['confidence']*100], marker_color='#06B6D4')
                    ])
                    fig.update_layout(title="Model Confidence Comparison", yaxis_title="Confidence (%)", yaxis_range=[0, 100])
                    st.plotly_chart(fig, use_container_width=True)
                    
                    if logistic_result['sentiment'] == nb_result['sentiment']:
                        st.success(f"✅ Both models agree! Sentiment: **{logistic_result['sentiment']}**")
                    else:
                        st.warning(f"⚠️ Models disagree! Logistic says **{logistic_result['sentiment']}**, Naive Bayes says **{nb_result['sentiment']}**")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
    
    elif st.button("🔬 Compare Models") and not text_input:
        st.warning("Please enter some text to analyze.")

# ============================================
# PAGE 3: BATCH ANALYSIS
# ============================================

elif page == "📊 Batch Analysis":
    st.markdown("## 📊 Batch Analysis")
    st.markdown("Analyze multiple reviews at once.")
    
    option = st.radio("Choose input method:", ["📝 Enter manually", "📁 Upload CSV"])
    texts = []
    
    if option == "📝 Enter manually":
        texts_input = st.text_area(
            "Enter one review per line:",
            height=200,
            placeholder="This movie is great!\nThis is terrible.\nI loved it!"
        )
        if texts_input:
            texts = [t.strip() for t in texts_input.split('\n') if t.strip()]
            st.info(f"✅ {len(texts)} reviews loaded")
    
    else:
        uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
        if uploaded_file:
            df = pd.read_csv(uploaded_file)
            if 'text' in df.columns:
                texts = df['text'].tolist()
                st.success(f"✅ Loaded {len(texts)} reviews from CSV")
            else:
                st.error("CSV must have a 'text' column")
    
    if texts:
        st.write(f"**📋 {len(texts)} reviews ready for analysis**")
        model_choice = st.selectbox("Select Model:", ["logistic", "naivebayes"])
        
        if st.button("🔬 Analyze Batch", type="primary"):
            with st.spinner(f"Analyzing {len(texts)} reviews..."):
                try:
                    response = requests.post(
                        f"{API_URL}/predict-batch",
                        json={"texts": texts, "model": model_choice}
                    )
                    
                    if response.status_code == 200:
                        results = response.json()
                        df_results = pd.DataFrame(results['results'])
                        df_results['emoji'] = df_results['sentiment'].apply(lambda x: '😊' if x == 'POSITIVE' else '😞')
                        
                        st.dataframe(df_results[['emoji', 'text', 'sentiment', 'confidence']], use_container_width=True)
                        
                        positive_count = sum(1 for r in results['results'] if r['sentiment'] == 'POSITIVE')
                        negative_count = sum(1 for r in results['results'] if r['sentiment'] == 'NEGATIVE')
                        
                        col1, col2, col3 = st.columns(3)
                        col1.metric("Positive Reviews", positive_count)
                        col2.metric("Negative Reviews", negative_count)
                        col3.metric("Total Reviews", len(results['results']))
                        
                        fig = go.Figure(data=[go.Pie(labels=['Positive', 'Negative'], values=[positive_count, negative_count], marker_colors=['#22C55E', '#EF4444'])])
                        fig.update_layout(title="Sentiment Distribution")
                        st.plotly_chart(fig, use_container_width=True)
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")

# ============================================
# PAGE 4: HISTORY
# ============================================

elif page == "📈 History":
    st.markdown("## 📈 Analysis History")
    
    if st.session_state.history:
        for i, entry in enumerate(reversed(st.session_state.history[-10:])):
            with st.expander(f"Analysis {len(st.session_state.history)-i} - {entry['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}"):
                st.write(f"**Text:** {entry['text']}")
                for result in entry['results']:
                    st.write(f"**{result['model']}:** {result['sentiment']} ({result['confidence']:.2%})")
        
        if st.button("🗑️ Clear All History"):
            st.session_state.history = []
            st.success("History cleared!")
            st.rerun()
    else:
        st.info("No analysis history yet. Analyze some reviews first!")

# ============================================
# PAGE 5: ABOUT
# ============================================

else:
    st.markdown("## ℹ️ About This Project")
    
    st.markdown("""
    ### 🧠 NeuralAICodeCraft - Sentiment Analysis Project
    
    This project is a **complete end-to-end NLP application** that demonstrates:
    
    - **FastAPI Backend** - REST API for sentiment prediction
    - **Streamlit Frontend** - Interactive web interface
    - **Two ML Models** - Logistic Regression & Naive Bayes
    - **Production-Ready** - Save/load models, batch processing, history tracking
    
    ### 📊 Model Performance
    
    | Model | Accuracy |
    |-------|----------|
    | Logistic Regression | 83.3% |
    | Naive Bayes | 75.0% |
    
    ### 🛠️ Technologies Used
    
    **Backend:** FastAPI, Scikit-learn, NLTK, Joblib
    **Frontend:** Streamlit, Plotly, Pandas, Requests
    
    ### 📺 Watch the Tutorial
    
    [![YouTube](https://img.shields.io/badge/YouTube-NeuralAICodeCraft-red)](https://youtube.com/@NeuralAIC)
    
    ### 💻 GitHub Repository
    
    [![GitHub](https://img.shields.io/badge/GitHub-Repository-black)](https://github.com/SaurabhPandey69/YouTube_NeuralAICodeCraft)
    """)
    
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; padding: 20px;">
            <p>Made with ❤️ by <strong>NeuralAICodeCraft</strong></p>
            <p>🎓 Learn AI/ML for FREE | 🚀 Build Real Projects | 🧠 Master NLP</p>
        </div>
        """,
        unsafe_allow_html=True
    )