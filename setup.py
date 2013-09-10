from setuptools import setup 

setup(name='twss',
        version='0.1.1',
        description='A Naive Bayes classifier that can identify double entendres.',
        url='https://github.com/sengupta/twss',
        author='Aditya Sengupta',
        author_email='aditya@sengupta.me',
        license='WTFPL',
        packages=['twss',],
        install_requires=[
            "nltk==2.0.1rc1",
            "PyYAML==3.10",
            ],
        zip_safe=False,
        )
