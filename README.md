# pytest - helps you write better programs


> *"The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries."*
> - <cite>[Pytest docs](docs.pytest.org/en/6.2.x)</cite>

## Requirements
To run the tests you should first install the project requirements.
- python >=3.8
- poetry >= 1.1.1
- pytest >= 5.4.3 (The `poetry install` command handles this requirement)
- pip >= 21.0.1

If you do not have this installed, you can do so by running the following commands. 

```bash
sudo apt install python3 
sudo apt install pip
pip install poetry
poetry install
```

For Windows installation you can follow the [Python documentation](https://www.python.org/downloads/) and [Pip tutorial](https://www.liquidweb.com/kb/install-pip-windows/)

## Running the tests

With all the requirements met, you can, for lack of a better word, test the tests, by running the following command:

```bash
poetry run pytest -v
```

> The **-v** flag sets the output to be verbose, this can be ignored.