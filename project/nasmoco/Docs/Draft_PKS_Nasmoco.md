# DRAFT PERJANJIAN KERJA SAMA (PKS)
## PENGEMBANGAN PLATFORM WEBSITE TERPUSAT NASMOCO
### Nomor: [Nomor PKS] / PKS-WINAMUS-NASMOCO / 2026

Perjanjian Kerja Sama ini (selanjutnya disebut "**Perjanjian**") dibuat dan ditandatangani pada hari [Hari], tanggal [Tanggal] [Bulan] 2026, oleh dan di antara pihak-pihak di bawah ini:

1.  **PT WINANDI MULTI SOLUSI (Winamus)**, suatu perseroan terbatas yang didirikan berdasarkan hukum Negara Republik Indonesia, beralamat di Semarang, Jawa Tengah, dalam hal ini diwakili oleh **Aris Winandi** selaku Direktur Utama, selanjutnya disebut sebagai "**PIHAK KESATU (Penyedia/Vendor)**".
2.  **PT NEW RATNA MOTOR (Nasmoco Group)**, suatu perseroan terbatas yang didirikan berdasarkan hukum Negara Republik Indonesia, selanjutnya disebut sebagai "**PIHAK KEDUA (Klien)**".

PIHAK KESATU dan PIHAK KEDUA secara bersama-sama disebut sebagai "**Para Pihak**". Para Pihak terlebih dahulu menerangkan hal-hal sebagai berikut:
*   Bahwa PIHAK KESATU adalah perusahaan penyedia jasa konsultansi IT dan pengembangan perangkat lunak profesional.
*   Bahwa PIHAK KEDUA memerlukan jasa pengembangan sistem berupa Platform Website Terpusat Nasmoco guna memenuhi kepatuhan regulasi digital asset Toyota-Astra Motor (TAM).

Oleh karena itu, Para Pihak sepakat untuk mengikatkan diri dalam Perjanjian ini dengan syarat-syarat dan ketentuan sebagai berikut:

---

## PASAL 1 — LINGKUP PEKERJAAN

PIHAK KESATU berkewajiban untuk melaksanakan pekerjaan pengembangan sistem aplikasi dengan rincian fase pengembangan sebagai berikut:
1.  **Fase 0: Discovery & Desain:** Penyusunan dokumen SRS (*Software Requirements Specification*), perancangan arsitektur, dan pembuatan UI/UX Design System di Figma.
2.  **Fase 1: Inti / MVP:** Migrasi basis data ke PostgreSQL, pembuatan sistem harga OTR terpusat, fitur *Page Builder*, fitur *Anti-Hijack Lead*, dan integrasi CRM & WhatsApp Business API.
3.  **Fase 2: Governance & Hardening:** Pembuatan *Approval Workflow* bertingkat untuk admin regional, fitur *Brand Lock*, *Audit Log*, implementasi *Multi-Factor Authentication* (MFA), dan perlindungan Cloudflare WAF.
4.  **Fase 3: Optimasi & Validasi:** Audit & optimasi SEO/GEO lokal untuk 22 cabang, pembuatan video tutorial, penyerahan dokumentasi teknis akhir, serta penyusunan laporan kepatuhan TAM.

---

## PASAL 2 — JANGKA WAKTU & KETERGANTUNGAN JADWAL (TIMELINE DEPENDENCIES)

1.  **Jangka Waktu:** Total durasi pelaksanaan pekerjaan adalah **18 (delapan belas) minggu** terhitung sejak diterimanya pembayaran Uang Muka (DP) Fase 0 oleh PIHAK KESATU.
2.  **Ketergantungan Timeline (Day-for-Day Extension):** Jangka waktu pengerjaan akan diperpanjang secara otomatis hari-demi-hari (*day-for-day*) atau diberhentikan sementara (*paused*) tanpa dikenakan denda keterlambatan bagi PIHAK KESATU, apabila terjadi keterlambatan dari sisi PIHAK KEDUA berupa:
    *   Keterlambatan penyediaan konten, data, informasi cabang/sales, atau aset merek melewati batas **2 (dua) hari kerja** sejak diminta oleh PIHAK KESATU.
    *   Keterlambatan pemberian kredensial, hak akses server staging/production, atau integrasi API sistem eksisting (CRM/WhatsApp/TAM).
    *   Keterlambatan keputusan persetujuan desain atau penyelesaian sesi pengujian UAT oleh PIHAK KEDUA.

---

## PASAL 3 — NILAI KONTRAK & KETENTUAN PEMBAYARAN

1.  **Nilai Kontrak:** Total nilai pekerjaan pengembangan berdasarkan Perjanjian ini adalah sebesar **Rp71.100.000,- (tujuh puluh satu juta seratus ribu rupiah)**.
2.  **Skema Pembayaran Per Fase:**
    *   **Fase 0:** Nilai Rp4.500.000,- (DP 30%: Rp1.350.000,- | Pelunasan 70%: Rp3.150.000,-)
    *   **Fase 1:** Nilai Rp27.000.000,- (DP 30%: Rp8.100.000,- | Pelunasan 70%: Rp18.900.000,-)
    *   **Fase 2:** Nilai Rp23.400.000,- (DP 30%: Rp7.020.000,- | Pelunasan 70%: Rp16.380.000,-)
    *   **Fase 3:** Nilai Rp16.200.000,- (DP 30%: Rp4.860.000,- | Pelunasan 70%: Rp11.340.000,-)
3.  **Tenggat Pembayaran:** Pembayaran setiap invoice wajib diselesaikan oleh PIHAK KEDUA dalam waktu maksimal **14 (empat belas) hari kalender** sejak invoice diterima secara lengkap dan benar.
4.  **Perpajakan PP 55/2022:** PIHAK KESATU mengenakan tarif PPh Final sebesar **0,5%** sesuai dengan PP No. 55 Tahun 2022 dan wajib melampirkan Surat Keterangan PP 55 yang sah pada setiap penagihan. PIHAK KEDUA berkewajiban melakukan pemotongan pajak sesuai tarif khusus tersebut.

---

## PASAL 4 — PENGUJIAN & SERAH TERIMA PEKERJAAN (UAT & BAST)

1.  **Sesi Pengujian (UAT):** Setelah PIHAK KESATU menyelesaikan pekerjaan di setiap fase dan menaruhnya di server uji coba (*staging*), PIHAK KEDUA diberikan waktu maksimal **10 (sepuluh) hari kerja** untuk melakukan pengujian fungsional menggunakan panduan *UAT Checklist*.
2.  **Persetujuan Otomatis (*Deemed Approved*):** Apabila dalam batas waktu 10 (sepuluh) hari kerja sebagaimana dimaksud pada ayat 1, PIHAK KEDUA tidak melakukan pengujian atau tidak memberikan laporan temuan kesalahan (*bug list*) secara tertulis kepada PIHAK KESATU, maka pekerjaan pada fase tersebut secara hukum **dianggap telah disetujui sepenuhnya (*deemed approved*)** oleh PIHAK KEDUA.
3.  **Serah Terima (BAST):** Penandatanganan Berita Acara Serah Terima (BAST) atau UAT Sign-off dilakukan setelah pekerjaan dinyatakan lulus UAT atau berstatus *deemed approved*. BAST yang ditandatangani menjadi syarat mutlak pencairan pelunasan 70% per fase.

---

## PASAL 5 — HAK KEKAYAAN INTELEKTUAL (IP RIGHTS)

1.  Seluruh Hak Kekayaan Intelektual, termasuk namun tidak terbatas pada kode sumber (*source code*), desain antarmuka, aset visual, dan dokumentasi sistem yang dibangun dalam Perjanjian ini, secara otomatis **beralih menjadi milik PIHAK KEDUA setelah PIHAK KEDUA melunasi seluruh pembayaran (100%) untuk fase terkait**.
2.  Sebelum terjadinya pelunasan penuh untuk fase berjalan, seluruh kode sumber dan hak cipta tetap di bawah kepemilikan PIHAK KESATU.

---

## PASAL 6 — JAMINAN & GARANSI PERBAIKAN BUG

1.  PIHAK KESATU memberikan jaminan bebas dari kesalahan sistem kritis (*critical bug*) selama **30 (tiga puluh) hari kalender** terhitung sejak Go-Live/serah terima pekerjaan di masing-masing fase berjalan.
2.  Garansi ini hanya mencakup perbaikan kesalahan yang diakibatkan oleh kesalahan penulisan kode program oleh PIHAK KESATU dan tidak mencakup kerusakan akibat modifikasi pihak ketiga, kesalahan server Klien, atau force majeure.

---

## PASAL 7 — KETENTUAN PENGUJIAN KEAMANAN (PENETRATION TESTING)

1.  Para Pihak sepakat bahwa pengujian keamanan aplikasi berupa *Penetration Testing* (Pen Test) **tidak termasuk** dalam lingkup pekerjaan PIHAK KESATU, dan akan dilaksanakan secara mandiri oleh tim internal PIHAK KEDUA.
2.  Apabila terjadi keterlambatan dalam pelaksanaan atau pelaporan hasil *Pen Test* oleh tim internal PIHAK KEDUA pada Fase 3, hal tersebut **tidak dapat dijadikan alasan bagi PIHAK KEDUA untuk menahan pembayaran pelunasan Fase 3** kepada PIHAK KESATU.

---

## PASAL 8 — PEMBATALAN SEPIHAK & DENDA PEMUTUSAN KONTRAK (TERMINATION FEE)

1.  Mengingat pengerjaan proyek (Fase 0 hingga Fase 3) merupakan satu kesatuan komitmen komersial dan investasi sumber daya bagi PIHAK KESATU, maka pembatalan sepihak sebelum seluruh pekerjaan selesai dilarang.
2.  Apabila PIHAK KEDUA melakukan pemutusan Perjanjian secara sepihak sebelum seluruh fase selesai dikembangkan, maka PIHAK KEDUA wajib membayar denda pemutusan kontrak (*Termination Fee*) kepada PIHAK KESATU sebesar **15% (lima belas persen)** dari sisa nilai total fase yang belum berjalan.

---

Demikian Perjanjian ini dibuat dalam rangkap 2 (dua) yang masing-masing memiliki kekuatan hukum yang sama, dibubuhi meterai yang cukup, dan ditandatangani oleh perwakilan sah dari Para Pihak.

| **PIHAK KESATU** | **PIHAK KEDUA** |
|---|---|
| **PT Winandi Multi Solusi** | **PT New Ratna Motor** |
| | |
| | |
| **Aris Winandi** | **[Nama Perwakilan]** |
| Direktur Utama | [Jabatan] |
