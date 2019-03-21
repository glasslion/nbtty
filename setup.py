import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nbtty",
    version="1.0.1",
    author="Leonardo Zhou",
    author_email="glasslion@gmail.com.com",
    description="Run web tty from jupyter notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/glasslion/nbtty",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
