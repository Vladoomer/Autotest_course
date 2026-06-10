import pytest
SYSTEM_VERSION = "1.0.0"
@pytest.mark.skip(reason="feature in development")
def test_feature_in_development():
    pass

@pytest.mark.skipif(SYSTEM_VERSION == "1.0.0", reason="feature in development")
def test_system_version_valid():
    pass

@pytest.mark.skipif(SYSTEM_VERSION=="1.0.1", reason="feature in development")
def test_system_version_invalid():
    pass

@pytest.mark.xfail(reason="bag found")
def test_with_bag():
    pass

@pytest.mark.xfail(reason="bag has been removed, but marks xfail yet")
def test_without_bag():
    pass
@pytest.mark.xfail(reason="external service temp unavailable")
def test_external_service_in_unavailable():
    pass