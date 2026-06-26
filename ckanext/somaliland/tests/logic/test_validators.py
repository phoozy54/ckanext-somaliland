"""Tests for validators.py."""

import pytest

import ckan.plugins.toolkit as tk

from ckanext.somaliland.logic import validators


def test_somaliland_reauired_with_valid_value():
    assert validators.somaliland_required("value") == "value"


def test_somaliland_reauired_with_invalid_value():
    with pytest.raises(tk.Invalid):
        validators.somaliland_required(None)
