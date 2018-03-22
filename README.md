TestFM
=========
Test suite for Foreman-Maintain(https://github.com/theforeman/foreman_maintain)

# Quickstart

The following is only a brief setup guide for TestFM.
The section on Running the Tests provides a more comprehensive guide to using
TestFM.

TestFM requires SSH access to the server system under test, and this SSH access
is implemented by pytest-ansible.

Get the source code and install dependencies:

$ git clone https://github.com/ntkathole/TestFM.git
$ pip install -r requirements.txt

That’s it! You can now go ahead and start testing The Foreman Maintain.
However, there are a few other things you need to do before continuing:

1. Make sure ssh-key is copied to the test system.

2. Make sure foreman maintain is installed on foreman/satellite server.

Running the Tests

Before running any tests, you must add foreman/satellite hostname to
TestFM/inventory file.

That done, you can run tests using pytest :

$ pytest --ansible-host-pattern foreman --ansible-inventory TestFM/inventory
tests/

It is possible to run a specific subset of tests:

$ pytest --ansible-host-pattern foreman --ansible-inventory TestFM/inventory
tests/test_case.py
$ pytest --ansible-host-pattern foreman --ansible-inventory TestFM/inventory
tests/test_case.py::test_case_name

TestFM is compatible with Python 2.7.

Want to contribute?

Thank you for considering contributing to TestFM! If you have any
question or concerns, feel free to reach out to the team.

Recommended

Import modules in alphabetical order.
Every method and function will have a properly formatted docstring.


In order to ensure you are able to pass the Travis CI build,
it is recommended that you run the following commands in the base of your
TestFM directory :

$flake8

flake8 will ensure that the changes you made are not in violation of PEP8
standards. If the command gives no output, then you have passed. If not, then
address any corrections recommended.

If you have something great, please submit a pull request anyway!
