#!/usr/bin/python3
import pytest
import branch_and_bound


@pytest.fixture
def input_file():
    return branch_and_bound.count_result("/home/kognic/tsp/burma14.json")

    
def test_branch_and_bound(input_file):
    assert input_file == 3323


