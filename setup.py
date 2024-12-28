from setuptools import setup, find_packages

setup(
    name="docspy",
    version="0.0.1",
    description="Simple creation of documentation for Python projects.",
    author="Jan-Markus Langer",
    packages=find_packages(),
    install_requires=["click"],
    entry_points={
        "console_scripts": [
            "docspy=docspy.cli:main",
        ],
    },
)
