# PROPOSAL TEKNIS
## Pengembangan Platform Website Terpusat Nasmoco
### Revisi 1 — Juli 2026

---

| | |
|---|---|
| **Pengaju (Vendor)** | PT Winandi Multi Solusi (Winamus) |
| **Penerima (Klien)** | PT New Ratna Motor (Nasmoco Group) |
| **Tujuan Dokumen** | Penjelasan Arsitektur Sistem, Kepatuhan (Compliance), dan Metodologi Kerja |

---

## 1. Latar Belakang & Urgensi Proyek

### A. Kepatuhan Regulasi (Compliance TAM)
*   **SOP Digital Asset TAM Juni 2025:** Toyota-Astra Motor (TAM) mewajibkan seluruh dealer resmi memenuhi standar aset digital sebelum **Juni 2026**.
*   **Status Audit Nasmoco (Gap Analysis):**
    *   *Sesuai (1 Aspek):* Domain utama (`nasmoco.co.id`).
    *   *Sesuai Sebagian / Partial (1 Aspek):* Konten digital & logo branding.
    *   *Belum Sesuai / Gap (6 Aspek):* Struktur website cabang, website wiraniaga (sales), keamanan MFA, infrastruktur cloud/hosting, monitoring lifecycle asset, dan SOP tata kelola internal.

### B. Tantangan Operasional
1.  **Konsistensi Brand:** Portal cabang dan wiraniaga dikelola mandiri dengan tampilan tidak seragam.
2.  **Efisiensi Update:** Pembaruan harga OTR mobil masih manual per cabang/sales, rawan kesalahan input.
3.  **Kebocoran Leads:** Tidak adanya atribusi terstandarisasi untuk mengarahkan pesan langsung ke wiraniaga yang tepat.

---

## 2. Arsitektur Solusi (Multi-Tenant CMS)

Winamus merancang platform dengan **Hierarki Tiga Tingkat** terintegrasi:

```
[Level 1: Homepage Utama (nasmoco.co.id)]
       │
       ├──> [Level 2: Halaman Cabang (nasmoco.co.id/cabang)]
               │
               └──> [Level 3: Halaman Sales (nasmoco.co.id/cabang/nama-sales)]
```

*   **Level 1 (Homepage Utama):** Pintu gerbang utama, katalog model lengkap, harga OTR nasional, dan program promo nasional.
*   **Level 2 (Halaman Cabang):** Informasi spesifik cabang, promo lokal, dan harga OTR wilayah yang **sinkron otomatis** dari sistem pusat.
*   **Level 3 (Halaman Sales):** Landing page personal bagi wiraniaga dengan standarisasi brand (foto, kontak, dan link WhatsApp teratribusi aman).

### Fitur Kunci:
*   **Single Source of Truth:** Perubahan harga OTR cukup dilakukan sekali di dashboard pusat, langsung terupdate ke seluruh cabang dan halaman sales.
*   **Anti-Hijack Lead:** Parameter pelacakan (*tracking*) WhatsApp sales dikunci di sisi server untuk mencegah manipulasi URL oleh pihak ketiga.

---

## 3. Integrasi & Keamanan Sistem

*   **Integrasi CRM:** leads data pelanggan dikirim via webhook terenkripsi ke CRM internal Nasmoco.
*   **Integrasi WhatsApp Business API (WABA):** Sinkronisasi chat menggunakan API resmi penyedia WABA eksisting Nasmoco.
*   **PostgreSQL Database:** Penyimpanan data terstruktur berkinerja tinggi.
*   **Hardening Keamanan:** Wajib Multi-Factor Authentication (MFA) untuk admin, enkripsi data sensitif (data *at-rest* & *in-transit*), dan implementasi Cloudflare WAF.

---

## 4. Metodologi Pengembangan (Hybrid Agile)

Untuk memberikan kepastian biaya (*Fixed Budget*) dan waktu (*Fixed Timeline* 18 Minggu) namun tetap lentur terhadap perubahan fitur, Winamus menggunakan pendekatan **Hybrid Agile (Water-Scrum-Fall)**:

1. **Sprint Berkala (Feedback Loop):** Pengembangan dibagi menjadi siklus kerja (sprint) 2 mingguan dengan demo berkala agar Klien memantau kemajuan nyata.
2. **Mekanisme Tukar Tambah Fitur (*Scope Trade-off*):** Fitur baru di tengah proyek dapat diakomodasi dengan cara **menukar** fitur lain yang memiliki bobot teknis (*story points*) setara, menjaga timeline & anggaran tetap stabil.

---

## 5. Standar Rekayasa & Arsitektur IT (IEEE & TOGAF)

Winamus menerapkan kedisiplinan rekayasa perangkat lunak standar industri guna menjamin keandalan sistem yang dikirim. Siklus hidup pengembangan produk ini diselaraskan dengan standar **IEEE 12207** (Software Life Cycle) dan kerangka arsitektur **TOGAF ADM** yang dipetakan sebagai berikut:

### A. Siklus Pengembangan & Jaminan Kualitas (IEEE 12207)
Setiap fase komersial didukung oleh sub-proses teknis yang terukur secara ketat *(Detail checklist lengkap dilampirkan pada dokumen terpisah: **Nasmoco-SOP-Software-Development-Checklist.md**)*:

*   **Fase 0: Discovery & Desain** (Mengaktifkan SOP Fase 1–3)
    *   *Requirement Elicitation:* Pemetaan kebutuhan fungsional & non-fungsional untuk menghasilkan dokumen **SRS (IEEE 830)**.
    *   *Visual Engineering:* Pembuatan *interactive prototype* dan *Design System* terpadu (Figma) guna meminimalkan ketidaksesuaian ekspektasi UI/UX.
*   **Fase 1: Pengembangan Inti & Integrasi** (Mengaktifkan SOP Fase 4–8, 10–12)
    *   *System Design:* Penyusunan arsitektur sistem (**HLD & LLD - IEEE 1016**) dan skema database (ERD).
    *   *Quality Control:* Penerapan *Unit Testing* otomatis dengan target *code coverage* 80%, standardisasi kode, serta *automated code review* via CI/CD.
    *   *Deployment:* Setup staging server (identik produksi), pengujian fungsional terarah menggunakan panduan skenario *UAT Checklist*, serah terima melalui **BAST**, dan *Hypercare* pemantauan ketat 48 jam pasca Go-Live.
*   **Fase 2: Alur Persetujuan & Keamanan** (Mengaktifkan SOP Fase 5, 7–8, 10)
    *   *Security Hardening:* Implementasi enkripsi data (*at-rest* & *in-transit*), tokenisasi otentikasi (MFA), mitigasi celah keamanan OWASP Top 10, dan integrasi Cloudflare WAF.
    *   *Governance Logic:* Rekayasa *Approval Workflow* multi-level dan perlindungan merek (*Brand Lock* & *Kill Switch*).
*   **Fase 3: Optimasi & Validasi** (Mengaktifkan SOP Fase 9, 12–14)
    *   *Performance Optimization:* Pelaksanaan pengujian beban (*load & stress testing*) untuk mengukur stabilitas aplikasi saat puncak trafik.
    *   *SEO & GEO Auditing:* Audit performa SEO lokal di 22 cabang dan validasi kepatuhan (*compliance*) digital asset standar TAM.
    *   *Technical Handover:* Penyerahan dokumentasi teknis, video panduan admin, serta laporan kepatuhan final.

### B. Keselarasan Arsitektur Enterprise (TOGAF ADM)
Penerapan kerangka kerja TOGAF ADM menjamin sistem baru terintegrasi secara strategis dengan infrastruktur internal Nasmoco:
*   **Business & Data Alignment:** Keselarasan alur prospek (*leads*) dari landing page sales langsung teratribusi ke CRM internal Nasmoco secara *real-time* via webhook terenkripsi.
*   **Technology Architecture:** Standardisasi lingkungan *hosting* (ISO 27001) dan konfigurasi Cloudflare WAF demi menjaga keandalan operasional perusahaan.
*   **Governance & Change Management:** Pengawasan kualitas (Governance) saat fase transisi migrasi data dari sistem lama ke platform baru tanpa mengganggu operasional dealer yang sedang berjalan.

---

## 6. Tata Kelola Pemeliharaan: Skema Self-Hosted (Skenario 2)

Apabila Klien memilih **Skenario 2** (Infrastruktur *Cloud Instance* & WAF dikelola secara mandiri oleh tim IT internal Nasmoco), ketentuan tata kelola dan batasan tanggung jawab disepakati sebagai berikut:

### A. Skema Biaya & Finansial
*   **Biaya Jasa Dukungan Winamus:** Rp1.800.000 / bulan (mencakup dukungan teknis aplikasi maksimal 8 jam/bulan dan pemantauan performa aplikasi).
*   **Biaya Infrastruktur Langsung:** Klien membayar langsung biaya operasional bulanan (*pay-as-you-go*) untuk *Cloud Instance*, penyimpanan basis data (PostgreSQL), dan lisensi WAF kepada masing-masing penyedia layanan (*cloud provider*) yang digunakan.

### B. Pembagian Tanggung Jawab (Siapa Melakukan Apa?)

| Aspek | Tanggung Jawab Klien (IT Nasmoco) | Tanggung Jawab Vendor (Winamus) |
|---|---|---|
| **Infrastruktur & OS** | Menyediakan dan memelihara *Cloud Instance* (Min. 2 vCPU, 4GB RAM, 40GB SSD, OS Ubuntu Server 22.04 LTS). | Memberikan rekomendasi teknis spesifikasi server minimum. |
| **Basis Data** | Mengelola ketersediaan, pemeliharaan, dan pencadangan otomatis (*backup*) harian PostgreSQL. | Merancang skema tabel data dan mengoptimalkan kueri (*database query*). |
| **Keamanan & SSL** | Konfigurasi port, pengaturan grup keamanan (*security groups*), konfigurasi SSL/domain, dan lisensi/aturan Cloudflare WAF. | Enkripsi data di level aplikasi dan kepatuhan kode terhadap standar keamanan OWASP Top 10. |
| **Uptime Server** | Memantau dan bertanggung jawab atas kelancaran koneksi fisik server (penanganan server *crash*, restart, *disk space* penuh, dll). | Menjamin performa aplikasi berjalan normal sepanjang server dalam kondisi stabil. |
| **Deployment** | Menyediakan jalur akses pengiriman kode yang aman (SSH, VPN, atau CI/CD credentials). | Melakukan rilis pembaruan kode (*code updates*) dan perbaikan *bug* (*hotfix*) melalui jalur akses tersebut. |
| **Jasa Support** | Menguji dan memvalidasi perbaikan aplikasi. | Menyediakan kuota bantuan teknis aplikasi maksimal 8 jam/bulan. |

### C. Batasan Garansi & Pengecualian SLA
1.  **Pengecualian SLA Downtime:** Jaminan respon cepat (SLA) untuk kondisi kritis ($\le$ 2 jam) oleh Winamus hanya berlaku jika terjadi kesalahan pada tingkat kode aplikasi (*application-level bugs*). Jika sistem tidak dapat diakses disebabkan oleh kegagalan server, gangguan jaringan, atau kesalahan konfigurasi firewall (WAF) oleh pihak Klien, hal tersebut dikecualikan dari jaminan SLA Winamus.
2.  **Batasan Garansi Performa:** Winamus dibebaskan dari tanggung jawab atas lambatnya respons sistem apabila spesifikasi infrastruktur server yang disediakan oleh Nasmoco berada di bawah standar minimum rekomendasi atau mengalami *overload* sumber daya di tingkat OS.

---

## 7. Dukungan Operasional & SLA (Service Level Agreement)

Dukungan pasca-peluncuran dikategorikan berdasarkan tingkat kekritisan untuk menjaga operasional Klien:

*   **Prioritas Kritis (Sistem Down / Lead Gagal):** Respon 2 jam, Resolusi  24 jam (berlaku untuk *application bug*, tidak termasuk server down pada Skenario 2).
*   **Prioritas Tinggi (Fitur Utama Error):** Respon  8 jam kerja, Resolusi  3 hari kerja.
*   **Prioritas Menengah (Bug Tampilan / Minor):** Respon  1 hari kerja, Resolusi 5 hari kerja.
