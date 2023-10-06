from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in night_badge/__init__.py
from night_badge import __version__ as version

setup(
	name="night_badge",
	version=version,
	description="Training",
	author="NexTash (SMC-PVT) Ltd",
	author_email="support@nextash.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
