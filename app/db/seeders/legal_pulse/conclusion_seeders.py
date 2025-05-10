from app.db.database import lp_conclusion_collection
from app.core.security import hash_password
import datetime
import uuid


async def seed_conclusions():
  conclusions = [
  {
    "title": "Penanganan Kekerasan Seksual dalam KUHP",
    "category": "Hukum Pidana",
    "body": "Diskusi ini membahas mekanisme penanganan kekerasan seksual dalam KUHP, termasuk perlindungan korban dan hukuman bagi pelaku.",
    "uu_reference": [
      "Pasal 285 KUHP",
      "Pasal 286 KUHP",
      "UU No. 12 Tahun 2022 tentang TPKS"
    ],
    "keyword": "Kekerasan Seksual"
  },
  {
    "title": "Sanksi Pidana bagi Pelanggaran Lalu Lintas",
    "category": "Hukum Lalu Lintas",
    "body": "Pembahasan mengenai sanksi pidana terhadap pelanggar aturan lalu lintas, seperti tilang elektronik dan penahanan SIM.",
    "uu_reference": [
      "Pasal 310 UU No. 22 Tahun 2009",
      "Pasal 313 UU No. 22 Tahun 2009"
    ],
    "keyword": "Tilang Elektronik"
  },
  {
    "title": "Hak dan Kewajiban Wajib Pajak dalam Sistem Perpajakan",
    "category": "Hukum Pajak",
    "body": "Diskusi seputar hak dan kewajiban wajib pajak, serta sanksi bagi mereka yang tidak memenuhi kewajiban pajaknya.",
    "uu_reference": [
      "Pasal 1 UU No. 28 Tahun 2007",
      "Pasal 39 UU KUP"
    ],
    "keyword": "Kewajiban Pajak"
  },
  {
    "title": "Perlindungan Hak Cipta Digital dalam UU Hak Cipta",
    "category": "Hukum Perdata",
    "body": "Pembahasan mengenai hak cipta digital dan perlindungan hukum terhadap pelanggaran hak cipta di dunia digital.",
    "uu_reference": [
      "Pasal 40 UU No. 28 Tahun 2014",
      "Pasal 113 UU Hak Cipta"
    ],
    "keyword": "Hak Cipta Digital"
  },
  {
    "title": "Penyelesaian Sengketa Perdata di Pengadilan",
    "category": "Hukum Perdata",
    "body": "Diskusi tentang prosedur penyelesaian sengketa perdata di pengadilan, mulai dari gugatan hingga putusan hakim.",
    "uu_reference": [
      "Pasal 118 HIR",
      "Pasal 124 RBg"
    ],
    "keyword": "Sengketa Perdata"
  },
  {
    "title": "Ketentuan Baru dalam KUHP 2023",
    "category": "Hukum Pidana",
    "body": "Pembahasan mengenai perubahan-perubahan dalam KUHP 2023, termasuk ketentuan baru terkait hukum pidana di Indonesia.",
    "uu_reference": [
      "UU No. 1 Tahun 2023 tentang KUHP"
    ],
    "keyword": "KUHP Baru 2023"
  },
  {
    "title": "Tanggung Jawab Hukum Perusahaan terhadap Pajak",
    "category": "Hukum Pajak",
    "body": "Pembahasan mengenai kewajiban pajak yang harus dipenuhi oleh perusahaan dan sanksi yang berlaku jika terjadi pelanggaran.",
    "uu_reference": [
      "Pasal 7 UU No. 36 Tahun 2008",
      "Pasal 17B UU KUP"
    ],
    "keyword": "Pajak Perusahaan"
  },
  {
    "title": "Aturan Parkir Liar dan Sanksinya",
    "category": "Hukum Lalu Lintas",
    "body": "Diskusi mengenai aturan dan sanksi bagi pengendara yang parkir sembarangan di wilayah publik dan mengganggu ketertiban umum.",
    "uu_reference": [
      "Pasal 287 UU No. 22 Tahun 2009",
      "Pasal 289 UU Lalu Lintas"
    ],
    "keyword": "Parkir Liar"
  },
  {
    "title": "Penyelesaian Sengketa Pajak melalui Pengadilan Pajak",
    "category": "Hukum Pajak",
    "body": "Pembahasan mengenai prosedur penyelesaian sengketa pajak melalui pengadilan pajak dan alternatif penyelesaian lainnya.",
    "uu_reference": [
      "Pasal 23 UU No. 14 Tahun 2002",
      "Pasal 36A UU KUP"
    ],
    "keyword": "Sengketa Pajak"
  },
  {
    "title": "Perlindungan Konsumen dalam Transaksi Online",
    "category": "Hukum Perdata",
    "body": "Diskusi tentang perlindungan hak konsumen dalam transaksi online serta mekanisme pengaduan jika terjadi pelanggaran.",
    "uu_reference": [
      "Pasal 4 UU No. 8 Tahun 1999",
      "Pasal 62 UU Perlindungan Konsumen"
    ],
    "keyword": "Perlindungan Konsumen"
  },{
    "title": "Hukuman bagi Pelaku Tindak Pidana Korupsi",
    "category": "Hukum Pidana",
    "isi": "Pembahasan mengenai hukuman yang dijatuhkan kepada pelaku tindak pidana korupsi sesuai dengan peraturan yang berlaku.",
    "uu_reference": [
      "Pasal 2 UU No. 31 Tahun 1999",
      "Pasal 3 UU Tipikor"
    ],
    "keyword": "Tindak Pidana Korupsi"
  },
  {
    "title": "Sanksi bagi Penghindar Pajak di Indonesia",
    "category": "Hukum Pajak",
    "isi": "Diskusi tentang konsekuensi hukum bagi wajib pajak yang menghindari kewajiban perpajakan, termasuk sanksi administratif dan pidana.",
    "uu_reference": [
      "Pasal 39 UU KUP",
      "Pasal 43 UU No. 36 Tahun 2008"
    ],
    "keyword": "Penghindaran Pajak"
  },
  {
    "title": "Aturan Keselamatan Berkendara di Jalan Raya",
    "category": "Hukum Lalu Lintas",
    "isi": "Pembahasan mengenai regulasi yang mengatur keselamatan berkendara di jalan raya serta sanksi bagi pelanggarnya.",
    "uu_reference": [
      "Pasal 106 UU No. 22 Tahun 2009",
      "Pasal 207 UU No. 22 Tahun 2009"
    ],
    "keyword": "Keselamatan Berkendara"
  },
  {
    "title": "Hak dan Kewajiban Konsumen dalam Perjanjian Jual Beli",
    "category": "Hukum Perdata",
    "isi": "Diskusi mengenai hak dan kewajiban konsumen dalam transaksi jual beli serta perlindungan hukum bagi konsumen.",
    "uu_reference": [
      "Pasal 4 UU No. 8 Tahun 1999",
      "Pasal 19 UU Perlindungan Konsumen"
    ],
    "keyword": "Hak Konsumen"
  },
  {
    "title": "Penipuan dalam Transaksi Digital dan Hukumnya",
    "category": "Hukum Pidana",
    "isi": "Pembahasan mengenai kejahatan penipuan dalam transaksi digital serta ketentuan hukum yang mengaturnya.",
    "uu_reference": [
      "Pasal 28 UU ITE",
      "Pasal 378 KUHP"
    ],
    "keyword": "Penipuan Digital"
  },
  {
    "title": "Prosedur Penyelidikan Kecelakaan Lalu Lintas",
    "category": "Hukum Lalu Lintas",
    "isi": "Pembahasan mengenai prosedur penyelidikan kecelakaan lalu lintas oleh pihak berwenang dan hak korban kecelakaan.",
    "uu_reference": [
      "Pasal 229 UU No. 22 Tahun 2009",
      "Pasal 231 UU Lalu Lintas"
    ],
    "keyword": "Kecelakaan Lalu Lintas"
  },
  {
    "title": "Hak Waris dan Pembagian Harta dalam Hukum Perdata",
    "category": "Hukum Perdata",
    "isi": "Diskusi tentang ketentuan hukum yang mengatur hak waris dan pembagian harta bagi ahli waris.",
    "uu_reference": [
      "Pasal 832 KUH Perdata",
      "Pasal 874 KUH Perdata"
    ],
    "keyword": "Hak Waris"
  },
  {
    "title": "Perlindungan Pekerja terhadap Pemutusan Hubungan Kerja (PHK)",
    "category": "Hukum Perdata",
    "isi": "Pembahasan mengenai hak-hak pekerja dalam kasus PHK serta ketentuan hukum yang mengatur kompensasi bagi pekerja yang terkena PHK.",
    "uu_reference": [
      "Pasal 151 UU No. 13 Tahun 2003",
      "Pasal 156 UU Ketenagakerjaan"
    ],
    "keyword": "Pemutusan Hubungan Kerja"
  },
  {
    "title": "Sanksi Bagi Pengemudi yang Mengemudi dalam Kondisi Mabuk",
    "category": "Hukum Lalu Lintas",
    "isi": "Diskusi mengenai sanksi yang diberikan kepada pengemudi yang berkendara dalam kondisi mabuk dan membahayakan pengguna jalan lainnya.",
    "uu_reference": [
      "Pasal 311 UU No. 22 Tahun 2009",
      "Pasal 315 UU Lalu Lintas"
    ],
    "keyword": "Mengemudi dalam Keadaan Mabuk"
  },
  {
    "title": "Regulasi Pajak E-Commerce di Indonesia",
    "category": "Hukum Pajak",
    "isi": "Pembahasan mengenai aturan pajak yang berlaku bagi pelaku usaha e-commerce di Indonesia serta kewajiban yang harus dipenuhi.",
    "uu_reference": [
      "PMK No. 210/PMK.010/2018",
      "Pasal 23 UU PPh"
    ],
    "keyword": "Pajak E-Commerce"
  },
  {
    "title": "Penerapan Hukuman Mati dalam Kasus Narkotika",
    "category": "Hukum Pidana",
    "isi": "Diskusi mengenai penerapan hukuman mati bagi pelaku tindak pidana narkotika di Indonesia serta dasar hukumnya.",
    "uu_reference": [
      "Pasal 113 UU No. 35 Tahun 2009",
      "Pasal 114 UU Narkotika"
    ],
    "keyword": "Hukuman Mati Narkotika"
  },
  {
    "title": "Sanksi bagi Wajib Pajak yang Tidak Melaporkan SPT",
    "category": "Hukum Pajak",
    "isi": "Pembahasan tentang konsekuensi hukum bagi wajib pajak yang tidak melaporkan Surat Pemberitahuan (SPT) Tahunan sesuai dengan ketentuan yang berlaku.",
    "uu_reference": [
      "Pasal 39 UU KUP",
      "Pasal 41 UU No. 28 Tahun 2007"
    ],
    "keyword": "Sanksi Pajak"
  },
  {
    "title": "Kewajiban Pengendara Menggunakan Helm Standar SNI",
    "category": "Hukum Lalu Lintas",
    "isi": "Diskusi mengenai peraturan yang mewajibkan penggunaan helm berstandar SNI bagi pengendara motor serta sanksi bagi pelanggarnya.",
    "uu_reference": [
      "Pasal 106 UU No. 22 Tahun 2009",
      "Pasal 291 UU Lalu Lintas"
    ],
    "keyword": "Helm SNI"
  },
  {
    "title": "Perlindungan Konsumen dalam Transaksi Online",
    "category": "Hukum Perdata",
    "isi": "Pembahasan mengenai hak-hak konsumen dalam transaksi online serta regulasi yang melindungi mereka dari penipuan digital.",
    "uu_reference": [
      "Pasal 4 UU No. 8 Tahun 1999",
      "Pasal 28 UU ITE"
    ],
    "keyword": "Perlindungan Konsumen Online"
  },
  {
    "title": "Pelanggaran Etika dalam Profesi Hukum",
    "category": "Hukum Pidana",
    "isi": "Diskusi mengenai konsekuensi hukum bagi advokat atau pejabat hukum yang melanggar kode etik profesi.",
    "uu_reference": [
      "Pasal 4 UU No. 18 Tahun 2003",
      "Pasal 16 Kode Etik Advokat"
    ],
    "keyword": "Etika Profesi Hukum"
  },
  {
    "title": "Denda bagi Kendaraan yang Tidak Membayar Pajak",
    "category": "Hukum Pajak",
    "isi": "Pembahasan mengenai sanksi administratif bagi pemilik kendaraan bermotor yang tidak membayar pajak tepat waktu.",
    "uu_reference": [
      "Pasal 74 UU No. 28 Tahun 2009",
      "Pasal 288 UU Lalu Lintas"
    ],
    "keyword": "Pajak Kendaraan"
  },
  {
    "title": "Kewajiban Pengusaha Memberikan Upah Sesuai UMK",
    "category": "Hukum Perdata",
    "isi": "Diskusi tentang kewajiban pengusaha untuk membayar upah sesuai dengan upah minimum kota (UMK) yang berlaku.",
    "uu_reference": [
      "Pasal 90 UU No. 13 Tahun 2003",
      "Pasal 88 UU Ketenagakerjaan"
    ],
    "keyword": "Upah Minimum"
  },
  {
    "title": "Ketentuan Hukum tentang Tilang Elektronik (ETLE)",
    "category": "Hukum Lalu Lintas",
    "isi": "Pembahasan mengenai sistem tilang elektronik (ETLE) yang digunakan untuk menindak pelanggaran lalu lintas secara digital.",
    "uu_reference": [
      "Pasal 272 UU No. 22 Tahun 2009",
      "Peraturan Kapolri No. 5 Tahun 2021"
    ],
    "keyword": "Tilang Elektronik"
  },
  {
    "title": "Penyelesaian Sengketa Tanah melalui Pengadilan",
    "category": "Hukum Perdata",
    "isi": "Diskusi mengenai prosedur hukum dalam penyelesaian sengketa tanah melalui jalur pengadilan atau mediasi.",
    "uu_reference": [
      "Pasal 32 UU No. 5 Tahun 1960",
      "Pasal 110 UU Agraria"
    ],
    "keyword": "Sengketa Tanah"
  },
  {
    "title": "Larangan Praktik Monopoli dalam Dunia Usaha",
    "category": "Hukum Perdata",
    "isi": "Pembahasan mengenai larangan praktik monopoli dalam dunia usaha serta sanksi bagi pelaku usaha yang melanggar aturan tersebut.",
    "uu_reference": [
      "Pasal 17 UU No. 5 Tahun 1999",
      "Pasal 25 UU Anti Monopoli"
    ],
    "keyword": "Praktik Monopoli"
  },
  {
    "title": "Tindak Pidana Korupsi dan Hukuman bagi Pelaku",
    "category": "Hukum Pidana",
    "isi": "Diskusi mengenai tindak pidana korupsi di Indonesia, hukuman bagi pelaku, serta dasar hukum yang mengaturnya.",
    "uu_reference": [
      "Pasal 2 UU No. 31 Tahun 1999",
      "Pasal 3 UU Tipikor"
    ],
    "keyword": "Tindak Pidana Korupsi"
  },
  {
    "title": "Sanksi Bagi Pengusaha yang Menghindari Pajak",
    "category": "Hukum Pajak",
    "isi": "Pembahasan mengenai konsekuensi hukum bagi pengusaha yang melakukan penghindaran pajak atau tidak membayar pajak sesuai ketentuan.",
    "uu_reference": [
      "Pasal 39 UU KUP",
      "Pasal 41 UU No. 28 Tahun 2007"
    ],
    "keyword": "Penghindaran Pajak"
  },
  {
    "title": "Kewajiban Kendaraan Bermotor Melakukan Uji Emisi",
    "category": "Hukum Lalu Lintas",
    "isi": "Diskusi mengenai kebijakan uji emisi bagi kendaraan bermotor sebagai salah satu upaya pengurangan polusi udara di kota-kota besar.",
    "uu_reference": [
      "Pasal 206 UU No. 22 Tahun 2009",
      "Peraturan Gubernur No. 66 Tahun 2020"
    ],
    "keyword": "Uji Emisi Kendaraan"
  },
  {
    "title": "Perlindungan Hak Cipta bagi Konten Digital",
    "category": "Hukum Perdata",
    "isi": "Pembahasan mengenai hak cipta bagi konten digital seperti video, musik, dan tulisan serta hukuman bagi pelanggar hak cipta.",
    "uu_reference": [
      "Pasal 40 UU No. 28 Tahun 2014",
      "Pasal 113 UU Hak Cipta"
    ],
    "keyword": "Hak Cipta Digital"
  },
  {
    "title": "Pelanggaran Etika dalam Profesi Kedokteran",
    "category": "Hukum Pidana",
    "isi": "Diskusi tentang kasus pelanggaran kode etik dalam profesi kedokteran dan konsekuensi hukumnya.",
    "uu_reference": [
      "Pasal 75 UU No. 29 Tahun 2004",
      "Kode Etik Kedokteran Indonesia"
    ],
    "keyword": "Etika Kedokteran"
  },
  {
    "title": "Pajak E-Commerce dan Kewajiban Pelaku Usaha Digital",
    "category": "Hukum Pajak",
    "isi": "Pembahasan mengenai pajak yang dikenakan pada transaksi e-commerce serta kewajiban pelaku usaha digital dalam pelaporan pajak.",
    "uu_reference": [
      "PMK No. 48/PMK.03/2020",
      "Pasal 4 UU PPh"
    ],
    "keyword": "Pajak E-Commerce"
  },
  {
    "title": "Sanksi Bagi Pengemudi yang Melanggar Batas Kecepatan",
    "category": "Hukum Lalu Lintas",
    "isi": "Diskusi tentang aturan batas kecepatan di jalan raya serta sanksi bagi pengemudi yang melanggar.",
    "uu_reference": [
      "Pasal 287 UU No. 22 Tahun 2009",
      "Peraturan Menteri Perhubungan No. 111 Tahun 2015"
    ],
    "keyword": "Batas Kecepatan"
  },
  {
    "title": "Hak dan Kewajiban Konsumen dalam Perjanjian Kredit",
    "category": "Hukum Perdata",
    "isi": "Pembahasan mengenai hak dan kewajiban konsumen dalam perjanjian kredit dengan perusahaan pembiayaan atau bank.",
    "uu_reference": [
      "Pasal 18 UU No. 8 Tahun 1999",
      "Pasal 1320 KUHPerdata"
    ],
    "keyword": "Perjanjian Kredit"
  },
  {
    "title": "Tata Cara Pengajuan Gugatan Cerai di Pengadilan",
    "category": "Hukum Perdata",
    "isi": "Diskusi mengenai prosedur hukum dalam pengajuan gugatan cerai di pengadilan agama atau pengadilan negeri.",
    "uu_reference": [
      "Pasal 39 UU No. 1 Tahun 1974",
      "Pasal 19 PP No. 9 Tahun 1975"
    ],
    "keyword": "Gugatan Cerai"
  },
  {
    "title": "Larangan dan Sanksi terhadap Jual Beli Data Pribadi",
    "category": "Hukum Pidana",
    "isi": "Pembahasan mengenai aturan hukum yang melarang praktik jual beli data pribadi serta sanksi bagi pelanggarnya.",
    "uu_reference": [
      "Pasal 26 UU ITE",
      "UU No. 27 Tahun 2022 tentang PDP"
    ],
    "keyword": "Perlindungan Data Pribadi"
  }
]

    # # if persona_collection.count_documents({}) == 0:
    # lp_conclusion_collection.insert_many(conclusions)
  for conclusion in conclusions:
    data = {
      "session_id": str(uuid.uuid4()),  # Generate random session_id
      "conclusion" : conclusion,
      "created_at": datetime.datetime.utcnow().isoformat(),
      "updated_at": datetime.datetime.utcnow().isoformat(),
    }
    result = lp_conclusion_collection.insert_one(data)

