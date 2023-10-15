import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    long_desc = file.read()

# Define package metadata
PACKAGE_NAME = "cnnClassifier"
VERSION = "0.1.0"
AUTHOR = "Anirudhra Rao"
AUTHOR_EMAIL = "raorudhra16@gmail.com"
DESCRIPTION = "Kidney disease classifier package"
URL = "https://github.com/Anirudhrarao/Kidney-Disease-Classification"

setuptools.setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url=URL,
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
)
