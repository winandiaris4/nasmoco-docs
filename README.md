# Nasmoco Docs — Winamus Project Management Repository

Repositori ini berfungsi sebagai **pusat manajemen proyek dan dokumentasi** untuk seluruh kebutuhan Winamus (PT Winandi Multi Solusi), baik dokumen korporat yang berlaku umum maupun dokumentasi spesifik per proyek klien.

**Proyek Aktif:** Pengembangan Platform Website Terpusat **Nasmoco (PT New Ratna Motor)**
**Status:** 🟡 Negosiasi — Menunggu persetujuan Quotation Rev.1
**Prototype:** 🌐 [nasmoco.winamus.com](https://nasmoco.winamus.com)

---

## Peran Konsultan Bisnis & IT

Seluruh dokumen dalam repositori ini disusun oleh **Aris Winandi (Winamus)** berkolaborasi dengan **Antigravity**, AI Agent dari tim Google DeepMind, yang bertindak sebagai **Konsultan Bisnis & IT**. Kolaborasi ini mencakup:

1. **Analisis Kepatuhan & Risiko Bisnis** — Memetakan kebutuhan compliance terhadap SOP Digital Asset TAM Juni 2025.
2. **Perancangan Strategi Arsitektur IT** — Tahapan keamanan bertahap (baseline → hardening → validation) & integrasi sistem existing.
3. **Penyusunan Materi Komersial** — Skema harga berbasis fase, klausul perlindungan vendor, negosiasi, dan perpajakan.

---

## Struktur Repositori

```
nasmoco-docs/
│
├── winamus/                        ← Dokumen korporat Winamus (berlaku lintas proyek)
│   ├── SOP/                        ← Standar Operasional Prosedur (Project Handling, Development, IEEE/TOGAF)
│   │   ├── Standar_IEEE_dan_TOGAF.md ← Penjelasan integrasi standar IEEE & TOGAF di Winamus
│   │   └── SOP-Software-Development-Checklist.md
│   ├── asset/                      ← Logo, gambar, dan aset visual Winamus
│   ├── company profile/            ← Profil perusahaan & website
│   ├── legal/                      ← Dokumen legalitas PT Perorangan
│   └── other information/
│       └── Pajak/                  ← Panduan PPh Final 0.5% (PP 55), simulasi pajak per termin
│
├── project/
│   └── nasmoco/                    ← Semua dokumen proyek Nasmoco
│       ├── progress.md             ← 📊 Dashboard tracking status & fase proyek (UPDATE DI SINI)
│       ├── Docs/                   ← Dokumen resmi (Quotation, Proposal, Kontrak)
│       │   └── Quotation_Nasmoco_Rev1.md   ← Penawaran harga resmi Rev.1 (Rp71.100.000)
│       ├── Other/                  ← Dokumen komersial & operasional detail
│       │   ├── Klarifikasi_Skema_Harga.md  ← Rincian biaya & termin per fase
│       │   ├── Alur_Fase_dan_UAT.md        ← Alur pengerjaan, UAT, BAST & klausul perlindungan
│       │   ├── Alur_Biaya_Maintenance.md   ← Skema maintenance bulanan/tahunan & excess hours
│       │   ├── Analisis_Hosting_Mandiri.md ← Analisis skenario hosting Nasmoco vs Winamus
│       │   └── Ringkasan_Poin_Proposal.md  ← Ringkasan eksekutif proposal
│       ├── slide/                  ← Materi presentasi
│       │   ├── Naskah_Presentasi_Nasmoco.md
│       │   ├── Antisipasi_Pertanyaan_Sulit_Nasmoco.md
│       │   └── *.pdf / *.pptx      ← File presentasi (perlu di-update ke angka terbaru)
│       ├── requirements_awal/      ← Dokumen acuan dari Nasmoco (Kisi-Kisi & Analisis Requirements)
│       └── Nasmoco-SOP-Software-Development-Checklist.md  ← SOP pengembangan standar industri
│
└── dokumen generator/              ← Konsep generator PDF otomatis dari Markdown
```

---

## Status Dokumen

| Dokumen | Lokasi | Status |
|---|---|---|
| Quotation Rev.1 | `project/nasmoco/Docs/` | ✅ Siap kirim *(lengkapi NPWP & rekening)* |
| Progress Tracker | `project/nasmoco/progress.md` | ✅ Up to date |
| Panduan Pajak | `winamus/other information/Pajak/` | ✅ Up to date |
| Slide Presentasi (PDF/PPTX) | `project/nasmoco/slide/` | ⚠️ Perlu regenerasi (angka lama Rp86.1jt) |
| Kontrak / PKS | `project/nasmoco/Docs/` | ⏳ Belum dibuat — menunggu PO |

---

## Panduan Penggunaan Cepat

- **Tracking status proyek** → buka `project/nasmoco/progress.md`
- **Kirim penawaran ke Nasmoco** → gunakan `project/nasmoco/Docs/Quotation_Nasmoco_Rev1.md`
- **Siapkan invoice & perpajakan** → rujuk `winamus/other information/Pajak/Panduan_Pajak_PT_Perorangan.md`
- **Diskusi teknis / klausul kontrak** → rujuk folder `project/nasmoco/Other/`
