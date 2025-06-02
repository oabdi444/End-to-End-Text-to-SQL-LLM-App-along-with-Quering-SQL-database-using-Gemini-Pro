from dotenv import load_dotenv
load_dotenv()  ## load all the environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

## Configure Genai Key
genai.configure(api_key=os.getenv("AIzaSyC7MCd54RAvdKuFOjI7LgeMjI2t7Crh-ps"))

## Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt[0], question])
    return response.text

## Function To retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

## Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION, MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    WHERE CLASS='Data Science'; 
    Always enclose string values in single quotes.
    Also, return only the SQL query—no ``` or the word 'sql'
    """
]

## Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# If submit is clicked
if submit:
    raw_response = get_gemini_response(question, prompt)

    # --- Clean the Gemini response ---
    cleaned_sql = raw_response.strip().replace("```", "").replace("sql", "").strip()
    
    st.subheader("Generated SQL Query")
    st.code(cleaned_sql, language="sql")
    print("Running SQL:", cleaned_sql)

    try:
        result = read_sql_query(cleaned_sql, "student1.db")
        st.subheader("Response is")
        st.write(result)

        for row in result:
            print(row)
            st.header(row)
    except sqlite3.OperationalError as e:
        st.error(f"SQL Error: {e}")
        st.info("Try rephrasing the question. The model may have generated invalid SQL.")


  

