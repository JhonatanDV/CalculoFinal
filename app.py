import streamlit as st
import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from assets.translations import get_text, LANGUAGES
from pages import definite_integrals, riemann_sums, area_between_curves, software_engineering_scenarios, documentation

# Configure page
st.set_page_config(
    page_title="Calculadora Matemática Avanzada",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
def init_session_state():
    """Initialize session state variables."""
    if "language" not in st.session_state:
        st.session_state.language = "es"
    
    if "function_str" not in st.session_state:
        st.session_state.function_str = "x^2"
    
    if "lower_bound" not in st.session_state:
        st.session_state.lower_bound = "0"
    
    if "upper_bound" not in st.session_state:
        st.session_state.upper_bound = "1"
    
    if "variable" not in st.session_state:
        st.session_state.variable = "x"
    
    if "current_page" not in st.session_state:
        st.session_state.current_page = "definite_integrals"

def main():
    """Main application function."""
    init_session_state()
    
    # Sidebar for navigation and language selection
    with st.sidebar:
        st.header("⚙️ " + get_text("navigation"))
        
        # Language selector
        st.subheader("🌐 " + get_text("language_selector"))
        selected_language = st.selectbox(
            get_text("select_language"),
            list(LANGUAGES.keys()),
            format_func=lambda x: LANGUAGES[x],
            index=list(LANGUAGES.keys()).index(st.session_state.language),
            key="language_selector"
        )
        
        if selected_language != st.session_state.language:
            st.session_state.language = selected_language
            st.rerun()
        
        st.markdown("---")
        
        # Page navigation
        st.subheader("📋 " + get_text("select_page"))
        
        pages = {
            "definite_integrals": "📐 " + get_text("definite_integrals"),
            "riemann_sums": "📊 " + get_text("riemann_sums"),
            "area_between_curves": "📏 " + get_text("area_between_curves"),
            "engineering_scenarios": "⚙️ " + get_text("engineering_scenarios"),
            "documentation": "📖 Documentación y Guías"
        }
        
        selected_page = st.radio(
            "",
            list(pages.keys()),
            format_func=lambda x: pages[x],
            index=list(pages.keys()).index(st.session_state.current_page),
            key="page_selector"
        )
        
        if selected_page != st.session_state.current_page:
            st.session_state.current_page = selected_page
            st.rerun()
        
        st.markdown("---")
        
        # App info
        st.markdown("### 📚 " + get_text("app_title"))
        st.markdown(get_text("app_description"))
        
        st.markdown("---")
        st.markdown(f"*{get_text('footer_info')}*")
    
    # Main content area
    if st.session_state.current_page == "definite_integrals":
        definite_integrals.show()
    elif st.session_state.current_page == "riemann_sums":
        riemann_sums.show()
    elif st.session_state.current_page == "area_between_curves":
        area_between_curves.show()
    elif st.session_state.current_page == "engineering_scenarios":
        software_engineering_scenarios.show()

if __name__ == "__main__":
    main()
