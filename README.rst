TWSS
====

This is an implementation of a simple double entendre classifier in Python. 

This currently uses a Naive Bayes classifier (the NLTK implementation) as a
Python package. This was inspired by the `bvandenvos Ruby TWSS project
<https://github.com/bvandenbos/twss/>`_ and uses the same data corpus. 

This was built on the eve of `Barcamp Mumbai <http://barcampmumbai.org/>`_ 8
and presented during a session there. 

Suggestions welcome. Do file bugs. Fork away. Send us pull requests. 

Setup Instructions
------------------

.. code-block:: bash

    $ virtualenv --no-site-packages --distribute venv 
    $ source venv/bin/activate 
    $ pip install -r requirements.txt

This creates a virtual environment for this project and install all the
packages necessary for the project to work. 

Demo
----

Once this is installed, you can take it out for a spin: 

.. code-block:: python 

    >>> from twss import TWSS 
    >>> twss = TWSS() 
    >>> twss("That was hard") 
    True
    >>> twss("Hello world") 
    False

The first call can take a while- the module needs to train the classifier
against the pre-installed training dataset. 

Getting dirty
-------------

You can supply your own training data using positive and negative corpus files: 

.. code-block:: python 

    >>> twss = TWSS(positive_corpus_file=open('foo.txt'), negative_corpus_file=open('bar.txt'))

or directly, as a list of tuples: 

.. code-block:: python 

    >>> training_data = [
    ... ("Sentence 1", True),
    ... ("Sentence 2", False),
    ...
    ... ]
    >>> twss = TWSS(training_data)

Roadmap
-------

- Making this pip-installable.
- Writing a sample web app.
- Writing a sample Twitter client.

