# Naskah Presentasi — Platform Website Terpusat Nasmoco

Catatan penggunaan: ini adalah naskah literal yang bisa langsung kamu ucapkan di depan audiens, slide per slide. Sampaikan dengan tempo wajar, tidak perlu hafal kata demi kata — pahami alurnya, lalu sampaikan dengan bahasamu sendiri saat di ruangan. Estimasi total durasi: 15–20 menit.

---

## Slide 1 — Cover

Selamat pagi/siang, Bapak/Ibu. Terima kasih atas waktunya hari ini.

Perkenalkan, saya Aris Winandi dari Winamus — atau secara legal, PT Winandi Multi Solusi. Hari ini saya ingin mempresentasikan usulan kami untuk pengembangan platform website terpusat Nasmoco, yang kami susun berdasarkan dokumen Kisi-Kisi Kebutuhan dan Analisis Requirements yang sudah kami terima dan pelajari secara mendalam.

Sebelum masuk ke solusi, saya ingin mulai dari satu hal penting dulu — soal apa sebenarnya yang mendasari kebutuhan proyek ini.

---

## Slide 2 — Konteks: Ini Bukan Proyek Marketing, Ini Proyek Compliance

Jadi begini. Dari dokumen yang kami terima, kami memahami bahwa proyek ini bukan sekadar inisiatif untuk mempercantik tampilan website atau menambah fitur marketing. Ini adalah proyek kepatuhan terhadap SOP yang sudah ditetapkan oleh Toyota-Astra Motor.

PT Toyota-Astra Motor menerbitkan SOP Penggunaan Dealer Digital Assets pada Juni 2025. SOP ini mewajibkan seluruh dealer resmi, termasuk Nasmoco, untuk memenuhi standar digital tertentu sebelum batas waktu Juni 2026. Dan kalau tidak terpenuhi, konsekuensinya jelas tertulis di dokumen yang kami terima — ada risiko teguran, bahkan sanksi sesuai Dealer Agreement.

Yang ingin saya tekankan di sini: audiens sesungguhnya dari proyek ini bukan hanya manajemen Nasmoco yang hadir di ruangan ini, tapi juga Toyota-Astra Motor sebagai principal yang mengawasi kepatuhan seluruh jaringan dealer. Jadi pendekatan kami dalam proposal ini dirancang untuk menjawab kebutuhan itu secara langsung — bukan sekadar tampilan yang lebih bagus, tapi kepatuhan yang terukur dan bisa dipertanggungjawabkan.

---

## Slide 3 — Gap Analysis: 6 dari 8 Aspek Perlu Perbaikan

Dari hasil audit internal yang sudah dilakukan tim Nasmoco sendiri, terlihat jelas bahwa dari delapan aspek standar SOP TAM, hanya satu yang sudah sepenuhnya sesuai — yaitu domain website, nasmoco.co.id. Enam aspek lainnya berstatus gap, dan satu aspek lagi berstatus partial.

Coba kita lihat satu per satu sekilas: website cabang dan website wiraniaga belum punya struktur yang konsisten — itu gap. Konten digital dan logo branding sudah sebagian sesuai tapi perlu standarisasi lebih lanjut — itu partial. Lalu yang paling kritis: keamanan MFA belum aktif di semua akun, cloud dan hosting perlu audit dan peningkatan, dan monitoring lifecycle belum punya SOP internal sama sekali — ketiganya gap.

Saya tunjukkan ini di awal supaya kita sama-sama punya peta yang jelas: ini bukan daftar keinginan, ini hasil audit resmi yang sudah ada. Dan di slide-slide berikutnya, saya akan tunjukkan bagaimana setiap gap ini punya jalan penyelesaian yang konkret.

---

## Slide 4 — Masalah Operasional yang Dihadapi Tim Digital Marketing

Di luar soal kepatuhan, kami juga memahami ada tantangan operasional nyata yang dihadapi tim digital marketing sehari-hari.

Pertama, portal yang tidak seragam. Dengan 22 cabang dan puluhan wiraniaga, tampilan dan kualitas portal yang ada saat ini berbeda-beda — sebagian bahkan dikelola sendiri oleh masing-masing sales dengan kualitas yang tidak konsisten.

Kedua, update harga yang masih manual. Setiap kali ada perubahan harga satu model, perubahan itu harus diulang di puluhan halaman cabang dan wiraniaga satu per satu. Ini jelas tidak efisien dan rawan kesalahan.

Ketiga, lead yang tidak ter-atribusi dengan baik. Calon pembeli yang menghubungi lewat website berisiko tidak tersambung secara akurat ke sales atau cabang yang seharusnya menangani mereka.

Tiga masalah ini yang menjadi dasar solusi yang akan saya jelaskan selanjutnya.

---

## Slide 5 — Solusi: Platform Terpusat dengan Hierarki Tiga Tingkat

Solusi yang kami usulkan adalah satu platform dengan struktur hierarki tiga tingkat.

Level pertama adalah homepage di nasmoco.co.id — ini jadi pintu gerbang utama, menampilkan katalog lengkap, harga OTR terkini, dan promo nasional.

Level kedua adalah halaman cabang, dengan format nasmoco.co.id slash nama cabang. Halaman ini menampilkan info spesifik cabang, promo lokal, dan harga OTR wilayah yang otomatis tersinkron dari sistem pusat — jadi tidak perlu diketik ulang manual.

Level ketiga adalah halaman sales individual, dengan format nasmoco.co.id slash cabang slash nama sales. Ini memberi personal branding untuk tiap wiraniaga — lengkap dengan link WhatsApp yang sudah membawa kode atribusi otomatis.

Yang ingin saya garis bawahi di sini: harga punya satu sumber kebenaran tunggal, dan atribusi lead dikunci di sisi server — artinya tidak bisa dimanipulasi oleh pengunjung yang mengubah-ubah parameter di link. Ini langsung menjawab dua dari tiga masalah operasional yang saya sebutkan sebelumnya.

---

## Slide 6 — Setiap Gap Memiliki Jalan Penyelesaian yang Konkret

Sekarang saya ingin kembali ke tabel gap analysis tadi, dan menunjukkan secara spesifik bagaimana kami menjawab masing-masing.

Untuk website cabang — solusinya halaman per cabang dengan harga dan promo yang tersinkron otomatis, seperti yang baru saya jelaskan. Untuk website wiraniaga — kami sediakan page builder dengan template yang sudah terkurasi, jadi sales tetap bisa personalisasi halamannya tapi komponennya dibatasi sesuai peran, supaya brand tetap konsisten.

Untuk keamanan MFA — kami terapkan RBAC dan password policy sejak fase pertama, dan MFA wajib di semua akun pada fase kedua. Untuk cloud dan hosting — kami akan migrasi bertahap ke hosting yang memenuhi standar ISO27001, dilengkapi WAF dan SSL penuh. Dan untuk monitoring lifecycle — kami sediakan audit log, prosedur deaktivasi akun untuk kasus mutasi atau resign, serta dokumentasi self-assessment berkala.

Jadi setiap baris di tabel gap analysis itu, sudah punya jawaban yang jelas dalam usulan kami.

---

## Slide 7 — Proof-of-Concept Sudah Berjalan

Saya tidak ingin proposal ini hanya berhenti di slide dan dokumen. Sebagai bagian dari proses kami memahami kebutuhan ini, tim kami sudah membangun proof-of-concept yang bisa dilihat langsung.

Yang Bapak/Ibu lihat di sini adalah dua contoh: dashboard analitik yang menampilkan leads, konversi, dan performa per cabang — dan page builder untuk halaman sales yang sudah berbasis template, persis seperti yang saya jelaskan di slide sebelumnya.

Saya ingin tegaskan satu hal: ini adalah proof-of-concept untuk membuktikan pendekatan teknis kami, bukan produk final yang siap pakai. Tapi ini cukup untuk menunjukkan bahwa apa yang kami usulkan bukan sekadar konsep di atas kertas.

*(Cue: di titik ini, lanjutkan ke demo langsung di browser — buka nasmoco.ariswinandi.com — sebelum melanjutkan ke slide berikutnya.)*

---

## Slide 8 — Keamanan & Kepatuhan: Bertahap, Bukan Ditunda

Sekarang saya ingin masuk ke pendekatan teknis yang lebih dalam, mulai dari keamanan.

Pendekatan kami adalah menerapkan standar keamanan SOP TAM secara bertahap dan terukur — bukan ditunda ke akhir proyek, dan bukan juga dipaksakan semuanya sejak hari pertama.

Di fase pertama, kami terapkan baseline: PostgreSQL dengan RBAC, password policy sesuai SOP TAM, rate limiting dan anti-spam di form, serta consent dan privacy policy dasar sesuai UU PDP.

Di fase kedua, kami masuk ke hardening: MFA wajib di seluruh akun, WAF dari Cloudflare, enkripsi data sensitif, dan migrasi ke hosting yang memenuhi ISO27001.

Di fase ketiga, kami lakukan validasi: pen testing secara mandiri oleh tim internal Nasmoco, laporan audit sebagai bukti kepatuhan ke TAM, dan prosedur respons insiden dengan batas waktu 24 jam.

Pendekatan berjenjang ini memastikan Bapak/Ibu melihat progres keamanan yang nyata di setiap fase, bukan menunggu sampai akhir untuk tahu apakah standarnya terpenuhi.

---

## Slide 9 — Integrasi dengan Sistem Existing & Stack Teknologi

Satu prinsip yang ingin saya tegaskan: kami memahami bahwa Nasmoco sudah punya sistem otomasi alur, CRM, dan notifikasi WhatsApp yang sudah berjalan. Peran kami adalah melakukan integrasi terhadap sistem-sistem itu, bukan menggantikannya.

Jadi nanti, lead yang masuk dari website akan tetap diteruskan lewat webhook ke CRM yang sudah ada sebagai tujuan akhir penyimpanan. Notifikasi tetap berjalan lewat WhatsApp WABA yang sudah dipakai sekarang. Dan untuk masa transisi, aset media bisa tetap bersumber dari CDN yang sudah ada.

Dari sisi stack teknologi, kami mengusulkan Next.js untuk frontend dengan rendering sisi server demi kebutuhan SEO, PostgreSQL sebagai basis data sejak fase pertama — bukan basis data ringan yang rawan masalah saat diakses bersamaan oleh banyak pengguna — lalu hosting dengan kepatuhan ISO27001 dan Cloudflare untuk WAF, serta sistem autentikasi yang mendukung MFA dan RBAC secara granular.

---

## Slide 10 — Roadmap: 18 Minggu, MVP Live di Minggu ke-8

Untuk timeline, kami usulkan total durasi pengembangan 18 minggu, terbagi dalam empat fase.

Fase 0 di dua minggu pertama, fokus finalisasi requirement dan desain. Fase 1 selesai di minggu ke-8, dengan milestone paling penting: MVP sudah live dan bisa digunakan. Fase 2 selesai di minggu ke-14, fokus governance dan hardening keamanan. Dan fase 3 selesai di minggu ke-18, fokus validasi dan penyusunan compliance report.

Saya ingin tekankan satu hal di sini: dengan struktur ini, Bapak/Ibu sudah punya bukti progres nyata di minggu ke-8 — jauh sebelum proyek selesai sepenuhnya. Jadi tidak perlu menunggu 18 minggu untuk melihat hasil konkret.

Timeline ini bersifat indikatif, dan kami terbuka untuk menyesuaikannya berdasarkan ketersediaan tim Nasmoco untuk proses review dan persetujuan di setiap fase.

---

## Slide 11 — Cakupan Utama per Fase

Sekilas rincian apa saja yang masuk di tiap fase.

Fase 0: finalisasi requirement, validasi arsitektur, dan desain UI/UX final.

Fase 1, ini fase inti: migrasi ke PostgreSQL, sistem harga terpusat dan page builder, atribusi lead yang anti-manipulasi, integrasi ke CRM dan WhatsApp, serta SEO dasar.

Fase 2: approval workflow berjenjang dari sales ke SPV cabang ke HO marketing, brand lock, pemeriksaan otomatis konten, kill switch, audit log, MFA, dan WAF.

Fase 3: optimasi SEO untuk pencarian berbasis AI, optimasi performa, koordinasi hasil pen testing internal, dan dokumentasi lengkap beserta pelatihan tim.

---

## Slide 12 — Estimasi Investasi Tahun Pertama

Sekarang saya masuk ke bagian investasi. Saya sengaja menyampaikan ini setelah Bapak/Ibu melihat keseluruhan cakupan kerja, supaya angkanya punya konteks yang jelas.

Total biaya pengembangan untuk seluruh fase pengembangan kami estimasikan Rp71.100.000, di luar biaya pen testing yang akan ditangani sendiri oleh Nasmoco secara internal. Breakdown-nya bisa dilihat di grafik — fase 1 yang paling besar porsinya karena itu fase inti pengembangan sistem.

Untuk pemeliharaan setelah go-live, kami estimasikan Rp43.200.000 per tahun, atau Rp3.600.000 per bulan, yang mencakup dukungan teknis, hosting setara ISO27001, dan WAF.

Jadi total investasi tahun pertama, gabungan pengembangan dan pemeliharaan, adalah Rp114.300.000 (untuk skenario pemeliharaan penuh/Skenario 1).

Saya ingin tegaskan: ini adalah estimasi awal berdasarkan ruang lingkup yang kami pahami saat ini. Kami terbuka penuh untuk mendiskusikan dan menyesuaikan angka ini bersama Bapak/Ibu.

---

## Slide 13 — Model Dukungan & Service Level Agreement

Untuk dukungan pasca-peluncuran, kami punya tiga tingkat prioritas dengan target waktu yang jelas.

Untuk kasus kritis, misalnya sistem down atau lead gagal tercatat — target respons maksimal 2 jam, target resolusi maksimal 24 jam. Untuk prioritas tinggi, seperti fitur utama tidak berfungsi — target respons 8 jam kerja, resolusi 3 hari kerja. Untuk prioritas menengah, seperti bug tampilan — target respons 1 hari kerja, resolusi 5 hari kerja.

Semua dukungan ini tercakup dalam biaya pemeliharaan bulanan, dengan batas jam yang akan kita sepakati bersama. Dan untuk kasus kritis, eskalasinya langsung ke saya sebagai project manager.

---

## Slide 14 — Tim & Pendekatan Kerja

Sedikit tentang kami. Saya Aris Winandi, sebagai Owner dan Project Manager di Winamus, secara legal PT Winandi Multi Solusi.

Ada tiga hal yang ingin saya tonjolkan soal cara kami bekerja. Pertama, delivery langsung oleh saya sebagai PM teknis — jadi komunikasi Bapak/Ibu langsung dengan orang yang memahami detail teknis, bukan lewat account manager perantara. Kedua, tim kami kecil, jadi komunikasi dan keputusan bisa berjalan cepat, dengan siklus pengembangan iteratif di setiap fase. Ketiga, tim kami punya pengalaman menangani proyek platform multi-tenant, CMS kustom, dan integrasi API untuk klien internasional — sebagian di bawah perjanjian kerahasiaan sehingga detailnya tidak bisa kami buka, tapi pengalaman itu yang mendasari pendekatan teknis yang kami usulkan hari ini.

---

## Slide 15 — Mari Diskusikan Langkah Selanjutnya

Sebagai penutup, ini tiga langkah yang kami usulkan ke depan.

Pertama, diskusi dan penyesuaian ruang lingkup bersama tim Nasmoco — karena semua yang saya sampaikan hari ini masih terbuka untuk dibahas. Kedua, setelah ada kesepakatan, finalisasi perjanjian kerja atau SPK. Dan ketiga, kick-off fase 0 untuk mulai discovery dan desain.

Proposal lengkap dengan seluruh detail teknis, breakdown biaya, dan syarat ketentuan sudah saya siapkan dalam bentuk dokumen tertulis, yang akan saya serahkan setelah sesi ini sebagai referensi resmi untuk pembahasan internal Bapak/Ibu.

Saya dan tim sangat terbuka untuk mendiskusikan setiap bagian dari proposal ini. Terima kasih banyak atas waktu dan kesempatannya.

*(Cue: buka sesi tanya jawab di sini.)*
