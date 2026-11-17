# Prototipe BNI Sandbox Tester (dokumen sumber, belum dieksekusi)

Catatan riset. Sumber diperiksa 17 November 2026.

## Ringkasan

Rancangan prototipe mengusulkan aplikasi Android untuk menguji konektivitas ke backend lokal dan meminta saldo dari lingkungan sandbox BNI melalui sebuah SDK. Ini rangkuman desain, bukan hasil build atau uji integrasi.

## Batas dan status

- Rancangan membatasi cakupan ke sandbox dan permintaan baca saldo; tidak mendeskripsikan transfer atau transaksi pembayaran.
- Kredensial sandbox diusulkan tetap di sisi backend, bukan di aplikasi ponsel. Ini pilihan desain tertulis, belum diuji.
- Generator, source proyek, instalasi dependency, unit test, build APK, lint, audit dependency, dan panggilan BNI belum dijalankan. Kode tidak diaudit baris per baris.
- Rujukan yang dicantumkan untuk rancangan awal - README SDK BNI dan catatan rilis Android Gradle Plugin 8.7 - belum diverifikasi ulang. Keaslian dan keamanan dependency juga belum diperiksa.
- Rancangan menyertakan checklist yang belum selesai. Tidak ada hasil tes sandbox yang dapat disimpulkan dari rancangan ini.

## Shortlist opsi koneksi Android ke API bank (belum diuji)

Rancangan berikutnya mengusulkan urutan BNI, BCA, lalu BRI dengan pola SNAP BI, berbeda dari rancangan awal BNI One Gate Payment.

1. **BNI:** menggunakan SDK Node.js dan metode `SnapBI.balanceInquiry()`. Rancangan menyebut perlu kredensial aplikasi, kunci privat RSA, dan channel ID.
2. **BCA:** rancangan menyebut endpoint `POST /openapi/v1.0/access-token/b2b` lalu SNAP balance inquiry; persyaratan yang disebut meliputi partner/corporate ID, channel ID, akun KlikBCA Bisnis terdaftar, dan tanda tangan permintaan.
3. **BRI:** rancangan menyebut `POST /snap/v1.0/access-token/b2b` dan `POST /snap/v1.0/balance-inquiry`; persyaratan yang disebut meliputi registrasi partner, kunci RSA, tanda tangan HMAC, dan entitlement layanan AIS. Rancangan menyebut masa berlaku token 15 menit.

Semua endpoint dan persyaratan di atas adalah klaim rancangan, belum diverifikasi ke dokumentasi resmi. Prinsip yang diusulkan adalah menaruh kredensial dan kunci bank di backend, dengan token sesi internal berumur singkat di aplikasi. Tidak ada koneksi API yang dilakukan.

**Pemeriksaan dokumentasi:** repositori `bni-api/bni-nodejs-sdk` dan dokumentasi developer BCA tersedia (tautan di bawah). Halaman dokumentasi SNAP BRI dikutip dalam rancangan tetapi tidak terbaca saat diperiksa; keberadaannya belum dapat dipastikan.

## Bagian terbuka

Source belum dieksekusi; belum ada bukti alur sandbox BNI berjalan. Keputusan apakah prototipe akan dibangun atau diuji belum ada. Semua pernyataan keamanan di atas adalah rancangan tertulis, bukan hasil audit.

## Sumber

- Cakupan catatan ini dibatasi pada ringkasan rancangan; source code tidak disertakan.
- Rujukan yang dicantumkan untuk rancangan awal: README SDK bni-nodejs (https://github.com/bni-api/bni-nodejs-sdk/blob/main/README.md) dan catatan rilis Android Gradle Plugin 8.7 (https://developer.android.com/build/releases/agp-8-7-0-release-notes).
