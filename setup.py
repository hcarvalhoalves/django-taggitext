import os
import codecs
from setuptools import setup, find_packages

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-taggitext',
    version='0.1',
    description="A django-taggit extension for autocompleting tags with jQuery's TextExt plugin.",
    long_description = read('README.rst'),
    author='Henrique C. Alves',
    author_email='hcarvalhoalves@gmail.com',
    download_url='',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe = False,
)
