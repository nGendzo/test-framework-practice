import pytest
from pages.app import App


@pytest.fixture
def app(page):
    return App(page)


@pytest.fixture
def logged_in_app(app):
    app.login.navigate()
    app.login.login("standard_user", "secret_sauce")

    return app
    