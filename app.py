import streamlit as st
from fpdf import FPDF
from datetime import datetime

st.set_page_config(page_title="Cute Agreement", page_icon="💖", layout="centered")


# ------------------- ROMANTIC UI CSS -----------------------
romantic_css = """
<style>

@import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Quicksand:wght@400;600&display=swap');

/* Background full of emojis */
body {
    background: #ffe6f3;
    background-image:
        url("https://em-content.zobj.net/source/apple/391/sparkling-heart_1f496.png"),
        url("https://em-content.zobj.net/source/apple/391/two-hearts_1f495.png"),
        url("https://em-content.zobj.net/source/apple/391/pink-heart_1f497.png");
    background-size: 80px, 90px, 70px;
    background-repeat: repeat;
    background-blend-mode: lighten;
}

/* Cute romantic titles */
.romantic-title {
    font-family: 'Pacifico', cursive;
    font-size: 45px;
    color: #ff3e96;
    text-shadow: 0 0 12px rgba(255, 130, 180, 0.5);
}

/* Normal text font */
body, p, label, div {
    font-family: 'Quicksand', sans-serif;
    font-size: 18px;
}

/* Glass Card */
.block-style {
    background: rgba(255, 240, 248, 0.75);
    padding: 30px 35px;
    border-radius: 22px;
    box-shadow: 0 4px 20px rgba(255, 105, 180, 0.3);
    backdrop-filter: blur(8px);
}

/* Glow Buttons */
.stButton button {
    background: linear-gradient(135deg, #ff7dcf, #ff48a9);
    color: white;
    padding: 14px 28px;
    border-radius: 15px;
    border: none;
    font-size: 20px;
    font-weight: bold;
    font-family: 'Quicksand';
    box-shadow: 0 4px 12px rgba(255, 70, 150, 0.5);
    transition: 0.2s ease;
}
.stButton button:hover {
    transform: scale(1.07);
    box-shadow: 0 4px 16px rgba(255, 70, 150, 0.7);
}

/* Floating Hearts Animation */
@keyframes float {
    0% { transform: translateY(0) scale(1); opacity:1; }
    100% { transform: translateY(-60px) scale(1.3); opacity:0; }
}

.emoji-heart {
    position: fixed;
    bottom: 30px;
    right: 40px;
    font-size: 30px;
    animation: float 2.5s infinite ease-in-out;
}
.emoji-heart2 {
    position: fixed;
    bottom: 80px;
    left: 30px;
    font-size: 35px;
    animation: float 3s infinite ease-in-out;
}

</style>

<div class="emoji-heart">💗</div>
<div class="emoji-heart2">💖</div>
"""

st.markdown(romantic_css, unsafe_allow_html=True)

# ---------------- PAGE CONTROLLER ----------------
if "page" not in st.session_state:
    st.session_state.page = 1


def go_to_page(p):
    st.session_state.page = p


# ---------------- PAGE 1 ----------------
if st.session_state.page == 1:

    st.markdown("<h1 class='romantic-title' style='text-align:center;'>💖 Hi Bestie 💖</h1>", unsafe_allow_html=True)

    st.markdown(
        "<div class='block-style' style='text-align:center;font-size:22px;'>"
        "Hello Mam aapke liye ek cute sa surprise banaya hai 😄💗"
        "</div><br>",
        unsafe_allow_html=True
    )

    st.button("Next ➜", on_click=lambda: go_to_page(2))


# ---------------- PAGE 2 ----------------
elif st.session_state.page == 2:

    st.markdown("<h2 class='romantic-title' style='text-align:center;'>💛 Our Cute Agreement 💛</h2>", unsafe_allow_html=True)

    st.markdown("<div class='block-style'>", unsafe_allow_html=True)

    st.write("Bas ye cute rules follow karne hai 😄👇")

    points_ui = {
        "p1": "Tu hamesha happy rahegi 😊",
        "p2": "Hum ek dusre ka support system rahenge 💪",
        "p3": "No ignoring rule 😤😂",
        "p4": "Hum week me ek baar meet karenge 🥹",
        "p5": "Tu apna khayal properly rakhegi ✨",
        "p6": "Mahine mein 2-3 baar date karlenge 💕",
        "p7": "Humesha ek dusre ko respect karenge 🙌",
        "p8": "Har din ek dusre ko appreciate karenge 🌸",
        "p9": "Hum agar ladenge bhi to phir se patchup karlenge 😅",
        "p10": "Tu hamesha meri best friend rahegi 💖",
        "p11": "Kabhi kabhi tu mujhe woh permissions bhi degi you know cutie what I say",
        "p12": "Hum dono milke life ko enjoy karenge 🎉",        
                }

    points_pdf = {k: v.encode("latin-1", "ignore").decode() for k, v in points_ui.items()}

    checked = {}
    for key, text in points_ui.items():
        checked[key] = st.checkbox(text)

    name = st.text_input("Sign ke liye apna naam ✍️:")

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("I Agree Idiot 💛"):
        if all(checked.values()) and name.strip() != "":
            st.session_state.name = name
            st.session_state.points_pdf = points_pdf
            go_to_page(3)
        else:
            st.error("Sab points tick kar aur naam likh 😄✨")


# ---------------- PAGE 3 (PDF DOWNLOAD) ----------------
elif st.session_state.page == 3:

    st.markdown("<h2 class='romantic-title' style='text-align:center;'>🎉 Agreement Ready! 🎉</h2>",
                unsafe_allow_html=True)

    st.markdown("<div class='block-style'>", unsafe_allow_html=True)
    st.write("Neeche se apna cute agreement PDF download kar le 😄💗")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(0, 10, "Our Cute Agreement", ln=True, align="C")
    pdf.ln(5)

    pdf.set_font("Arial", size=12)
    for p in st.session_state.points_pdf.values():
        pdf.cell(0, 8, f"- {p}", ln=True)

    pdf.ln(10)
    pdf.cell(0, 10, f"Signed by: {st.session_state.name}", ln=True)
    pdf.cell(0, 10, f"Date: {datetime.now().strftime('%d-%m-%Y')}", ln=True)

    pdf_bytes = pdf.output(dest='S').encode('latin-1')

    st.download_button(
        label="📄 Download Agreement PDF",
        data=pdf_bytes,
        file_name="CuteAgreement.pdf",
        mime="application/pdf"
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.success("PDF ready! Apne phone me save kar lena 💖")

    st.title("🔥 Cute Agreement v2 Live")
