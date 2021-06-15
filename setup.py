from setuptools import setup

requirements = ['bs4>=0.0.1', 'requests>=2.25.1']


setup(name='wbscrp',
      version='3.2.1',
      description='web scraper with methods',
      long_description=open('README.txt').read(),
      packages=['wbscrp'],
      install_requires=requirements,
      author='ivt3-20',
      author_email='hotammm@mail.ru',
      url='https://github.com/BulgarinIvt3/scrp',
      zip_safe=False)
