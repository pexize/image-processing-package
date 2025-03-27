from setuptools  import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()
    
setup(
    name="px-image_processing",
    version="0.1.0",
    author="Pexis",
    author_email="pxpxpx@gmail.com",
    description="A package for image processing using skimage.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pexize/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.8",

)