import setuptools


setuptools.setup(
    name='cm3d2_parser',
    version='1.0.0',
    author='RimoChan',
    author_email='the@librian.net',
    description='librian',
    long_description=open('readme.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/RimoChan/cm3d2-parser',
    packages=[
        'cm3d2_parser',
    ],
    package_data={},
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[],
    python_requires='>=3.8',
)
