import streamlit as st

st.set_page_config(page_title="CowDoc", layout="centered")

# === Knowledge Base ===
rules = [
    {
        "penyakit": "Antraks",
        "gejala": ["Nafsu Makan Menurun", "Suhu Tubuh Tinggi", "Luka Pada Kulit", "Lesu dan Tidak Aktif"],
        "solusi": "Segera hubungi dokter hewan."
    },
    {
        "penyakit": "Penyakit Mulut dan Kuku (PMK)",
        "gejala": ["Diare", "Luka Pada Kulit", "Perut Kembung"],
        "solusi": "Cuci luka, hindari kontak dengan ternak lain."
    },
    {
        "penyakit": "Pneumonia",
        "gejala": ["Nafsu Makan Menurun", "Suhu Tubuh Tinggi", "Keluarnya Lendir dari Hidung", "Batuk"],
        "solusi": "Isolasi, beri antibiotik dan vitamin."
    },
    {
        "penyakit": "Diare Akut",
        "gejala": ["Nafsu Makan Menurun", "Suhu Tubuh Tinggi", "Diare"],
        "solusi": "Berikan oralit, dan jaga kebersihan kandang."
    },
    {
        "penyakit": "Mastitis",
        "gejala": ["Produksi Susu Menurun", "Lesu dan Tidak Aktif", "Suhu Tubuh Tinggi"],
        "solusi": "Periksa ambing, kompres hangat, beri antibiotik."
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
    "Nafsu Makan Menurun",
    "Suhu Tubuh Tinggi",
    "Diare",
    "Keluarnya Lendir dari Hidung",
    "Batuk",
    "Luka Pada Kulit",
    "Lesu dan Tidak Aktif",
    "Mata Berair",
    "Perut Kembung",
    "Produksi Susu Menurun"
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