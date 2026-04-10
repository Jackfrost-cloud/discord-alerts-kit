from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="discord-alerts-kit",
    version="0.3.0",
    author="jackfrost_13",
    description="A Python library to build Discord alert bots easily",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jackfrost_13/discord-alerts-kit",
    packages=find_packages(),
    install_requires=[
        "discord.py>=2.0.0",
        "pyyaml>=6.0"
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)