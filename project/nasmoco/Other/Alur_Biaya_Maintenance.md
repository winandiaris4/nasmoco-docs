# Panduan Alur Biaya Pemeliharaan & Dukungan (Maintenance & Support)

Dokumen ini menjelaskan alur operasional, pemicu penagihan (*billing trigger*), serta batasan cakupan kerja untuk layanan **Maintenance & Support** senilai **Rp3.600.000/bulan** (atau **Rp43.200.000/tahun**) yang disediakan oleh **Winamus (PT Winandi Multi Solusi)** untuk Platform Website Terpusat Nasmoco.

---

## 1. Timeline & Pemicu Mulai Penagihan (Trigger)

Biaya pemeliharaan bulanan bersifat operasional (*recurring*) dan baru akan ditagihkan sejak sistem mulai aktif digunakan di server produksi:

```
[ Fase 0 & 1: Pengembangan ] ──> [ Minggu 8: Go-Live MVP ] ──> [ Mulai Siklus Maintenance ]
       (Biaya: Rp 0)                (Infrastruktur Aktif)          (Tagihan: Rp3.600.000/bln)
```

*   **Masa Pengerjaan (Minggu 1 s.d 8):** Tidak ada biaya pemeliharaan yang ditagihkan.
*   **Titik Awal (Go-Live MVP):** Begitu website versi MVP resmi diluncurkan pada Minggu ke-8, server produksi standar ISO27001, database PostgreSQL, dan Cloudflare WAF mulai aktif sepenuhnya. Periode ini menandai dimulainya bulan pertama pemeliharaan.

---

## 2. Siklus & Pilihan Metode Penagihan (Billing Options)

Untuk memberikan fleksibilitas administratif bagi Klien, Vendor menyediakan dua pilihan metode penagihan untuk biaya pemeliharaan:

### A. Metode Penagihan Bulanan (Monthly in Advance)
*   **Prosedur:**
    1.  Vendor menerbitkan **Invoice Maintenance** pada hari pertama setiap periode bulan berjalan (misal: setiap tanggal 1).
    2.  Klien melakukan pelunasan tagihan dalam tenggat waktu pembayaran yang disepakati (misal: 14 hari kalender).
    3.  Layanan pemeliharaan berlanjut secara otomatis untuk bulan berikutnya.

### B. Metode Penagihan Tahunan (Annual in Advance) — *Direkomendasikan*
*   *Insenstif:* Klien mendapatkan potongan harga setara **gratis 1 bulan pemeliharaan** jika melakukan pembayaran 1 tahun penuh di muka.
*   **Prosedur:**
    1.  Vendor menerbitkan **Invoice Maintenance Tahunan** (untuk masa aktif 12 bulan) pada hari pertama setelah Fase 1 Go-Live.
    2.  Klien melakukan pembayaran satu kali di muka untuk masa aktif 1 tahun penuh.
    3.  Penagihan tahun kedua akan diterbitkan kembali pada bulan ke-13.

| Skenario Pengelolaan | Tarif Bulanan | Tarif Tahunan *(Diskon 1 Bulan)* | Total Penghematan Klien |
| :--- | :--- | :--- | :--- |
| **Skenario 1:** Hosting & WAF di Winamus | Rp3.600.000 / bulan | **Rp39.600.000 / tahun** | **Rp3.600.000** (Hemat 9.1%) |
| **Skenario 2:** Hosting & WAF di Nasmoco | Rp1.800.000 / bulan | **Rp19.800.000 / tahun** | **Rp1.800.000** (Hemat 9.1%) |

---

## 3. Opsi Skema Pemeliharaan (Menyesuaikan Kebijakan Anggaran Klien)

Untuk mengakomodasi kebijakan anggaran internal Nasmoco, Vendor menawarkan dua pilihan skema pemeliharaan dengan biaya tetap bulanan yang disesuaikan dengan skenario pengelolaan infrastruktur:

*   **Skenario 1 (Hosting & WAF dikelola Winamus):** **Rp3.600.000/bulan** (atau Rp43.200.000/tahun).
*   **Skenario 2 (Hosting & WAF dikelola mandiri oleh Nasmoco):** **Rp1.800.000/bulan** (atau Rp21.600.000/tahun).

Berikut adalah pilihan skema pengelolaan kuota jam kerja untuk kedua skenario di atas:

### OPSI A: Skema Anggaran Tetap dengan Antrean Prioritas (Flat Rate & Prioritization Queue)
*Direkomendasikan jika Nasmoco memiliki kebijakan anggaran tahunan yang terkunci mutlak (tidak menerima tagihan tambahan di tengah jalan).*

*   **Ketentuan Biaya:** Biaya tetap bulanan sesuai skenario yang dipilih (**Rp3.600.000/bulan** atau **Rp1.800.000/bulan**).
*   **Batasan Kapasitas:** Alokasi waktu kerja Vendor untuk dukungan non-keamanan dibatasi maksimal **8 jam kerja per bulan**.
*   **Alur Penanganan Kelebihan Jam:**
    *   **Metode Utama (Gratis):** Permintaan non-kritis yang melebihi kuota 8 jam akan ditunda secara otomatis dan dimasukkan ke antrean (*backlog*) untuk dikerjakan menggunakan kuota bulan berikutnya.
    *   **Metode Akselerasi (Berbayar):** Jika Klien menghendaki pekerjaan non-kritis tersebut diselesaikan segera pada bulan berjalan tanpa menunggu antrean, kelebihan jam akan dikenakan biaya tambahan sebesar **Rp250.000/jam** (ditagihkan pada invoice bulan berikutnya).
    *   Gangguan berkategori *Kritis* (misalnya server down atau database tidak dapat diakses) tetap diselesaikan seketika tanpa memotong kuota dan tanpa biaya tambahan.

### OPSI B: Skema Kuota Akumulatif (Rollover Hours)
*Menghindari hilangnya kuota jam kerja yang tidak terpakai pada bulan-bulan di mana sistem sangat stabil.*

*   **Ketentuan Biaya:** Biaya tetap bulanan sesuai skenario yang dipilih (**Rp3.600.000/bulan** atau **Rp1.800.000/bulan**).
*   **Sistem Rollover:** Jika kuota 8 jam kerja pada bulan berjalan tidak habis digunakan, sisa jam tersebut akan **diakumulasikan (ditabung) ke bulan berikutnya**, dengan batas akumulasi maksimal sebesar **24 jam**.
*   **Alur Penanganan Kelebihan Jam:**
    *   Jika kuota bulanan (8 jam) beserta sisa tabungan jam (*rollover*) telah habis terpakai, setiap tambahan pekerjaan dukungan yang diminta Klien pada bulan berjalan akan dikenakan tarif tambahan sebesar **Rp250.000/jam**.
    *   *Rumus Perhitungan:* `Biaya Tambahan = (Total Jam Kerja Aktual - (8 Jam + Sisa Tabungan Jam)) x Rp250.000`.
    *   Biaya tambahan ini akan diakumulasikan dan ditagihkan pada invoice bulan berikutnya (*Monthly in Arrears*).
*   **Contoh:** Jika pada Bulan 1 hanya terpakai 2 jam (sisa 6 jam), maka kuota di Bulan 2 menjadi 14 jam (8 jam kuota dasar + 6 jam tabungan). Jika di Bulan 2 Anda bekerja selama 16 jam, maka kelebihan 2 jam akan dikenakan biaya tambahan: `(16 - 14) x Rp250.000 = Rp500.000` pada invoice Bulan 3.

### 3.1 Ketentuan Kuota Jam & Biaya Tambahan pada Metode Tahunan

Jika Klien memilih **Metode Penagihan Tahunan (Annual in Advance)**, maka untuk mencegah munculnya invoice-invoice kecil di tengah tahun yang dapat mengganggu administrasi keuangan Klien, aturan kuota jam disesuaikan sebagai berikut:

#### A. Konversi ke Kumpulan Jam Tahunan (Annual Pool of Hours)
*   Kuota jam kerja tidak lagi dibatasi kaku sebesar 8 jam/bulan, melainkan dikonversi menjadi satu kumpulan waktu sebesar **96 Jam per Tahun** (8 jam x 12 bulan).
*   Klien dapat menggunakan kuota 96 jam ini secara fleksibel kapan saja sepanjang tahun berjalan (misalnya: menggunakan 15 jam di bulan pertama untuk penyesuaian intensif, dan hanya 1 jam di bulan berikutnya saat sistem stabil).

#### B. Rekonsiliasi Kelebihan Jam di Akhir Tahun (Annual Reconciliation)
*   Jika total akumulasi penggunaan jam kerja sepanjang tahun melebihi **96 jam**, kelebihan jam tersebut tetap dihitung dengan tarif **Rp250.000 / jam**.
*   **Metode Penagihan:** Vendor **tidak akan menerbitkan invoice bulanan** untuk kelebihan jam tersebut. Seluruh kelebihan jam akan dicatat dan ditagihkan **sekaligus di akhir tahun** (pada bulan ke-12) bersamaan dengan invoice perpanjangan pemeliharaan tahun berikutnya.
*   *Laporan Rutin:* Vendor wajib mengirimkan **Laporan Pemakaian Jam Kerja (Timesheet Report)** bulanan via email sebagai transparansi sisa kuota jam tahunan yang dimiliki Klien.

---

## 4. Batasan Penggunaan Wajar (Fair Use Policy)

Untuk kedua opsi di atas, biaya pemeliharaan rutin bulanan **tidak mencakup** pekerjaan kategori berikut (yang harus diajukan melalui mekanisme *Change Request* terpisah):
1.  **Pengembangan Fitur Baru:** Penambahan modul atau fungsi baru yang tidak ada dalam dokumen spesifikasi Fase 1-3 (misalnya: menambahkan kalkulator simulasi kredit baru atau modul integrasi payment gateway baru).
2.  **Redesain Layout Besar:** Perubahan struktur visual fungsional pada website secara menyeluruh di luar template *page builder* yang sudah disepakati.
3.  **Integrasi Pihak Ketiga Baru:** Menyambungkan sistem website ke API eksternal baru di luar sistem CRM dan WhatsApp WABA yang sudah disepakati di awal.

### 4.1 Skema Biaya & Prosedur Pekerjaan Tambahan (Change Request)

Jika Nasmoco mengajukan permintaan pekerjaan yang masuk dalam batasan *Fair Use Policy* di atas, maka pengerjaan dan pembiayaan akan diatur dengan skema berikut:

#### A. Pilihan Skema Biaya
Vendor menawarkan dua metode perhitungan biaya untuk pekerjaan tambahan:
1.  **Skema Paket Tetap (Fixed Price):**
    *   Vendor menganalisis kebutuhan fitur dan memberikan satu harga bulat (*lump sum*) yang sudah mencakup seluruh proses dari desain hingga go-live.
    *   *Kelebihan:* Nasmoco mendapatkan kepastian anggaran tanpa risiko pembengkakan biaya.
2.  **Skema Tarif Jam Kerja (Time & Material):**
    *   Biaya dihitung berdasarkan estimasi jam kerja yang dibutuhkan dikalikan dengan **Tarif Profesional Jasa Tambahan** sebesar **Rp200.000 / jam**.
    *   *Rumus:* `Biaya = Estimasi Jam Kerja x Rp200.000`.
    *   *Contoh:* Pengembangan fitur "Kalkulator Simulasi Kredit" diestimasikan membutuhkan waktu 20 jam kerja. Maka biayanya adalah `20 jam x Rp200.000 = Rp4.000.000`.

#### B. Prosedur Administrasi Change Request (Alur Kerja)
Proses pengerjaan fitur tambahan wajib melewati 5 tahapan formal berikut untuk menjaga transparansi:
1.  **Pengajuan Kebutuhan (Request):** Nasmoco mengirimkan deskripsi kebutuhan fitur baru secara tertulis kepada Vendor.
2.  **Proposal Teknis & Biaya (Quotation):** Vendor mengirimkan dokumen proposal *Change Request* yang berisi estimasi waktu pengerjaan, skema biaya yang dipilih (Fixed Price atau Tarif Jam), serta dampak teknis terhadap sistem existing.
3.  **Persetujuan Kerja (Approval):** Nasmoco menerbitkan *Purchase Order* (PO) atau Surat Perintah Kerja (SPK) Tambahan sebagai dasar hukum pengerjaan dan pembayaran.
4.  **Pengerjaan & UAT:** Vendor melakukan pengembangan fitur baru pada server *staging*, diikuti dengan pengujian bersama (*User Acceptance Test*) oleh tim Nasmoco.
5.  **Penagihan (Invoicing):** Setelah fitur dinyatakan lolos UAT dan dirilis ke server produksi, Vendor mengirimkan invoice penagihan (termin pembayaran dapat disepakati di awal, misalnya 100% setelah UAT atau DP 50% / Pelunasan 50% untuk nilai di atas Rp10.000.000).

---

## 5. Perbedaan Garansi (*Warranty*) vs Pemeliharaan (*Maintenance*)

*   **Masa Garansi (30 Hari Pasca Go-Live per Fase):** 
    *   Merupakan jaminan bahwa fitur yang baru dirilis bebas dari cacat bawaan (*development bugs*). 
    *   Perbaikan terhadap bug bawaan dari fase tersebut dilakukan secara **gratis** dan **tidak memotong** kuota jam pemeliharaan bulanan.
*   **Layanan Maintenance (Berjalan terus setiap bulan):**
    *   Mencakup biaya sewa infrastruktur fisik pihak ketiga (*hosting* awan, penyimpanan database, proteksi Cloudflare).
    *   Mencakup dukungan operasional harian untuk membantu admin klien, melakukan pemulihan data jika terjadi kesalahan admin (*human error*), serta penyesuaian minor di luar cacat program awal.
