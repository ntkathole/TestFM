.. testfm documentation master file, created by
   sphinx-quickstart on Wed Oct  3 23:55:16 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to testfm's documentation!
==================================

# testfm


[![Build Status](https://api.travis-ci.org/SatelliteQE/testfm.svg?branch=master)](https://travis-ci.org/SatelliteQE/testfm) [![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


A test suite based on pytest-ansible that exercises The Foreman maintenance tool

# Quickstart

The following is only a brief setup guide for TestFM.
The section on Running the Tests provides a more comprehensive guide to using
TestFM.

TestFM requires SSH access to the server system under test, and this SSH access
is implemented by pytest-ansible.

Get the source code and install dependencies:

    $ git clone https://github.com/SatelliteQE/testfm.git
    $ pip3 install -r requirements.txt

That’s it! You can now go ahead and start testing The Foreman Maintain.
However, there are a few other things you need to do before continuing:

- Make sure ssh-key is copied to the test system.

- Make sure foreman maintain is installed on foreman/satellite server.

## Running the Tests

Before running any tests, you must add foreman or satellite hostname to the
`testfm/inventory` file (first copy it from`testfm/inventory.sample`).

That done, you can run tests using pytest :

    $ pytest --ansible-host-pattern satellite --ansible-user=root  --ansible-inventory testfm/inventory
    tests/

It is possible to run a specific subset of tests:

    $ pytest --ansible-host-pattern satellite --ansible-user=root --ansible-inventory testfm/inventory
    tests/test_case.py

    $ pytest --ansible-host-pattern satellite --ansible-user=root  --ansible-inventory testfm/inventory
    tests/test_case.py::test_case_name

## Want to contribute?

Thank you for considering contributing to TestFM! If you have any
question or concerns, feel free to reach out to the team.

### Recommended

- Import modules in alphabetical order.
- Every method and function will have a properly formatted docstring.


In order to ensure you are able to pass the Travis CI build,
it is recommended that you run the following commands in the base of your
testfm directory :

    $ flake8

flake8 will ensure that the changes you made are not in violation of PEP8
standards. If the command gives no output, then you have passed. If not, then
address any corrections recommended.

If you have something great, please submit a pull request anyway!

## Licensing

TestFM is licensed under GNU General Public License v3.0.

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
