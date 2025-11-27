import os
import json
import logging
from typing import Any, Optional
from mcp.server import Server
from mcp.types import Tool, TextContent, ImageContent, EmbeddedResource
from pydantic import AnyUrl
from .client import MatomoClient

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("matomo-mcp-server")

# Initialize the MCP server
app = Server("matomo-mcp-server")

# Global client instance
matomo_client: Optional[MatomoClient] = None


def get_client() -> MatomoClient:
    """Get or create the Matomo client instance."""
    global matomo_client
    if matomo_client is None:
        base_url = os.getenv("MATOMO_URL")
        token = os.getenv("MATOMO_TOKEN")

        if not base_url or not token:
            raise ValueError(
                "MATOMO_URL and MATOMO_TOKEN environment variables must be set"
            )

        matomo_client = MatomoClient(base_url, token)

    return matomo_client


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available Matomo reporting tools."""
    return [
        Tool(
            name="get_site_info",
            description="Get information about a specific Matomo site including name, URLs, timezone, and creation date",
            inputSchema={
                "type": "object",
                "properties": {
                    "site_id": {
                        "type": "integer",
                        "description": "The ID of the Matomo site"
                    }
                },
                "required": ["site_id"]
            }
        ),
        Tool(
            name="get_visits_summary",
            description="Get a summary of visits for a site including total visits, unique visitors, actions, bounce rate, and visit duration",
            inputSchema={
                "type": "object",
                "properties": {
                    "site_id": {
                        "type": "integer",
                        "description": "The ID of the Matomo site"
                    },
                    "period": {
                        "type": "string",
                        "description": "Time period: day, week, month, year, or range",
                        "enum": ["day", "week", "month", "year", "range"],
                        "default": "day"
                    },
                    "date": {
                        "type": "string",
                        "description": "Date or date range (e.g., '2024-01-01', 'last30', 'today', '2024-01-01,2024-01-31')",
                        "default": "today"
                    }
                },
                "required": ["site_id"]
            }
        ),
        Tool(
            name="get_page_urls",
            description="Get the most visited page URLs for a site with metrics like pageviews, unique pageviews, bounce rate, and time spent",
            inputSchema={
                "type": "object",
                "properties": {
                    "site_id": {
                        "type": "integer",
                        "description": "The ID of the Matomo site"
                    },
                    "period": {
                        "type": "string",
                        "description": "Time period: day, week, month, year, or range",
                        "enum": ["day", "week", "month", "year", "range"],
                        "default": "day"
                    },
                    "date": {
                        "type": "string",
                        "description": "Date or date range",
                        "default": "today"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of results to return",
                        "default": 10
                    }
                },
                "required": ["site_id"]
            }
        ),
        Tool(
            name="get_countries",
            description="Get visitor statistics by country including visits, actions, and conversion metrics",
            inputSchema={
                "type": "object",
                "properties": {
                    "site_id": {
                        "type": "integer",
                        "description": "The ID of the Matomo site"
                    },
                    "period": {
                        "type": "string",
                        "description": "Time period: day, week, month, year, or range",
                        "enum": ["day", "week", "month", "year", "range"],
                        "default": "day"
                    },
                    "date": {
                        "type": "string",
                        "description": "Date or date range",
                        "default": "today"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of results to return",
                        "default": 10
                    }
                },
                "required": ["site_id"]
            }
        ),
        Tool(
            name="get_user_settings",
            description="Get visitor device type information (desktop, mobile, tablet) with usage statistics",
            inputSchema={
                "type": "object",
                "properties": {
                    "site_id": {
                        "type": "integer",
                        "description": "The ID of the Matomo site"
                    },
                    "period": {
                        "type": "string",
                        "description": "Time period: day, week, month, year, or range",
                        "enum": ["day", "week", "month", "year", "range"],
                        "default": "day"
                    },
                    "date": {
                        "type": "string",
                        "description": "Date or date range",
                        "default": "today"
                    }
                },
                "required": ["site_id"]
            }
        ),
        Tool(
            name="get_browsers",
            description="Get visitor browser statistics including browser name, version, and usage metrics",
            inputSchema={
                "type": "object",
                "properties": {
                    "site_id": {
                        "type": "integer",
                        "description": "The ID of the Matomo site"
                    },
                    "period": {
                        "type": "string",
                        "description": "Time period: day, week, month, year, or range",
                        "enum": ["day", "week", "month", "year", "range"],
                        "default": "day"
                    },
                    "date": {
                        "type": "string",
                        "description": "Date or date range",
                        "default": "today"
                    }
                },
                "required": ["site_id"]
            }
        ),
        Tool(
            name="get_referrers",
            description="Get referrer information showing where visitors came from (search engines, websites, social media, etc.)",
            inputSchema={
                "type": "object",
                "properties": {
                    "site_id": {
                        "type": "integer",
                        "description": "The ID of the Matomo site"
                    },
                    "period": {
                        "type": "string",
                        "description": "Time period: day, week, month, year, or range",
                        "enum": ["day", "week", "month", "year", "range"],
                        "default": "day"
                    },
                    "date": {
                        "type": "string",
                        "description": "Date or date range",
                        "default": "today"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of results to return",
                        "default": 10
                    }
                },
                "required": ["site_id"]
            }
        ),
        Tool(
            name="query_custom_report",
            description="Execute a custom Matomo API query for advanced reporting needs. Use this for any API method not covered by other tools.",
            inputSchema={
                "type": "object",
                "properties": {
                    "method": {
                        "type": "string",
                        "description": "Matomo API method name (e.g., 'Actions.getPageTitles', 'Goals.get')"
                    },
                    "site_id": {
                        "type": "integer",
                        "description": "The ID of the Matomo site"
                    },
                    "period": {
                        "type": "string",
                        "description": "Time period: day, week, month, year, or range",
                        "enum": ["day", "week", "month", "year", "range"],
                        "default": "day"
                    },
                    "date": {
                        "type": "string",
                        "description": "Date or date range",
                        "default": "today"
                    },
                    "additional_params": {
                        "type": "string",
                        "description": "Additional parameters as JSON string (e.g., '{\"segment\": \"browserName==Chrome\"}')"
                    }
                },
                "required": ["method", "site_id"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Handle tool calls for Matomo reporting."""
    try:
        client = get_client()

        if name == "get_site_info":
            site_id = arguments["site_id"]
            result = await client.get_site_info(site_id)
            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]

        elif name == "get_visits_summary":
            site_id = arguments["site_id"]
            period = arguments.get("period", "day")
            date = arguments.get("date", "today")
            result = await client.get_visits_summary(site_id, period, date)
            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]

        elif name == "get_page_urls":
            site_id = arguments["site_id"]
            period = arguments.get("period", "day")
            date = arguments.get("date", "today")
            limit = arguments.get("limit", 10)
            result = await client.get_page_urls(site_id, period, date, limit)
            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]

        elif name == "get_countries":
            site_id = arguments["site_id"]
            period = arguments.get("period", "day")
            date = arguments.get("date", "today")
            limit = arguments.get("limit", 10)
            result = await client.get_countries(site_id, period, date, limit)
            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]

        elif name == "get_user_settings":
            site_id = arguments["site_id"]
            period = arguments.get("period", "day")
            date = arguments.get("date", "today")
            result = await client.get_user_settings(site_id, period, date)
            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]

        elif name == "get_browsers":
            site_id = arguments["site_id"]
            period = arguments.get("period", "day")
            date = arguments.get("date", "today")
            result = await client.get_browsers(site_id, period, date)
            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]

        elif name == "get_referrers":
            site_id = arguments["site_id"]
            period = arguments.get("period", "day")
            date = arguments.get("date", "today")
            limit = arguments.get("limit", 10)
            result = await client.get_referrers(site_id, period, date, limit)
            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]

        elif name == "query_custom_report":
            method = arguments["method"]
            site_id = arguments["site_id"]
            period = arguments.get("period", "day")
            date = arguments.get("date", "today")

            params = {
                "idSite": site_id,
                "period": period,
                "date": date
            }

            if "additional_params" in arguments:
                additional = json.loads(arguments["additional_params"])
                params.update(additional)

            result = await client.call_api(method, params)
            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]

        else:
            raise ValueError(f"Unknown tool: {name}")

    except Exception as e:
        logger.error(f"Error executing tool {name}: {str(e)}")
        return [TextContent(
            type="text",
            text=f"Error: {str(e)}"
        )]


async def main():
    """Run the Matomo MCP server."""
    from mcp.server.stdio import stdio_server

    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
