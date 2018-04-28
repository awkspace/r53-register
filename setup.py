from setuptools import setup, find_packages

with open('requirements.txt') as fd:
    setup(name='r53-register-ip',
          author='awk',
          author_email='self@awk.space',
          version='0.1.0',
          install_requires=fd.readlines(),
          packages=find_packages(),
          entry_points={
              'console_scripts': [
                  'r53-register = r53_register.cli:main'
              ]
          })
