# extract text
from langchain.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_google_genai import GoogleGenerativeAIEmbeddings


llm = ChatGoogleGenerativeAI(
        google_api_key="AIzaSyBuBnDizsZfq0tai2ExloP8TvTuYCV8_ss",
        model="gemini-pro",
        convert_system_message_to_human=True
        
    )


embeddings = GoogleGenerativeAIEmbeddings(
    google_api_key="AIzaSyBuBnDizsZfq0tai2ExloP8TvTuYCV8_ss",
    model="models/embedding-001",


)

persist_directory = "C:/Users/DELL/OneDrive/GenAI-usecase/db2/"

# Set the embedding function and directory for vector storage
embedding = embeddings
vectordb = Chroma(embedding_function=embedding, persist_directory=persist_directory)

with open(r"C:/Users/DELL/OneDrive/GenAI-usecase/dbdemo/text.txt", "r") as file:
    content = file.read() 

from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=50, chunk_overlap=10,separator="\n")
splits = text_splitter.split_text(content)

for t in splits:
    vectordb.add_texts(
    texts = [t],
)
    

    
