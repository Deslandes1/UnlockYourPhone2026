import streamlit as st
import re

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Unlock Your Phone | Gesner Deslandes",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================================================
# CUSTOM CSS — LIGHT BLUE THEME + BRIGHT COLORED BOX TEXT
# =========================================================
st.markdown("""
<style>
    /* -------- Global — Light Blue Background -------- */
    html, body, .stApp {
        background: linear-gradient(160deg, #4A9EE0 0%, #3A87CC 45%, #2E7BC4 100%) !important;
        background-attachment: fixed !important;
        color: #ffffff !important;
    }

    .main, .block-container, section.main {
        background: transparent !important;
        color: #ffffff !important;
    }

    h1, h2, h3, h4, h5, h6, p, span, div, label, li, ul, ol {
        color: #ffffff;
    }

    /* -------- Hero Header -------- */
    .hero-header {
        background: linear-gradient(180deg, rgba(255,255,255,.18), rgba(255,255,255,.10));
        border: 3px solid #ffffff;
        border-radius: 22px;
        padding: 28px 24px;
        text-align: center;
        margin-bottom: 24px;
        box-shadow: 0 16px 50px rgba(0,0,0,.30), 0 0 60px rgba(255,255,255,.35);
        backdrop-filter: blur(6px);
    }
    .hero-title {
        font-size: clamp(2rem, 5vw, 3.4rem);
        font-weight: 900;
        letter-spacing: 4px;
        line-height: 1.05;
        color: #ffffff !important;
        text-shadow: 0 3px 18px rgba(0,0,0,.35), 0 0 40px rgba(255,255,255,.45);
        margin: 0;
    }
    .hero-subtitle {
        font-size: clamp(1rem, 2vw, 1.4rem);
        font-weight: 800;
        letter-spacing: 4px;
        color: #ffffff !important;
        text-transform: uppercase;
        margin: 8px 0 6px;
        text-shadow: 0 2px 12px rgba(0,0,0,.30);
    }
    .hero-role {
        font-size: clamp(.72rem, 1.2vw, .88rem);
        font-weight: 700;
        letter-spacing: 3px;
        color: #ffffff !important;
        text-transform: uppercase;
        margin-bottom: 16px;
        opacity: .92;
    }
    .hero-contact {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 12px;
        font-size: clamp(.88rem, 1.4vw, 1.05rem);
        font-weight: 800;
    }
    .hero-contact span {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 8px 16px;
        border-radius: 999px;
        background: rgba(255,255,255,.22);
        border: 1px solid rgba(255,255,255,.55);
        color: #ffffff !important;
        backdrop-filter: blur(4px);
    }
    .hero-contact a {
        color: #ffffff !important;
        text-decoration: none;
        font-weight: 900;
        border-bottom: 1px dotted rgba(255,255,255,.7);
    }
    .hero-contact a:hover { color: #FFF9C4 !important; }

    /* -------- Feature Cards -------- */
    .feature-card {
        background: rgba(255,255,255,.16);
        border: 2px solid rgba(255,255,255,.55);
        border-radius: 18px;
        padding: 20px;
        height: 100%;
        box-shadow: 0 10px 30px rgba(0,0,0,.20);
        transition: all .25s ease;
        backdrop-filter: blur(6px);
    }
    .feature-card:hover {
        border-color: #ffffff;
        transform: translateY(-4px);
        box-shadow: 0 14px 40px rgba(0,0,0,.30), 0 0 40px rgba(255,255,255,.45);
        background: rgba(255,255,255,.24);
    }
    .feature-icon {
        font-size: 2.2rem;
        line-height: 1;
        margin-bottom: 10px;
        filter: drop-shadow(0 0 12px rgba(255,255,255,.8));
    }
    .feature-title {
        font-size: 1.05rem;
        font-weight: 900;
        letter-spacing: 1px;
        color: #ffffff !important;
        margin-bottom: 6px;
    }
    .feature-desc {
        font-size: .85rem;
        color: #ffffff !important;
        line-height: 1.55;
        font-weight: 600;
        opacity: .95;
    }

    /* -------- MonCash Block -------- */
    .moncash-box {
        background: linear-gradient(135deg, rgba(255,255,255,.24), rgba(255,255,255,.14));
        border: 3px solid #ffffff;
        border-radius: 20px;
        padding: 22px 22px;
        text-align: center;
        margin: 16px 0 20px;
        box-shadow: 0 0 40px rgba(255,255,255,.35);
        backdrop-filter: blur(6px);
    }
    .moncash-label {
        font-size: .78rem;
        letter-spacing: 3px;
        color: #ffffff !important;
        text-transform: uppercase;
        font-weight: 900;
        margin-bottom: 8px;
    }
    .moncash-number {
        font-size: clamp(1.6rem, 4vw, 2.4rem);
        font-weight: 900;
        font-family: 'Courier New', monospace;
        color: #FFEB3B !important;
        text-shadow: 0 3px 20px rgba(0,0,0,.35), 0 0 30px rgba(255,235,59,.75);
        letter-spacing: 3px;
        margin: 6px 0;
    }
    .moncash-amount {
        font-size: 1.1rem;
        font-weight: 900;
        color: #00E676 !important;
        letter-spacing: 1.5px;
        text-shadow: 0 2px 12px rgba(0,0,0,.30);
    }
    .moncash-note {
        font-size: .78rem;
        color: #ffffff !important;
        font-weight: 700;
        margin-top: 8px;
        letter-spacing: .5px;
        opacity: .95;
    }

    /* -------- Section Title -------- */
    .section-title {
        font-size: clamp(1.3rem, 2.6vw, 1.8rem);
        font-weight: 900;
        letter-spacing: 2px;
        color: #FFEB3B !important;
        margin: 20px 0 10px;
        text-shadow: 0 2px 14px rgba(0,0,0,.35), 0 0 20px rgba(255,235,59,.4);
    }

    /* -------- Result Boxes -------- */
    .result-good {
        background: rgba(0,255,136,.22);
        border: 2px solid #ffffff;
        border-radius: 14px;
        padding: 16px;
        color: #00E676 !important;
        font-weight: 800;
        font-size: 1rem;
        text-shadow: 0 1px 4px rgba(0,0,0,.35);
        backdrop-filter: blur(4px);
    }
    .result-good b { color: #ffffff !important; }
    .result-bad {
        background: rgba(255,59,59,.22);
        border: 2px solid #ffffff;
        border-radius: 14px;
        padding: 16px;
        color: #FF8A80 !important;
        font-weight: 800;
        font-size: 1rem;
        text-shadow: 0 1px 4px rgba(0,0,0,.35);
        backdrop-filter: blur(4px);
    }
    .result-bad b { color: #ffffff !important; }

    /* -------- Intro box -------- */
    .intro-box {
        max-width: 900px;
        margin: 0 auto 24px;
        padding: 18px 22px;
        border-radius: 16px;
        background: rgba(255,255,255,.16);
        border: 1px solid rgba(255,255,255,.45);
        color: #ffffff !important;
        font-size: 1rem;
        line-height: 1.65;
        font-weight: 600;
        backdrop-filter: blur(6px);
    }

    /* -------- Trust & Safety -------- */
    .safety-box {
        background: rgba(255,255,255,.16);
        border: 2px solid #ffffff;
        border-radius: 16px;
        padding: 20px 22px;
        color: #ffffff !important;
        line-height: 1.65;
        font-weight: 600;
        font-size: .92rem;
        backdrop-filter: blur(6px);
    }

    /* ===================================================
       INPUT BOXES — BRIGHT COLORED TEXT
       =================================================== */

    /* ---------- TEXT INPUTS ---------- */
    .stTextInput input {
        background: rgba(255,255,255,.22) !important;
        color: #FFEB3B !important;
        border: 2px solid rgba(255,255,255,.55) !important;
        border-radius: 10px !important;
        font-weight: 900 !important;
        font-size: 1rem !important;
        letter-spacing: .5px !important;
        text-shadow: 0 1px 3px rgba(0,0,0,.35) !important;
        transition: all .2s ease !important;
    }
    .stTextInput input::placeholder {
        color: rgba(255,255,255,.55) !important;
        font-weight: 700 !important;
        font-style: italic !important;
    }
    /* FOCUSED input — brighter, glowing */
    .stTextInput input:focus {
        background: rgba(255,255,255,.32) !important;
        color: #00E5FF !important;
        border: 2px solid #00E5FF !important;
        box-shadow: 0 0 0 3px rgba(0,229,255,.35), 0 0 24px rgba(0,229,255,.55) !important;
        text-shadow: 0 0 12px rgba(0,229,255,.7) !important;
    }

    /* ---------- TEXT AREAS ---------- */
    .stTextArea textarea {
        background: rgba(255,255,255,.22) !important;
        color: #FFEB3B !important;
        border: 2px solid rgba(255,255,255,.55) !important;
        border-radius: 10px !important;
        font-weight: 800 !important;
        font-size: .96rem !important;
        letter-spacing: .3px !important;
        text-shadow: 0 1px 3px rgba(0,0,0,.35) !important;
        transition: all .2s ease !important;
    }
    .stTextArea textarea::placeholder {
        color: rgba(255,255,255,.55) !important;
        font-weight: 700 !important;
        font-style: italic !important;
    }
    .stTextArea textarea:focus {
        background: rgba(255,255,255,.32) !important;
        color: #00E5FF !important;
        border: 2px solid #00E5FF !important;
        box-shadow: 0 0 0 3px rgba(0,229,255,.35), 0 0 24px rgba(0,229,255,.55) !important;
        text-shadow: 0 0 12px rgba(0,229,255,.7) !important;
    }

    /* ---------- SELECT BOX (dropdown container) ---------- */
    .stSelectbox div[data-baseweb="select"] > div {
        background: rgba(255,255,255,.22) !important;
        border: 2px solid rgba(255,255,255,.55) !important;
        border-radius: 10px !important;
        transition: all .2s ease !important;
    }

    /* The selected value shown inside the closed box */
    .stSelectbox div[data-baseweb="select"] div[data-testid="stSelectbox"] div,
    .stSelectbox div[data-baseweb="select"] span,
    .stSelectbox div[data-baseweb="select"] input,
    .stSelectbox div[data-baseweb="select"] [class*="ValueContainer"],
    .stSelectbox div[data-baseweb="select"] [class*="singleValue"] {
        color: #FFEB3B !important;
        font-weight: 900 !important;
        letter-spacing: .5px !important;
        text-shadow: 0 1px 3px rgba(0,0,0,.35) !important;
    }

    /* Focus / selected state — bright cyan glow */
    .stSelectbox div[data-baseweb="select"]:focus-within > div {
        background: rgba(255,255,255,.32) !important;
        border: 2px solid #00E5FF !important;
        box-shadow: 0 0 0 3px rgba(0,229,255,.35), 0 0 24px rgba(0,229,255,.55) !important;
    }
    .stSelectbox div[data-baseweb="select"]:focus-within span,
    .stSelectbox div[data-baseweb="select"]:focus-within [class*="singleValue"] {
        color: #00E5FF !important;
        text-shadow: 0 0 12px rgba(0,229,255,.8) !important;
    }

    /* The dropdown arrow icon */
    .stSelectbox div[data-baseweb="select"] svg {
        fill: #ffffff !important;
        color: #ffffff !important;
    }

    /* ---------- DROPDOWN MENU (popup list) ---------- */
    div[data-baseweb="popover"] ul,
    div[data-baseweb="popover"] li,
    div[role="listbox"] {
        background: #2E7BC4 !important;
        color: #ffffff !important;
        border-radius: 10px !important;
    }
    div[role="option"] {
        color: #FFEB3B !important;
        font-weight: 800 !important;
        background: #2E7BC4 !important;
    }
    div[role="option"]:hover {
        background: rgba(0,229,255,.35) !important;
        color: #00E5FF !important;
    }
    /* Highlighted / currently-selected option */
    div[role="option"][aria-selected="true"] {
        background: rgba(255,235,59,.30) !important;
        color: #FFEB3B !important;
        font-weight: 900 !important;
    }

    /* ---------- LABELS ---------- */
    .stTextInput label,
    .stTextArea label,
    .stSelectbox label {
        color: #ffffff !important;
        font-weight: 800 !important;
        letter-spacing: .5px !important;
        text-shadow: 0 1px 3px rgba(0,0,0,.30) !important;
    }

    /* ---------- BUTTONS ---------- */
    .stButton > button {
        background: #ffffff !important;
        color: #2E7BC4 !important;
        font-weight: 900 !important;
        border-radius: 12px !important;
        border: 2px solid #ffffff !important;
        box-shadow: 0 4px 0 rgba(0,0,0,.20) !important;
        transition: all .12s !important;
        letter-spacing: 1px !important;
    }
    .stButton > button:hover {
        background: #FFEB3B !important;
        color: #1A3A5C !important;
        transform: translateY(-1px);
    }
    .stButton > button:active {
        transform: translateY(3px) !important;
        box-shadow: 0 1px 0 rgba(0,0,0,.20) !important;
    }

    /* Form submit buttons */
    div[data-testid="stFormSubmitButton"] button {
        background: #FFEB3B !important;
        color: #1A3A5C !important;
        font-weight: 900 !important;
        border: 2px solid #ffffff !important;
    }
    div[data-testid="stFormSubmitButton"] button:hover {
        background: #00E5FF !important;
        color: #1A3A5C !important;
    }

    /* ---------- CODE BLOCK ---------- */
    .stCodeBlock, pre, code {
        background: rgba(0,0,0,.32) !important;
        color: #00E5FF !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255,255,255,.35) !important;
    }
    pre code, code span {
        color: #00E5FF !important;
        font-weight: 700 !important;
    }

    /* Streamlit default markdown text */
    .stMarkdown, .stMarkdown * {
        color: #ffffff !important;
    }

    /* Help tooltips */
    .stTooltipIcon svg {
        fill: #FFEB3B !important;
        color: #FFEB3B !important;
    }

    /* ---------- FOOTER ---------- */
    .app-footer {
        text-align: center;
        padding: 24px 16px 12px;
        border-top: 2px solid rgba(255,255,255,.35);
        margin-top: 30px;
        color: #ffffff !important;
        font-size: .78rem;
        font-weight: 700;
        letter-spacing: .6px;
    }
    .app-footer .fname {
        font-size: 1rem;
        font-weight: 900;
        color: #FFEB3B !important;
        letter-spacing: 2px;
        margin-bottom: 4px;
        text-shadow: 0 2px 14px rgba(0,0,0,.35), 0 0 22px rgba(255,235,59,.5);
    }
    .app-footer .frole {
        font-size: .7rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #ffffff !important;
        margin-bottom: 8px;
        opacity: .92;
    }
    .app-footer a {
        color: #00E5FF !important;
        text-decoration: none;
        font-weight: 800;
        margin: 0 6px;
        border-bottom: 1px dotted rgba(0,229,255,.7);
    }
</style>
""", unsafe_allow_html=True)

# =========================================================
# HERO HEADER
# =========================================================
st.markdown("""
<div class="hero-header">
    <h1 class="hero-title">GESNER DESLANDES</h1>
    <div class="hero-subtitle">📱 Unlock Your Phone Application</div>
    <div class="hero-role">Software Engineer · Engineer-in-Chief, GlobalInternet.py</div>
    <div class="hero-contact">
        <span>📞 <a href="tel:+50947385663">(509) 4738-5663</a></span>
        <span>✉️ <a href="mailto:deslandes78@gmail.com">deslandes78@gmail.com</a></span>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================================================
# INTRODUCTION
# =========================================================
st.markdown("""
<div class="intro-box">
    Welcome to the <b>Unlock Your Phone Application</b> — a professional,
    all-in-one assistant for legitimate phone diagnostics and carrier unlock requests.<br><br>
    This tool helps you:
    <ul style="margin: 8px 0 0 20px; padding: 0;">
        <li>✅ Validate any phone's <b>IMEI number</b> using the international Luhn algorithm</li>
        <li>✅ Look up <b>device specifications</b> by brand and model</li>
        <li>✅ Generate the <b>official carrier unlock request</b> to send to Digicel, Natcom, or any carrier</li>
        <li>✅ Get <b>direct 1-on-1 consultation</b> with Gesner for advanced troubleshooting</li>
    </ul>
    <br>
    <b>⚠️ Important:</b> This app only supports <b>legitimate</b> phone
    operations. We do NOT bypass lock screens, FRP locks, iCloud activation locks, or any security feature.
    All services require proof of device ownership.
</div>
""", unsafe_allow_html=True)

# =========================================================
# SERVICES GRID
# =========================================================
st.markdown('<div class="section-title">🛠️ Our Services</div>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔍</div>
        <div class="feature-title">IMEI Validator</div>
        <div class="feature-desc">Check if an IMEI is mathematically valid using the official Luhn algorithm used by every carrier worldwide.</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📋</div>
        <div class="feature-title">Device Lookup</div>
        <div class="feature-desc">Look up device specs by brand and model. Get processor info, storage options, and OS guidance.</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🔓</div>
        <div class="feature-title">Carrier Unlock</div>
        <div class="feature-desc">Generate a professional unlock request to send to your carrier (Digicel, Natcom, AT&T, etc.).</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">💬</div>
        <div class="feature-title">Consultation</div>
        <div class="feature-desc">Talk 1-on-1 with Gesner via WhatsApp for advanced phone troubleshooting and repair guidance.</div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# SECTION 1 — IMEI VALIDATOR
# =========================================================
st.markdown('<div class="section-title">🔍 IMEI Validator</div>', unsafe_allow_html=True)

def luhn_check(imei: str) -> bool:
    """Validate an IMEI using the Luhn algorithm."""
    if not imei.isdigit() or len(imei) != 15:
        return False
    total = 0
    for i, ch in enumerate(imei):
        d = int(ch)
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0

imei_input = st.text_input(
    "Enter your 15-digit IMEI number",
    max_chars=15,
    placeholder="e.g. 358751234567890",
    help="Dial *#06# on your phone to see your IMEI.",
)

col_a, col_b = st.columns([1, 3])
with col_a:
    check_imei = st.button("✅ Validate IMEI", use_container_width=True)

if check_imei:
    imei_clean = re.sub(r"\D", "", imei_input or "")
    if len(imei_clean) != 15:
        st.markdown('<div class="result-bad">❌ IMEI must be exactly 15 digits.</div>', unsafe_allow_html=True)
    elif luhn_check(imei_clean):
        st.markdown(f"""
        <div class="result-good">
            ✅ <b>Valid IMEI</b> — {imei_clean}<br>
            This IMEI passes the Luhn checksum used by all carriers worldwide.
            You can safely include it in your carrier unlock request below.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-bad">
            ❌ <b>Invalid IMEI</b> — {imei_clean}<br>
            This IMEI fails the Luhn checksum. Please re-check the number —
            dial *#06# on your phone to see the correct IMEI.
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# SECTION 2 — DEVICE LOOKUP
# =========================================================
st.markdown('<div class="section-title">📋 Device Lookup</div>', unsafe_allow_html=True)

DEVICE_DB = {
    ("Apple", "iPhone 12"): "A14 Bionic · 6.1\" OLED · 64/128/256 GB · iOS 14+",
    ("Apple", "iPhone 13"): "A15 Bionic · 6.1\" OLED · 128/256/512 GB · iOS 15+",
    ("Apple", "iPhone 14"): "A15 Bionic · 6.1\" OLED · 128/256/512 GB · iOS 16+",
    ("Samsung", "Galaxy S21"): "Exynos 2100 · 6.2\" AMOLED · 128/256 GB · Android 11+",
    ("Samsung", "Galaxy S22"): "Snapdragon 8 Gen 1 · 6.1\" AMOLED · 128/256 GB · Android 12+",
    ("Samsung", "Galaxy A54"): "Exynos 1380 · 6.4\" AMOLED · 128/256 GB · Android 13+",
    ("Xiaomi", "Redmi Note 12"): "Snapdragon 685 · 6.67\" AMOLED · 64/128/256 GB · Android 13",
    ("Xiaomi", "Poco X5"): "Snapdragon 695 · 6.67\" AMOLED · 128/256 GB · Android 13",
    ("Tecno", "Spark 10"): "Helio G37 · 6.6\" IPS · 64/128 GB · Android 13",
    ("Tecno", "Camon 20"): "Helio G85 · 6.67\" AMOLED · 128/256 GB · Android 13",
    ("Infinix", "Hot 30"): "Helio G88 · 6.78\" IPS · 128/256 GB · Android 13",
    ("Itel", "A60"): "Unisoc SC9863A · 6.6\" IPS · 32/64 GB · Android 12",
}

col_x, col_y = st.columns(2)
with col_x:
    brand = st.selectbox("Brand", sorted(set(k[0] for k in DEVICE_DB)))
with col_y:
    models = sorted([k[1] for k in DEVICE_DB if k[0] == brand])
    model = st.selectbox("Model", models)

if st.button("🔎 Look Up Device"):
    specs = DEVICE_DB.get((brand, model))
    if specs:
        st.markdown(f"""
        <div class="result-good">
            📱 <b>{brand} {model}</b><br>
            {specs}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<div class="result-bad">❌ Device not found in our database. Please contact Gesner for a custom lookup.</div>', unsafe_allow_html=True)

# =========================================================
# SECTION 3 — CARRIER UNLOCK ASSISTANT
# =========================================================
st.markdown('<div class="section-title">🔓 Carrier Unlock Assistant</div>', unsafe_allow_html=True)

st.markdown("""
<div style="color:#ffffff; font-size:.92rem; font-weight:600; line-height:1.6; margin-bottom:14px;">
    Fill in the details below. The app will generate a <b>professional unlock request email</b>
    that you can send directly to your carrier (Digicel, Natcom, AT&T, T-Mobile, etc.).
    This is the only legal path to remove a carrier SIM lock.
</div>
""", unsafe_allow_html=True)

with st.form("unlock_form"):
    fcol1, fcol2 = st.columns(2)
    with fcol1:
        owner_name = st.text_input("Your Full Name", placeholder="e.g. Jean Baptiste")
        owner_email = st.text_input("Your Email Address", placeholder="you@example.com")
    with fcol2:
        carrier = st.selectbox("Your Carrier", ["Digicel Haiti", "Natcom Haiti", "AT&T", "T-Mobile", "Verizon", "Other"])
        imei_unlock = st.text_input("Device IMEI (15 digits)", max_chars=15, placeholder="358751234567890")

    device_info = st.text_input("Device Model", placeholder="e.g. iPhone 12, Galaxy S21")
    reason = st.text_area("Reason for unlock request", placeholder="I am the original owner of this device and I want to use it with another carrier.", height=80)

    submitted = st.form_submit_button("📧 Generate Unlock Request Email", use_container_width=True)

if submitted:
    imei_clean = re.sub(r"\D", "", imei_unlock or "")
    if not owner_name or not owner_email or not imei_clean or not device_info:
        st.markdown('<div class="result-bad">❌ Please fill in all fields before generating the email.</div>', unsafe_allow_html=True)
    elif len(imei_clean) != 15 or not luhn_check(imei_clean):
        st.markdown('<div class="result-bad">❌ The IMEI you entered is not valid. Please check it and try again.</div>', unsafe_allow_html=True)
    else:
        email_body = f"""Subject: Carrier Unlock Request — IMEI {imei_clean}

Dear {carrier} Customer Support,

I am writing to formally request a SIM network unlock for my device. I am the
original owner and I have fulfilled all contractual obligations associated with this device.

Please find the details below:

    Owner Name:     {owner_name}
    Owner Email:    {owner_email}
    Device Model:   {device_info}
    IMEI:           {imei_clean}
    Carrier:        {carrier}

Reason for request:
    {reason if reason else "I want to use this device with a different carrier network."}

I have attached my proof of purchase and a copy of my ID for verification.
Please process this unlock request at your earliest convenience and let me know
the expected turnaround time and any additional requirements.

Thank you for your time and assistance.

Sincerely,
{owner_name}
{owner_email}
"""
        st.markdown('<div class="result-good">✅ Your unlock request email is ready. Copy it below and send it to your carrier.</div>', unsafe_allow_html=True)
        st.code(email_body, language="text")

# =========================================================
# SECTION 4 — PAID CONSULTATION (MONSASH)
# =========================================================
st.markdown('<div class="section-title">💬 Personal Consultation with Gesner</div>', unsafe_allow_html=True)

st.markdown("""
<div style="color:#ffffff; font-size:.95rem; font-weight:600; line-height:1.65; margin-bottom:16px;">
    Need <b>direct 1-on-1 help</b> with a specific phone issue? Book a personal consultation with Gesner.
    He will guide you through the process over WhatsApp — step by step, in Kreyòl or English.<br><br>
    <b>Consultation includes:</b><br>
    • Personalized diagnosis of your phone issue<br>
    • Detailed walkthrough for legitimate fixes<br>
    • Carrier unlock guidance specific to your device<br>
    • Follow-up support for 7 days
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="moncash-box">
    <div class="moncash-label">💳 MonCash Payment</div>
    <div class="moncash-number">(509) 4738-5663</div>
    <div class="moncash-amount">Send $5 USD · ~700 HTG</div>
    <div class="moncash-note">
        Open MonCash → Transfer → Prisme → Prisme<br>
        Enter the number above → Confirm $5 → Copy your transaction reference
    </div>
</div>
""", unsafe_allow_html=True)

with st.form("consult_form"):
    cc1, cc2 = st.columns(2)
    with cc1:
        client_name = st.text_input("Your Name", placeholder="Full name")
        client_phone = st.text_input("Your WhatsApp Number", placeholder="+509 XXXX XXXX")
    with cc2:
        moncash_ref = st.text_input("MonCash Transaction Reference", placeholder="e.g. MC987654321")
        device_issue = st.text_input("Your Phone Issue (short)", placeholder="e.g. Cannot unlock carrier")

    consult_notes = st.text_area("Tell Gesner more about your issue", placeholder="Describe what you need help with…", height=90)

    consult_submit = st.form_submit_button("📩 Submit Consultation Request", use_container_width=True)

if consult_submit:
    if not client_name or not client_phone or not moncash_ref:
        st.markdown('<div class="result-bad">❌ Please fill in your name, WhatsApp number, and MonCash reference.</div>', unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="result-good">
            ✅ <b>Thank you, {client_name}!</b><br>
            Your consultation request has been received.<br><br>
            📞 Gesner will contact you on WhatsApp within 24 hours at
            <b>{client_phone}</b>.<br>
            💳 Your MonCash reference: <b>{moncash_ref}</b><br><br>
            For urgent matters, call <b>(509) 4738-5663</b> directly.
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# TRUST & SAFETY
# =========================================================
st.markdown('<div class="section-title">🛡️ Trust & Safety</div>', unsafe_allow_html=True)

st.markdown("""
<div class="safety-box">
    <b style="font-size:1.05rem;">⚠️ What this app does NOT do:</b><br><br>
    • ❌ Does NOT bypass lock screens (PIN, pattern, password)<br>
    • ❌ Does NOT bypass iCloud activation locks<br>
    • ❌ Does NOT bypass Google FRP (Factory Reset Protection)<br>
    • ❌ Does NOT bypass any manufacturer or owner security feature<br><br>
    <b style="font-size:1.05rem;">✅ What this app DOES do:</b><br><br>
    • ✅ Validate IMEI numbers (Luhn algorithm)<br>
    • ✅ Look up legitimate device specifications<br>
    • ✅ Generate carrier unlock request emails<br>
    • ✅ Connect you to a certified technician for consultation<br><br>
    <b>For your protection:</b> We require proof of ownership for all services. Any attempt to
    use this app to bypass security on a device you do not own is strictly forbidden and may be illegal.
</div>
""", unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================
st.markdown("""
<div class="app-footer">
    <div class="fname">GESNER DESLANDES</div>
    <div class="frole">Software Engineer · Engineer-in-Chief, GlobalInternet.py</div>
    <div>
        📞 <a href="tel:+50947385663">(509) 4738-5663</a> &nbsp;·&nbsp;
        ✉️ <a href="mailto:deslandes78@gmail.com">deslandes78@gmail.com</a>
    </div>
    <div style="margin-top: 12px; font-size: .68rem; opacity: .8;">
        © 2026 Unlock Your Phone Application · Built with Streamlit
    </div>
</div>
""", unsafe_allow_html=True)
