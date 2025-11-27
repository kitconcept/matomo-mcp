# Matomo MCP Server Usage Guide

This guide provides examples of how to use the Matomo MCP server with Claude.

## Setup

1. Install the package:
```bash
pip install -e .
```

2. Configure your environment variables in `.env`:
```bash
cp .env.example .env
# Edit .env with your Matomo URL and token
```

3. Add to Claude Desktop configuration (see README.md for location):
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

4. Restart Claude Desktop

## Example Queries

Once configured, you can ask Claude questions like:

### Basic Site Information
```
"What information do you have about site 1 in Matomo?"
```

### Visitor Statistics
```
"Show me the visitor summary for site 1 for the last 30 days"
```

```
"Get the visits summary for site 1 for the month of January 2024"
```

### Page Performance
```
"What are the top 10 most visited pages on site 1 today?"
```

```
"Show me page statistics for site 1 for the last week"
```

### Geographic Data
```
"Which countries are my visitors from on site 1 for the last month?"
```

```
"Show me the top 20 countries for site 1 in the last 7 days"
```

### Browser and Device Analytics
```
"What devices are visitors using to access site 1?"
```

```
"Show me browser statistics for site 1 for the last month"
```

### Referrer Analysis
```
"Where are visitors coming from on site 1?"
```

```
"Show me the top referrers for site 1 in the last 30 days"
```

### Custom Queries
```
"Run a custom Matomo query for site 1 using method 'Actions.getPageTitles' for the last week"
```

```
"Query site 1 for goal conversions using the Goals.get API method for January 2024"
```

## Date Parameters

The Matomo API supports various date formats:

- `today` - Current day
- `yesterday` - Previous day
- `lastX` - Last X days (e.g., `last7`, `last30`)
- `YYYY-MM-DD` - Specific date (e.g., `2024-01-15`)
- `YYYY-MM-DD,YYYY-MM-DD` - Date range (e.g., `2024-01-01,2024-01-31`)

## Period Options

- `day` - Daily data
- `week` - Weekly data
- `month` - Monthly data
- `year` - Yearly data
- `range` - Date range (requires appropriate date parameter)

## Advanced Usage

### Segmentation
Use the `query_custom_report` tool with additional parameters:

```
"Run a custom query on site 1 for browser='Chrome' visitors using Actions.getPageUrls for last month"
```

The additional_params would be:
```json
{"segment": "browserName==Chrome"}
```

### Multiple Metrics
Combine multiple queries to get comprehensive reports:

```
"For site 1, show me:
1. Visit summary for the last 30 days
2. Top 5 pages
3. Top 5 countries
4. Device breakdown"
```

## Troubleshooting

### Authentication Errors
If you see authentication errors:
1. Verify your `MATOMO_TOKEN` is correct
2. Check that the token has appropriate permissions in Matomo
3. Ensure your `MATOMO_URL` is correct and accessible

### API Errors
If you encounter API errors:
1. Check that the site_id exists in your Matomo instance
2. Verify the API method is available in your Matomo version
3. Review the Matomo API documentation for parameter requirements

### Connection Issues
If the server can't connect:
1. Ensure your Matomo instance is accessible
2. Check firewall rules if using a self-hosted instance
3. Verify SSL certificates are valid

## API Method Reference

Common Matomo API methods you can use with `query_custom_report`:

- `SitesManager.getAllSites` - List all sites
- `Actions.getPageUrls` - Page URLs
- `Actions.getPageTitles` - Page titles
- `Actions.getDownloads` - Download tracking
- `Actions.getOutlinks` - Outbound links
- `Referrers.getAll` - All referrer types
- `Referrers.getSearchEngines` - Search engine referrers
- `Referrers.getWebsites` - Website referrers
- `Referrers.getSocials` - Social media referrers
- `UserCountry.getCountry` - Country statistics
- `UserCountry.getCity` - City statistics
- `DevicesDetection.getType` - Device types
- `DevicesDetection.getBrand` - Device brands
- `DevicesDetection.getModel` - Device models
- `DevicesDetection.getBrowsers` - Browser statistics
- `DevicesDetection.getOsVersions` - OS version statistics
- `VisitsSummary.get` - Visit summary
- `Goals.get` - Goal conversions
- `Events.getCategory` - Event categories
- `Events.getAction` - Event actions

For a complete list, refer to the [Matomo API Reference](https://developer.matomo.org/api-reference/reporting-api).
