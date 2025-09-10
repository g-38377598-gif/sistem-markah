import streamlit as st
import pandas as pd

st.title("📊 Sistem Markah Pelajar")

# Simpan data dalam session
if "pelajar" not in st.session_state:
    st.session_state["pelajar"] = []

def kira_gred(markah):
    if markah >= 80:
        return "A"
    elif markah >= 65:
        return "B"
    elif markah >= 50:
        return "C"
    else:
        return "Gagal"

# Input pelajar baru
with st.form("pelajar_form"):
    nama = st.text_input("Nama Pelajar")
    markah = st.number_input("Markah", 0, 100, 50)
    submit = st.form_submit_button("Tambah")

    if submit and nama:
        gred = kira_gred(markah)
        st.session_state["pelajar"].append({"Nama": nama, "Markah": markah, "Gred": gred})
        st.success(f"{nama} ditambah dengan gred {gred}")

# Paparan data
if st.session_state["pelajar"]:
    df = pd.DataFrame(st.session_state["pelajar"])
    st.table(df)

    purata = df["Markah"].mean()
    st.write(f"**Purata Kelas:** {purata:.2f}")

    # Graf taburan markah
    st.bar_chart(df.set_index("Nama")["Markah"])
