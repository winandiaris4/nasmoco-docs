# QUOTATION / PENAWARAN HARGA
## Pengembangan Platform Website Terpusat Nasmoco
### Revisi 1 — Juli 2026

---

| | |
|---|---|
| **Dari (Vendor)** | PT Winandi Multi Solusi (Winamus) |
| **Website** | www.winamus.com |
| **Kepada (Klien)** | PT New Ratna Motor (Nasmoco Group) |
| **Nomor Quotation** | QT-NASMOCO-2026-R1 |
| **Tanggal Terbit** | 15 Juli 2026 |
| **Berlaku Hingga** | 15 Agustus 2026 |
| **Revisi** | Rev.1 — Pen Testing dihapus (ditangani internal Klien) |

---

## Lingkup Pekerjaan & Rincian Biaya

### Fase 0: Discovery & Desain
| | |
|---|---|
| Durasi | 1–2 Minggu |
| Deliverables | Finalisasi SRS, Desain UI/UX Figma, Arsitektur Sistem |
| **Total Biaya** | **Rp4.500.000** |
| DP 30% (Awal Fase) | Rp1.350.000 |
| Pelunasan 70% (Setelah UAT) | Rp3.150.000 |

### Fase 1: Inti / MVP
| | |
|---|---|
| Durasi | 4–6 Minggu *(Go-Live MVP Minggu ke-8)* |
| Deliverables | Migrasi PostgreSQL, Sistem Harga Terpusat, Page Builder, Anti-Hijack Lead, Integrasi CRM & WABA |
| **Total Biaya** | **Rp27.000.000** |
| DP 30% (Awal Fase) | Rp8.100.000 |
| Pelunasan 70% (Setelah UAT) | Rp18.900.000 |

### Fase 2: Governance & Hardening
| | |
|---|---|
| Durasi | 4–6 Minggu |
| Deliverables | Approval Workflow Bertingkat, Brand Lock, Kill Switch, Audit Log, MFA, Cloudflare WAF |
| **Total Biaya** | **Rp23.400.000** |
| DP 30% (Awal Fase) | Rp7.020.000 |
| Pelunasan 70% (Setelah UAT) | Rp16.380.000 |

### Fase 3: Optimasi & Validasi
| | |
|---|---|
| Durasi | 3–4 Minggu |
| Deliverables | SEO Lokal (22 Cabang), GEO Optimization, Dokumentasi Teknis, Video Tutorial & Technical Support melalui Email atau Phone/WhatsApp, Compliance Report TAM |
| **Total Biaya** | **Rp16.200.000** |
| DP 30% (Awal Fase) | Rp4.860.000 |
| Pelunasan 70% (Setelah UAT) | Rp11.340.000 |

> [!NOTE]
> *Pengujian keamanan (Penetration Testing)* tidak termasuk dalam quotation ini dan akan ditangani secara mandiri oleh tim internal Klien (Nasmoco).

---

## Ringkasan Total Biaya Pengembangan

| Komponen | Nilai |
|---|---|
| Fase 0 — Discovery & Desain | Rp4.500.000 |
| Fase 1 — Inti / MVP | Rp27.000.000 |
| Fase 2 — Governance & Hardening | Rp23.400.000 |
| Fase 3 — Optimasi & Validasi | Rp16.200.000 |
| **TOTAL PENGEMBANGAN** | **Rp71.100.000** |
| | |
| Total Uang Muka / DP (30%) | Rp21.330.000 |
| Total Pelunasan (70%) | Rp49.770.000 |
| **Total Estimasi Waktu** | **18 Minggu** |

---

## Biaya Pemeliharaan (Maintenance & Support)

Berlaku mulai setelah **Go-Live MVP (Fase 1)** secara pro-rata.

| Skenario | Bulanan | Tahunan *(Hemat 1 Bulan)* | Cakupan |
|---|---|---|---|
| **Skenario 1:** Hosting & WAF dikelola Winamus | Rp3.600.000 | Rp39.600.000 | Support 8 jam/bulan + Hosting ISO27001 + WAF |
| **Skenario 2:** Hosting & WAF dikelola Nasmoco | Rp1.800.000 | Rp19.800.000 | Support 8 jam/bulan + Pemantauan aplikasi |

---

## Syarat & Ketentuan Utama

1.  **Termin Pembayaran:** DP 30% di awal setiap fase; Pelunasan 70% setelah UAT & BAST ditandatangani. Tenggat pembayaran: **14 hari kalender** sejak invoice diterima.
2.  **Garansi Bug:** 30 hari setelah Go-Live di setiap fase untuk perbaikan bug yang timbul dari pengerjaan Vendor.
3.  **Fleksibilitas Scope:** Rincian biaya ini merupakan estimasi awal. Re-evaluasi final dilakukan setelah Fase 0 (SRS & Figma) selesai dan dituangkan dalam Adendum Kontrak.
4.  **Hak Kekayaan Intelektual:** Beralih ke Klien setelah pelunasan per fase. Desain dan source code tidak boleh digunakan pihak lain tanpa pelunasan penuh.
5.  **Ketergantungan Timeline:** Durasi pengerjaan dapat diperpanjang secara *day-for-day* jika terjadi keterlambatan dari sisi Klien (aset, API, keputusan UAT, atau pembayaran DP).
6.  **Komitmen Paket:** Seluruh fase (0–3) merupakan satu kesatuan komitmen proyek. Pembatalan sepihak sebelum proyek selesai dikenakan *Termination Fee* 15% dari sisa nilai fase yang belum berjalan.

---

## Lampiran: Metodologi & Jaminan Kualitas Pengembangan (Hybrid Agile)

Untuk memberikan kepastian investasi (*Fixed Budget*) dan ketepatan waktu peluncuran (*Fixed Timeline* 18 Minggu) bagi Nasmoco, namun tetap menjaga kelenturan pengembangan fitur, PT Winandi Multi Solusi menerapkan pendekatan **Hybrid Agile (Water-Scrum-Fall)**. 

Di balik setiap Fase Komersial yang disepakati, tim kami menjalankan siklus rekayasa perangkat lunak standar industri (IEEE/TOGAF) yang terperinci sebagai berikut:

### 1. Pemetaan Fase Komersial ke SOP Pengembangan Profesional
*   **Fase 0: Discovery & Desain** *(SOP Fase 1–3)*
    *   *Aktivitas:* Elicitation (SRS/BRD), analisis proses bisnis AS-IS & TO-BE, penyusunan WBS, dan pembuatan *Interactive Prototype* serta *Design System* (Figma) untuk validasi UI/UX awal.
*   **Fase 1: Pengembangan Inti & Integrasi** *(SOP Fase 4–12)*
    *   *Aktivitas:* Pembuatan arsitektur sistem (HLD/LLD), skema database (ERD), setup CI/CD pipeline otomatis, coding core engine, unit testing (coverage target ≥80%), deployment ke server Staging, pengujian UAT, hingga *Hypercare* 48 jam pasca Go-Live.
*   **Fase 2: Alur Persetujuan & Keamanan** *(SOP Fase 5, 7–12)*
    *   *Aktivitas:* Desain keamanan (data encryption, MFA, perlindungan OWASP Top 10), coding persetujuan berjenjang & brand lock, setup Cloudflare WAF, dan verifikasi integrasi.
*   **Fase 3: Optimasi & Validasi** *(SOP Fase 9, 12–14)*
    *   *Aktivitas:* Pengetesan beban (*Stress & Load Testing*), audit SEO lokal & berbasis AI (GEO), dokumentasi teknis akhir, pembuatan video tutorial, penyediaan bantuan teknis (Technical Support via Email/WA), dan penyusunan *Compliance Report* standar TAM.

### 2. Jaminan Kelenturan (Agile Flexibility)
*   **Sprint Berkala (Feedback Loop):** Pengembangan di setiap fase dibagi menjadi siklus kerja (sprint) 2 mingguan. Klien akan dilibatkan dalam demo berkala untuk melihat progress nyata dan memberikan masukan awal.
*   **Mekanisme Tukar Tambah Fitur (*Scope Trade-off*):** Jika di tengah jalan Klien membutuhkan perubahan atau penambahan fitur baru, hal tersebut dapat diakomodasi dengan cara **menukar** fitur lain yang setara dalam hal bobot teknis (*story points*) pada fase berjalan, tanpa mengubah nilai kontrak dasar dan timeline.

---

## Informasi Penagihan

| | |
|---|---|
| **Nama Perusahaan** | PT Winandi Multi Solusi |
| **NPWP** | 1000000009851947 |
| **Bank** | ----- |
| **No. Rekening** | ----- |
| **Atas Nama** | PT Winandi Multi Solusi |

> [!IMPORTANT]
> Untuk efisiensi perpajakan, Vendor akan melampirkan **Surat Keterangan PP 55/2022** pada setiap invoice. Mohon pemotongan PPh disesuaikan menjadi **tarif 0,5%** (bukan 2% PPh 23 standar).

---

*Quotation ini berlaku hingga **15 Agustus 2026**. Untuk konfirmasi atau negosiasi lebih lanjut, hubungi: Aris Winandi — PT Winandi Multi Solusi.*
