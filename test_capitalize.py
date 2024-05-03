import pytest
from capitalize import *

def test_capital_case():
    assert capitalize_function("elvebakken") == "Elvebakken"

def test_capital_case_lowercase():
    assert capitalize_function("elvebakken") != "Elvebakken"