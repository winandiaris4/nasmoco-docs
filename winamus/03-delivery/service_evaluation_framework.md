# 🧭 Framework Evaluasi Kelayakan Service Baru — Winamus

> **Tujuan:** Dokumen ini menjadi panduan internal sebelum memutuskan untuk menawarkan suatu layanan baru kepada calon klien. SDM (tim pengerjaan) dianggap tersedia.

---

## A. Apa Itu "Service yang Layak Ditawarkan"?

Sebuah layanan baru dianggap **siap ditawarkan** ke pasar jika memenuhi kesiapan di 5 dimensi berikut secara bersamaan:

```
[1. Komersial] + [2. Delivery] + [3. Legal & Kontrak] + [4. Harga & Margin] + [5. Pasar & Posisi]
         └───────────────────────────────┬─────────────────────────────────────────┘
                                  SERVICE LAYAK DIJUAL
```

---

## 1. VARIABEL KOMERSIAL (Business Case)

Apakah layanan ini menguntungkan dan berkelanjutan untuk Winamus?

*   [ ] **Recurring vs One-off?**
    Apakah layanan ini menghasilkan pemasukan sekali saja (*one-off project*) atau ada komponen berulang (*retainer/maintenance*)?
    > Winamus harus secara strategis mendorong lebih banyak layanan berbasis *retainer* untuk menjaga stabilitas arus kas, terutama di fase awal pertumbuhan perusahaan.
*   [ ] **Estimasi Margin Bersih**
    Hitung: `Biaya Jual - (Biaya SDM + Biaya Tool/Lisensi + Overhead Operasional)`. Target margin bersih minimum yang sehat untuk agensi IT kelas menengah adalah **30-40%**.
*   [ ] **Upsell & Cross-sell Potential**
    Apakah layanan ini bisa membuka peluang penjualan layanan lain Winamus? Contoh: proyek *web app* membuka pintu untuk *maintenance retainer*, kemudian *AI implementation*, dsb.

---

## 2. VARIABEL DELIVERY (Kemampuan Eksekusi)

*Asumsi SDM tersedia.* Tapi SDM saja tidak cukup.

*   [ ] **Tooling & Infrastruktur**
    Apakah Winamus sudah memiliki (atau siap menyewa) alat kerja, lisensi software, dan infrastruktur yang dibutuhkan untuk menjalankan layanan ini? Contoh: untuk layanan AI Agent, dibutuhkan akun API OpenAI/Gemini, server untuk *hosting* model, dsb.
*   [ ] **Standar Kualitas & QA**
    Apakah ada SOP dan proses Quality Assurance yang bisa diulang (*repeatable*) untuk memastikan kualitas konsisten antar proyek, antar klien?
*   [ ] **Estimasi Waktu Per Proyek (Time-to-Delivery)**
    Berapa lama rata-rata satu proyek layanan ini bisa diselesaikan dari *kickoff* hingga *serah terima*? Ini kritis untuk mengatur kapasitas tim agar tidak *overload*.
*   [ ] **Kapasitas Paralel**
    Berapa proyek dari layanan ini yang bisa dikerjakan secara bersamaan tanpa menurunkan kualitas? Ini menentukan batas penerimaan klien.
*   [ ] **Dokumentasi Teknis Internal**
    Apakah ada dokumentasi, *template*, atau *codebase boilerplate* internal yang mempercepat pengerjaan proyek serupa di masa depan?

---

## 3. VARIABEL LEGAL & KONTRAK

*   [ ] **Template Kontrak Spesifik Layanan**
    Setiap jenis layanan memiliki klausul risiko yang berbeda. Pastikan ada draf Perjanjian Kerja Sama (PKS) atau Surat Perjanjian Layanan (SPL) yang sudah disesuaikan dengan karakteristik layanan tersebut.
    *   Contoh: Layanan **AI Agent** perlu klausul khusus tentang keakuratan output AI (*AI Disclaimer*) dan batas tanggung jawab atas keputusan bisnis yang dibuat berdasarkan rekomendasi AI.
    *   Contoh: Layanan **Mobile Apps** perlu klausul khusus untuk biaya *App Store/Play Store developer account* dan proses *review* Apple/Google yang tidak berada di bawah kendali Winamus.
*   [ ] **Kejelasan Hak Kekayaan Intelektual (IP)**
    Apakah kode, model AI, atau aset yang dibuat untuk klien tersebut 100% menjadi milik klien setelah pelunasan? Atau ada komponen *proprietary library/framework* milik Winamus yang perlu dikecualikan?
*   [ ] **Klausul Data & Privasi**
    Apabila layanan menyentuh atau memproses data pengguna atau data bisnis sensitif klien (terutama layanan AI, CRM, RPA), pastikan ada klausul Perlindungan Data yang mengacu pada **UU PDP (Perlindungan Data Pribadi)** Indonesia.

---

## 4. VARIABEL HARGA & STRATEGI PENAWARAN

*   [ ] **Model Harga yang Tepat**
    Pilih model harga yang sesuai dengan karakteristik layanan:
    | Model | Cocok Untuk |
    |---|---|
    | **Fixed Price per Project** | Scope yang jelas dan terukur (web app, mobile app) |
    | **Time & Material (T&M)** | Scope tidak pasti atau sering berubah (konsultansi, R&D) |
    | **Monthly Retainer** | Dukungan berkelanjutan (maintenance, SLA support, AI monitoring) |
    | **Lisensi SaaS** | Jika Winamus membangun produk yang bisa disewakan ke banyak klien |
*   [ ] **Anchoring Price**
    Siapkan 2-3 paket harga (misalnya: *Starter, Growth, Enterprise*) untuk mengakomodasi berbagai ukuran klien. Paket tengah (*Growth*) biasanya menjadi pilihan mayoritas klien.
*   [ ] **Biaya Tersembunyi yang Harus Diantisipasi**
    Identifikasi semua komponen biaya yang tidak terlihat: lisensi API pihak ketiga, biaya *cloud provider*, biaya revisi melebihi batas, *App Store fee*, dan sebagainya — lalu masukkan ke dalam kalkulasi harga jual.

---

## 5. VARIABEL PASAR & POSITIONING

*   [ ] **Siapa Target Klien yang Paling Ideal? (ICP — Ideal Customer Profile)**
    Tentukan profil klien paling ideal untuk layanan ini berdasarkan:
    *   *Industri:* Apa industri yang paling membutuhkan layanan ini? (Otomotif, Retail, Properti, dll.)
    *   *Ukuran Perusahaan:* UKM, *mid-market* (50-500 karyawan), atau *enterprise*?
    *   *Tingkat Kematangan Digital:* Apakah klien sudah melek digital atau masih perlu edukasi dasar?
*   [ ] **Diferensiasi dari Kompetitor**
    Apa yang membuat penawaran layanan Winamus berbeda atau lebih baik dibanding kompetitor lokal di Semarang/Jawa Tengah? Contoh: "Kami satu-satunya agensi di Semarang yang menawarkan AI Agent custom berbasis data internal klien."
*   [ ] **Cara Akuisisi Klien (Go-to-Market Strategy)**
    Bagaimana klien baru untuk layanan ini akan ditemukan? Pilih minimum satu saluran utama:
    *   Referral dari klien yang ada (Word of Mouth)
    *   Konten edukasi (artikel, demo video di LinkedIn/YouTube)
    *   *Cold outreach* ke ICP yang ditarget
    *   Kemitraan dengan agensi lain yang tidak melayani layanan ini

---

## Ringkasan: Kapan Sebuah Service Siap Dijual?

| Dimensi | Pertanyaan Kunci | Status |
|---|---|---|
| **Komersial** | Margin bersih minimal 30%? Recurring component ada? | - |
| **Delivery** | Tooling siap? SOP ada? Estimasi waktu realistis? | - |
| **Legal** | Template kontrak spesifik tersedia? Klausul IP & data jelas? | - |
| **Harga** | Model harga ditentukan? Biaya tersembunyi diperhitungkan? | - |
| **Pasar** | ICP jelas? Diferensiasi ada? Saluran akuisisi dipilih? | - |

> Jika **minimal 4 dari 5 dimensi** di atas terpenuhi, layanan tersebut layak untuk mulai ditawarkan secara terbatas kepada klien pilot (*early adopter*). Jangan tunggu sempurna — validasi di pasar nyata adalah cara tercepat untuk menyempurnakan layanan.
