import pytest


@pytest.fixture(scope="session")
def neo(accounts):
    yield accounts[0]


@pytest.fixture(scope="session")
def morpheus(accounts):
    yield accounts[1]


@pytest.fixture(scope="session")
def trinity(accounts):
    yield accounts[2]


@pytest.fixture(scope="session")
def oracle(accounts):
    yield accounts[3]
