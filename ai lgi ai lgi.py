<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Skor Efektivitas Obat</title>
    <style>
        body (
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(to left, #691b1b, #691b1b);
            text-align: center;
        )
        .container {
            max-width: 500px;
            margin: 50px auto;
            padding: 20px;
            background: #e2ceb1;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        }
        input, button {
            margin-top: 10px;
            padding: 10px;
            width: 90%;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        button {
            background: #691b1b;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background: #000000;
        }
        .header {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }
        .header img {
            width: 40px;
            height: 40px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="image-removebg-preview.png" alt="Obat">
            <h2>Skor Efektivitas Obat</h2>
        </div>
        <input type="text" id="gejala" placeholder="Masukkan gejala...">
        <button onclick="cariObat()">Cari Obat</button>
        <p id="hasil"></p>
        <p id="keterangan"></p>
    </div>

    <script>
        function cariObat() {
            let gejala = document.getElementById("gejala").value.toLowerCase();
            let hasil = "";
            let keterangan = "";
            
            const daftarObat = {
                "perut kembung": { penyakit: "Gastritis", obat: "Antasida, Omeprazole", skor: 4.0 },
                "mual": { penyakit: "Gastritis", obat: "Antasida, Omeprazole", skor: 4.0 },
                "sakit perut": { penyakit: "Gastritis", obat: "Antasida, Omeprazole", skor: 4.0 },
                "demam": { penyakit: "Flu", obat: "Paracetamol, Ibuprofen", skor: 4.5 },
                "batuk": { penyakit: "Infeksi Saluran Pernapasan", obat: "Dextromethorphan, Guaifenesin", skor: 4.2 },
                "batuk kering": { penyakit: "Iritasi tenggorokan", obat: "Dextromethorphan, Antihistamin", skor: 4.1 },
                "batuk berdahak": { penyakit: "Infeksi saluran pernapasan", obat: "Guaifenesin, Bromhexine", skor: 4.3 },
                "pilek": { penyakit: "Flu", obat: "Antihistamin, Dekongestan", skor: 4.0 },
                "sakit kepala": { penyakit: "Migrain", obat: "Paracetamol, Ibuprofen", skor: 4.3 },
                "pusing": { penyakit: "Vertigo", obat: "Betahistine, Dimenhydrinate", skor: 4.1 },
                "nyeri sendi": { penyakit: "Artritis", obat: "Ibuprofen, Naproxen", skor: 4.3 },
                "nyeri otot": { penyakit: "Cedera otot", obat: "Paracetamol, Ibuprofen", skor: 4.0 },
                "sakit gigi": { penyakit: "Infeksi gigi", obat: "Ibuprofen, Asam Mefenamat", skor: 4.4 },
                "sakit tenggorokan": { penyakit: "Radang tenggorokan", obat: "Lozenges, Ibuprofen", skor: 4.2 },
                "mimisan": { penyakit: "Iritasi hidung", obat: "Oksimetazolin, Air garam", skor: 3.8 },
                "diare": { penyakit: "Infeksi pencernaan", obat: "Loperamide, Oralit", skor: 4.3 },
                "sembelit": { penyakit: "Konstipasi", obat: "Laksatif, Serat tambahan", skor: 4.1 },
                "asam lambung": { penyakit: "GERD", obat: "Omeprazole, Ranitidine", skor: 4.4 },
                "muntah": { penyakit: "Mual", obat: "Domperidone, Metoclopramide", skor: 4.2 },
                "gatal-gatal": { penyakit: "Alergi", obat: "Cetirizine, Loratadine", skor: 4.3 },
                "ruam kulit": { penyakit: "Dermatitis", obat: "Hidrokortison, Antihistamin", skor: 4.0 },
                "sesak napas": { penyakit: "Asma", obat: "Salbutamol, Kortikosteroid inhalasi", skor: 4.5 }
            };
            
            function getKeteranganSkor(skor) {
                if (skor <= 1) return "Tidak efektif";
                if (skor <= 2) return "Kurang efektif";
                if (skor <= 3) return "Cukup efektif";
                if (skor <= 4) return "Efektif";
                return "Sangat efektif";
            }
            
            if (daftarObat[gejala]) {
                let data = daftarObat[gejala];
                hasil = `Penyakit: ${data.penyakit}<br>Obat yang direkomendasikan: ${data.obat}<br>Skor Efektivitas: ${data.skor}`;
                keterangan = `Kategori: ${getKeteranganSkor(data.skor)}`;
            } else {
                hasil = "Gejala tidak ditemukan. Konsultasikan dengan dokter.";
                keterangan = "";
            }
            
            document.getElementById("hasil").innerHTML = hasil;
            document.getElementById("keterangan").innerHTML = keterangan;
        }
    </script>
</body>
</html>
