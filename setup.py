import setuptools

VERSION = "1.0.0"

with open("README.md", "r") as f:
	long_description = f.read()
	
setuptools.setup(
	name="iconic",
	packages=setuptools.find_packages(),
	version=VERSION,
	license="MIT",
	description="Identicon generator version 2.0!",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/aleeazam/iconic",
	download_url=f"https://github.com/aleeazam/iconic/archive/refs/tags/{VERSION}.tar.gz",
	keywords=["identicon", "generator", "pillow", "icon"],
	install_requires=["Pillow>=9.0.1"],
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3.10"
	],
)
