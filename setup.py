from setuptools import setup, find_packages

setup(
    name="nexus-flux",
    version="1.0.0",
    author="YEO Kaffanan Issa",
    author_email="contact@ikaffanan.com",
    description="NEXUS-FLUX — A Non-Anthropomorphic Collective Intelligence Engine (Open-source safe version)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/<ton-compte>/nexus-flux",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "fastapi",
        "uvicorn",
        "pydantic",
        "python-dotenv",
        "redis",
        "typer",
        "pytest",
        "openai",     # utilisé si l'API KEY est fournie
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.10",
)
