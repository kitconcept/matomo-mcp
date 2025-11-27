import httpx
from typing import Any, Dict, Optional
from urllib.parse import urljoin


class MatomoClient:
    """Client for interacting with the Matomo Reporting API."""

    def __init__(self, base_url: str, token_auth: str):
        """
        Initialize the Matomo client.

        Args:
            base_url: Base URL of the Matomo instance
            token_auth: API authentication token
        """
        self.base_url = base_url.rstrip('/')
        self.token_auth = token_auth
        self.api_url = urljoin(self.base_url + '/', 'index.php')

    async def call_api(
        self,
        method: str,
        params: Optional[Dict[str, Any]] = None
    ) -> Any:
        """
        Make an API call to Matomo.

        Args:
            method: API method name (e.g., 'SitesManager.getSiteFromId')
            params: Additional parameters for the API call

        Returns:
            API response data

        Raises:
            httpx.HTTPError: If the request fails
        """
        query_params = {
            'module': 'API',
            'method': method,
            'format': 'JSON',
            'token_auth': self.token_auth,
        }

        if params:
            query_params.update(params)

        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(self.api_url, params=query_params)
            response.raise_for_status()
            data = response.json()

            # Check for Matomo API errors
            if isinstance(data, dict) and 'result' in data and data['result'] == 'error':
                raise Exception(f"Matomo API error: {data.get('message', 'Unknown error')}")

            return data

    async def get_site_info(self, site_id: int) -> Dict[str, Any]:
        """Get information about a specific site."""
        return await self.call_api('SitesManager.getSiteFromId', {'idSite': site_id})

    async def get_visits_summary(
        self,
        site_id: int,
        period: str = 'day',
        date: str = 'today'
    ) -> Dict[str, Any]:
        """Get visits summary for a site."""
        return await self.call_api('VisitsSummary.get', {
            'idSite': site_id,
            'period': period,
            'date': date
        })

    async def get_page_urls(
        self,
        site_id: int,
        period: str = 'day',
        date: str = 'today',
        limit: int = 10
    ) -> Any:
        """Get most visited page URLs."""
        return await self.call_api('Actions.getPageUrls', {
            'idSite': site_id,
            'period': period,
            'date': date,
            'filter_limit': limit
        })

    async def get_countries(
        self,
        site_id: int,
        period: str = 'day',
        date: str = 'today',
        limit: int = 10
    ) -> Any:
        """Get visitor statistics by country."""
        return await self.call_api('UserCountry.getCountry', {
            'idSite': site_id,
            'period': period,
            'date': date,
            'filter_limit': limit
        })

    async def get_user_settings(
        self,
        site_id: int,
        period: str = 'day',
        date: str = 'today'
    ) -> Any:
        """Get visitor browser and device information."""
        return await self.call_api('DevicesDetection.getType', {
            'idSite': site_id,
            'period': period,
            'date': date
        })

    async def get_browsers(
        self,
        site_id: int,
        period: str = 'day',
        date: str = 'today'
    ) -> Any:
        """Get visitor browser statistics."""
        return await self.call_api('DevicesDetection.getBrowsers', {
            'idSite': site_id,
            'period': period,
            'date': date
        })

    async def get_referrers(
        self,
        site_id: int,
        period: str = 'day',
        date: str = 'today',
        limit: int = 10
    ) -> Any:
        """Get referrer information."""
        return await self.call_api('Referrers.getAll', {
            'idSite': site_id,
            'period': period,
            'date': date,
            'filter_limit': limit
        })
