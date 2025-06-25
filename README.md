End-to-End Text-to-SQL LLM App using Gemini Pro


This project is a full-stack, interactive application that allows users to convert natural language questions into SQL queries using Google's Gemini Pro (LLM) and execute those queries against a local SQLite database. It showcases the integration of LLMs with structured databases and the potential for building AI-assisted data querying interfaces.

Project Overview
Key Features:

Converts English-language questions into SQL statements using Gemini Pro (gemini-1.5-flash)

Executes the generated SQL against a local SQLite database (student1.db)

Returns structured results in a web interface powered by Streamlit

Includes error handling and query validation feedback

Technologies Used
Python 3.10+

Streamlit – Frontend interface

Google Generative AI SDK – LLM API (Gemini)

SQLite3 – Lightweight local database

dotenv – For secure API key management

Folder Structure
pgsql
Copy
Edit
End-to-End-Text-to-SQL-LLM-App/


│
├── .env                 # Environment variables (contains Gemini API key)
├── .gitignore           # Prevents sensitive files from being tracked
├── requirements.txt     # Project dependencies
├── sql.py               # (Optional) SQL utility functions (if any)
├── sqlite.py            # (Optional) DB connection/setup script
├── student1.db          # Sample SQLite database
├── test.py              # Main Streamlit application
└── README.md            # Project documentation


Setup Instructions
Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/end-to-end-text-to-sql-llm-app.git
cd end-to-end-text-to-sql-llm-app
Set Up Virtual Environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install Dependencies

bash
Copy
Edit
pip install -r requirements.txt
Add Your Google API Key
Create a .env file in the root directory with:

ini
Copy
Edit
GOOGLE_API_KEY=your_gemini_api_key_here
Run the Application

bash
Copy
Edit
streamlit run test.py
Example Prompts
Input any of the following in the app's input field:

How many students are in the database?

List all students in the Data Science class

What are the names of students who scored above 80?

The model will convert this to valid SQL, query the student1.db SQLite database, and return results.

 Notes
The student1.db database should contain a table named STUDENT with columns: NAME, CLASS, SECTION, MARKS.

The Gemini API may occasionally generate incorrect SQL. The app includes error handling and suggestions for rephrasing.

Ensure the .env file is never committed to source control. The .gitignore file handles this by default.

Future Improvements
Add schema introspection to dynamically adapt to different databases

Support multi-table joins and advanced SQL generation

Add PDF/CSV data upload for dynamic database creation

Enable secure deployment to cloud platforms with user authentication

📄 License
This project is released under the MIT License.

