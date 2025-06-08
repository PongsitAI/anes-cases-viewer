from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import models
from pydantic import BaseModel

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request/response
class AnesCaseBase(BaseModel):
    patient_name: str
    asa_status: str
    operation: str
    admit_date: str

class AnesCaseCreate(AnesCaseBase):
    pass

class AnesCase(AnesCaseBase):
    id: int

    class Config:
        orm_mode = True

# Dependency
def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to Anesthesia Cases API"}

@app.get("/cases", response_model=List[AnesCase])
def read_cases(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cases = db.query(models.AnesCase).offset(skip).limit(limit).all()
    return cases

@app.get("/cases/{case_id}", response_model=AnesCase)
def read_case(case_id: str, db: Session = Depends(get_db)):
    case = db.query(models.AnesCase).filter(models.AnesCase.case_id == case_id).first()
    if case is None:
        raise HTTPException(status_code=404, detail="Case not found")
    return case

@app.post("/cases/", response_model=AnesCase)
def create_case(case: AnesCaseCreate, db: Session = Depends(get_db)):
    db_case = models.AnesCase(**case.dict())
    db.add(db_case)
    db.commit()
    db.refresh(db_case)
    return db_case 