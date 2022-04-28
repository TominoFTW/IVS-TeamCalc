from setuptools import setup, find_packages

setup(
   name='ivscalc',
   version='1.3',
   description='School project calculator',
   author='4bitnebude',
   author_email='',
   packages=find_packages(),  #same as name
   entry_points={
    'console_scripts': [
        'ivscalc = ivscalc.calc:main',
    ],
   },
   package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.qss'],
   },
   python_requires='>=3.9',
   license="GPLv3",
   install_requires=['wheel', 'pyqt5'], #external packages as dependencies
)