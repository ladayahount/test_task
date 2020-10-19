from sqlalchemy import Column, Integer, String, Boolean

from .database import Base


class Camera(Base):
    __tablename__ = "devices"

    doorbot_id = Column(Integer, primary_key=True)
    online_status = Column(Boolean, default=False)
    doorbot_type = Column(String)
    firmware_version = Column(String)
