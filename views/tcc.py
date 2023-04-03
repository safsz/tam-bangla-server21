from fastapi import APIRouter, status
from database import users_collection
from dtos.tcc import Users
import json
from bson.json_util import loads, dumps

router = APIRouter()

@router.post("/tcc", status_code=status.HTTP_201_CREATED)
async def add_new_tcc_team(team: Users):
    team_data = team.dict()
            
    data = users_collection.find({"email": team_data["email"]})
  
    user =json.loads(dumps(data))
     
    if len(user) !=0:
        filter = { 'email': team_data["email"] }
        newvalues = { "$set": {'name': team_data["name"], 
                               'email': team_data["email"],
                               'picture': team_data["picture"], 
                               'tcc': team_data["tcc"] } }
        result = users_collection.update_one(filter, newvalues)
    else:
        result = users_collection.insert_one(team_data)
    return {
        "status" : result.acknowledged
    }


@router.get("/tcc/{id}", status_code=status.HTTP_200_OK)
async def get_one_user_tcc_team_data(id: str):
    data = users_collection.find({"email": str(id)})
    user =json.loads(dumps(data))
    if len(user) !=0 :
        return user[0]
    else:
        return None