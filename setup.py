from setuptools import setup, find_packages

__version__ = "0.1"

setup(
    name="challenge",
    version=__version__,
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "flask",
        "flask-login",
        "flask-migrate",
        "flask-marshmallow",
        "flask-sqlalchemy",
        "flask-static-digest",
        "flask-wtf",
        "marshmallow-sqlalchemy",
        "python-dotenv",
        "passlib",
    ],
    entry_points={
        "console_scripts": [
            "challenge = challenge.manage:cli"
        ]
    },
)
