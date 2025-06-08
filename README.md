# Anesthesia Cases Viewer

## Objective
แอปพลิเคชันนี้ใช้สำหรับอ่านข้อมูลจากฐานข้อมูล SQLite (`anes_cases.db`) และแสดงผลในหน้าเว็บ พร้อมฟีเจอร์ filter ข้อมูลด้วย `asa_status` และแสดงผลในรูปแบบตาราง

## โครงสร้างโปรเจกต์

```
api-test/
├── anes_cases/
│   └── anes_cases.db        # ไฟล์ฐานข้อมูล SQLite
├── index.html               # หน้าเว็บสำหรับแสดงข้อมูล
├── main.py                  # โค้ด FastAPI backend (API)
├── models.py                # โค้ด SQLAlchemy ORM สำหรับเชื่อมต่อฐานข้อมูล
├── requirements.txt         # รายการ dependencies ที่ต้องใช้
└── README.md                # คำอธิบายโปรเจกต์ (ไฟล์นี้)
```

## วิธีติดตั้งและรันโปรเจกต์

1. **ติดตั้ง dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **รัน FastAPI backend**
   ```bash
   uvicorn main:app --reload --port 8081
   ```
   - API จะรันที่ http://localhost:8000
   - สามารถดูเอกสาร API ได้ที่ http://localhost:8000/docs

3. **รันเว็บเซิร์ฟเวอร์สำหรับ frontend** (เพื่อให้ fetch API ได้สมบูรณ์)
   ```bash
   python -m http.server 8080
   ```
   - จากนั้นเปิดเบราว์เซอร์ไปที่ http://localhost:8081

## รายละเอียดแต่ละไฟล์
- **index.html**: หน้าเว็บสำหรับแสดงข้อมูลเคสในรูปแบบตาราง พร้อม filter `asa_status`
- **main.py**: โค้ด FastAPI สำหรับสร้าง API `/cases` ที่ดึงข้อมูลจากฐานข้อมูลและส่งกลับเป็น JSON
- **models.py**: กำหนด ORM Model สำหรับ table `anes_cases` ให้ตรงกับโครงสร้างฐานข้อมูล
- **requirements.txt**: รายการไลบรารีที่ต้องใช้ เช่น fastapi, sqlalchemy, uvicorn
- **anes_cases/anes_cases.db**: ไฟล์ฐานข้อมูล SQLite ที่มีข้อมูลจริง

## ฟีเจอร์
- แสดงข้อมูลเคสทั้งหมดจากฐานข้อมูล SQLite
- Filter ข้อมูลด้วย ASA Status
- ตารางแสดงผลสวยงามและอ่านง่าย

## โครงสร้างฐานข้อมูล
- Table: `anes_cases`
- Fields: `id`, `patient_name`, `asa_status`, `operation`, `admit_date`

## (Bonus) Version Control
- สามารถใช้ git สำหรับ version control ได้ เช่น
  ```bash
  git init
  git add .
  git commit -m "Initial commit"
  ```

---

**หากมีข้อสงสัยหรือปัญหา สามารถสอบถามได้ตลอดครับ** 