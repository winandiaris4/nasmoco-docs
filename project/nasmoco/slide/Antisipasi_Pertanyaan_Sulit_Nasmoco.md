# Antisipasi Pertanyaan Sulit — Sesi Presentasi Nasmoco

Disusun berdasarkan kemungkinan pertanyaan dari Manager Pemasaran dan Manager IT. Jawaban ditulis sebagai panduan poin, sampaikan dengan bahasamu sendiri — yang penting intinya kena dan kamu tidak terlihat ragu.

---

## A. Soal Biaya (paling mungkin ditanya duluan)

**Q1: "Kok bisa naik jauh dari Rp60 juta yang sempat dibicarakan?"**

Ini pertanyaan yang paling pasti muncul. Jangan defensif, jawab dengan percaya diri:

> "Angka awal itu muncul sebelum kami menerima dokumen Kisi-Kisi dan Analisis Requirements resmi. Begitu kami pelajari, scope-nya jauh lebih luas dari obrolan awal — ini bukan sekadar refresh tampilan, tapi mencakup governance berjenjang, atribusi lead anti-hijack, keamanan setingkat SOP TAM, dan validasi keamanan. Setiap komponen biaya di proposal kami terhubung langsung ke requirement yang tertulis di dokumen Bapak/Ibu sendiri. Dan kami sudah mengakomodasi permintaan Bapak/Ibu untuk menghapus biaya Pen Testing eksternal karena akan ditangani internal — sehingga total pengembangan sekarang adalah Rp71.100.000."

Kalau didesak lebih jauh: tawarkan untuk membahas per fase mana yang bisa disesuaikan (lihat Q2), bukan mempertahankan angka total secara kaku.

**Q2: "Bisa dipangkas supaya lebih dekat ke budget awal?"**

> "Bisa kita diskusikan per fase. Fase 1 itu inti yang tidak bisa dikompromikan karena di situ letak kepatuhan utamanya. Yang punya ruang fleksibel adalah cakupan GEO di Fase 3 — itu bisa disesuaikan tanpa mengorbankan kepatuhan inti. Biaya pen testing juga sudah kami keluarkan dari penawaran sesuai permintaan Bapak/Ibu karena akan ditangani internal."

Jangan langsung setuju potong harga di tempat tanpa mengurangi scope — itu akan terlihat bahwa harga awal memang asal pasang.

**Q3: "Termin pembayarannya bagaimana?"**

> "30% di awal tiap fase, 70% setelah deliverable fase itu disetujui lewat UAT. Jadi Bapak/Ibu tidak membayar penuh di muka untuk sesuatu yang belum terlihat hasilnya."

---

## B. Soal Keamanan & Teknis (paling mungkin dari Manager IT)

**Q4: "ISO27001 itu maksudnya hosting-nya, atau perusahaan vendor yang harus tersertifikasi?"**

Karena ini sudah terkonfirmasi sebelumnya sebagai infrastruktur hosting, jawab dengan tegas:

> "Itu mengacu pada infrastruktur hosting — kami akan menggunakan cloud provider yang sudah memegang sertifikasi ISO27001, bukan PT kami sendiri yang harus tersertifikasi. Itu sudah dikonfirmasi di awal."

**Q5: "Tim kalian kecil. Kalau Anda sakit atau tidak tersedia di tengah proyek, bagaimana?"**

Ini pertanyaan wajar dari IT manager yang menilai risiko vendor kecil. Jangan terlihat defensif:

> "Kami menjaga dokumentasi teknis berjalan terus selama development, bukan ditulis di akhir. Akses source code dan infrastruktur juga akan diberikan ke tim Nasmoco sejak awal, bukan dipegang eksklusif oleh kami — jadi tidak ada single point of failure yang membuat Nasmoco terkunci kalau terjadi sesuatu."

**Q6: "Awalnya rencana stack Next+Django+Postgres, tapi demo yang ditunjukkan pakai Prisma+SQLite. Apakah nanti dibangun ulang dari nol?"**

> "Tidak dari nol. SQLite di demo itu murni untuk kecepatan validasi konsep. Karena kami pakai Prisma sebagai ORM, migrasi ke PostgreSQL itu perubahan konfigurasi koneksi, bukan rewrite logic. Soal Django, itu keputusan yang akan kami tinjau berdasarkan kebutuhan riil di Fase 1 — bukan diasumsikan wajib sejak awal."

**Q7: "Bagaimana skema backup dan disaster recovery? Kalau server down berapa lama downtime?"**

> "Backup otomatis terjadwal, dan untuk kasus kritis seperti sistem down, target respons kami maksimal 2 jam dengan target resolusi 24 jam, sesuai SLA yang ada di proposal. Detail RTO/RPO bisa kita formalkan lebih spesifik di kontrak."

**Q8: "Apakah source code dan domain sepenuhnya jadi milik Nasmoco?"**

Ini pertanyaan penting soal lock-in — jawab dengan jelas dan jangan ambigu:

> "Ya. Source code menjadi milik Nasmoco setelah pelunasan tiap fase, dan domain serta akun hosting kami sarankan didaftarkan atas nama Nasmoco sejak awal, bukan atas nama kami — supaya tidak ada ketergantungan ke vendor manapun di kemudian hari."

**Q9: "Bagaimana sistem ini menangani lonjakan traffic, misal saat promo besar?"**

> "Load testing masuk dalam Fase 3 sebelum validasi akhir. Kami akan tentukan target kapasitas konkret bersama tim IT berdasarkan data traffic historis Nasmoco, supaya angkanya realistis bukan asumsi sepihak dari kami."

**Q10: "Kalau terjadi kebocoran data, siapa yang tanggung jawab?"**

> "Secara UU PDP, Nasmoco berperan sebagai Pengendali Data, dan kami sebagai Prosesor Data pada sistem yang kami kelola. Kami bertanggung jawab menjaga keamanan teknis sesuai standar yang disepakati, dan akan membantu proses notifikasi kalau insiden terjadi di sistem yang kami pegang. Ini akan kami tuangkan jelas di kontrak supaya tidak ada area abu-abu."

---

## C. Soal Operasional & Tim (paling mungkin dari Manager Pemasaran)

**Q11: "Sales kami yang akan pakai page builder ini setiap hari — sulit tidak dipelajari? Berapa lama training?"**

> "Tidak butuh kemampuan teknis. Sales tinggal pilih template, isi konten lewat komponen yang sudah disiapkan — sama seperti mengisi formulir. Training dan dokumentasi sudah masuk di Fase 3, idealnya 1-2 sesi singkat per cabang."

**Q12: "Bagaimana memastikan SEO tidak turun saat pindah dari website lama?"**

> "Strategi migrasi kami pakai 301 redirect dari URL lama ke URL baru, dilakukan di luar jam kerja, dengan monitoring intensif di 72 jam pertama. Website lama juga tetap kami pertahankan sebagai cadangan selama beberapa minggu sebelum benar-benar dinonaktifkan — supaya tidak ada risiko kehilangan ranking secara tiba-tiba."

**Q13: "Kalau sales resign, bagaimana nasib halaman dan lead yang sudah masuk?"**

> "Ada prosedur deaktivasi akun untuk kasus mutasi atau resign — halaman bisa dinonaktifkan atau dialihkan, dan lead yang sudah masuk bisa di-reassign ke sales lain tanpa hilang datanya. Ini bagian dari audit log dan monitoring lifecycle yang kami usulkan di Fase 2."

**Q14: "Bagaimana kalau ada kebutuhan tambahan di luar yang dibahas hari ini, setelah proyek berjalan?"**

> "Itu kami sebut change request — dibahas dan disepakati tertulis dengan estimasi biaya dan waktu terpisah, supaya scope awal tetap terjaga dan tidak membengkak tanpa kesepakatan jelas."

**Q15: "Kapan kita bisa lihat hasil konkret — peningkatan lead atau efisiensi?"**

Jangan overpromise angka spesifik yang belum bisa dibuktikan:

> "MVP sudah live di minggu ke-8, jadi struktur intinya — harga terpusat, atribusi lead, halaman sales — sudah bisa langsung dirasakan dampaknya sejak titik itu. Untuk metrik seperti peningkatan SEO dan konversi, itu akan kami monitor bertahap pasca-launch karena sifatnya kumulatif, bukan instan."

---

## D. Pertanyaan Lintas / Bisa dari Siapa Saja

**Q16: "Kenapa harus PT kalian yang baru, bukan vendor besar yang sudah berpengalaman?"**

> "Kami pahami PT kami relatif baru. Tapi yang kami tawarkan adalah delivery langsung oleh saya sebagai project manager teknis — tanpa lapisan account manager yang memperlambat komunikasi — dan proof-of-concept yang sudah bisa dilihat langsung hari ini sebagai bukti konkret, bukan sekadar klaim pengalaman di atas kertas."

**Q17: "Kita sudah lewat deadline TAM di Juni 2026. Bagaimana ini diantisipasi?"**

Ini sensitif — jawab dengan tenang, jangan terkesan panik:

> "Kami sarankan Nasmoco menyiapkan laporan kemajuan ke TAM yang menunjukkan remediation plan sudah berjalan aktif — itu biasanya jadi pertimbangan baik oleh principal, dibanding tidak ada tindakan sama sekali. Dengan MVP live di minggu ke-8, ada bukti progres nyata yang bisa disampaikan lebih awal, sebelum seluruh proyek selesai."

**Q18: "Apakah ada vendor lain yang dibandingkan untuk proyek ini?"**

Jawab netral, fokus ke kekuatan sendiri, jangan berasumsi soal proses internal mereka:

> "Itu di luar kendali kami. Yang bisa kami pastikan adalah proposal ini disusun berdasarkan pemahaman mendalam terhadap dokumen requirement Bapak/Ibu, dengan bukti kapabilitas teknis yang sudah berjalan — itu yang kami harap jadi pertimbangan utama."

---

## Catatan Umum Saat Menjawab

- Kalau ada pertanyaan yang benar-benar belum punya jawaban pasti, lebih baik bilang **"itu poin bagus, saya akan konfirmasi dan kirimkan jawabannya setelah ini"** daripada mengarang jawaban di tempat. Kredibilitas lebih penting daripada terlihat tahu segalanya.
- Kalau didesak soal harga di ruangan, jangan langsung setuju turun angka tanpa mengubah scope — itu sinyal bahwa harga awal tidak serius dihitung.
- Catat setiap pertanyaan yang membuatmu ragu menjawab — itu sinyal bagian proposal yang perlu diperjelas di revisi berikutnya.
