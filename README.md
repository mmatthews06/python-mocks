# Python Unit Testing Mock Examples
Some example Python unit test mocks.

**NOTE**: This is, by no means, an example of best general coding practices in Python, or even best testing practices. Some tests, like testing log output, may be questionable, but they fit a narrow use case that was good to build these examples. **This code is only meant to demonstrate unit test mocking in Python.**

This code has been tested with Python 3.7, though should be backwards compatible to 3.6 and maybe 3.5.

## Running the Tests
To run the tests, do the following:

1. Clone the repository:
 ```{bash}
 git clone https://github.com/mmatthews06/python-mocks.git
 ```
2. Change into the source directory:
 ```{bash}
 cd python-mocks/src
 ```
3. Run the unit tests
 ```{bash}
 python -m unittest discover
 ```

## Running the example app.
There is not much there, but you may also want to run the app:
```{bash}
python src/main.py --foo hello --bar bye -r -p ltra
```
## Linting
This project uses *pytlint* rules that were changed slightly from PEP8:

```{bash}
pip install -r requirements.txt
pylint ./src
```
