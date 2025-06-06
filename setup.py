from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cowboat",
    version="1.0.0",
    author="Cowboat Developer",
    description="A whimsical terminal animation of cows sailing away on boats",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/cowboat",
    py_modules=["cowboat"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "cowboat=cowboat:main",
        ],
    },
) 