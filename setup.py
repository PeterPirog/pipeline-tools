#https://www.youtube.com/watch?v=GIF3LaRqgXo
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='pipeline-tools',
      version='0.0.1',
      description='ML pipeline tools',
      py_modules=['pipeline-tools'],
      package_dir={'': 'src'},
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: 3.9",
          "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
          "Operating System :: OS Independent"
      ],
      long_description=long_description,
      long_description_content_type="text/markdown",
      install_requires=[
          "pandas>=1.3.2",
      ],
      extras_require={
          "dev": [
              "pytest>=3.7",
              "tox>=3.24.3",
              "check-manifest",
              "twine"
          ],
      },
      url='https://github.com/PeterPirog/pipeline-tools',
      author='Peter Pirog',
      author_email='peterpirogtf@gmail.com',
      )
