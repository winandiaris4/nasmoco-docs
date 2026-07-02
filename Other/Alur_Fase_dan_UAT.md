# Panduan Alur Kerja Proyek: Pengerjaan, UAT, dan Pembayaran

Dokumen ini menjelaskan alur operasional standar (*Standard Operating Procedure*) yang digunakan oleh **Winamus (PT Winandi Multi Solusi)** dalam menjalankan proyek pengembangan perangkat lunak berbasis fase.

---

## 1. Diagram Alur Siklus Fase

Setiap fase pengembangan akan melewati siklus terstruktur berikut:

```mermaid
graph TD
    A[1. Kick-off & Invoice DP 30%] --> B[2. Pembayaran DP 30% oleh Klien]
    B --> C[3. Proses Development & Tes Internal]
    C --> D[4. Sesi UAT (User Acceptance Test)]
    D -->|Ada Temuan Bug| E[5. Perbaikan & Retest oleh Vendor]
    E --> D
    D -->|Lolos UAT / Sesuai Spesifikasi| F[6. Tanda Tangan BAST / Sign-off]
    F --> G[7. Invoice & Pelunasan 70%]
    G -->|Masuk Fase Berikutnya| A
```

---

## 2. Rincian 7 Langkah Siklus Fase

### Langkah 1: Kick-off Fase & Invoice DP 30%
*   **Tujuan:** Menandai dimulainya fase baru dan mengajukan komitmen biaya awal.
*   **Aksi Vendor (Winamus):** Mengirimkan notifikasi tertulis bahwa fase siap dimulai beserta **Invoice Down Payment (DP) senilai 30%** dari total anggaran fase tersebut.
*   **Aksi Klien (Nasmoco):** Memproses verifikasi internal untuk pembayaran DP.

### Langkah 2: Pembayaran DP 30%
*   **Tujuan:** Mengaktifkan masa pengerjaan proyek sesuai timeline yang disepakati.
*   **Aksi Klien:** Melakukan transfer dana DP 30% ke rekening Vendor.
*   **Catatan:** Durasi pengerjaan fase (*timeline*) secara resmi mulai dihitung sejak tanggal dana DP diterima di rekening Vendor.

### Langkah 3: Proses Development & Tes Internal
*   **Tujuan:** Membangun fitur-fitur sesuai dengan ruang lingkup (*scope*) fase terkait.
*   **Aksi Vendor:** 
    *   Melakukan penulisan kode (*coding*), konfigurasi sistem, dan integrasi.
    *   Melakukan pengujian internal secara intensif (*Alpha & Beta Testing*) untuk meminimalkan error sebelum diserahkan ke klien.

### Langkah 4: Sesi UAT (User Acceptance Test)
*   **Tujuan:** Memvalidasi bahwa fitur yang dibangun telah berfungsi sesuai dengan dokumen kebutuhan (*System Requirement Specification*).
*   **Aksi Vendor:** 
    *   Men-deploy sistem hasil pengerjaan ke server uji coba (*Staging Environment*).
    *   Menyerahkan dokumen **UAT Checklist** (panduan skenario pengujian) kepada klien.
*   **Aksi Klien:** Tim penanggung jawab dari sisi Klien melakukan pengujian langsung pada sistem menggunakan panduan UAT Checklist. Waktu pengujian standar adalah **3-5 hari kerja**.

### Langkah 5: Perbaikan & Retest (Jika Ada Temuan)
*   **Tujuan:** Menyelesaikan kendala atau ketidaksesuaian yang ditemukan selama UAT.
*   **Aksi Klien:** Memberikan laporan temuan (*bug/defect list*) secara tertulis jika ada fitur yang tidak berfungsi.
*   **Aksi Vendor:** Melakukan perbaikan (*bug fixing*) dan menyerahkan kembali sistem untuk diuji ulang (*re-test*) oleh klien hingga semua poin UAT Checklist berstatus **"PASSED"**.

### Langkah 6: Tanda Tangan BAST / Sign-off UAT
*   **Tujuan:** Pernyataan formal bahwa fase pekerjaan telah diselesaikan dan diterima dengan baik.
*   **Aksi Klien & Vendor:** Menandatangani dokumen **BAST (Berita Acara Serah Terima)** atau formulir *UAT Sign-off*. Dokumen ini berfungsi sebagai persetujuan formal untuk melakukan rilis produksi (*Go-Live*) dan penagihan sisa pembayaran.

### Langkah 7: Invoice & Pelunasan 70%
*   **Tujuan:** Penyelesaian kewajiban finansial fase terkait.
*   **Aksi Vendor:** Mengirimkan **Invoice Pelunasan senilai 70%** dari total anggaran fase dengan melampirkan dokumen BAST yang telah ditandatangani.
*   **Aksi Klien:** Melakukan transfer sisa pembayaran 70%. Setelah pelunasan diterima, sistem pada fase tersebut dapat dipindahkan ke server produksi (*Go-Live*).

---

## 3. Contoh Simulasi Keuangan (Fase 1 - MVP)

Sebagai gambaran nyata, berikut adalah alur uang pada **Fase 1 (Sistem Inti / MVP)** dengan nilai **Rp27.000.000**:
1.  **Awal Fase:** Winamus mengirimkan invoice Rp8.100.000 (30%). Nasmoco membayar $\rightarrow$ Pekerjaan dimulai.
2.  **Tengah Fase:** Pengerjaan coding oleh Winamus selama 4-6 minggu $\rightarrow$ Selesai $\rightarrow$ Masuk sesi UAT oleh Nasmoco.
3.  **Akhir Fase:** UAT disetujui $\rightarrow$ Penandatanganan BAST $\rightarrow$ Winamus mengirimkan invoice Rp18.900.000 (70%) $\rightarrow$ Nasmoco melunasi $\rightarrow$ MVP diluncurkan ke publik $\rightarrow$ Lanjut ke Fase 2.

---

## 4. Ketentuan Khusus & Pengaman Risiko Vendor

Untuk menjaga kelancaran arus kas (*cash flow*) selama masa pengembangan dan menghindari keterlambatan proyek yang disebabkan oleh proses internal Klien, klausul-klausul berikut diberlakukan dalam kontrak kerja sama:

### A. Klausul Persetujuan Otomatis (Deemed Approved)
*   Setelah Vendor menyerahkan sistem di server *staging* beserta dokumen *UAT Checklist*, Klien diberikan waktu maksimal **10 hari kerja** untuk melakukan pengujian dan memberikan laporan temuan (*bug list*) tertulis.
*   Jika dalam batas waktu **10 hari kerja** tersebut Klien tidak memberikan umpan balik tertulis atau laporan temuan, maka sistem pada fase tersebut secara hukum **dianggap telah disetujui sepenuhnya (*deemed approved*)**.
*   Dengan status *deemed approved*, dokumen BAST dianggap sah untuk ditandatangani, dan Vendor berhak menerbitkan Invoice Pelunasan 70%.

### B. Ketergantungan Pihak Ketiga pada Fase 3
*   Pekerjaan **Fase 3 (Optimasi & Validasi)** senilai **Rp16.200.000** dan pekerjaan **Subkontrak Pen Testing** senilai **Rp15.000.000** adalah dua entitas penagihan yang terpisah.
*   Apabila pekerjaan optimasi dari Vendor telah selesai dan lulus UAT, namun laporan hasil *Pen Testing* dari pihak ketiga independen mengalami keterlambatan yang disebabkan oleh pihak ketiga atau proses birokrasi TAM, maka Klien **tidak diperkenankan menahan pembayaran pelunasan Fase 3 (Rp16.200.000)** milik Vendor.

### C. Tenggat Waktu Pembayaran (Term of Payment)
*   Setiap invoice yang diterbitkan oleh Vendor (baik DP 30% maupun Pelunasan 70%) wajib dilunasi oleh Klien dalam waktu maksimal **14 hari kalender** sejak dokumen invoice diterima secara lengkap dan benar oleh bagian Keuangan Klien.
*   Keterlambatan pembayaran DP akan berdampak pada pergeseran jadwal mulai pengerjaan (*timeline shift*) secara pro-rata.

### D. Ketergantungan Timeline & Penanganan Keterlambatan (Timeline Dependencies)
Durasi pengerjaan setiap fase yang disepakati dalam proposal ini sangat bergantung pada kerja sama aktif dari Klien dan pihak ketiga terkait. Durasi pengerjaan akan diperpanjang secara otomatis (*day-for-day extension*) atau dihentikan sementara (*paused*) tanpa penalti denda bagi Vendor jika terjadi keterlambatan yang disebabkan oleh:
1. **Keterlambatan Aset & Informasi:** Klien terlambat menyerahkan data, konten, panduan merek, atau informasi spesifik yang dibutuhkan untuk pengembangan dalam waktu maksimal **2 hari kerja** setelah diminta oleh Vendor.
2. **Akses API & Lingkungan Kerja:** Keterlambatan pemberian kredensial, hak akses server, atau API sistem eksisting Nasmoco (termasuk akses database lama, CRM, dan WhatsApp Business API) serta lambatnya respons dukungan teknis dari pihak ketiga (seperti TAM / Toyota Astra Motor).
3. **Keterlambatan Keputusan & Feedback:** Klien memerlukan waktu lebih lama dari batas **10 hari kerja** untuk melakukan pengujian UAT atau memberikan keputusan persetujuan desain/fitur.
4. **Keterlambatan Pembayaran DP:** Pengerjaan setiap fase baru akan dimulai setelah pembayaran DP 30% untuk fase tersebut diterima di rekening Vendor. Durasi pengerjaan otomatis bergeser menyesuaikan tanggal diterimanya dana tersebut.


