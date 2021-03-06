.. include:: global.rst

anom: an om for Cloud Datastore
===============================

Release v\ |release|. (:doc:`installation`, :doc:`changelog`)

.. image:: https://img.shields.io/badge/license-BSD--3-blue.svg
   :target: license.html
.. image:: https://travis-ci.org/Bogdanp/anom-py.svg?branch=master
   :target: https://travis-ci.org/Bogdanp/anom-py
.. image:: https://codeclimate.com/github/Bogdanp/anom-py/badges/coverage.svg
   :target: https://codeclimate.com/github/Bogdanp/anom-py/coverage
.. image:: https://codeclimate.com/github/Bogdanp/anom-py/badges/gpa.svg
   :target: https://codeclimate.com/github/Bogdanp/anom-py
.. image:: https://badge.fury.io/py/anom.svg
   :target: https://badge.fury.io/py/anom
.. image:: https://img.shields.io/badge/Say%20Thanks!-%F0%9F%A6%89-1EAEDB.svg
   :target: https://saythanks.io/to/Bogdanp

**anom** is an object mapper for `Google Cloud Datastore`_ heavily
inspired by ndb_ with a focus on simplicity, correctness and
performance.

Here's what it looks like:

::

   from anom import Model, props

   class Greeting(Model):
     email = props.String(indexed=True, optional=True)
     message = props.Text()
     created_at = props.DateTime(indexed=True, auto_now_add=True)
     updated_at = props.DateTime(indexed=True, auto_now=True)

   greeting = Greeting(message="Hi!")
   greeting.put()

**anom** is :doc:`licensed<license>` under the 3-clause BSD license
and it officially supports Python 3.6 and later.

Get It Now
----------

::

   $ pip install -U anom

Read the :doc:`quickstart` if you're ready to get started or check out
some of the :doc:`examples`.


User Guide
----------

This part of the documentation is focused primarily on teaching you
how to use anom.

.. toctree::
   :maxdepth: 2

   installation
   quickstart
   examples
   advanced


API Reference
-------------

This part of the documentation is focused on detailing the various
bits and pieces of the anom developer interface.

.. toctree::
   :maxdepth: 2

   reference


Project Info
------------

.. toctree::
   :maxdepth: 1

   changelog
   license
