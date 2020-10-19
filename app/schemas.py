from pydantic import BaseModel


class CameraBase(BaseModel):
    pass


class CameraCreate(CameraBase):
    doorbot_id: int
    doorbot_type: str
    firmware_version: str
    pass


class CameraUpdate(CameraBase):
    firmware_version: str
    online_status: bool
    pass


class Camera(CameraBase):
    doorbot_id: int
    doorbot_type: str
    firmware_version: str
    online_status: bool

    class Config:
        orm_mode = True
