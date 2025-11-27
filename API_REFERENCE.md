# Matomo MCP Server API Reference

This document provides detailed information about all available tools in the Matomo MCP server.

## Tools

### get_site_info

Get detailed information about a specific Matomo site.

**Parameters:**
- `site_id` (integer, required): The ID of the Matomo site

**Returns:**
```json
{
  "idsite": "1",
  "name": "My Website",
  "main_url": "https://example.com",
  "ts_created": "2024-01-01 00:00:00",
  "ecommerce": "0",
  "sitesearch": "1",
  "sitesearch_keyword_parameters": "",
  "sitesearch_category_parameters": "",
  "timezone": "UTC",
  "currency": "USD",
  "exclude_unknown_urls": "0",
  "excluded_ips": "",
  "excluded_parameters": "",
  "excluded_user_agents": "",
  "group": "",
  "type": "website"
}
```

**Example:**
```
Get information about Matomo site 1
```

---

### get_visits_summary

Get a comprehensive summary of visits for a site including key metrics.

**Parameters:**
- `site_id` (integer, required): The ID of the Matomo site
- `period` (string, optional): Time period - one of: `day`, `week`, `month`, `year`, `range` (default: `day`)
- `date` (string, optional): Date or date range (default: `today`)
  - Examples: `today`, `yesterday`, `last7`, `last30`, `2024-01-01`, `2024-01-01,2024-01-31`

**Returns:**
```json
{
  "nb_uniq_visitors": 1234,
  "nb_visits": 1567,
  "nb_actions": 8901,
  "nb_visits_converted": 42,
  "bounce_count": 456,
  "sum_visit_length": 567890,
  "max_actions": 123,
  "bounce_rate": "29%",
  "nb_actions_per_visit": 5.7,
  "avg_time_on_site": 362
}
```

**Example:**
```
Show me the visits summary for site 1 for the last 30 days
```

---

### get_page_urls

Get statistics about the most visited page URLs.

**Parameters:**
- `site_id` (integer, required): The ID of the Matomo site
- `period` (string, optional): Time period (default: `day`)
- `date` (string, optional): Date or date range (default: `today`)
- `limit` (integer, optional): Maximum number of results (default: 10)

**Returns:**
```json
[
  {
    "label": "/products",
    "nb_visits": 1234,
    "nb_uniq_visitors": 890,
    "nb_hits": 2345,
    "sum_time_spent": 456789,
    "entry_nb_visits": 567,
    "entry_nb_actions": 2890,
    "entry_sum_visit_length": 234567,
    "entry_bounce_count": 123,
    "exit_nb_visits": 543,
    "avg_time_on_page": 370,
    "bounce_rate": "22%",
    "exit_rate": "44%"
  }
]
```

**Example:**
```
What are the top 20 pages on site 1 for the last week?
```

---

### get_countries

Get visitor statistics segmented by country.

**Parameters:**
- `site_id` (integer, required): The ID of the Matomo site
- `period` (string, optional): Time period (default: `day`)
- `date` (string, optional): Date or date range (default: `today`)
- `limit` (integer, optional): Maximum number of results (default: 10)

**Returns:**
```json
[
  {
    "label": "United States",
    "code": "us",
    "logo": "plugins/Morpheus/icons/dist/flags/us.png",
    "nb_visits": 1234,
    "nb_uniq_visitors": 890,
    "nb_actions": 5678,
    "sum_visit_length": 456789,
    "bounce_count": 234,
    "nb_visits_converted": 45,
    "nb_conversions": 67,
    "revenue": 1234.56
  }
]
```

**Example:**
```
Show me visitor countries for site 1 in January 2024
```

---

### get_user_settings

Get statistics about visitor device types (desktop, mobile, tablet).

**Parameters:**
- `site_id` (integer, required): The ID of the Matomo site
- `period` (string, optional): Time period (default: `day`)
- `date` (string, optional): Date or date range (default: `today`)

**Returns:**
```json
[
  {
    "label": "Desktop",
    "nb_visits": 5678,
    "nb_uniq_visitors": 3456,
    "nb_actions": 23456,
    "sum_visit_length": 2345678,
    "bounce_count": 1234,
    "nb_visits_converted": 234
  },
  {
    "label": "Smartphone",
    "nb_visits": 3456,
    "nb_uniq_visitors": 2345,
    "nb_actions": 12345,
    "sum_visit_length": 1234567,
    "bounce_count": 890,
    "nb_visits_converted": 123
  }
]
```

**Example:**
```
What devices are people using to visit site 1?
```

---

### get_browsers

Get statistics about visitor web browsers.

**Parameters:**
- `site_id` (integer, required): The ID of the Matomo site
- `period` (string, optional): Time period (default: `day`)
- `date` (string, optional): Date or date range (default: `today`)

**Returns:**
```json
[
  {
    "label": "Chrome",
    "nb_visits": 6789,
    "nb_uniq_visitors": 4567,
    "nb_actions": 34567,
    "sum_visit_length": 3456789,
    "bounce_count": 1567,
    "nb_visits_converted": 345,
    "logo": "plugins/Morpheus/icons/dist/browsers/chrome.png"
  }
]
```

**Example:**
```
Show me browser statistics for site 1 for the last month
```

---

### get_referrers

Get information about where visitors are coming from (referrer sources).

**Parameters:**
- `site_id` (integer, required): The ID of the Matomo site
- `period` (string, optional): Time period (default: `day`)
- `date` (string, optional): Date or date range (default: `today`)
- `limit` (integer, optional): Maximum number of results (default: 10)

**Returns:**
```json
[
  {
    "label": "Search Engines",
    "nb_visits": 2345,
    "nb_uniq_visitors": 1890,
    "nb_actions": 12345,
    "sum_visit_length": 1234567,
    "bounce_count": 567,
    "nb_visits_converted": 123,
    "nb_conversions": 145,
    "revenue": 2345.67
  },
  {
    "label": "Direct Entry",
    "nb_visits": 1234,
    "nb_uniq_visitors": 890,
    "nb_actions": 6789,
    "sum_visit_length": 678901,
    "bounce_count": 234,
    "nb_visits_converted": 67,
    "nb_conversions": 89,
    "revenue": 1234.56
  }
]
```

**Example:**
```
Where are visitors to site 1 coming from in the last 30 days?
```

---

### query_custom_report

Execute any custom Matomo API query for advanced reporting needs.

**Parameters:**
- `method` (string, required): Matomo API method name
  - Examples: `Actions.getPageTitles`, `Goals.get`, `Events.getCategory`
- `site_id` (integer, required): The ID of the Matomo site
- `period` (string, optional): Time period (default: `day`)
- `date` (string, optional): Date or date range (default: `today`)
- `additional_params` (string, optional): Additional parameters as JSON string
  - Example: `{"segment": "browserName==Chrome", "filter_limit": 20}`

**Returns:**
Varies depending on the API method called.

**Example:**
```
Run a custom query on site 1 using method 'Goals.get' for goal 1 in January 2024
```

With additional parameters:
```json
{
  "idGoal": "1"
}
```

---

## Common Patterns

### Date Ranges

Use the `period` and `date` parameters to specify time ranges:

**Last N days:**
```json
{
  "period": "day",
  "date": "last30"
}
```

**Specific date:**
```json
{
  "period": "day",
  "date": "2024-01-15"
}
```

**Date range:**
```json
{
  "period": "range",
  "date": "2024-01-01,2024-01-31"
}
```

**Month:**
```json
{
  "period": "month",
  "date": "2024-01"
}
```

### Segmentation

Use the `query_custom_report` tool with segments for advanced filtering:

**Chrome users only:**
```json
{
  "method": "VisitsSummary.get",
  "site_id": 1,
  "additional_params": "{\"segment\": \"browserName==Chrome\"}"
}
```

**Mobile visitors:**
```json
{
  "method": "VisitsSummary.get",
  "site_id": 1,
  "additional_params": "{\"segment\": \"deviceType==smartphone\"}"
}
```

**Returning visitors:**
```json
{
  "method": "VisitsSummary.get",
  "site_id": 1,
  "additional_params": "{\"segment\": \"visitorType==returning\"}"
}
```

## Error Handling

All tools return errors in plain text format:

```
Error: Matomo API error: Invalid authentication token
```

```
Error: MATOMO_URL and MATOMO_TOKEN environment variables must be set
```

Common errors:
- Invalid authentication token: Check your API token
- Site not found: Verify the site_id exists
- Invalid date format: Use YYYY-MM-DD format
- Method not found: Check the API method name spelling

## Rate Limiting

The server respects Matomo's rate limiting. If you encounter rate limit errors:
- Reduce the frequency of requests
- Use broader date ranges instead of multiple specific dates
- Contact your Matomo administrator to adjust rate limits

## Additional Resources

- [Matomo Reporting API Documentation](https://developer.matomo.org/api-reference/reporting-api)
- [Matomo Segmentation Documentation](https://matomo.org/docs/segmentation/)
- [Matomo API Reference](https://developer.matomo.org/api-reference/reporting-api-introduction)
