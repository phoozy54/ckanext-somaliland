"""Tests for helpers.py."""

import ckanext.somaliland.helpers as helpers


def test_somaliland_hello():
    assert helpers.somaliland_hello() == "Hello, somaliland!"
