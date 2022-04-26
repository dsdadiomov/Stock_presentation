from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'Streaming video data via networks'

# Setting up
setup(
    name="Stock03071994",
    version=VERSION,
    author="David",
    author_email="<daviddadiomov@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['bs4', 'requests', 'Datetime', 'pandas', 'matplotlib', 'termcolor'],
    keywords=['stock'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)