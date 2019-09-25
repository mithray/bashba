from setuptools import setup

setup(
	name="Radioactive Terminal",
	version="0.0.1",
	py_modules=["radioactive"],
	install_requires=[
		'Click',
		'beautifulsoup4'
	],
	entry_points='''
		[console_scripts]
		radioactive=radioactive:read
	'''
)
