from sqlalchemy.orm import Session

from . import models, schemas


def get_cameras(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Camera).offset(skip).limit(limit).all()


def get_camera(db: Session, doorbot_id: int):
    return db.query(models.Camera).filter(models.Camera.doorbot_id == doorbot_id).first()


def get_camera_by_doorbot_id(db: Session, doorbot_id: int):
    return db.query(models.Camera).filter(models.Camera.doorbot_id == doorbot_id).first()


def create_camera(db: Session, camera: schemas.CameraCreate):
    item = models.Camera(doorbot_id=camera.doorbot_id, firmware_version=camera.firmware_version,
                              doorbot_type=camera.doorbot_type)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


def delete_camera(db: Session, doorbot_id: int):
    item = db.query(models.Camera).filter(models.Camera.doorbot_id == doorbot_id).first()
    db.delete(item)
    db.commit()
    return


def replace_camera(db: Session, doorbot_id: int, camera: schemas.CameraUpdate):
    item = db.query(models.Camera).filter(models.Camera.doorbot_id == doorbot_id).first()
    item.firmware_version = camera.firmware_version
    item.online_status = camera.online_status
    db.commit()
    return item

