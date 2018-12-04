import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="domain-checker",
    version="0.1",
    author="muhzi",
    author_email="air.oamyst517@yahoo.com",
    description="Quick Domain WHOIS resolver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/muhzii/domain-checker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)