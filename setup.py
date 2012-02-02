from setuptools import setup, find_packages
import os


setup(
    author="Ben Lopatin",
    author_email="ben.lopatin@wellfireinteractive.com",
    name='django-site-broadcasts',
    version='0.0.1',
    description='Group accounts for Django.',
    long_description=open(os.path.join(os.path.dirname(__file__),
        'README.rst')).read(),
    url='https://github.com/bennylope/django-site-broadcasts/',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=[
        'Django>=1.3',
    ],
    test_suite='tests.runtests.runtests',
    packages=find_packages(),
    zip_safe = False
)

