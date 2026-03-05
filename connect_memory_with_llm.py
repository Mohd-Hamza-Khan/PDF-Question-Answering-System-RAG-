from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import RetrievalQA
from langchain_community.vectorstores import FAISS

def load_llm():
    """
    Returns a configured Ollama LLM instance.
    """
    return OllamaLLM(
        model="phi3:mini",
        temperature=0.3,
        num_predict=100
    )

# 2. Connect LLM with FAISS and Create a Chain
custom_prompt_template = """
        You are a strict assistant.

        Answer ONLY using the information provided in the context.

        Rules:
        1. If the answer is not explicitly present in the context, say:
        "I don't know. The information is not present in the provided documents."
        2. Do NOT use prior knowledge.
        3. Do NOT guess.

        Context:
        {context}

        Question:
        {question}

        Answer:
    """

def set_custom_prompt(custom_prompt_template):
    prompt = PromptTemplate(template=custom_prompt_template, input_variables=["context", "question"])
    return prompt

# Load database
embedding_model = OllamaEmbeddings(model="mxbai-embed-large")
DB_FAISS_PATH = "vectorestore/db_faiss"
db=FAISS.load_local(DB_FAISS_PATH, embeddings=embedding_model, allow_dangerous_deserialization=True)
retriever = db.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={
        "k": 4,
        "score_threshold": 0.5
    }
)

# Create QA Chain
prompt = set_custom_prompt(custom_prompt_template)
llm = load_llm()


qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt}
)

# Now invoke a simple querry 
user_query = input("Write Query Here: ")


response = qa_chain.invoke({"query": user_query})

if len(response["source_documents"]) == 0:
    print("Result: I don't know. The answer is not present in the documents.")
else:
    print("Result:", response["result"])
    print("Sources:", response["source_documents"])
