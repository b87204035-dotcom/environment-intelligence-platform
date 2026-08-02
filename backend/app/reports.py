from uuid import UUID
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from psycopg.rows import dict_row
from .db import connection
router=APIRouter(prefix="/api/v1/reports",tags=["Reports"])
class ReportCreate(BaseModel):
    project_id: UUID|None=None
    title: str=Field(min_length=1,max_length=300)
class SectionUpsert(BaseModel):
    heading: str=Field(min_length=1,max_length=300)
    content: str|None=None
@router.post("",status_code=201)
def create_report(body:ReportCreate):
    with connection() as conn:
        row=conn.execute("INSERT INTO reports(project_id,title) VALUES(%s,%s) RETURNING *",(body.project_id,body.title),row_factory=dict_row).fetchone(); conn.commit()
    return row
@router.get("/{report_id}")
def get_report(report_id:UUID):
    with connection() as conn:
        report=conn.execute("SELECT * FROM reports WHERE id=%s",(report_id,),row_factory=dict_row).fetchone()
        sections=conn.execute("SELECT * FROM report_sections WHERE report_id=%s ORDER BY section_code",(report_id,),row_factory=dict_row).fetchall()
    if not report: raise HTTPException(404,"report not found")
    return {**report,"sections":sections,"release_blocked":report["status"] not in ("approved","published")}
@router.put("/{report_id}/sections/{section_code}")
def upsert_section(report_id:UUID,section_code:str,body:SectionUpsert):
    with connection() as conn:
        row=conn.execute("""INSERT INTO report_sections(report_id,section_code,heading,content) VALUES(%s,%s,%s,%s)
          ON CONFLICT(report_id,section_code) DO UPDATE SET heading=excluded.heading,content=excluded.content,review_status='unreviewed' RETURNING *""",
          (report_id,section_code,body.heading,body.content),row_factory=dict_row).fetchone(); conn.commit()
    return row
