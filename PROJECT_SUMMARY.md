# Matomo MCP Server - Project Summary

## Overview

This project implements a Model Context Protocol (MCP) server that provides access to Matomo's Reporting API. It allows Claude Desktop and other MCP clients to query Matomo analytics data through natural language.

## Project Structure

```
matomo-mcp/
├── matomo_mcp/              # Main package
│   ├── __init__.py          # Package initialization
│   ├── __main__.py          # Entry point for python -m matomo_mcp
│   ├── client.py            # Matomo API client
│   └── server.py            # MCP server implementation
├── tests/                   # Test suite
│   ├── __init__.py
│   └── test_client.py       # Client tests
├── examples/                # Example configurations
│   └── claude_config.json   # Claude Desktop config example
├── pyproject.toml           # Project metadata and dependencies
├── README.md                # Main documentation
├── QUICKSTART.md            # Quick start guide
├── USAGE.md                 # Detailed usage examples
├── API_REFERENCE.md         # Complete API documentation
├── LICENSE                  # MIT License
├── .gitignore               # Git ignore rules
├── .env.example             # Environment variable template
└── install.sh               # Installation script
```

## Key Features

### 8 Reporting Tools

1. **get_site_info** - Site configuration and metadata
2. **get_visits_summary** - Visit metrics and statistics
3. **get_page_urls** - Page performance data
4. **get_countries** - Geographic visitor distribution
5. **get_user_settings** - Device type analytics
6. **get_browsers** - Browser usage statistics
7. **get_referrers** - Traffic source analysis
8. **query_custom_report** - Custom API queries

### Technical Implementation

- **Protocol**: Model Context Protocol (MCP)
- **Language**: Python 3.10+
- **Dependencies**:
  - `mcp>=0.9.0` - MCP SDK
  - `httpx>=0.27.0` - Async HTTP client
- **Architecture**: Async/await pattern for all API calls
- **Communication**: stdio-based MCP server

## API Coverage

The server focuses exclusively on Matomo's Reporting API, providing access to:

- **Site Management**: Site information and configuration
- **Visit Analytics**: Visitor counts, unique visitors, actions
- **Page Analytics**: Page views, time on page, bounce rates
- **Geographic Data**: Country and city visitor distribution
- **Device Analytics**: Desktop, mobile, tablet usage
- **Browser Analytics**: Browser and OS statistics
- **Referrer Analytics**: Traffic sources and campaigns
- **Custom Queries**: Access to any Matomo reporting API method

## Configuration

### Environment Variables

```bash
MATOMO_URL=https://your-matomo-instance.com
MATOMO_TOKEN=your_api_token_here
```

### Claude Desktop Integration

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

## Installation Methods

### 1. Automated Script
```bash
./install.sh
```

### 2. Manual Installation
```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

## Testing

The project includes unit tests with mocking:

```bash
pytest                     # Run all tests
pytest --cov=matomo_mcp   # Run with coverage
```

Test coverage includes:
- Client initialization
- API call methods
- Error handling
- Response parsing

## Usage Examples

### Basic Queries
```
"Show me today's visitor statistics for site 1"
"What are the top pages on site 1 this month?"
"Which countries are my visitors from?"
```

### Advanced Queries
```
"Get visits for site 1 segmented by Chrome users for last 30 days"
"Show me goal conversions for January 2024"
"Compare desktop vs mobile traffic for site 1"
```

## Security Considerations

- API tokens are stored in environment variables
- No credentials in code or version control
- HTTPS enforced for all API calls
- Token permissions controlled in Matomo
- Read-only access (reporting API only)

## Error Handling

The server provides clear error messages for:
- Missing environment variables
- Invalid authentication tokens
- Invalid site IDs
- Malformed API requests
- Network connectivity issues
- Matomo API errors

## Limitations

By design, this server:
- **Only** supports the Reporting API
- Does **not** support write operations
- Does **not** support the Tracking API
- Does **not** support user management
- Does **not** support site configuration changes

This ensures the server is safe for read-only analytics access.

## Performance

- Async/await for non-blocking I/O
- HTTP connection pooling via httpx
- 30-second timeout for API calls
- Efficient JSON parsing
- Minimal memory footprint

## Future Enhancements

Potential improvements for future versions:

1. **Caching**: Add response caching for frequently accessed data
2. **Batch Queries**: Support multiple queries in one call
3. **Real-time Data**: WebSocket support for live metrics
4. **Data Visualization**: Return chart/graph data structures
5. **Export Formats**: Support CSV, Excel export formats
6. **Segments**: Pre-configured common segments
7. **Dashboards**: Custom dashboard configurations
8. **Alerts**: Anomaly detection and alerting

## Contributing

To contribute:

1. Install development dependencies: `pip install -e ".[dev]"`
2. Write tests for new features
3. Follow existing code style
4. Update documentation
5. Test with real Matomo instance

## Documentation Files

- **README.md**: Main overview and setup instructions
- **QUICKSTART.md**: 5-minute setup guide
- **USAGE.md**: Detailed usage examples and patterns
- **API_REFERENCE.md**: Complete tool documentation
- **PROJECT_SUMMARY.md**: This file - architectural overview

## License

MIT License - see LICENSE file for details

## Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [Matomo API Documentation](https://developer.matomo.org/api-reference/reporting-api)
- [Python MCP SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Claude Desktop](https://claude.ai/download)

## Version History

### v0.1.0 (Current)
- Initial release
- 8 reporting tools
- Full Matomo Reporting API support
- Claude Desktop integration
- Comprehensive documentation
- Test suite
- Installation scripts

---

**Built with the Model Context Protocol for seamless integration with Claude and other AI assistants.**
