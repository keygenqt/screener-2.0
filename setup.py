import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='screener',
    version='0.0.1',
    author='Vitaliy Zarubin',
    author_email='keygenqt@gmail.com',
    description='Application "screener" for easy screenshot.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/keygenqt/screener-2.0",
    packages=setuptools.find_packages(exclude=['*tests.*', '*tests']),
    include_package_data=True,
    py_modules=['colors'],
    install_requires=[
        'click',
        'pyYaml'
    ],
    python_requires='>=3.6'
)
