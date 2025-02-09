# Data Analysis and Preprocessing App

A modern Streamlit application for data analysis and preprocessing, featuring an intuitive UI and comprehensive data processing capabilities.

## Features

- Upload CSV files for analysis
- Automatic column type classification:
  - Nominal, Ordinal, Discrete, Continuous
  - Numerical, Textual, Date-based data types
  - Automatic ID column detection
- Smart preprocessing pipeline:
  - Removes NULL and NONE values
  - Eliminates duplicates
  - Text processing:
    - Lowercasing and punctuation removal
    - Stopword removal and lemmatization
    - Number to word conversion
    - TF-IDF transformation with feature selection
  - Numerical processing:
    - Standard scaling for continuous data
    - Min-Max scaling for discrete data
  - Date normalization
  - ID preservation
- Modern UI with custom styling
- Detailed processing information and statistics
- Processed file download capability

## Project Structure

```
data_analysis_app/
├── app.py                 # Main application file
├── requirements.txt       # Project dependencies
├── README.md             # Documentation
├── static/               # Static assets
│   └── images/           # Application images
└── src/                  # Source code
    ├── preprocessing/    # Data processing modules
    │   ├── text_processor.py
    │   ├── numeric_processor.py
    │   └── date_processor.py
    ├── utils/            # Utility functions
    │   └── column_classifier.py
    └── ui/               # UI components
        └── styles.py     # Custom styling
```

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd data_analysis_app
```

2. Install the required packages:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

1. Launch the application and upload your CSV file
2. Review the automatic column analysis
3. Click 'Preprocess Data' to start the preprocessing pipeline
4. Monitor the transformation progress and statistics
5. Download the processed dataset

Processed files are automatically saved in the `output` directory with timestamps.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License
