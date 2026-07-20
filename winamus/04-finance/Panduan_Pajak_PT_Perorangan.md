# Panduan Aspek Perpajakan PT Perorangan — Proyek Nasmoco

Dokumen ini menjelaskan aspek perpajakan, skema pemotongan pajak, serta panduan administratif untuk **PT Winandi Multi Solusi (Winamus)** yang berstatus sebagai **PT Perorangan (Non-PKP)** dalam transaksi bisnis dengan **PT New Ratna Motor (Nasmoco Group)**.

---

## 1. Status Hukum & Klasifikasi Pajak

*   **Status Wajib Pajak:** **Wajib Pajak Badan (Badan Hukum)**. 
    *   *Keterangan:* Meskipun dimiliki oleh satu orang, PT Perorangan secara hukum setara dengan PT biasa dalam transaksi B2B. Nasmoco akan memotong pajak menggunakan tarif Wajib Pajak Badan, bukan individu.
*   **Status PPN:** **Non-PKP (Pengusaha Kena Pajak)**.
    *   *Keterangan:* Karena omzet tahunan di bawah Rp4,8 Miliar, Winamus tidak memungut PPN 11% kepada Nasmoco dan tidak menerbitkan Faktur Pajak.

---

## 2. Skema Pemotongan Pajak Penghasilan (Withholding Tax)

Nasmoco sebagai pemotong pajak wajib memotong pembayaran jasa sesuai aturan berikut:

### A. Skema PPh Final PP 55/2022 (Sangat Direkomendasikan) — **Tarif 0.5%**
Sebagai PT Perorangan kategori UMKM, Winamus berhak menggunakan tarif PPh Final 0.5% dari nilai bruto invoice.
*   *Syarat:* Wajib melampirkan **Surat Keterangan (Suket) PP 55/PP 23** yang diunduh dari DJP Online.
*   *Masa Berlaku:* Maksimal 3 tahun pajak sejak PT Perorangan didirikan.

### B. Skema PPh Pasal 23 (Tarif Standar Jasa IT) — **Tarif 2.0%**
Jika Winamus tidak melampirkan Suket PP 55 saat penagihan, Nasmoco akan menggunakan tarif standar PPh 23 untuk jasa teknik/manajemen/IT sebesar 2.0%.

---

## 3. Panduan Mendapatkan Suket PP 55 (Tarif 0.5%)

Ikuti langkah berikut untuk mengunduh Surat Keterangan secara online dan instan:

1.  Buka situs resmi [DJP Online](https://djponline.pajak.go.id/).
2.  Login menggunakan **NPWP 15/16 Digit PT Perorangan** Anda dan kata sandi terkait.
3.  Masuk ke menu **Layanan** $\rightarrow$ pilih **KSWP** (Konfirmasi Status Wajib Pajak).
4.  Pada kolom *Keperluan*, pilih jenis dokumen: **Surat Keterangan (Suket) PP 55**.
5.  Isi kode keamanan (Captcha), lalu klik **Submit**.
6.  Sistem DJP akan memvalidasi kepatuhan SPT tahunan Anda. Jika valid, tombol **Cetak Suket** akan aktif.
7.  Unduh dan simpan dokumen tersebut dalam format PDF.

---

## 4. Simulasi Pemotongan Pajak per Termin

Berikut adalah perbandingan uang bersih yang diterima (*net transfer*) antara tarif PPh 23 (2%) dengan PPh Final PP 55 (0.5%):

| Termin Pekerjaan | Nilai Bruto | Potongan PPh 23 (2%) | Net Transfer (PPh 23) | Potongan PPh Final (0.5%) | Net Transfer (PP 55) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Fase 0** (Desain) | Rp4.500.000 | Rp90.000 | **Rp4.410.000** | Rp22.500 | **Rp4.477.500** |
| **Fase 1** (MVP) | Rp27.000.000 | Rp540.000 | **Rp26.460.000** | Rp135.000 | **Rp26.865.000** |
| **Fase 2** (Governance) | Rp23.400.000 | Rp468.000 | **Rp22.932.000** | Rp117.000 | **Rp23.283.000** |
| **Fase 3** (Optimasi) | Rp16.200.000 | Rp324.000 | **Rp15.876.000** | Rp81.000 | **Rp16.119.000** |
| **Maintenance** (Managed) | Rp3.600.000/bln | Rp72.000 | **Rp3.528.000** | Rp18.000 | **Rp3.582.000** |
| **Maintenance** (Self-Host)| Rp1.800.000/bln | Rp36.000 | **Rp1.764.000** | Rp9.000 | **Rp1.791.000** |

> [!NOTE]
> *Pen Testing* tidak tercantum di tabel ini karena ditangani secara internal oleh Nasmoco. Selisih potongan antara PPh 23 (2%) dan PPh Final PP 55 (0.5%) untuk **keseluruhan biaya pengembangan (Rp71.100.000)** mencapai **Rp1.066.500** — ini adalah penghematan nyata yang bisa langsung Anda amankan dengan menyerahkan Suket PP 55 saat invoicing.

---

## 5. Dokumen yang Harus Diserahkan ke Keuangan Nasmoco

Saat melakukan penagihan (*invoicing*) di setiap akhir fase, serahkan dokumen berikut dalam satu berkas:
1.  **Invoice** atas nama PT Winandi Multi Solusi.
2.  **Kuitansi** bermeterai (jika nilai di atas Rp5.000.000).
3.  **Berita Acara Serah Terima (BAST)** / Lembar *UAT Sign-off* yang sudah ditandatangani kedua belah pihak.
4.  **Fotokopi NPWP PT Perorangan** Anda.
5.  **Surat Keterangan PP 55** (untuk mengunci potongan di 0.5%).
6.  **Bukti Rekening Koran/Informasi Rekening Bank** atas nama PT Winandi Multi Solusi.

---

## 6. Pengetahuan Operasional: Metodologi Rekayasa & Pengiriman Proyek (Hybrid Agile)

Bagian ini mendokumentasikan metodologi pengiriman proyek (*Project Delivery Methodology*) yang digunakan oleh Winamus dalam menghadapi tantangan umum B2B: **Klien meminta fleksibilitas (Agile) namun dengan anggaran tetap (*Fixed Price*) dan tenggat waktu ketat (*Fixed Timeline*)**.

### A. Konsep Dasar: Hybrid Agile (Water-Scrum-Fall)
Winamus menggunakan pendekatan gabungan yang menyeimbangkan kepastian komersial dengan kelenturan operasional:
1.  **Macro-Level (Waterfall):** Proyek dikunci dalam fase komersial yang terstruktur (Fase 0 - Fase 3) dengan durasi total 18 minggu dan anggaran Rp71.100.000. Hal ini melindungi Winamus dari risiko *scope creep* tanpa batas akhir, serta memberikan kepastian anggaran bagi klien.
2.  **Micro-Level (Agile/Scrum):** Pengerjaan internal dan interaksi harian dilakukan secara iteratif dalam siklus sprint 2 mingguan. Setiap akhir sprint diadakan demo berkala agar klien bisa memberikan masukan lebih cepat.

### B. Mekanisme Negosiasi Fleksibilitas (*Scope Trade-off*)
Jika klien meminta perubahan atau penambahan fitur di tengah jalan tanpa ingin menaikkan budget, gunakan aturan **Tukar Tambah Fitur (*Feature Swapping*)**:
*   *Aturan:* Fitur baru boleh masuk dengan syarat ada fitur lama dengan bobot teknis (*story points*) yang setara yang dikeluarkan dari scope fase tersebut.
*   *Manfaat:* Klien mendapatkan fleksibilitas tanpa membahayakan margin keuntungan Winamus atau menunda tenggat waktu go-live secara keseluruhan.

### C. Pemetaan 4 Fase Komersial ke 14 Langkah SOP Teknis
Gunakan pemetaan ini untuk meyakinkan tim IT klien/auditor TAM bahwa setiap fase komersial didukung oleh kedisiplinan rekayasa perangkat lunak yang matang:
*   **Fase 0 (Discovery & Desain):** Mengaktifkan **SOP Fase 1** (Discovery & BA), **SOP Fase 2** (Project Planning), dan **SOP Fase 3** (UI/UX Design).
*   **Fase 1 (Pengembangan Inti & Integrasi):** Mengaktifkan **SOP Fase 4** (System Analysis), **SOP Fase 5** (System Design), **SOP Fase 6** (Dev Preparation), **SOP Fase 7-8** (Dev backend/frontend), **SOP Fase 9** (QA), **SOP Fase 10** (Pre-Prod/Staging), **SOP Fase 11** (Production Deployment), dan **SOP Fase 12** (Post-Production/Hypercare).
*   **Fase 2 (Alur Persetujuan & Keamanan):** Mengaktifkan **SOP Fase 5** (Security Design), **SOP Fase 7-8** (Dev Alur & Hardening), **SOP Fase 9** (QA Security Testing), dan **SOP Fase 10-12** (Deployment).
*   **Fase 3 (Optimasi & Validasi):** Mengaktifkan **SOP Fase 9** (Load/Stress Testing), **SOP Fase 10** (Security Scanning), **SOP Fase 12-13** (Documentation, Tutorial, SLA), dan **SOP Fase 14** (BAST Sign-off & Compliance).
