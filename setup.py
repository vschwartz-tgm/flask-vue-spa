import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask-vue-spa-test",
    version="0.0.1",
    author="Vincent Schwartz",
    author_email="vschwartz@student.tgm.ac.at",
    description="flask vue testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vschwartz-tgm/flask-vue-spa",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

