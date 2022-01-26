from fastapi import APIRouter, HTTPException, Depends
from db.table import saving, users
from saving import model
from auth.model import User_ID
from utils import util

from users.controller import read_user_Id

from configs.connection import database
import uuid, datetime
from fastapi_pagination import Page, paginate
import sqlalchemy as db
router = APIRouter()


@router.get("/all_saving", response_model=Page[model.SavingList])
async def find_allsavings(currentUser: model.SavingList = Depends(util.get_current_active_user)):
    query = saving.select()
    res = await database.fetch_all(query)
    return paginate(res)


@router.get("/likesaving/{names}", response_model=Page[model.SavingList])
async def find_like_saving(names: str, currentUser: model.SavingList = Depends(util.get_current_active_user)):

    query = "select * from saving where saving_name like '%{}%'".format(names)
    res= await database.fetch_all(query=query, values={})
    return paginate(res)



@router.get("/users_id", response_model=User_ID)
async def read_user_Id(currentUserId: User_ID = Depends(util.get_current_active_user)):

    print(currentUserId.id)
    return currentUserId

@router.post("/addsaving", response_model=model.SavingList)
async def registersaving(svg: model.SavingCreate):

    #Last_user_id = users.select().where(users.c.id == id)

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = saving.insert().values(

        
        id = gid,
        user_id=svg.user_id,
        saving_name = svg.saving_name,
        description = svg.description,
        currency = svg.currency,
        income= svg.income,  
        target= svg.target,
        created_at = gdate,
        status = "1"
    )

    await database.execute(query)
    return {
        **svg.dict(),
        "id": gid,
        "created_at": gdate,
        "status": "1"
    }




