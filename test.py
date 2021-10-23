import streamlit as st
import streamlit.components.v1 as components
from st_btn_select import st_btn_select

st.set_page_config(
    page_title='Button Select Demo',
)


page = st_btn_select(
    ('home', 'testing'),
    nav=True,
    format_func=lambda x: x.capitalize(),
)

if page == 'home':
    """
    # Streamlit Button Select Demo
    This page is the official demo for the custom `st_btn_select` component.

    ## Documentation
    """
    st.help(st_btn_select)

    """
    ## Example
    """
    with st.echo():
        option = st_btn_select(('option1', 'option2', 'option3', 'option4'), index=2)
        st.write(f'Selected option: {option}')
elif page == 'testing':
    sel = st_btn_select(('on', 'off')) == 'on'
    btn = st.button('button')
    st.sidebar.slider('slider', 0, 100)
    st.write(f'Select: {sel} | Button: {btn}')
