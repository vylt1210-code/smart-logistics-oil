import streamlit as st
from utils.assets import asset_path

def setup_page(title="FuelInsight AI"):
    st.set_page_config(page_title=title, page_icon="⛽", layout="wide")

    bg = asset_path("background_pattern.png")
    bg_css = ""
    if bg:
        bg_css = f'''
        background-image:
            linear-gradient(rgba(248,250,252,.92), rgba(248,250,252,.96)),
            url("{bg.as_posix()}");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        '''

    st.markdown(
        f'''
        <style>
        .stApp {{ {bg_css} }}
        .block-container {{padding-top: 1.1rem; max-width: 1280px;}}
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, #020617, #0f172a, #075985);
        }}
        [data-testid="stSidebar"] * {{color: white !important;}}
        .hero {{
            position: relative;
            padding: 36px;
            border-radius: 32px;
            background:
                radial-gradient(circle at top right, rgba(14,165,233,.48), transparent 34%),
                linear-gradient(135deg, rgba(2,6,23,.98), rgba(15,23,42,.96) 45%, rgba(3,105,161,.94));
            color: white;
            margin-bottom: 22px;
            box-shadow: 0 20px 65px rgba(2,6,23,.26);
            overflow: hidden;
        }}
        .hero h1 {{margin: 0; font-size: 46px; font-weight: 950; letter-spacing: -.9px;}}
        .hero p {{margin-top: 10px; font-size: 18px; opacity: .95; max-width: 850px;}}
        .hero .chips {{margin-top: 18px;}}
        .chip {{
            display: inline-block;
            padding: 8px 13px;
            border-radius: 999px;
            background: rgba(255,255,255,.12);
            border: 1px solid rgba(255,255,255,.22);
            color: white;
            font-size: 13px;
            font-weight: 850;
            margin-right: 8px;
            margin-bottom: 8px;
            backdrop-filter: blur(10px);
        }}
        .metric-card {{
            background: rgba(255,255,255,.94);
            border: 1px solid rgba(226,232,240,.9);
            padding: 18px;
            border-radius: 24px;
            box-shadow: 0 12px 34px rgba(15,23,42,.08);
            margin-bottom: 14px;
            min-height: 118px;
        }}
        .metric-label {{color:#475569; font-weight:850; font-size:14px;}}
        .metric-value {{color:#0f172a; font-size:31px; font-weight:950; margin-top: 7px;}}
        .section-title {{font-size: 27px; font-weight: 950; color: #0f172a; margin: 22px 0 12px;}}
        .soft-card, .image-card {{
            background: rgba(255,255,255,.95);
            padding: 20px;
            border-radius: 24px;
            border: 1px solid #e2e8f0;
            box-shadow: 0 12px 34px rgba(15,23,42,.07);
            margin-bottom: 16px;
            overflow: hidden;
        }}
        .image-card img {{
            border-radius: 20px;
            box-shadow: 0 12px 30px rgba(15,23,42,.12);
        }}
        .image-card h3 {{font-size: 21px; margin: 14px 0 6px; color: #0f172a;}}
        .image-card p {{font-size: 15px; color: #475569; margin: 0;}}
        .placeholder-card {{
            min-height: 180px;
            background: linear-gradient(135deg, #e0f2fe, #f8fafc);
            border: 1px dashed #38bdf8;
        }}
        .pill {{
            display: inline-block;
            padding: 7px 12px;
            border-radius: 999px;
            font-weight: 850;
            font-size: 13px;
            margin-right: 6px;
            margin-bottom: 6px;
        }}
        .pill-blue {{background:#e0f2fe; color:#075985;}}
        .pill-green {{background:#dcfce7; color:#166534;}}
        .pill-yellow {{background:#fef3c7; color:#92400e;}}
        .pill-red {{background:#fee2e2; color:#991b1b;}}
        .big-image {{
            border-radius: 28px;
            overflow: hidden;
            box-shadow: 0 18px 50px rgba(15,23,42,.18);
            margin-bottom: 18px;
        }}
        </style>
        ''',
        unsafe_allow_html=True
    )

def hero(title, subtitle, chips=None):
    chips = chips or []
    chips_html = "".join([f"<span class='chip'>{c}</span>" for c in chips])
    st.markdown(
        f'''
        <div class='hero'>
            <h1>{title}</h1>
            <p>{subtitle}</p>
            <div class='chips'>{chips_html}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

def metric_card(label, value, icon="📌"):
    st.markdown(
        f'''
        <div class='metric-card'>
            <div class='metric-label'>{icon} {label}</div>
            <div class='metric-value'>{value}</div>
        </div>
        ''',
        unsafe_allow_html=True
    )

def section(title):
    st.markdown(f"<div class='section-title'>{title}</div>", unsafe_allow_html=True)

def soft_card(title, text, icon="📌"):
    st.markdown(
        f'''
        <div class='soft-card'>
            <h3>{icon} {title}</h3>
            <p>{text}</p>
        </div>
        ''',
        unsafe_allow_html=True
    )
