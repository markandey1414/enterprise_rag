from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict, Optional
from .security import verify_token
from .knowledge_base import EnterpriseKnowledgeBase, SourceSystem

router = APIRouter()
kb = EnterpriseKnowledgeBase()

@router.post("/documents/ingest")
async def ingest_documents(
    source_system: SourceSystem,
    credentials: Dict,
    paths: List[str],
    department: str,
    access_level: int,
    token: dict = Depends(verify_token)
):
    try:
        result = await kb.ingest_documents(
            source_system,
            credentials,
            paths,
            department,
            access_level
        )
        return {"status": "success", "processed_documents": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/query")
async def query_kb(
    query: str,
    filters: Optional[Dict] = None,
    token: dict = Depends(verify_token)
):
    try:
        user = token.get("user")  # Get user from token
        result = await kb.query_knowledge_base(query, user, filters)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))