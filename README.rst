acclaim-badges
=============================

|pypi-badge| |travis-badge| |codecov-badge| |doc-badge| |pyversions-badge|
|license-badge|

Issue badges from Acclaim upon edx course completion.

Acclaim Badges for EDX

Overview
------------------------

Adds a djangoapp to edx which provides a UI and API backend into Acclaim.  Once installed, EDX adminstrators
will be able to add Acclaim auth tokens and select badges to be issued upon course completion.  This app
then listens for course complete events, and issues badges if the student obtains a passing score.

Install
------------------------
1. Install "acclaim_badges" using pip::

    pip install acclaim_badges

2. Add "acclaim_badges" to your INSTALLED_APPS ``/edx-platform/lms/envs/common.py`` like this::
    
    INSTALLED_APPS = [
        ...
        'acclaim_badges',
    ]

3. Include the acclaim_badges URL conf in ``lms/urls.py`` like this::

    urlpatterns += (
        url(r'^acclaim/', include('acclaim_badges.urls')),
    )

4. The authorization token field will be encypted.  create a AES-256 keyset using keyzar for encryption and decryption::

    $ mkdir fieldkeys
    $ keyczart create --location=fieldkeys --purpose=crypt
    $ keyczart addkey --location=fieldkeys --status=primary --size=256

5. Add keyset location to ``/edx-platform/lms/envs/common.py``::

    ENCRYPTED_FIELDS_KEYDIR = '/path/to/fieldkeys'

6. Run ``./manage.py lms syncdb --settings aws`` to create the acclaim_badges lms app.

7. Depending on how assets are configured, you'll need to run ``collectstatic`` to make css and images available::

    ./manage.py lms --settings aws collectstatic
    
8. Restart webserver

Usage
-------------
The following useful URLs are made available after installation:
``/acclaim/tokens/``
``/acclaim/badge-courses/``

1) Add Acclaim organization and authorization token using ``/acclaim/tokens/``
2) Define a mapping between badge and course by accessing ``/acclaim/badge-courses/``

Note: when defining a mapping, the dropdown will populate with badge templates
if the Acclaim API call is successful (valid token and orgainzation combination are used).

Troubleshooting
---------------
Debugging info is made available in the file ``edx.log``.  This file can be found under the ``/var/log/lms`` directory.

Documentation
-------------

The full documentation is at https://acclaim-badges.readthedocs.org.

License
-------

The code in this repository is licensed under the AGPL 3.0 unless
otherwise noted.

Please see ``LICENSE.txt`` for details.

How To Contribute
-----------------

Contributions are very welcome.

Please read `How To Contribute <https://github.com/edx/edx-platform/blob/master/CONTRIBUTING.rst>`_ for details.

Even though they were written with ``edx-platform`` in mind, the guidelines
should be followed for Open edX code in general.

PR description template should be automatically applied if you are sending PR from github interface; otherwise you
can find it it at `PULL_REQUEST_TEMPLATE.md <https://github.com/edx/acclaim-badges/blob/master/.github/PULL_REQUEST_TEMPLATE.md>`_

Issue report template should be automatically applied if you are sending it from github UI as well; otherwise you
can find it at `ISSUE_TEMPLATE.md <https://github.com/edx/acclaim-badges/blob/master/.github/ISSUE_TEMPLATE.md>`_

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@edx.org.

Getting Help
------------

Have a question about this repository, or about Open edX in general?  Please
refer to this `list of resources`_ if you need any assistance.

.. _list of resources: https://open.edx.org/getting-help


.. |pypi-badge| image:: https://img.shields.io/pypi/v/acclaim-badges.svg
    :target: https://pypi.python.org/pypi/acclaim-badges/
    :alt: PyPI

.. |travis-badge| image:: https://travis-ci.org/edx/acclaim-badges.svg?branch=master
    :target: https://travis-ci.org/edx/acclaim-badges
    :alt: Travis

.. |codecov-badge| image:: http://codecov.io/github/edx/acclaim-badges/coverage.svg?branch=master
    :target: http://codecov.io/github/edx/acclaim-badges?branch=master
    :alt: Codecov

.. |doc-badge| image:: https://readthedocs.org/projects/acclaim-badges/badge/?version=latest
    :target: http://acclaim-badges.readthedocs.io/en/latest/
    :alt: Documentation

.. |pyversions-badge| image:: https://img.shields.io/pypi/pyversions/acclaim-badges.svg
    :target: https://pypi.python.org/pypi/acclaim-badges/
    :alt: Supported Python versions

.. |license-badge| image:: https://img.shields.io/github/license/edx/acclaim-badges.svg
    :target: https://github.com/edx/acclaim-badges/blob/master/LICENSE.txt
    :alt: License
