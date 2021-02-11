import setuptools

setuptools.setup(
    name="winos",
    version="0.0.2",
    packages=["winos"],
    install_requires=[
        "pandas",
        "plotly",
        "matplotlib",
        "country-converter",
        "sklearn",
        "imblearn",
        "seaborn"
    ]
)