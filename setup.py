import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ansiColor",
    version="1.0.1",
    author="MiranDaniel",
    author_email="mirandanielcz@gmail.com",
    description="Small package made for using ANSI codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MiranDaniel/ansiColor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)