"""
Simplified tests for the Hello World endpoint using direct function testing
"""

import pytest
from core.data_models import HelloWorldResponse


def test_hello_world_response_model():
    """Test that the HelloWorldResponse model works correctly"""
    response = HelloWorldResponse(message="Hello World")
    assert response.message == "Hello World"
    assert response.model_dump() == {"message": "Hello World"}


def test_hello_world_response_model_json():
    """Test that the HelloWorldResponse model serializes to JSON correctly"""
    response = HelloWorldResponse(message="Hello World")
    assert response.model_dump_json() == '{"message":"Hello World"}'
