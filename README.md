# Bank Statement Analyzer

## Overview

The **Bank Statement Analyzer** is a Streamlit application that allows users to analyze bank statements using machine learning and natural language processing. Users can input their bank statement data, specify queries, and receive extracted information and analyses based on their queries.

## Features

- Upload and process bank statement documents.
- Query the bank statements for specific information.
- Analyze the extracted data using the Anthropic API.
- Intuitive user interface with real-time data visualization.

  ![image](https://github.com/user-attachments/assets/86599084-814f-423a-b948-9254d22757bc)


## Directory Structure

```
bank_statement_analyzer/
│
├── app.py                  # Main entry point for the Streamlit app
├── components/
│   ├── __init__.py         # Makes components a package
│   ├── bank_statement.py    # Contains BankStatement and BankStatements models
│   ├── data_loader.py       # Handles data loading and Qdrant interactions
│   ├── query_processor.py    # Processes user queries
│   └── anthropic_client.py   # Handles calls to the Anthropic API
└── requirements.txt         # Dependencies for the project
└── README.md                # Project documentation
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/manas95826/truffles-assgn
   ```
2. Navigate to the project directory:
   ```bash
   cd truffles-assgn
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
2. Open your web browser and go to `http://localhost:8501`.

3. Use the sidebar to view available data and input your queries:
   - Enter the collection name.
   - Input the text you are searching for in the bank statements.
   - Optionally, provide a user query for analysis.

4. Click the "Submit" button to process your input and view results.

## Requirements

- Python 3.x
- Streamlit
- Qdrant (for document storage)
- Anthropic API client
