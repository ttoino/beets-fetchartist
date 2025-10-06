import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="beets-fetchartist",
    version="1.0.0",
    author="anon",
    packages=['beetsplug'],
    author_email="",
    description="Sources artist images from Last.fm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheDuckMan64/beets-fetchartist",
    python_requires='>=3.6',
    install_requires=[
        "beets>=1.5.0",
        "pylast",
        "requests",
    ],
)
