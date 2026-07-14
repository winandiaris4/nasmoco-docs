# 🗂️ Winamus Document Generator

Sistem generator dokumen profesional berbasis FastAPI untuk mengubah file Markdown (`.md`) menjadi dokumen PDF, DOCX, dan HTML berkop surat Winamus.

Sistem ini mendukung **3 Visual Styles** (Modern, Classic, Bold) dan **2 Layout Varian** per tipe dokumen.

---

## 🚀 Cara Menjalankan (Web UI)

Web UI menyediakan interface di browser untuk memilih file Markdown, melihat preview HTML kop surat secara real-time, dan mengunduh format PDF/DOCX dengan satu klik.

Jalankan perintah berikut di terminal Anda:

```bash
# Pindah ke directory generator
cd "dokumen generator"

# Jalankan script run.sh (akan otomatis setup virtualenv & install dependencies)
./run.sh
```

Setelah server berjalan, buka browser Anda di:
👉 **[http://localhost:8000](http://localhost:8000)**

---

## ⌨️ Cara Menggunakan (Command Line Interface - CLI)

Anda juga bisa melakukan *batch generation* atau otomatisasi langsung lewat terminal menggunakan script CLI.

### 1. Masuk ke Virtual Environment
```bash
cd "dokumen generator"
source .venv/bin/activate
```

### 2. Jalankan Perintah CLI
Berikut adalah beberapa contoh penggunaan CLI yang sering dipakai:

*   **Generate PDF, DOCX, dan HTML sekaligus (Quotation Nasmoco):**
    ```bash
    python -m app.cli generate \
      --source ../project/nasmoco/Docs/Quotation_Nasmoco_Rev1.md \
      --type quotation \
      --all-formats
    ```

*   **Generate PDF saja dengan style "classic" dan langsung disalin ke folder Docs proyek Nasmoco:**
    ```bash
    python -m app.cli generate \
      --source ../project/nasmoco/Docs/Quotation_Nasmoco_Rev1.md \
      --type quotation \
      --style classic \
      --format pdf \
      --project ../project/nasmoco/Docs/
    ```

*   **Melihat daftar template style & tipe dokumen yang tersedia:**
    ```bash
    python -m app.cli list-templates
    ```

*   **Melihat info konfigurasi & data perusahaan aktif:**
    ```bash
    python -m app.cli info
    ```

---

## ⚙️ Konfigurasi & Data Sensitif

Sebelum digunakan untuk pengiriman resmi, pastikan Anda telah melengkapi data-data berikut:

1.  **`dokumen generator/config.yml`**: Berisi konfigurasi branding global (nama PT, tagline, website, logo URL, dan palet warna).
2.  **`dokumen generator/.env`**: Berisi data sensitif (NPWP, detail Rekening Bank, Nama Penandatangan/Direktur). File ini otomatis dibuat dari `.env.example` saat pertama kali Anda menjalankan `./run.sh`. Sila isi nilainya secara manual.

---

## 📂 Struktur Output
Secara default, seluruh dokumen yang digenerate akan disimpan di folder:
`dokumen generator/output/`
Jika opsi `--project` (CLI) atau `Project Output` (Web UI) diisi, salinan hasil generate akan diletakkan langsung di dalam folder Docs proyek klien terkait.
