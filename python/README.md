# Legacy code implementation and testing

This project should allow us to explore implementation of new features in a legacy software using TDD principles such as Golden Master testing.

Instructions here: https://github.com/Axeedo/kata-gilded-rose.

# Installation and set up

## Create python virtual environment

In command line, go to project directory and type:

$ python3 -m venv venv

## Activate virtual environment

(OS X & Linux)
$ . venv/bin/activate

(Windows)
$ venv\Scripts\activate

# Golden Master testing

First, let's persist the output of our initial program using the following command.

$ python update_output.py

The legacy output is stored in golden-master/expected-output.txt
