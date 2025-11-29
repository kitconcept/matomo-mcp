# Changelog

All notable changes to the Matomo MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0a1] - 2025-11-29

### Added

- Initial release of Matomo MCP Server @tisto

---

## Version History

### Version Numbering

This project follows semantic versioning:

- **MAJOR** version for incompatible API changes
- **MINOR** version for new functionality in a backwards compatible manner
- **PATCH** version for backwards compatible bug fixes

### Release Notes

#### - Initial Release

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

[]: https://github.com/yourusername/matomo-mcp/releases/tag/1.0.0a1
