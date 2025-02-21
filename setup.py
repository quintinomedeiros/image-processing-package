from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Quintino Medeiros",
    author_email="quintinomedeiros@gmail.com",
    description="Pacote para combinação, transformação, identificação e plotagem de imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quintinomedeiros/image-processing-package.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)