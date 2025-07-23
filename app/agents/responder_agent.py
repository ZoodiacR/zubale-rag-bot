from typing import List, TypedDict
from langchain.schema import Document
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

class ResponderState(TypedDict):
    query: str
    documents: List[Document]
    answer: str

class ResponderAgent:
    def __init__(self, llm: ChatOpenAI):
        self.llm = llm

    def __call__(self, state: ResponderState) -> ResponderState:
        context = "\n".join([doc.page_content for doc in state["documents"]])
        prompt = PromptTemplate(
            input_variables=["query", "context"],
            template="""You are a helpful assistant for a grocery shopping app.
Use only the following context to answer the user's question.
If the answer is not in the context, say "I don’t know."

Context:
{context}

User question:
{query}
Answer:"""
        )
        chain = prompt | self.llm
        response = chain.invoke({"query": state["query"], "context": context})
        state["answer"] = response.content.strip()
        return state