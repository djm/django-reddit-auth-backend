import os
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
        name='django-reddit-auth-backend',
        version='0.1',
        description='A Django authentication backend which utilises the Reddit Auth API.',
        long_description=readme,
        author='Darian Moody',
        author_email='mail@djm.org.uk',
        url='https://github.com/djm/django-reddit-auth-backend',
        packages=find_packages(),
        include_package_data=True,
        install_requires=['requests>=0.4'],
        classifiers=[
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Framework :: Django',
            ],
        )
