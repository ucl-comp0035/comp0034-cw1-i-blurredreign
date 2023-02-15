from setuptools import setup, find_packages

setup(
    name="comp0034-cw1-i-blurredreign",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,  # automatically install any data files found
    install_requires=[
        "dash",
        "pandas",
        "dash-bootstrap-components",
        "plotly",
    ],
)