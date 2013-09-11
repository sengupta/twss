from setuptools import setup 

setup(name='twss',
        version='0.1.6',
        description='TWSS: A Naive Bayes classifier that can identify double entendres.',
        long_description=open('README.rst').read(),
        url='https://github.com/sengupta/twss',
        author='Aditya Sengupta',
        author_email='aditya@sengupta.me',
        license=open('LICENSE.txt').read(),
        packages=['twss',],
        package_dir={'twss': 'twss'},
        package_data={'twss': ['*.txt']},
        install_requires=[
            "nltk==2.0.4",
            ],
        zip_safe=False,
        )
