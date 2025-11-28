#!/usr/bin/env python3
"""
Test MCP protocol communication with the server.
This simulates how Claude Desktop would communicate with the server.
"""

import asyncio
import json
import sys
from io import StringIO


async def test_mcp_protocol():
    """Test MCP protocol initialization and tool listing."""
    print("=" * 70)
    print("TESTING MCP PROTOCOL COMMUNICATION")
    print("=" * 70)

    # Import the server components
    from mcp.server import Server
    from mcp.types import InitializeRequest, ListToolsRequest
    from matomo_mcp.server import app, list_tools

    print("\n1. Testing server instance...")
    assert isinstance(app, Server)
    assert app.name == "matomo-mcp-server"
    print("   ✓ Server instance is valid")

    print("\n2. Testing tool listing...")
    tools = await list_tools()
    print(f"   ✓ Server provides {len(tools)} tools")

    tool_summary = {}
    for tool in tools:
        tool_summary[tool.name] = {
            "description": tool.description[:50] + "...",
            "required_params": tool.inputSchema.get("required", []),
            "optional_params": [
                k for k in tool.inputSchema.get("properties", {}).keys()
                if k not in tool.inputSchema.get("required", [])
            ]
        }

    print("\n3. Tool Summary:")
    for name, info in tool_summary.items():
        print(f"\n   {name}:")
        print(f"      Description: {info['description']}")
        print(f"      Required: {', '.join(info['required_params'])}")
        if info['optional_params']:
            print(f"      Optional: {', '.join(info['optional_params'])}")

    print("\n4. Testing tool schemas...")
    schema_tests = {
        "get_site_info": {
            "required": ["site_id"],
            "optional": []
        },
        "get_visits_summary": {
            "required": ["site_id"],
            "optional": ["period", "date"]
        },
        "get_page_urls": {
            "required": ["site_id"],
            "optional": ["period", "date", "limit"]
        },
        "query_custom_report": {
            "required": ["method", "site_id"],
            "optional": ["period", "date", "additional_params"]
        }
    }

    for tool_name, expected in schema_tests.items():
        tool = next((t for t in tools if t.name == tool_name), None)
        assert tool is not None, f"Tool {tool_name} not found"

        actual_required = set(tool.inputSchema.get("required", []))
        expected_required = set(expected["required"])
        assert actual_required == expected_required, \
            f"{tool_name}: Expected required {expected_required}, got {actual_required}"

        all_params = set(tool.inputSchema.get("properties", {}).keys())
        actual_optional = all_params - actual_required
        expected_optional = set(expected["optional"])
        assert actual_optional == expected_optional, \
            f"{tool_name}: Expected optional {expected_optional}, got {actual_optional}"

        print(f"   ✓ {tool_name} schema correct")

    print("\n5. Testing parameter types and constraints...")

    visits_tool = next(t for t in tools if t.name == "get_visits_summary")
    period_schema = visits_tool.inputSchema["properties"]["period"]
    assert period_schema["type"] == "string"
    assert set(period_schema["enum"]) == {"day", "week", "month", "year", "range"}
    assert period_schema["default"] == "day"
    print("   ✓ Period enum values correct")

    pages_tool = next(t for t in tools if t.name == "get_page_urls")
    limit_schema = pages_tool.inputSchema["properties"]["limit"]
    assert limit_schema["type"] == "integer"
    assert limit_schema["default"] == 10
    print("   ✓ Limit parameter correct")

    print("\n6. Testing all tools have consistent parameters...")
    reporting_tools = [
        "get_visits_summary", "get_page_urls", "get_countries",
        "get_user_settings", "get_browsers", "get_referrers",
        "query_custom_report"
    ]

    for tool_name in reporting_tools:
        tool = next(t for t in tools if t.name == tool_name)
        props = tool.inputSchema["properties"]

        # All should have site_id
        assert "site_id" in props
        assert props["site_id"]["type"] == "integer"

        # Most should have period and date
        if tool_name != "get_site_info":
            assert "period" in props or tool_name == "query_custom_report"
            assert "date" in props or tool_name == "query_custom_report"

    print("   ✓ All tools have consistent parameter patterns")

    print("\n7. Testing error handling without credentials...")
    from matomo_mcp.server import call_tool
    import os

    # Ensure no credentials are set
    old_url = os.environ.pop("MATOMO_URL", None)
    old_token = os.environ.pop("MATOMO_TOKEN", None)

    # Reset client
    import matomo_mcp.server as server_module
    server_module.matomo_client = None

    result = await call_tool("get_site_info", {"site_id": 1})
    assert len(result) == 1
    assert "Error:" in result[0].text
    assert "MATOMO_URL" in result[0].text or "MATOMO_TOKEN" in result[0].text
    print("   ✓ Error handling works correctly")

    # Restore env vars
    if old_url:
        os.environ["MATOMO_URL"] = old_url
    if old_token:
        os.environ["MATOMO_TOKEN"] = old_token

    print("\n" + "=" * 70)
    print("MCP PROTOCOL TESTS PASSED ✓")
    print("=" * 70)
    print("\nThe MCP server is ready for use with Claude Desktop!")
    print("\nNext steps:")
    print("1. Set MATOMO_URL and MATOMO_TOKEN in your environment")
    print("2. Add the server to Claude Desktop config")
    print("3. Restart Claude Desktop")
    print("4. Ask Claude to query your Matomo data")

    return True


if __name__ == "__main__":
    try:
        asyncio.run(test_mcp_protocol())
        sys.exit(0)
    except Exception as e:
        print(f"\n✗ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
