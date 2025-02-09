import streamlit as st
import pandas as pd
import numpy as np
import os
from datetime import datetime

# Import custom modules
from src.preprocessing.text_processor import process_text_column
from src.preprocessing.numeric_processor import process_numeric_column
from src.preprocessing.date_processor import process_date_column
from src.utils.column_classifier import classify_column
from src.ui.styles import apply_custom_styles, display_banner

# Download required NLTK data
import nltk
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('omw-1.4')

def create_output_directory():
    """Create output directory if it doesn't exist"""
    if not os.path.exists('output'):
        os.makedirs('output')

def preprocess_column(series, col_type, data_type):
    """Apply appropriate preprocessing based on column type and data type"""
    if data_type == 'ID':
        return pd.DataFrame({series.name: series})  # Keep ID columns unchanged
    
    if data_type == 'Date':
        return pd.DataFrame({series.name: process_date_column(series)})
    
    if data_type == 'Text':
        return process_text_column(series)
    
    if data_type == 'Numeric':
        return pd.DataFrame({series.name: process_numeric_column(series, col_type)})
    
    return pd.DataFrame({series.name: series})

def main():
    """Main application function"""
    # Apply custom styling
    apply_custom_styles()
    
    # Display banner and title
    display_banner()

# File upload
uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])

if uploaded_file is not None:
    # Read the data
    df = pd.read_csv(uploaded_file)
    
    # Display original data
    st.subheader('Original Data Preview')
    st.write(df.head())
    st.write(f'Original shape: {df.shape}')
    
    # Remove NULL and NONE values
    df = df.replace(['NULL', 'NONE'], np.nan)
    
    # Analyze columns
    st.subheader('Column Analysis')
    col_analysis = {}
    
    for col in df.columns:
        col_type, data_type = classify_column(col, df[col])
        col_analysis[col] = {
            'Type': col_type,
            'Data': data_type,
            'Missing Values': df[col].isnull().sum(),
            'Unique Values': df[col].nunique()
        }
    
    analysis_df = pd.DataFrame.from_dict(col_analysis, orient='index')
    st.write(analysis_df)
    
    # Preprocessing
    st.subheader('Preprocessing Options')
    
    if st.button('Preprocess Data'):
        st.info('Starting preprocessing pipeline...')
        
        # Step 1: Remove duplicates
        initial_rows = len(df)
        df = df.drop_duplicates()
        st.write(f'Removed {initial_rows - len(df)} duplicate rows')
        
        # Step 2: Process each column
        processed_dfs = []
        
        for col in df.columns:
            col_type = col_analysis[col]['Type']
            data_type = col_analysis[col]['Data']
            
            # Process column
            processed_result = preprocess_column(df[col], col_type, data_type)
            
            # Handle different return types
            if isinstance(processed_result, pd.DataFrame):
                processed_dfs.append(processed_result)
            else:
                processed_dfs.append(pd.DataFrame({col: processed_result}))
        
        # Combine all processed columns
        processed_df = pd.concat(processed_dfs, axis=1)
        
        st.subheader('Processed Data Preview')
        st.write(processed_df.head())
        st.write(f'Processed shape: {processed_df.shape}')
        
        # Save processed data
        create_output_directory()
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_path = f'output/processed_data_{timestamp}.csv'
        processed_df.to_csv(output_path, index=False)
        
        # Provide download link
        with open(output_path, 'rb') as f:
            st.download_button(
                label="Download Processed Data",
                data=f,
                file_name=f"processed_data_{timestamp}.csv",
                mime="text/csv"
            )
        
        # Display processing summary
        st.success('Preprocessing completed successfully!')
        st.write('Processing Summary:')
        st.write(f'- Initial number of rows: {initial_rows}')
        st.write(f'- Final number of rows: {len(processed_df)}')
        st.write(f'- Initial number of columns: {len(df.columns)}')
        st.write(f'- Final number of columns: {len(processed_df.columns)}')

# Display instructions when no file is uploaded
else:
    st.write("Please upload a CSV file to begin analysis.")

if __name__ == '__main__':
    main()
