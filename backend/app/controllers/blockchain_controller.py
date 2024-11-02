from fastapi import APIRouter
from app.blockchain.blockchain import Blockchain
from ..models.schemas import DataModel


api_router = APIRouter()
blockchain = Blockchain()



@api_router.post("/add_data")
async def add_data(data: DataModel):
    blockchain.add_block(data.dict())
    return {"message": "Data added to the blockchain"}


@api_router.get("/validate_chain")
async def validate_chain():
    if blockchain.is_chain_valid():
        return {"message": "Blockchain is valid"}
    return {"message": "Blockchain is invalid"}
