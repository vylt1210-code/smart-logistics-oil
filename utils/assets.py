from pathlib import Path
import streamlit as st

ASSET_DIR = Path(__file__).resolve().parents[1] / "assets"

def asset_path(name: str):
    path = ASSET_DIR / name
    return path if path.exists() else None

def show_logo(width=120):
    logo = asset_path("logo.png")
    if logo:
        try:
            st.logo(str(logo))
        except Exception:
            st.sidebar.image(str(logo), width=width)

def show_banner(name: str, caption: str = None):
    path = asset_path(name)
    if path:
        st.image(str(path), use_container_width=True, caption=caption)
    else:
        st.info(f"Chưa có ảnh: assets/{name}")

def image_card(name: str, title: str, text: str):
    path = asset_path(name)
    if path:
        st.markdown("<div class='image-card'>", unsafe_allow_html=True)
        st.image(str(path), use_container_width=True)
        st.markdown(f"<h3>{title}</h3><p>{text}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown(
            f'''
            <div class='image-card placeholder-card'>
                <h3>{title}</h3>
                <p>{text}</p>
                <small>Thiếu ảnh: assets/{name}</small>
            </div>
            ''',
            unsafe_allow_html=True
        )
