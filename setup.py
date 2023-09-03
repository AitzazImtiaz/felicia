from setuptools import setup

setup(
    name = "felicia",
    version = "0.1.0",
    description = "Just an AI",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/felicia",
    packages = ["felicia"],
    entry_points = {
        'console_scripts': [
            'felicia = felicia.__main__:main'
        ]
    },
)
