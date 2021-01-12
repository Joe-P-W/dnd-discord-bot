import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dnd_discord_bot-Joe_P_W",
    version="0.0.2",
    author="Joe W",
    author_email="",
    description="A dnd discord bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Joe-P-W/dnd-discord-bot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    python_requires='>=3.8',
)
