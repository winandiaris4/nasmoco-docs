# 🚀 Agency Readiness Checklist: Winamus Business & IT Roadmap
> **Peran:** Konsultan Bisnis & IT  
> **Status Perusahaan:** PT Perorangan Baru (Non-PKP)  
> **Klien Pertama:** Nasmoco Group (Enterprise Level)

Selamat! Mendapatkan klien pertama berskala *enterprise* seperti Nasmoco Group adalah pencapaian luar biasa untuk PT Perorangan yang baru berdiri. Namun, berbisnis dengan korporasi besar membutuhkan kesiapan administratif, operasional, dan infrastruktur IT yang ketat agar tidak terjadi kendala pada saat penagihan atau pelaksanaan proyek.

Dokumen ini memetakan **Kesenjangan (Gap Analysis)** dan langkah-langkah konkret yang harus segera dilengkapi oleh **PT Winandi Multi Solusi (Winamus)**.

---

## 1. ADMINISTRASI & KEUANGAN (Prioritas Kritis)

Keuangan korporasi besar memiliki birokrasi audit yang ketat. Kekurangan di area ini akan menunda pembayaran termin Anda.

*   [ ] **Pembukaan Rekening Bank PT (Corporate Bank Account)**
    *   *Kondisi Sekarang:* Nomor rekening bank di Quotation masih dikosongkan (`----`).
    *   *Risiko:* Pihak Keuangan Nasmoco secara regulasi **tidak boleh/tidak akan mentransfer** pembayaran ke rekening pribadi atas nama Aris Winandi. Dana wajib masuk ke rekening dengan nama yang sama persis dengan kontrak (PT Winandi Multi Solusi).
    *   *Tindakan:* Segera datang ke Bank (BCA/Mandiri/BNI) membawa sertifikat Kemenkumham, NIB, dan NPWP Badan untuk membuat Rekening Giro/Bisnis atas nama PT.
*   [x] **Aktivasi Akun Pajak (NPWP Badan & E-FIN)**
    *   *Kondisi Sekarang:* E-FIN sudah diaktifkan dan akun DJP Online Badan telah siap digunakan untuk mengunduh Surat Keterangan PP 55/2022 (tarif 0,5%).
*   [ ] **Stempel Resmi Perusahaan (Fisik & Digital)**
    *   *Tindakan:* Buat stempel fisik untuk dokumen cetak dan stempel digital (format PNG transparan) untuk dibubuhkan pada dokumen invoice PDF, BAST, dan kuitansi digital yang dihasilkan oleh generator.
*   [ ] **Setup Pembukuan Keuangan & Akuntansi Sederhana**
    *   *Risiko:* PT Perorangan wajib melaporkan laporan keuangan tahunan (neraca dan laba-rugi) ke Kemenkumham serta melaporkan SPT Tahunan Badan.
    *   *Tindakan:* Mulai catat setiap pemasukan proyek dan pengeluaran operasional (sewa server, lisensi, gaji freelancer) sejak hari pertama menggunakan *spreadsheet* terstruktur atau aplikasi akuntansi (seperti Kledo/Accurate/Jurnal).

---

## 2. KREDIBILITAS & BRANDING (Daya Tawar Klien)

Nasmoco perlu diyakinkan bahwa meskipun Winamus adalah PT baru, kapasitas tim di dalamnya setara dengan vendor kawakan.

*   [ ] **Dokumen Company Profile (Profil Perusahaan)**
    *   *Kondisi Sekarang:* Folder `winamus/company profile/` hanya berisi link website kosong.
    *   *Tindakan:* Susun berkas PDF *Company Profile* profesional. 
    *   *Strategi Klien Pertama:* Kemas pengalaman-pengalaman proyek pribadi Anda (sebelum ber-PT) sebagai **"Founder's Track Record / Portofolio Tim Pendiri"** untuk membuktikan keahlian teknis.
*   [x] **Optimalisasi Website Utama (www.winamus.com)**
    *   *Kondisi Sekarang:* Website utama sudah online dengan tampilan minimalis premium serta mencantumkan nomor legalitas legal (NIB & Keputusan Menkumham) di bagian footer.
*   [x] **Email Bisnis Resmi (Enterprise Email)**
    *   *Kondisi Sekarang:* Menggunakan email berdomain bisnis resmi (seperti `hello@winamus.com` atau `aris@winamus.com`) untuk menjamin profesionalisme korespondensi.

---

## 3. INFRASTRUKTUR IT & OPERASIONAL AGENCY (Penyediaan Layanan)

Untuk mengelola proyek Nasmoco dan bersiap menerima proyek-proyek berikutnya secara paralel.

*   [x] **GitHub Organization untuk PT**
    *   *Kondisi Sekarang:* Repositori resmi Winamus telah dibuat untuk mengamankan seluruh kode sumber proyek Nasmoco dan memisahkannya dari akun personal.
*   [ ] **Platform Kolaborasi & Pelacakan Proyek (Client-facing Dashboard)**
    *   *Tindakan:* Sediakan satu tempat kolaborasi terpusat. Untuk Nasmoco, dashboard tracking berbasis Markdown ([`progress.md`](file:///home/dev-02/aris/other/nasmoco-docs/nasmoco-docs/project/nasmoco/progress.md)) sudah sangat bagus. Di masa depan, pertimbangkan menggunakan Jira/Linear yang dibagikan secara terbatas (*guest access*) kepada Klien.
*   [ ] **SOP Pengelolaan Kontributor / Freelancer**
    *   *Risiko:* Jika Anda merekrut tim pengembang tambahan (*freelance/kontrak*), ada risiko kebocoran kode sumber atau penurunan kualitas penulisan kode.
    *   *Tindakan:* Siapkan template **Perjanjian Kerahasiaan (NDA)** dan draf kerja sama *freelancer* yang menyatakan bahwa seluruh Hak Cipta pekerjaan beralih ke PT Winamus sejak awal.
*   [ ] **Standardisasi Keamanan Internal (Credential Management & 2FA)**
    *   *Risiko:* Kehilangan akses akun, serangan malware, atau kebocoran kredensial (API key WABA, CRM, password server staging) dapat merusak kredibilitas Winamus.
    *   *Tindakan:* Wajibkan penggunaan Password Manager terenkripsi (seperti Bitwarden/1Password) untuk membagikan kredensial di internal tim secara aman, serta aktifkan Two-Factor Authentication (2FA) di semua akun krusial (GitHub, Hosting, Cloudflare, dan Email Bisnis).

---

## 4. SKALABILITAS & DOKUMEN MASTER (Ekspansi Bisnis)

Mempersiapkan Winamus untuk memenangkan klien kedua, ketiga, dan seterusnya dengan cepat setelah sukses dengan Nasmoco.

*   [ ] **Standardisasi Template Dokumen Legal & Penjualan**
    *   *Tindakan:* Simpan berkas master yang dapat digunakan kembali untuk klien baru di masa depan, meliputi:
        *   Master Proposal Teknis (Format Markdown/PDF)
        *   Master Quotation (Format Markdown/PDF)
        *   Master Draf Perjanjian Kerja Sama (PKS) Umum
        *   Master Berita Acara Serah Terima (BAST) & UAT Checklist
*   [ ] **Setup Shared Staging Server untuk Portofolio**
    *   *Tindakan:* Sewa satu Cloud Virtual Machine (VPS) khusus sebagai server demo portofolio mandiri milik Winamus. Server ini digunakan untuk menayangkan demo prototype/aplikasi yang sedang didevelop sebelum diserahkan ke server production masing-masing klien (seperti `nasmoco.winamus.com`, `xyz.winamus.com`).
