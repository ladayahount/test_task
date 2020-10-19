from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# get the list of all devices
@app.get("/api/v1/devices", response_model=List[schemas.Camera])
def read_cameras(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cameras = crud.get_cameras(db, skip=skip, limit=limit)
    return cameras


# find device via doorbot_id
@app.get("/api/v1/devices/{doorbot_id}", response_model=schemas.Camera)
def read_camera_by_id(doorbot_id: int, db: Session = Depends(get_db)):
    db_camera = crud.get_camera(db, doorbot_id=doorbot_id)
    if db_camera is None:
        raise HTTPException(status_code=404, detail="Camera not found")
    return db_camera


# add device
@app.post("/api/v1/devices", response_model=schemas.Camera)
def create_camera(camera: schemas.CameraCreate, db: Session = Depends(get_db)):
    db_camera = crud.get_camera_by_doorbot_id(db, doorbot_id=camera.doorbot_id)
    if db_camera:
        raise HTTPException(status_code=400, detail="Camera already registered for this doorbot id")
    return crud.create_camera(db=db, camera=camera)


# delete device via doorbot_id
@app.delete("/api/v1/devices/{doorbot_id}", response_model=schemas.Camera)
def delete_camera(doorbot_id: int, db: Session = Depends(get_db)):
    db_camera = crud.get_camera(db, doorbot_id=doorbot_id)
    if db_camera is None:
        raise HTTPException(status_code=404, detail="Camera not found")
    crud.delete_camera(db, doorbot_id=doorbot_id)
    raise HTTPException(status_code=200,
                        detail="Device with id " + str(doorbot_id) + " successfully deleted")


# update device via doorbot_id
@app.put("/api/v1/devices/{doorbot_id}", response_model=schemas.Camera)
def update_camera(doorbot_id: int, camera: schemas.CameraUpdate, db: Session = Depends(get_db)):
    db_camera = crud.get_camera(db, doorbot_id=doorbot_id)
    if db_camera is None:
        raise HTTPException(status_code=404, detail="Camera not found")
    return crud.replace_camera(db=db, doorbot_id=doorbot_id, camera=camera)
