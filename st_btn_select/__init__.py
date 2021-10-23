import os
import streamlit as st
import streamlit.components.v1 as components

__all__ = ['st_btn_select']
__RELEASE = True


if not __RELEASE:
    _btn_select = components.declare_component(
        "btn_select",
        url="http://localhost:3001",
    )

    _btn_select_nav = components.declare_component(
        "btn_select_nav",
        url="http://localhost:3001",
    )
else:
    _btn_select = components.declare_component(
        "btn_select",
        path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend/build"),
    )

    _btn_select_nav = components.declare_component(
        "btn_select_nav",
        path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend/build"),
    )

def st_btn_select(options, index=0, format_func=str, nav=False, key=None):
    """Create a new instance of "st_btn_select".

    Parameters
    ----------
    options: Sequence, numpy.ndarray, pandas.Series, pandas.DataFrame or pandas.Index
        Labels for the select options.
        This will be cast to str internally by default.
        For pandas.DataFrame, the first column is selected.
    index: int, optional
        The index of the preselected option on first render.
        Default ``0``
    format_func: function
        Function to modify the display of the labels.
        It receives the option as an argument and its output will be cast to str.
        Default ``str``
    nav: bool, optional
        Whether to use this widget as a top-anchored navigation.
        Default ``False``
    key: str or None
        An optional key that uniquely identifies this component.
        If this is None and the component's arguments are changed,
        the component will be re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    string
        Which button was selected.

    Warning
    -------
    You can only have one `st_btn_select` as navigation, as others will be displayed on top of it.
    """
    key = st.type_util.to_key(key)
    opt = st.type_util.ensure_indexable(options)

    if nav:
        st.markdown(
            """
                <style>
                iframe[title="st_btn_select.btn_select_nav"] {
                    position: fixed;
                    top: 0;
                    z-index: 1;
                }
                </style>
            """,
            unsafe_allow_html=True,
        )
        
        idx = _btn_select_nav(
            options=[str(format_func(option)) for option in opt],
            default=index,
            nav=nav,
            key=key,
        )
    else:
        idx = _btn_select(
            options=[str(format_func(option)) for option in opt],
            default=index,
            nav=nav,
            key=key,
        )

    return opt[idx]
