import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tabreloader",
    version="2.1",
    author="Talha Asghar",
    author_email="talhaasghar.contact@simplelogin.fr",
    description="A very easy and simple to use tool to stay online on any website as long as your PC is on.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iamtalhaasghar/browser-tab-reloader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=['tabreloader.py'],
    install_requires=["keyboard"],
    python_requires='>=3.6',
)