from unittest.mock import AsyncMock, patch

import pytest

from matomo_mcp.client import MatomoClient


@pytest.fixture
def matomo_client():
    """Create a Matomo client for testing."""
    return MatomoClient("https://matomo.example.com", "test_token_123")


@pytest.mark.asyncio
async def test_client_initialization(matomo_client):
    """Test that the client initializes correctly."""
    assert matomo_client.base_url == "https://matomo.example.com"
    assert matomo_client.token_auth == "test_token_123"
    assert matomo_client.api_url == "https://matomo.example.com/index.php"


@pytest.mark.asyncio
async def test_get_site_info(matomo_client):
    """Test getting site information."""
    mock_response = {
        "idsite": "1",
        "name": "Test Site",
        "main_url": "https://example.com",
        "timezone": "UTC"
    }

    with patch("httpx.AsyncClient.get") as mock_get:
        mock_get.return_value = AsyncMock(
            json=lambda: mock_response,
            raise_for_status=lambda: None
        )

        result = await matomo_client.get_site_info(1)
        assert result == mock_response


@pytest.mark.asyncio
async def test_get_visits_summary(matomo_client):
    """Test getting visits summary."""
    mock_response = {
        "nb_visits": 100,
        "nb_uniq_visitors": 80,
        "nb_actions": 500,
        "bounce_rate": "45%"
    }

    with patch("httpx.AsyncClient.get") as mock_get:
        mock_get.return_value = AsyncMock(
            json=lambda: mock_response,
            raise_for_status=lambda: None
        )

        result = await matomo_client.get_visits_summary(1, "day", "today")
        assert result == mock_response


@pytest.mark.asyncio
async def test_api_error_handling(matomo_client):
    """Test that API errors are handled correctly."""
    error_response = {
        "result": "error",
        "message": "Invalid authentication token"
    }

    with patch("httpx.AsyncClient.get") as mock_get:
        mock_get.return_value = AsyncMock(
            json=lambda: error_response,
            raise_for_status=lambda: None
        )

        with pytest.raises(Exception, match="Matomo API error"):
            await matomo_client.call_api("SitesManager.getSiteFromId", {"idSite": 1})
