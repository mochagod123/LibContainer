from setuptools import setup, find_packages

setup(
    name="libcontainer",
    version="1.0.2",
    author="neko",
    packages=find_packages(),
    install_requires=["aiohttp"],
    include_package_data=True,
)