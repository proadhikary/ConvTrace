
<div align="center"><img src="https://raw.githubusercontent.com/proadhikary/ConvTrace/main/static/images/logo.png" alt="TRAVID" width="180"/><br>ConvTrace is a flask based app for Uploading, Displaying, and Summarizing Conversations from CSV files with Bootstrap UI<br> <a href="http://proadhikary.pythonanywhere.com/"><kbd> <br> Use App<br> </kbd></a></div> <br>


<img src="https://raw.githubusercontent.com/proadhikary/ConvTrace/main/static/images/screenshot.png" width=100%>



## Requirements

- Python 3.x
- Flask
- pandas

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/proadhikary/ConvTrace.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ConvTrace
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask app:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
3. Upload a CSV file on the index page to display the chat conversation.
4. Save summaries by entering the summary and selecting the summary type.
5. Download the CSV.
