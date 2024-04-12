"""Tests for statistics functions within the Model layer."""

import pandas as pd
import pytest

def test_max_mag_integers():
    # Test that max_mag function works for integers
    from lcanalyzer.models import max_mag

    test_input_df = pd.DataFrame(data=[[1, 5, 3], 
                                       [7, 8, 9], 
                                       [3, 4, 1]], columns=list("abc"))
    test_input_colname = "a"
    test_output = 7

    assert max_mag(test_input_df, test_input_colname) == test_output

def test_max_mag_zeros():
    # Test that max_mag function works for zeros
    from lcanalyzer.models import max_mag

    test_input_df = pd.DataFrame(data=[[0, 0, 0], 
                                       [0, 0, 0], 
                                       [0, 0, 0]], columns=list("abc"))
    test_input_colname = "b"
    test_output = 0

    assert max_mag(test_input_df, test_input_colname) == test_output

def test_max_mag_strings():
    # Test for TypeError when passing a string
    from lcanalyzer.models import max_mag

    test_input_colname = "b"
    with pytest.raises(TypeError):
        error_expected = max_mag('string', test_input_colname)

def test_mean_mag_integers():
    # Test that mean mag works for ints
    from lcanalyzer.models import mean_mag

    test_input_df = pd.DataFrame(data=[[1, 5, 3], 
                                       [7, 8, 9], 
                                       [3, 4, 1]], columns=list("abc"))
    test_input_colname = "a"
    test_output = (1 + 7 + 3) / 3.

    assert mean_mag(test_input_df, test_input_colname) == test_output

def test_mean_mag_zeros():
    # Test that mean_mag function works for ones
    from lcanalyzer.models import mean_mag

    test_input_df = pd.DataFrame(data=[[1, 1, 1], 
                                       [1, 1, 1], 
                                       [1, 1, 1]], columns=list("abc"))
    test_input_colname = "b"
    test_output = 1.0

    assert mean_mag(test_input_df, test_input_colname) == test_output

def test_mean_mag_negatives():
    # Test that mean_mag function works for negative and positive numbers
    from lcanalyzer.models import mean_mag

    test_input_df = pd.DataFrame(data=[[-1, 1,- 1], 
                                       [1, -1, 1], 
                                       [0, 0, 0]], columns=list("abc"))
    test_input_colname = "b"
    test_output = 0.0

    assert mean_mag(test_input_df, test_input_colname) == test_output

def test_min_mag_integers():
    # Test that min mag works for ints
    from lcanalyzer.models import min_mag

    test_input_df = pd.DataFrame(data=[[1, 5, 3], 
                                       [7, 8, 9], 
                                       [3, 4, 1]], columns=list("abc"))
    test_input_colname = "c"
    test_output = 1

    assert min_mag(test_input_df, test_input_colname) == test_output

def test_min_mag_negatives():
    # Test that min mag works for negatives
    from lcanalyzer.models import min_mag

    test_input_df = pd.DataFrame(data=[[-1, -5, -3], 
                                       [-7, -8, -9], 
                                       [-3, -4, -1]], columns=list("abc"))
    test_input_colname = "c"
    test_output = -9

    assert min_mag(test_input_df, test_input_colname) == test_output