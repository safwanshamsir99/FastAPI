from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

@app.get("/")
def root():
    return {"status": "success"}

# Path parameter
@app.get("/car", status_code=200, tags=["about car"], summary="get car info", 
         description="more details", response_description="list of car")
def get_car():
    return ...

# Query parameter
@app. get("/car/{id}")
def get_car(name:str, brand:str):
    return ...

# Pydantic Base Model
class CarInfo(BaseModel):
    name: str
    brand: str
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "wira",
                    "brand": "proton"
                }
            ]
        }
    }


@app.post("/car")
def get_car(car_info: CarInfo)->CarInfo:
    return {
        "Name":car_info.name,
        "Brand": car_info.brand
    }

# typing data validation
# @app.get("/job")
# def get_car(job_name: Union[str, None], job_amount: Union[int, 0]):
# 	return {
# 			"job_name":job_name, 
# 			"job_amount": job_amount, 
# }	

