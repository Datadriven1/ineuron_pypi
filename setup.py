import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "ineuron_pypi"
USER_NAME = 'PATEL'
setuptools.setup(
    name=f{PROJECT_NAME}-{USER_NAME}",
    version="0.0.1",
    author="USER_NAME",
    author_email="bhupendra.patel147@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Datadriven1/ineuron_pypi.git",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    
)