from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from backend.services.embedder import get_index_path
from backend.config import GROQ_API_KEY

def get_answer(repo_url: str, question: str) -> str:
    embeddings = FastEmbedEmbeddings()
    index_path = get_index_path(repo_url)

    db = FAISS.load_local(index_path, embeddings,
                          allow_dangerous_deserialization=True)

    retriever = db.as_retriever(search_kwargs={"k": 5})

    llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)

    prompt = PromptTemplate.from_template("""
Use the following code context to answer the question.
Context: {context}
Question: {question}
Answer:""")

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain.invoke(question)