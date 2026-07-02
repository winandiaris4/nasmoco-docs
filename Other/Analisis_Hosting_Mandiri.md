# Analisis Opsi: Hosting & WAF Dikelola Mandiri oleh Nasmoco

Dokumen ini menganalisis skenario di mana **PT New Ratna Motor (Nasmoco Group)** memilih untuk menyediakan dan mengelola infrastruktur *hosting cloud* serta *Web Application Firewall* (WAF) menggunakan akun internal mereka sendiri, dibandingkan menggunakan layanan terkelola (*managed service*) dari **Winamus**.

---

## 1. Perubahan Struktur Biaya Pemeliharaan

Jika opsi ini dipilih, rincian biaya pemeliharaan bulanan disesuaikan sebagai berikut:

*   **Skema Awal (Managed by Winamus):** Rp3.600.000 / bulan (All-in).
*   **Skema Penyesuaian (Self-Hosted by Nasmoco):** **Rp1.800.000 / bulan**.
    *   *Cakupan:* Hanya jasa profesional *Support Cap* (maksimal 8 jam kerja/bulan) dan pemantauan aplikasi (*application monitoring*).
    *   *Biaya Langsung:* Nasmoco membayar tagihan penggunaan server (*pay-as-you-go*) dan Cloudflare WAF secara langsung ke penyedia layanan (*provider*).

---

## 2. Dampak bagi Nasmoco (Klien)

### Keuntungan (Pros):
1.  **Kedaulatan Data (Data Sovereignty):** Data pelanggan dan basis data PostgreSQL berada 100% di bawah kendali infrastruktur Nasmoco. Hal ini sangat mendukung kepatuhan terhadap **UU Perlindungan Data Pribadi (UU PDP)**.
2.  **Kontrol Akses Penuh:** Tim IT Nasmoco memegang kunci utama (*root access*) terhadap server dan keamanan sejak hari pertama, meminimalkan risiko keamanan dari pihak ketiga.
3.  **Konsolidasi Anggaran:** Nasmoco dapat memanfaatkan sisa kapasitas (*resource*) dari server *cloud* yang sudah mereka miliki saat ini tanpa harus menyewa server baru dari nol.

### Konsekuensi & Tanggung Jawab (Cons):
1.  **Tanggung Jawab Uptime & Pemulihan:** Jika terjadi kegagalan sistem pada tingkat infrastruktur (misal: server kehabisan memori, koneksi database terputus, atau server fisik mati), tim IT Nasmoco yang bertanggung jawab menyelesaikannya.
2.  **Beban Kerja Admin IT Internal:** Tim IT Nasmoco harus mengalokasikan waktu untuk melakukan pengaturan awal server (*setup environment*), konfigurasi SSL, pengelolaan akun Cloudflare, serta pembuatan prosedur pencadangan (*backup*) data harian.
3.  **Manajemen Akses Vendor:** IT Nasmoco harus menyiapkan jalur akses yang aman (misal: VPN, kredensial SSH terbatas, atau jalur CI/CD) agar tim Winamus tetap dapat melakukan pembaharuan kode (*deployment*).

---

## 3. Dampak bagi Winamus (Vendor)

### Keuntungan (Pros):
1.  **Risiko Operasional Lebih Rendah:** Winamus tidak bertanggung jawab atas kegagalan infrastruktur. Target *Service Level Agreement* (SLA) untuk respons 2 jam (kondisi kritis) hanya berlaku untuk kesalahan pada tingkat aplikasi (*application-level bugs*), bukan server mati.
2.  **Bebas Risiko Arus Kas:** Tidak perlu menanggung biaya langganan infrastruktur bulanan terlebih dahulu (menghindari risiko selisih kurs mata uang asing untuk biaya sewa server berbasis USD).
3.  **Fokus pada Pengembangan:** Winamus dapat fokus sepenuhnya pada pemeliharaan kualitas kode program dan performa aplikasi tanpa terdistraksi masalah jaringan server.

### Kerugian & Risiko (Cons):
1.  **Penurunan Pendapatan Pasif (Recurring Revenue):** Pendapatan bulanan rutin berkurang sebesar 50% (dari Rp3.600.000 menjadi Rp1.800.000). Margin keuntungan dari selisih biaya sewa server hilang.
2.  **Ketergantungan Proses Deployment:** Kecepatan rilis fitur atau perbaikan bug sangat bergantung pada kesiapan tim IT Nasmoco dalam memberikan akses server. Jika akses dibatasi, proses pengerjaan dapat terhambat.
3.  **Risiko Perselisihan Performa (Kambing Hitam):** Jika website terasa lambat akibat spesifikasi server yang disediakan Nasmoco terlalu rendah (di bawah standar rekomendasi), ada risiko kode program vendor disalahkan. Winamus harus melakukan dokumentasi batas minimum spesifikasi server secara tertulis di awal.

---

## 4. Spesifikasi Minimum Rekomendasi (Jika Self-Hosted)

Untuk menjamin aplikasi berjalan dengan performa optimal dan memenuhi standar TAM, Nasmoco wajib menyediakan infrastruktur dengan spesifikasi minimum sebagai berikut:

*   **Virtual Private Server (VPS) / Cloud Instance:**
    *   *CPU:* Minimal 2 vCPU
    *   *RAM:* Minimal 4 GB
    *   *Storage:* Minimal 40 GB SSD / NVMe
    *   *OS:* Ubuntu Server 22.04 LTS atau setara
*   **Database Service (Managed PostgreSQL):**
    *   PostgreSQL v15 atau di atasnya.
*   **Kepatuhan Infrastruktur:**
    *   Lokasi Server: Indonesia (untuk kepatuhan UU PDP & kecepatan akses lokal).
    *   Sertifikasi Data Center: Minimal ISO 27001 (Kepatuhan SOP TAM).
