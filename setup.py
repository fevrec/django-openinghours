from setuptools import setup, find_packages
import openinghours as app

setup(
    name="django-openinghours",
    version=app.__version__,
    description=open('DESCRIPTION').read(),
    with open('README.rst', encoding="utf8") as file:
        long_description = file.read()
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, app, openinghours, opening hours, opening times',
    author='arteria GmbH, fmalina',
    author_email='admin@arteria.ch, fmalina@pm.me',
    url="https://github.com/arteria/django-openinghours",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Topic :: Internet',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
    ],
    install_requires=['django', 'django-threadlocals'],
    tests_require=['coverage', 'freezegun'],
)
