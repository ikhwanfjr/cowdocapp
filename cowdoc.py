import streamlit as st

st.set_page_config(page_title="CowDoc", layout="centered")

# === Knowledge Base ===
rules = [
    {
        "penyakit": "Penyakit Antrax (Radang Limpa)",
        "gejala": ["Demam tinggi, gemetar, berjalan sempoyongan, kondisi lemah, ambruk",
                   "Kematian Mendadak",
                   "Kesulitan Bernafas"],
        "solusi": "Isolasi segera hewan yang terduga terinfeksi, jangan membedah bangkai agar bakteri tidak menyebar, dan segera laporkan ke dinas peternakan."
    },
    {
        "penyakit": "Septichaemia Epizotica (SE/Ngorok)",
        "gejala": ["Keluar air liur terus menerus",
                   "Tubuh gemetar",
                   "Pada kondisi kronis hewan menjadi kurus dan sering batuk, nafsu makan terganggu"],
        "solusi": "Isolasi hewan yang terinfeksi, berikan antibiotik spektrum luas seperti oksitetrasiklin dan pastikan hewan tidak stress."
    },
    {
        "penyakit": "Surra (Trypanosomiasis/Penyakit Mubeng)",
        "gejala": ["Anemia, kurus, bulu rontok, busung daerah dagu dan anggota gerak dan akhirnya akan mati",
                   "Keluar getah radang dari hidung dan mata",
                   "Jalan sempoyongan, kejang dan berputar putar (mubeng)"],
        "solusi": "Isolasi, segera beri obat trypanocidal seperti diminazen aceturate, dan kendalikan vektor (lalat penghisap darah) dengan insektisida."
    },
    {
        "penyakit": "Malignant Catharral Fever (MCF) atau Penyakit Ingusan",
        "gejala": ["Demam tinggi 40 – 41 Derajat Calcius",
                   "Kondisi badan menurun, lemah dan menjadi kurus",
                   "Otot-otot menjadi gemetar, berjalan sempoyongan, torticolis dan bersifat agresif",
                   "Kematian terjadi biasanya antara 4-13 hari setelah timbul gejala penyakit"],
        "solusi": "Isolasi dan berikan perawatan suportif seperti vitamin dan antiinflamasi."
    },
    {
        "penyakit": "Scabies (Budug, Manga, Kudis Menular)",
        "gejala": ["Hewan menggosok-gosokkan badan pada dinding kandang serta menggigit-gigit bagian tubuh yang terserang penyakit sehingga terjadi luka-luka dan lecet",
                   "Kerak pada permukaan kulit berwarna keabuan"],
        "solusi": "Isolasi, bersihkan kandang dan semprot dengan desinfektan/insektisida, dan mandikan hewan dengan larutan obat anti-kutu."
    },
    {
        "penyakit": "Bovine Ephemeral Fever (BEF / Demam Tiga hari)",
        "gejala": ["Kelemahan anggota gerak sampai tidak sanggup berdiri",
                   "Keluar sedikit cairan dari mata dan hidung",
                   "Pada sapi menyusui, produksi air susu turun atau terhenti sama sekali"],
        "solusi": "Berikan antiinflamasi dan vitamin, serta cukup air minum."
    },
    {
        "penyakit": "Helminthiasis (Cacingan)",
        "gejala": ["Badan Kurus",
                   "Bulu kusam dan berdiri",
                   "Diare atau bahkan sembelit"],
        "solusi": "Berikan obat cacing seperti albendazole atau ivermectin, serta bersihkan kandang."
    },
    {
        "penyakit": "Brucellosis (Keluron Menular)",
        "gejala": ["Pada sapi betina gejala keguguran, biasanya terjadi pada kebuntingan 5 - 8 bulan, kadang diikuti dengan kemajiran. Pada ternak jantan terjadi kebengkakan pada testes dan persendian lutut",
                   "Perubahan pasca mati yang terlihat adalah penebalan pada plasenta dengan bercak-bercak pada permukaan lapisan chorion. cairan janin terlihat keruh berwarna kuning coklat dan kadang-kadang bercampur nanah. Pada ternak jantan ditemukan proses pernanahan pada testis yang dapat diikuti dengan nekrose"],
        "solusi": "Isolasi, jangan sentuh cairan atau jaringan abortus tanpa pelindung, dan segera laporkan ke dinas peternakan."
    },
    {
        "penyakit": "Mastitis (Radang Ambing)",
        "gejala": ["Kebengkakan ambing",
                   "Air susu berubah sifat, menjadi pecah, bercampur endapan atau jonjot fibrin"],
        "solusi": "Lakukan pemerahan rutin pada ambing yang sakit, cuci dan desinfeksi ambing sebelum dan sesudah pemerahan, dan gunakan antibiotik intramammary."
    },
    {
        "penyakit": "Pink Eye (Penyakit Mata)",
        "gejala": ["Mata berair, kemerahan pada bagian mata yang putih dan kelopaknya",
                   "Selaput bening mata/kornea menjadi keruh"],
        "solusi": "Isolasi, bersihkan mata dengan larutan salin steril, dan berikan tetes mata antibiotik atau salep mata."
    },
    {
        "penyakit": "Penyakit Mulut dan Kuku (PMK)",
        "gejala": ["Demam tinggi 40 – 41 Derajat Calcius",
                   "Mengalami anorexia (tidak nafsu makan)",
                   "Penurunan produksi susu yang drastis pada sapi perah untuk 2-3 hari",
                   "Saliva terlihat menggantung, air liur berbusa di lantai kandang",
                   "Hewan lebih sering berbaring",
                   "Luka pada kuku dan kukunya lepas",
                   "Menggeretakan gigi, menggosokkan mulut, leleran mulut, suka menendangkan kaki",
                   "Keluar air liur berlebihan disertai busa"],
        "solusi": "Isolasi, disinfeksi kandang, berikan perawatan suportif, dan segera lapor ke dinas peternakan."
    }
]

# === Inference Engine ===
def diagnosa(gejala_input):
    for rule in rules:
        if all(g in gejala_input for g in rule["gejala"]):
            return rule
    return None

# === User Interface ===
st.title("🐄 CowDoc 🐄")

st.image("sapi.jpg", use_container_width=True)

st.markdown("""
<div style="text-align: justify; font-size:16px; padding-top: 10px;">
    <strong>CowDoc</strong> merupakan sistem pakar berbasis komputer yang dirancang untuk membantu peternak dalam mendiagnosa penyakit pada 
    ternak sapi secara cepat dan  mandiri berdasarkan gejala klinis yang terlihat. Sistem ini bekerja dengan meniru cara berpikir peternak/dokter 
    melalui metode inferensi forward chaining. gejala yang di input oleh pengguna akan diproses dan dicocokkan dengan basis pengetahuan yang 
    telah dirancang oleh para ahli.
    <br>
    <br>
    CowDoc akan menampilkan hasil diagnosis berupa penyakit yang memungkinkan menyerang sapi, disertai dengan saran penanganan awal yang sesuai.
""", unsafe_allow_html=True)

st.markdown("---")
st.write("Pilih gejala yang dialami oleh ternak sapi Anda:")

gejala_list = [
    "Demam tinggi, gemetar, berjalan sempoyongan, kondisi lemah, ambruk",
    "Kematian Mendadak",
    "Kesulitan Bernafas",
    "Keluar air liur terus menerus",
    "Tubuh gemetar",
    "Pada kondisi kronis hewan menjadi kurus dan sering batuk, nafsu makan terganggu",
    "Anemia, kurus, bulu rontok, busung daerah dagu dan anggota gerak dan akhirnya akan mati",
    "Keluar getah radang dari hidung dan mata",
    "Jalan sempoyongan, kejang dan berputar putar (mubeng)",
    "Demam tinggi 40 – 41 Derajat Calcius",
    "Kondisi badan menurun, lemah dan menjadi kurus",
    "Otot-otot menjadi gemetar, berjalan sempoyongan, torticolis dan bersifat agresif",
    "Kematian terjadi biasanya antara 4-13 hari setelah timbul gejala penyakit",
    "Hewan menggosok-gosokkan badan pada dinding kandang serta menggigit-gigit bagian tubuh yang terserang penyakit sehingga terjadi luka-luka dan lecet",
    "Kerak pada permukaan kulit berwarna keabuan",
    "Kelemahan anggota gerak sampai tidak sanggup berdiri",
    "Keluar sedikit cairan dari mata dan hidung",
    "Pada sapi menyusui, produksi air susu turun atau terhenti sama sekali",
    "Badan Kurus",
    "Bulu kusam dan berdiri",
    "Diare atau bahkan sembelit",
    "Mata berair, kemerahan pada bagian mata yang putih dan kelopaknya",
    "Selaput bening mata/kornea menjadi keruh",
    "Kebengkakan ambing",
    "Air susu berubah sifat, menjadi pecah, bercampur endapan atau jonjot fibrin",
    "Pada sapi betina gejala keguguran, biasanya terjadi pada kebuntingan 5 - 8 bulan, kadang diikuti dengan kemajiran. Pada ternak jantan terjadi kebengkakan pada testes dan persendian lutut",
    "Perubahan pasca mati yang terlihat adalah penebalan pada plasenta dengan bercak-bercak pada permukaan lapisan chorion. cairan janin terlihat keruh berwarna kuning coklat dan kadang-kadang bercampur nanah. Pada ternak jantan ditemukan proses pernanahan pada testis yang dapat diikuti dengan nekrose",
    "Mengalami anorexia (tidak nafsu makan)",
    "Penurunan produksi susu yang drastis pada sapi perah untuk 2-3 hari",
    "Saliva terlihat menggantung, air liur berbusa di lantai kandang",
    "Hewan lebih sering berbaring",
    "Luka pada kuku dan kukunya lepas",
    "Menggeretakan gigi, menggosokkan mulut, leleran mulut, suka menendangkan kaki",
    "Keluar air liur berlebihan disertai busa"
]

selected_gejala = []
for gejala in gejala_list:
    if st.checkbox(gejala):
        selected_gejala.append(gejala)

if st.button("Diagnosa Sekarang"):
    hasil = diagnosa(selected_gejala)
    if hasil:
        st.success(f"### Penyakit: {hasil['penyakit']}")
        st.markdown(f"**Solusi:** {hasil['solusi']}")
    else:
        st.warning("Gejala yang dipilih belum cukup untuk menyimpulkan penyakit tertentu. Silakan periksa kembali.")

# === Footer ===
st.markdown("""
<br><hr>
<div style="text-align: center; font-size: 14px;">
    &copy; 2025 CowDoc. Sistem Pakar Diagnosa Penyakit Pada Hewan Ternak Sapi.<br>
    Ikhwan Fajar Khatamy (2255061007) Siti Fatiha Diza Rahman (2215061084) Deti Dwi Anugra (2215061058) 
</div>
""", unsafe_allow_html=True)