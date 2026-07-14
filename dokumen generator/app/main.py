"""
main.py — Winamus Document Generator — FastAPI Web App
"""
import os
import json
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Request, Form, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .generator import generate, generate_html
from .config import get_config

# ── Paths ──
BASE_DIR = Path(__file__).parent.parent.parent  # nasmoco-docs/
APP_DIR = Path(__file__).parent
TEMPLATES_DIR = APP_DIR / "templates" / "ui"
OUTPUT_DIR = APP_DIR.parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

app = FastAPI(title="Winamus Doc Generator", version="1.0.0")

# Serve output files
app.mount("/output", StaticFiles(directory=str(OUTPUT_DIR)), name="output")

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


def get_markdown_files(base_dir: Path) -> list[dict]:
    """Rekursif cari semua file .md di bawah base_dir."""
    files = []
    for md in sorted(base_dir.rglob("*.md")):
        rel = md.relative_to(base_dir)
        files.append({"path": str(md), "label": str(rel)})
    return files


# ── Routes ──

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    cfg = get_config()
    md_files = get_markdown_files(BASE_DIR)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "company": cfg["company"],
        "doc_types": cfg["document_types"],
        "styles": ["modern", "classic", "bold"],
        "md_files": md_files,
    })


@app.post("/preview", response_class=HTMLResponse)
async def preview(
    source_path: str = Form(...),
    doc_type: str = Form(...),
    style: str = Form("modern"),
    layout: str = Form("table"),
):
    """Render preview HTML dokumen."""
    try:
        html = generate_html(
            source_path=Path(source_path),
            doc_type=doc_type,
            style=style,
            layout=layout,
        )
        return HTMLResponse(content=html)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/generate")
async def generate_doc(
    source_path: str = Form(...),
    doc_type: str = Form(...),
    style: str = Form("modern"),
    layout: str = Form("table"),
    formats: str = Form("pdf,docx,html"),  # comma-separated
    project_docs_dir: Optional[str] = Form(None),
):
    """Generate dokumen dan kembalikan list file hasil."""
    fmt_list = [f.strip() for f in formats.split(",") if f.strip()]

    try:
        results = generate(
            source_path=Path(source_path),
            doc_type=doc_type,
            style=style,
            layout=layout,
            formats=fmt_list,
            output_dir=OUTPUT_DIR,
            project_docs_dir=Path(project_docs_dir) if project_docs_dir else None,
        )

        files = []
        for fmt, path in results.items():
            files.append({
                "format": fmt,
                "filename": path.name,
                "url": f"/output/{path.name}",
                "size_kb": round(path.stat().st_size / 1024, 1),
            })

        return JSONResponse({"success": True, "files": files})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/download/{filename}")
async def download(filename: str):
    """Download file dari output directory."""
    file_path = OUTPUT_DIR / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File tidak ditemukan")
    return FileResponse(path=str(file_path), filename=filename)


@app.get("/history")
async def history():
    """Daftar file yang pernah digenerate."""
    files = []
    for f in sorted(OUTPUT_DIR.iterdir(), key=lambda x: x.stat().st_mtime, reverse=True):
        if f.is_file():
            files.append({
                "filename": f.name,
                "url": f"/output/{f.name}",
                "size_kb": round(f.stat().st_size / 1024, 1),
                "modified": f.stat().st_mtime,
            })
    return JSONResponse(files)
