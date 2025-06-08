from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///anes_cases/anes_cases.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ปรับ model ให้ตรงกับโจทย์
class AnesCase(Base):
    __tablename__ = "anes_cases"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String)
    asa_status = Column(String)
    operation = Column(String)
    admit_date = Column(String)

# ไม่ต้องสร้างตารางใหม่เพราะใช้ฐานข้อมูลที่มีอยู่แล้ว
# Base.metadata.create_all(bind=engine) 