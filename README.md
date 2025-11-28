# Matomo MCP Server

[![Tests](https://github.com/kitconcept/matomo-mcp/actions/workflows/test.yml/badge.svg)](https://github.com/kitconcept/matomo-mcp/actions/workflows/test.yml)
[![Code Quality](https://github.com/kitconcept/matomo-mcp/actions/workflows/lint.yml/badge.svg)](https://github.com/kitconcept/matomo-mcp/actions/workflows/lint.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Model Context Protocol (MCP) server that provides access to Matomo's Reporting API.

## Features

- Access Matomo reporting data through MCP tools
- Query website statistics, visitor information, and analytics data
- Support for multiple Matomo sites
- Secure API token authentication

## Installation

```bash
pip install -e .
```

## Configuration

The server requires the following environment variables:

- `MATOMO_URL`: Your Matomo instance URL (e.g., `https://analytics.example.com`)
- `MATOMO_TOKEN`: Your Matomo API authentication token

You can obtain an API token from your Matomo instance under:
Personal Settings → Security → Auth tokens

## Usage with Claude Desktop

Add this to your Claude Desktop configuration:

### MacOS
`~/Library/Application Support/Claude/claude_desktop_config.json`

### Windows
`%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "matomo": {
      "command": "python",
      "args": ["-m", "matomo_mcp"],
      "env": {
        "MATOMO_URL": "https://your-matomo-instance.com",
        "MATOMO_TOKEN": "your_api_token_here"
      }
    }
  }
}
```

## Available Tools

### get_site_info
Get information about a specific Matomo site.

**Parameters:**
- `site_id`: The ID of the site (integer)

### get_visits_summary
Get a summary of visits for a site within a date range.

**Parameters:**
- `site_id`: The ID of the site (integer)
- `period`: Time period (day, week, month, year, range)
- `date`: Date or date range (e.g., "2024-01-01", "last30", "today")

### get_page_urls
Get the most visited page URLs for a site.

**Parameters:**
- `site_id`: The ID of the site (integer)
- `period`: Time period (day, week, month, year, range)
- `date`: Date or date range
- `limit`: Maximum number of results (default: 10)

### get_countries
Get visitor statistics by country.

**Parameters:**
- `site_id`: The ID of the site (integer)
- `period`: Time period (day, week, month, year, range)
- `date`: Date or date range
- `limit`: Maximum number of results (default: 10)

### get_user_settings
Get visitor browser and device information.

**Parameters:**
- `site_id`: The ID of the site (integer)
- `period`: Time period (day, week, month, year, range)
- `date`: Date or date range

### query_custom_report
Execute a custom Matomo API query.

**Parameters:**
- `method`: Matomo API method (e.g., "Actions.getPageUrls")
- `site_id`: The ID of the site (integer)
- `period`: Time period (day, week, month, year, range)
- `date`: Date or date range
- `additional_params`: Optional JSON object with additional parameters

## Development

Install development dependencies:

```bash
pip install -e ".[dev]"
```

Run tests:

```bash
pytest
```

## License

MIT
