from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in fitness_center/__init__.py
from fitness_center import __version__ as version

setup(
	name="fitness_center",
	version=version,
	description="Fitness center",
	author="edom ibrahim",
	author_email="abolupna1@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
