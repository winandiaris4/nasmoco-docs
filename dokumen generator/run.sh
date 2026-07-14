#!/usr/bin/env bash
# ══════════════════════════════════════════
# run.sh — Winamus Document Generator
# ══════════════════════════════════════════

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

VENV_DIR="$SCRIPT_DIR/.venv"
PYTHON="$VENV_DIR/bin/python"
PIP="$VENV_DIR/bin/pip"

# ── Setup venv jika belum ada ──
if [ ! -d "$VENV_DIR" ]; then
  echo "🔧 Membuat virtual environment..."
  python3 -m venv "$VENV_DIR"
fi

# ── Install dependencies jika belum ──
if ! "$PYTHON" -c "import fastapi" 2>/dev/null; then
  echo "📦 Menginstall dependencies..."
  "$PIP" install --quiet -r requirements.txt
fi

# ── Setup .env jika belum ada ──
if [ ! -f ".env" ]; then
  echo "⚙️  File .env tidak ditemukan. Menyalin dari .env.example..."
  cp .env.example .env
  echo "   ⚠️  Edit file .env dan isi NPWP, rekening, dll sebelum generate!"
fi

# ── Buat folder output ──
mkdir -p output

# ── Jalankan server ──
echo ""
echo "🚀 Winamus Document Generator"
echo "   URL: http://localhost:8000"
echo "   Tekan Ctrl+C untuk berhenti."
echo ""

"$VENV_DIR/bin/uvicorn" app.main:app \
  --host 0.0.0.0 \
  --port 8000 \
  --reload \
  --app-dir "$SCRIPT_DIR"
