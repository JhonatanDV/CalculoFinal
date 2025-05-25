import streamlit as st
import sympy as sp
from assets.translations import get_text, LANGUAGES, set_language

# Page configuration
st.set_page_config(
    page_title="Calculadora Matemática Avanzada",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Remove URL routing by clearing any URL parameters
if "page" in st.session_state:
    del st.session_state["page"]

# Initialize session state
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

def main():
    # Language selector in sidebar
    st.sidebar.markdown("### " + get_text("language_selector"))
    selected_language = st.sidebar.selectbox(
        get_text("select_language"),
        options=list(LANGUAGES.keys()),
        format_func=lambda x: LANGUAGES[x],
        index=0 if st.session_state.language == "es" else 1,
        key="language_selector"
    )
    
    if selected_language != st.session_state.language:
        set_language(selected_language)
        st.rerun()

    # Main title
    st.title("🧮 " + get_text("app_title"))
    st.markdown(get_text("app_description"))

    # Navigation
    st.sidebar.markdown("### " + get_text("navigation"))
    
    pages = {
        get_text("definite_integrals"): "definite_integrals",
        get_text("riemann_sums"): "riemann_sums", 
        get_text("area_between_curves"): "area_between_curves",
        get_text("engineering_scenarios"): "software_engineering_scenarios"
    }
    
    selected_page = st.sidebar.radio(
        get_text("select_page"),
        list(pages.keys()),
        key="page_selector"
    )
    
    # Import and show the selected page
    page_module = pages[selected_page]
    
    try:
        if page_module == "definite_integrals":
            from pages.definite_integrals import show
        elif page_module == "riemann_sums":
            from pages.riemann_sums import show
        elif page_module == "area_between_curves":
            from pages.area_between_curves import show
        elif page_module == "software_engineering_scenarios":
            from pages.software_engineering_scenarios import show
        
        show()
        
    except Exception as e:
        st.error(f"{get_text('error_loading_page')}: {str(e)}")

    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown(get_text("footer_info"))

if __name__ == "__main__":
    main()
