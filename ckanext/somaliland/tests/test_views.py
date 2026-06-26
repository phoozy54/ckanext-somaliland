"""Tests for views.py."""

import pytest

import ckanext.somaliland.validators as validators


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "somaliland")
@pytest.mark.usefixtures("with_plugins")
def test_somaliland_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("somaliland.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, somaliland!"
