# Changelog

All notable changes to the Matomo MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-11-27

### Added
- Initial release of Matomo MCP Server
- Core MCP server implementation with stdio communication
- Matomo API client with async/await support
- 8 reporting tools:
  - `get_site_info` - Retrieve site configuration
  - `get_visits_summary` - Get visit statistics
  - `get_page_urls` - Analyze page performance
  - `get_countries` - Geographic visitor data
  - `get_user_settings` - Device type analytics
  - `get_browsers` - Browser usage statistics
  - `get_referrers` - Traffic source analysis
  - `query_custom_report` - Custom API queries
- Comprehensive documentation:
  - README.md with setup instructions
  - QUICKSTART.md for rapid deployment
  - USAGE.md with example queries
  - API_REFERENCE.md with complete tool documentation
  - PROJECT_SUMMARY.md with architecture overview
- Test suite with pytest and async support
- Automated installation script (install.sh)
- Example Claude Desktop configuration
- Environment variable configuration
- MIT License

### Features
- Support for all Matomo Reporting API date formats
- Flexible period selection (day, week, month, year, range)
- Configurable result limits for list-based queries
- Error handling with clear error messages
- HTTP timeout configuration (30 seconds)
- Environment-based configuration

### Security
- API token authentication
- Environment variable-based credentials
- No hardcoded credentials
- Read-only API access (reporting only)
- HTTPS-only connections

### Documentation
- Complete API reference for all tools
- Multiple usage examples
- Troubleshooting guide
- Development setup instructions
- Claude Desktop integration guide

## [Unreleased]

### Planned Features
- Response caching for performance optimization
- Batch query support
- Pre-configured segment templates
- Data export in multiple formats
- Dashboard configuration support
- Real-time metrics via WebSocket
- Anomaly detection and alerting
- Enhanced error messages with suggestions
- Pagination support for large datasets
- Rate limiting with automatic retry

### Under Consideration
- Support for Matomo Cloud and self-hosted instances
- Multi-site query support
- Custom date range presets
- Query result visualization helpers
- Integration with other MCP servers
- Webhook support for notifications

---

## Version History

### Version Numbering

This project follows semantic versioning:
- **MAJOR** version for incompatible API changes
- **MINOR** version for new functionality in a backwards compatible manner
- **PATCH** version for backwards compatible bug fixes

### Release Notes

#### 0.1.0 - Initial Release
This is the first public release of the Matomo MCP Server. It provides comprehensive access to Matomo's Reporting API through the Model Context Protocol, enabling natural language queries via Claude Desktop.

**Key Highlights:**
- 8 specialized reporting tools covering common analytics needs
- Full support for Matomo's date range and period options
- Clean, async Python implementation
- Extensive documentation and examples
- Easy installation and configuration
- Works out-of-the-box with Claude Desktop

**Limitations:**
- Currently supports Reporting API only (no Tracking or Admin APIs)
- No built-in caching (queries hit the Matomo API directly)
- Single-site queries only (no cross-site aggregation)
- No real-time streaming support

---

[0.1.0]: https://github.com/yourusername/matomo-mcp-python/releases/tag/v0.1.0
