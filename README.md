<div align="center">

<img
  alt="Logo"
  src="https://raw.githubusercontent.com/0phoff/st-btn-select/master/public/logo.svg"
  width="100%"
/>

[![Version][version-badge]][version-url]
[![License][license-badge]][license-url]
<a href="https://ko-fi.com/D1D31LPHE"><img alt="Ko-Fi" src="https://www.ko-fi.com/img/githubbutton_sm.svg" height="20"></a>

_Streamlit Button Select Component_

</div>

---

Sometimes you want a user to make a selection, but you only have a few options.  
Using an `st.selectbox` component works, but wouldn't it be easier to simply have a few buttons in a row ?  
Well, this custom component allows just that !


# Installation
```bash
pip install st_btn_select
```


# Getting Started
Creating a Button Selection is really easy.
```python
from st_btn_select import st_btn_select

selection = st_btn_select(('option 1', 'option 2', 'option 3'))
```

You can also use this component as a small top navigation bar.  
```python
from st_btn_select import st_btn_select

page = st_btn_select(
  # The different pages
  ('home', 'about', 'docs', 'playground'),
  # Enable navbar
  nav=True,
  # You can pass a formatting function. Here we capitalize the options
  format_func=lambda name: name.capitalize(),
)

# Display the right things according to the page
if page == 'home':
  st.write('HOMEPAGE')
```

> **NOTE**  
> There can only be one navbar per page, as they will be displayed on top of each other.
> 
> The navbar buttons do not set any URL hashes, and thus the different pages are not bookmarkable, nor can you use the browser history.


## Documentation
Check out this streamlit app for the documentation, as well as a demo.
[![Open in Streamlit][share-badge]][share-url] 



[version-badge]: https://img.shields.io/pypi/v/st_btn_select?label=version
[version-url]: https://github.com/0phoff/st-btn-select/releases

[license-badge]: https://img.shields.io/pypi/l/st_btn_select
[license-url]: https://github.com/0phoff/st-btn-select/blob/master/LICENSE.md

[share-badge]: https://static.streamlit.io/badges/streamlit_badge_black_white.svg
[share-url]: https://share.streamlit.io/0phoff/st-btn-select/demo/test.py
