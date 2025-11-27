# Quick Start Guide

Get up and running with the Matomo MCP Server in 5 minutes.

## Prerequisites

- Python 3.10 or higher
- A Matomo instance with API access
- Claude Desktop app

## Installation

### Option 1: Automated Installation (Recommended)

```bash
./install.sh
```

This script will:
1. Check your Python version
2. Create a virtual environment
3. Install all dependencies
4. Create a `.env` file from the template

### Option 2: Manual Installation

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the package
pip install -e .

# Copy environment template
cp .env.example .env
```

## Configuration

### 1. Get Your Matomo API Token

1. Log into your Matomo instance
2. Go to **Personal Settings** → **Security** → **Auth tokens**
3. Create a new token or copy an existing one

### 2. Configure Environment Variables

Edit `.env` and add your credentials:

```bash
MATOMO_URL=https://your-matomo-instance.com
MATOMO_TOKEN=your_api_token_here
```

### 3. Add to Claude Desktop

Find your Claude Desktop config file:
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

Add this configuration:

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

**Note**: You can also reference the example in `examples/claude_config.json`

### 4. Restart Claude Desktop

Close and reopen Claude Desktop for the changes to take effect.

## Verify Installation

In Claude Desktop, try asking:

```
What information do you have about Matomo site 1?
```

If configured correctly, Claude will use the Matomo MCP server to fetch site information.

## First Steps

Try these example queries to get familiar with the server:

### Check Site Info
```
Show me information about Matomo site 1
```

### Get Today's Statistics
```
What are today's visit statistics for site 1?
```

### View Top Pages
```
What are the top 10 pages on site 1 today?
```

### Check Geographic Distribution
```
Which countries are my visitors from on site 1?
```

### Analyze Device Usage
```
What devices are people using to visit site 1?
```

## Troubleshooting

### "Connection refused" or "Cannot connect"
- Verify your `MATOMO_URL` is correct and accessible
- Check if your Matomo instance is running
- Ensure there are no firewall rules blocking access

### "Invalid authentication token"
- Verify your `MATOMO_TOKEN` is correct
- Check that the token has not expired
- Ensure the token has appropriate permissions

### "Site not found"
- Verify the site ID exists in your Matomo instance
- Check that your API token has access to this site

### Server Not Showing in Claude
- Ensure Claude Desktop has been restarted
- Check the config file for JSON syntax errors
- Verify the file path is correct for your OS

### Python Version Errors
- Ensure you have Python 3.10 or higher
- Check with: `python3 --version`

## Next Steps

- Read the [Usage Guide](USAGE.md) for more example queries
- Check the [API Reference](API_REFERENCE.md) for detailed tool documentation
- Explore the [Matomo API Documentation](https://developer.matomo.org/api-reference/reporting-api) for advanced features

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review the error messages in Claude Desktop
3. Verify your configuration settings
4. Consult the Matomo API documentation

## Development

To contribute or modify the server:

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run tests with coverage
pytest --cov=matomo_mcp
```

See the main [README.md](README.md) for more information.
