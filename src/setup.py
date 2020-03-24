from setuptools import find_packages, setup

setup(
    name="report_generator",
    version="1.0",
    # mandatory
    author_email="fangfangsheng46@gmail.com",
    packages=find_packages(),
#     entry_points={
#         "console_scripts": [
#             "pepweb=ngpep.app:run",
#             "pepctl=ngpep.cli:main",  # cli: command line interface
#         ]
#     },
)
