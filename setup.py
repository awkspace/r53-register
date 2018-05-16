from setuptools import setup, find_packages

with open('requirements.txt') as fd:
    setup(name='r53-register',
          author='awk',
          author_email='self@awk.space',
          version='0.1.0',
          description='Register your host IP address with Amazon Route 53.',
          license='MIT',
          url='https://github.com/awkspace/r53-register',
          install_requires=fd.readlines(),
          packages=find_packages(),
          entry_points={
              'console_scripts': [
                  'r53-register = r53_register.cli:main'
              ]
          })
