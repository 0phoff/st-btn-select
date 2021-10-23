import setuptools

setuptools.setup(
    name="st_btn_select",
    version="0.1.1",
    author="0phoff",
    description="Streamlit Button Selection Component",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/0phoff/st-btn-select",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    license="MIT",
    license_files=('LICENSE'),
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
    ],
)
