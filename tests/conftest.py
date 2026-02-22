"""
Pytest configuration for vvuq-technical-validator tests.
"""
import pytest
import resource


@pytest.fixture(autouse=True)
def limit_memory():
    """Prevent any single test from using >2GB RAM."""
    try:
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, hard))
        yield
        resource.setrlimit(resource.RLIMIT_AS, (soft, hard))
    except (ValueError, resource.error):
        # Resource limits not supported on this platform
        yield
