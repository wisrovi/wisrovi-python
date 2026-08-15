"""Mocking de Servicios Externos."""
from unittest.mock import MagicMock
mock_api = MagicMock(return_value={'ok': True})
print('Mock resultado:', mock_api())
