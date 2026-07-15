# Klarifikasi Skema Fase Pengembangan & Pembayaran — Platform Website Terpusat Nasmoco

Dokumen ini berisi rincian penjelasan mengenai alokasi biaya, cakupan pekerjaan (*deliverables*) per fase, serta skema pembayaran dan pemeliharaan untuk proyek pengembangan Platform Website Terpusat Nasmoco (PT New Ratna Motor).

---

## 1. Rincian Biaya & Termin Pembayaran per Fase

Total biaya pengembangan (Fase 0–3) adalah **Rp71.100.000** (tidak termasuk pengujian keamanan *penetration testing* yang didelegasikan ke pihak internal Klien). Rincian alokasi biaya, durasi, dan cakupan pekerjaan per fase adalah sebagai berikut:

### 1. **Fase 0: Discovery & Desain**
*   **Durasi:** 1–2 Minggu
*   **Total Biaya:** **Rp4.500.000**
    *   *Uang Muka (DP 30%):* Rp1.350.000 (Dibayar di awal fase)
    *   *Pelunasan (70%):* Rp3.150.000 (Setelah UAT & BAST disetujui)
*   **Cakupan Pekerjaan (Deliverables):**
    *   Finalisasi dokumen kebutuhan teknis (*System Requirement Specification - SRS*)
    *   Desain UI/UX fungsional (Figma) untuk seluruh halaman utama
    *   Perancangan arsitektur data & alur integrasi sistem

### 2. **Fase 1: Inti / MVP (Minimum Viable Product)**
*   **Durasi:** 4–6 Minggu *(Target Go-Live MVP pada Minggu ke-8)*
*   **Total Biaya:** **Rp27.000.000**
    *   *Uang Muka (DP 30%):* Rp8.100.000 (Dibayar di awal fase)
    *   *Pelunasan (70%):* Rp18.900.000 (Setelah UAT & BAST disetujui)
*   **Cakupan Pekerjaan (Deliverables):**
    *   Migrasi database ke PostgreSQL & pembuatan sistem harga terpusat
    *   Modul *Page Builder* & sistem atribusi lead (*Anti-Hijack Sales*)
    *   Integrasi CRM Nasmoco & WhatsApp Business API (WABA)

### 3. **Fase 2: Governance & Hardening**
*   **Durasi:** 4–6 Minggu
*   **Total Biaya:** **Rp23.400.000**
    *   *Uang Muka (DP 30%):* Rp7.020.000 (Dibayar di awal fase)
    *   *Pelunasan (70%):* Rp16.380.000 (Setelah UAT & BAST disetujui)
*   **Cakupan Pekerjaan (Deliverables):**
    *   *Approval workflow* bertingkat (Sales $\rightarrow$ Supervisor $\rightarrow$ Head Office)
    *   Fitur *Brand Lock* & sistem pemeriksaan konten otomatis
    *   Fitur keamanan *Kill Switch* & pembuatan *Audit Log* aktivitas
    *   Implementasi Multi-Factor Authentication (MFA) & Cloudflare WAF

### 4. **Fase 3: Optimasi & Validasi**
*   **Durasi:** 3–4 Minggu
*   **Total Biaya:** **Rp16.200.000**
    *   *Uang Muka (DP 30%):* Rp4.860.000 (Dibayar di awal fase)
    *   *Pelunasan (70%):* Rp11.340.000 (Setelah UAT & BAST disetujui)
*   **Cakupan Pekerjaan (Deliverables):**
    *   Optimasi SEO Lokal untuk 22 Cabang Nasmoco
    *   Optimasi SEO berbasis pencarian kecerdasan buatan (*GEO - Generative Engine Optimization*)
    *   Penyusunan dokumentasi teknis & pembuatan video tutorial serta penyediaan bantuan teknis (technical support) melalui email atau telepon/WhatsApp
    *   Penyusunan Laporan Kepatuhan (*Compliance Report*) untuk standar TAM

---

**RINGKASAN TOTAL BIAYA PENGEMBANGAN (Fase 0 - 3):** **Rp71.100.000**  
*   **Total Uang Muka (DP 30%):** Rp21.330.000  
*   **Total Pelunasan (70%):** Rp49.770.000  
*   **Total Estimasi Waktu:** 18 Minggu  

---

## 2. Skema Biaya Pemeliharaan (Maintenance & Support)

Biaya pemeliharaan disesuaikan dengan skenario infrastruktur dan metode pembayaran yang dipilih oleh Nasmoco:

### A. Rincian Biaya Berdasarkan Skenario & Metode Pembayaran

| Skenario Pengelolaan                               | Metode Bulanan      | Metode Tahunan *(Diskon 1 Bulan)*                  | Cakupan Utama                                                                                                                   |
| :------------------------------------------------- | :------------------ | :------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| **Skenario 1:** <br>Hosting & WAF dikelola Winamus | Rp3.600.000 / bulan | **Rp39.600.000 / tahun** <br>*(Hemat Rp3.600.000)* | • Jasa Support Cap (maks 8 jam/bulan)<br>• Sewa Server Cloud ISO27001 & PostgreSQL<br>• Cloudflare WAF & Backup harian otomatis |
| **Skenario 2:** <br>Hosting & WAF dikelola Nasmoco | Rp1.800.000 / bulan | **Rp19.800.000 / tahun** <br>*(Hemat Rp1.800.000)* | • Jasa Support Cap (maks 8 jam/bulan)<br>• Pemantauan performa aplikasi (*app level*)                                           |

> [!IMPORTANT]
> **Ketentuan Mulai Berlaku:** Biaya pemeliharaan ini **tidak ditagihkan di muka proyek**, melainkan baru mulai berjalan secara pro-rata **setelah MVP Fase 1 Go-Live** (Minggu ke-8), ketika sistem sudah mulai digunakan secara operasional.

### B. Breakdown Komponen Biaya Bulanan (Skenario 1)
Jika Nasmoco memilih Skenario 1 dengan pembayaran bulanan, rincian alokasinya adalah:
1. **Support & Bugfix (Rp1.800.000):** Dukungan teknis harian, pemantauan performa, perbaikan *bug*, dan alokasi waktu untuk permintaan bantuan minor sesuai dengan kesepakatan SLA (target respons cepat hingga maks 2 jam untuk kasus kritis).
2. **Hosting Standar ISO27001 (Rp1.500.000):** Biaya sewa server *cloud* berstandar keamanan tinggi (ISO27001), penyimpanan basis data, CDN untuk kecepatan akses gambar/aset, dan sistem *backup* otomatis harian.
3. **Keamanan WAF / Cloudflare (Rp300.000):** Biaya perlindungan lalu lintas data dari serangan siber (DDoS, spam *form*, dll.) menggunakan Web Application Firewall.

---

## 3. Nilai Strategis Skema Fase bagi Nasmoco

1. **Mitigasi Risiko Keuangan:** Nasmoco tidak perlu membayar investasi penuh di depan. Porsi terbesar pembayaran (70%) di setiap fase dikunci oleh mekanisme **UAT (User Acceptance Test)**. Jika hasil kerja di fase tersebut belum sesuai kesepakatan, pelunasan tidak dilakukan.
2. **Kecepatan Value (Time-to-Value):** Dibandingkan metode *waterfall* tradisional di mana klien harus menunggu 18 minggu untuk melihat hasil, dengan skema ini Nasmoco sudah memiliki **website operasional yang fungsional (MVP) di Minggu ke-8**.
3. **Fleksibilitas Anggaran:** Jika di tengah jalan terdapat penyesuaian strategi dari manajemen Nasmoco, ruang lingkup di Fase 2 atau Fase 3 (misalnya skala *pen testing* atau cakupan GEO) dapat disesuaikan tanpa mengganggu pondasi sistem yang sudah dibangun di Fase 1.

---

## 4. Ketentuan Komitmen Paket & Hak Kekayaan Intelektual (Intellectual Property)

Untuk melindungi investasi waktu, analisis, dan perencanaan teknis yang telah dilakukan oleh Vendor, ketentuan komitmen berikut diberlakukan dalam kontrak kerja sama:

### A. Satu Kesatuan Komitmen Proyek (Single Package Commitment)
*   Keseluruhan nilai proyek sebesar **Rp71.100.000** (Fase 0 s.d Fase 3) ditawarkan sebagai **satu kesatuan paket**.
*   Harga Fase 0 (Discovery & Desain) senilai **Rp4.500.000** merupakan harga subsidi khusus (*loss leader*) yang diberikan karena Klien berkomitmen untuk melaksanakan seluruh rangkaian fase hingga selesai.

### B. Batasan Hak Kekayaan Intelektual (Intellectual Property Rights)
*   Hak kepemilikan intelektual atas seluruh hasil kerja (Desain UI/UX Figma, Dokumen Spesifikasi SRS, Kode Sumber/Source Code, dan Arsitektur Database) baru akan **dialihkan secara penuh kepada Klien setelah Klien melunasi pembayaran pada fase terkait**.
*   Apabila Klien menghentikan proyek secara sepihak setelah **Fase 0** selesai:
    *   Seluruh hak kekayaan intelektual atas desain visual (Figma) dan dokumen analisis (SRS) tetap menjadi milik **Vendor**.
    *   Klien **dilarang keras** menggunakan hasil desain dan dokumen analisis tersebut untuk dikerjakan oleh pihak ketiga (internal IT maupun vendor lain).
    *   Jika Klien ingin menggunakan hasil desain tersebut untuk didevelop oleh pihak lain, Klien wajib membayar **Biaya Pelepasan Hak Cipta (*Buyout Fee*) sebesar Rp15.000.000**.

### C. Kompensasi Pembatalan Sepihak (Termination Fee)
*   Apabila Klien memutuskan untuk menghentikan kerja sama secara sepihak pada pertengahan proyek (setelah Fase 1 atau Fase 2 berjalan) bukan disebabkan karena kelalaian teknis (*default*) dari Vendor, maka:
    1.  Klien wajib melunasi seluruh kewajiban pembayaran pada fase yang sedang berjalan.
    2.  Klien dikenakan **Biaya Pembatalan (*Termination Fee*) sebesar 15% dari total nilai fase-fase tersisa yang belum berjalan**, sebagai kompensasi atas alokasi sumber daya (*dedicated resource*) Vendor yang telah diblokir untuk proyek ini.

---

## 5. Klausul Fleksibilitas Ruang Lingkup & Penyesuaian Biaya (Scope & Cost Flexibility)

Mengingat proyek pengembangan ini melibatkan integrasi teknis, penyesuaian alur kerja (*workflow*), dan optimasi sistem yang dinamis di setiap tahapan, kedua belah pihak menyepakati ketentuan fleksibilitas berikut:

### A. Estimasi Awal Kontrak
*   Rincian pekerjaan dan biaya untuk Fase 1, Fase 2, dan Fase 3 yang tercantum dalam dokumen ini adalah **estimasi awal** berdasarkan analisis kebutuhan tingkat tinggi (*high-level requirements*) saat proposal diajukan.

### B. Re-evaluasi dan Finalisasi Pasca-Fase 0
*   Setelah **Fase 0 (Discovery & Desain)** selesai dilaksanakan, dokumen kebutuhan detail (*System Requirement Specification - SRS*) serta desain UI/UX (Figma) disetujui, Vendor dan Klien akan melakukan **tinjauan bersama (re-evaluation)**.
*   Apabila hasil analisis detail pada dokumen SRS menunjukkan adanya kompleksitas teknis tambahan (seperti perubahan spesifikasi integrasi, penambahan kebutuhan keamanan, optimasi performa, atau kustomisasi fitur yang melebihi estimasi awal), maka **ruang lingkup, durasi, dan biaya pada seluruh fase berikutnya (Fase 1, Fase 2, dan/atau Fase 3) akan disesuaikan secara proporsional**.
*   Penyesuaian ini akan dituangkan secara sah melalui **Adendum Kontrak** atau **Formulir Persetujuan Change Request** sebelum pengerjaan Fase 1 dimulai.

### C. Penyesuaian Selama Proses Pengembangan (Agile Scope Adjustment)
*   Ruang lingkup pekerjaan di setiap fase dapat disesuaikan sewaktu-waktu selama proses pengembangan berjalan demi menyesuaikan dengan kebutuhan operasional terbaru Klien atau kendala integrasi teknis di lapangan.
*   Setiap perubahan ruang lingkup yang berdampak pada penambahan waktu kerja atau biaya wajib melalui prosedur *Change Request* formal sebagaimana diatur dalam dokumen pemeliharaan (menggunakan tarif profesional Rp200.000/jam atau harga paket baru yang disepakati).
