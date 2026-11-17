# Prototipe BNI Sandbox Tester (dokumen sumber, belum dieksekusi)

Catatan riset. Sumber diperiksa 17 November 2026.

## Ringkasan

Dokumen Word yang diteruskan mengusulkan aplikasi Android untuk menguji konektivitas ke backend lokal, lalu meminta saldo dari lingkungan sandbox BNI melalui sebuah SDK. Ini rangkuman desain dalam dokumen, bukan hasil build atau uji integrasi.

## Batas dan status

- Dokumen menyebut rancangan dibatasi ke sandbox dan permintaan baca saldo; tidak mendeskripsikan transfer atau transaksi pembayaran.
- Dokumen mengusulkan penyimpanan kredensial sandbox hanya di sisi backend, bukan di aplikasi ponsel. Ini pilihan desain yang tertulis, belum diuji.
- Generator, source proyek, instalasi dependency, unit test, build APK, lint, audit dependency, dan panggilan BNI belum dijalankan. Kode tidak diaudit baris per baris.
- Rujukan yang dicantumkan dokumen - README SDK BNI dan catatan rilis Android Gradle Plugin 8.7 - belum diverifikasi ulang. Keaslian dan keamanan dependency juga belum diperiksa.
- Dokumen menyertakan checklist yang belum selesai. Tidak ada hasil tes sandbox yang dapat disimpulkan dari materi ini.

## Bagian terbuka

Source belum dieksekusi; belum ada bukti alur sandbox BNI berjalan. Keputusan apakah prototipe akan dibangun atau diuji belum ada. Semua pernyataan keamanan di atas adalah rancangan tertulis, bukan hasil audit.

## Sumber

- Dokumen "BNI Sandbox Tester - Source Android dan Backend.docx" (diteruskan untuk pencatatan; tidak dipublikasikan utuh).
- Rujukan dalam dokumen: README SDK bni-nodejs (https://github.com/bni-api/bni-nodejs-sdk/blob/main/README.md) dan catatan rilis Android Gradle Plugin 8.7 (https://developer.android.com/build/releases/agp-8-7-0-release-notes).
