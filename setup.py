import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="robinhood-stop-automate-psantanusaha",
    version="0.0.1",
    author="Santanu Saha",
    author_email="p.santanusaha@gmail.com",
    description="Packge that can help to order stop-loss sells on existing positions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/robinhood-automate-stop-loss",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    dependency_links=['git+https://github.com/picklu13/robin_stocks.git'],
    # install_requires=[
    #     'git+https://github.com/picklu13/robin_stocks.git',
    # ],

)
