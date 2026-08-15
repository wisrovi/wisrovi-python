"""Fixtures de Pytest."""
def fixture_db(): return {'status': 'ready'}
print('Fixture:', fixture_db())
