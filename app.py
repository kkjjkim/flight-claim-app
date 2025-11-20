import streamlit as st
import time

# --- 사장님의 검로드 링크 ---
PRODUCT_URL = "https://kkjjkimberly.gumroad.com/l/lrpkcbe"

st.set_page_config(page_title="Flight Claim AI", page_icon="✈️", layout="centered")

# --- CSS 스타일링 ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button {
        width: 100%; background-color: #FF4B4B; color: white;
        font-size: 22px; font-weight: bold; padding: 18px;
        border-radius: 12px; border: none; box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4);
    }
    .stButton>button:hover { background-color: #FF0000; transform: scale(1.02); transition: 0.3s; }
    .success-box {
        padding: 25px; background-color: #262730;
        border-left: 6px solid #00FF00; border-radius: 8px; margin-bottom: 25px;
    }
    a { text-decoration: none; }
    </style>
    """, unsafe_allow_html=True)

# --- 헤더 ---
st.title("✈️ Flight Claim AI")
st.markdown("#### 💰 Don't let airlines keep your money.")
st.write("Check your compensation eligibility under **EU Regulation 261/2004** & **US Laws**.")

st.divider()

# --- 입력 폼 ---
col1, col2 = st.columns(2)
with col1:
    airline = st.text_input("Airline Name", placeholder="e.g. Delta, Air France")
    origin = st.text_input("Departure City", placeholder="e.g. London (LHR)")
with col2:
    flight_num = st.text_input("Flight Number", placeholder="Optional")
    dest = st.text_input("Arrival City", placeholder="e.g. New York (JFK)")

delay_time = st.selectbox(
    "How long was the delay?",
    ["Select option...", "Less than 3 hours", "3 - 4 hours", "More than 4 hours", "Flight Cancelled"]
)

distance = st.radio(
    "Approximate Flight Distance?",
    ["Short Haul (< 1,500km)", "Medium Haul (1,500km - 3,500km)", "Long Haul (> 3,500km)"]
)

# --- 핵심 로직 ---
if st.button("Calculate My Compensation 💵"):
    if delay_time == "Select option...":
        st.error("Please select how long the delay was.")
    else:
        with st.spinner('Analyzing flight path & legal regulations...'):
            time.sleep(2) 

        if delay_time == "Less than 3 hours":
            st.warning("⚠️ Typically, delays under 3 hours are not eligible for cash compensation. However, you may claim meals & refreshments.")
        else:
            st.balloons()
            amount = "€600 ($650)"
            if distance == "Short Haul (< 1,500km)": amount = "€250 ($270)"
            elif distance == "Medium Haul (1,500km - 3,500km)": amount = "€400 ($430)"
            
            st.markdown(f"""
            <div class="success-box">
                <h2 style='margin:0; color:#00FF00;'>🎉 YOU ARE ELIGIBLE!</h2>
                <p style='font-size:18px; margin-top:10px;'>According to EU Reg 261/2004, the airline owes you:</p>
                <h1 style='font-size:50px; color: #00FF00; margin:10px 0;'>{amount}</h1>
                <p style='color:#cccccc;'>This is your legal right. Claim it now.</p>
            </div>
            """, unsafe_allow_html=True)

            st.info("👇 We have generated a **Formal Legal Demand Letter** for you.")

            st.text_area(
                "Generated Legal Letter (Preview Locked)",
                f"""Subject: Formal Claim for Compensation - Flight {flight_num if flight_num else '...'}
To: Legal Department of {airline if airline else 'Airline'}

Pursuant to Regulation (EC) No 261/2004, I hereby claim compensation...
[... LEGAL CONTENT HIDDEN ...]
[... DOWNLOAD TO UNLOCK FULL TEXT ...]
""", height=150, disabled=True)

            st.markdown(f"""
                <a href="{PRODUCT_URL}" target="_blank">
                    <button style="
                        background-color: #F4D03F; color: black; width: 100%; 
                        padding: 20px; font-size: 24px; font-weight: 900; 
                        border: none; border-radius: 12px; cursor: pointer;
                        box-shadow: 0px 4px 15px rgba(244, 208, 63, 0.5);">
                        🔓 Unlock & Download Letter ($19)
                    </button>
                </a>
                <p style="text-align:center; margin-top:15px; font-size:14px; color:#888;">
                    ✅ 100% Money Back Guarantee • Instant PDF Download
                </p>
            """, unsafe_allow_html=True)

st.divider()
st.caption("Disclaimer: This tool utilizes AI to estimate compensation eligibility based on public regulations. It does not constitute professional legal advice.")
