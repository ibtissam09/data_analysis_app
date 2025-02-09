import streamlit as st

# Color scheme based on the turquoise theme from the image
COLORS = {
    'primary': '#00B4B4',
    'secondary': '#008080',
    'background': '#E6F3F3',
    'text': '#2C3E50',
    'accent': '#FF6B6B'
}

def apply_custom_styles():
    """Apply custom styles to the Streamlit app"""
    st.markdown(
        f"""
        <style>
        .stButton > button {{
            background-color: {COLORS['primary']};
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            border: none;
            transition: background-color 0.3s;
        }}
        .stButton > button:hover {{
            background-color: {COLORS['secondary']};
        }}
        .stProgress > div > div > div {{
            background-color: {COLORS['primary']};
        }}
        .stInfo {{
            background-color: {COLORS['background']};
            color: {COLORS['text']};
            padding: 1rem;
            border-radius: 5px;
            border-left: 5px solid {COLORS['primary']};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def display_banner():
    """Display the application banner"""
    st.image('static/images/data_analysis_banner.png', use_column_width=True)
    st.markdown(
        f"""
        <h1 style='color: {COLORS["primary"]}; text-align: center;'>
            Data Analysis and Preprocessing App
        </h1>
        """,
        unsafe_allow_html=True
    )
