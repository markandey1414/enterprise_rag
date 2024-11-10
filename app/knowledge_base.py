from typing import List, Dict, Optional
from datetime import datetime
import logging
from enum import Enum
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from config.settings import get_settings

settings = get_settings()

# say, sharepoint and confluence support
class SourceSystem(Enum):
    SHAREPOINT = "sharepoint"
    CONFLUENCE = "confluence"
    FILE_SYSTEM = "file_system"

class EnterpriseKnowledgeBase:
    def __init__(self):
        # Initialize components
        self.embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
        self.vector_store = Pinecone.from_existing_index(
            index_name="enterprise-kb",
            embedding=self.embeddings
        )
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        self.llm = OpenAI(temperature=0)
        
        # logging
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    # basic knowledge base setup, rest can be added later