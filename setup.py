from setuptools import setup

requirements = ['bs4>=0.0.1', 'requests>=2.25.1']


setup(name='scrp',
      version='0.0',
      description='web scraper',
      long_description=open('README.txt').read(),
      packages=['scrp'],
      install_requires=requirements,
      author='ivt3-20',
      author_email='hotammm@mail.ru',
      url='https://github.com/BulgarinIvt3/scrp',
      zip_safe=False)
