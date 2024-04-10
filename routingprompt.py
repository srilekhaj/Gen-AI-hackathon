from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_google_genai import GoogleGenerativeAIEmbeddings
import re

#importing files
import db as db
import textextract as txt


llm = ChatGoogleGenerativeAI(
        google_api_key="AIzaSyBuBnDizsZfq0tai2ExloP8TvTuYCV8_ss",
        model="gemini-pro",
        convert_system_message_to_human=True
        
    )


embeddings = GoogleGenerativeAIEmbeddings(
    google_api_key="AIzaSyBuBnDizsZfq0tai2ExloP8TvTuYCV8_ss",
    model="models/embedding-001",


)

def navigator(Query):
    template = f"""
Categorize the given query and select the appropriate  repository to retrieve data from. 

Repositories:
1. Database: Contains information that can be easily converted from a query to PostgreSQL query 
2. Text file: Contains information about standard banking FAQ questions.

Query:
{Query}

Provide your response in the below format:
Reason: <Provide your Reason here>
Answer: <Provide Database or Text file>

"""
    
    result = llm.invoke(template)
    result = result.content

    match = re.search(r"Answer:\s*(.*)", result, flags= re.DOTALL)
    if match:
        navigator_match = match.group(1)
        if navigator_match == 'Database':
            return db.sqlquery_retriever(Query)
        elif navigator_match == 'Text file':
            return txt.text_retrieve(Query)
        else:
            return "The requested information not found"


