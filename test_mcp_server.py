#!/usr/bin/env python3
"""
Test script to verify MCP server functionality without requiring a live Matomo instance.
"""

import asyncio
import os
from matomo_mcp.server import app, list_tools, call_tool


async def test_server_initialization():
    """Test that the server initializes correctly."""
    print("Testing MCP server initialization...")
    assert app.name == "matomo-mcp-server"
    print("✓ Server name correct")


async def test_list_tools():
    """Test that all tools are properly defined."""
    print("\nTesting tool definitions...")
    tools = await list_tools()

    expected_tools = [
        "get_site_info",
        "get_visits_summary",
        "get_page_urls",
        "get_countries",
        "get_user_settings",
        "get_browsers",
        "get_referrers",
        "query_custom_report"
    ]

    tool_names = [tool.name for tool in tools]

    print(f"Found {len(tools)} tools:")
    for tool in tools:
        print(f"  - {tool.name}: {tool.description[:60]}...")

    for expected in expected_tools:
        assert expected in tool_names, f"Missing tool: {expected}"

    print(f"✓ All {len(expected_tools)} expected tools found")
    return tools


def validate_tool_schema(tool):
    """Validate that a tool has proper schema."""
    assert tool.name, "Tool must have a name"
    assert tool.description, "Tool must have a description"
    assert tool.inputSchema, "Tool must have input schema"
    assert tool.inputSchema.get("type") == "object", "Input schema must be object type"
    assert "properties" in tool.inputSchema, "Schema must have properties"
    assert "required" in tool.inputSchema, "Schema must specify required fields"


async def test_tool_schemas():
    """Test that all tool schemas are valid."""
    print("\nTesting tool schemas...")
    tools = await list_tools()

    for tool in tools:
        try:
            validate_tool_schema(tool)

            # Verify site_id is in all tools
            assert "site_id" in tool.inputSchema["properties"], \
                f"{tool.name} should have site_id parameter"

            # Verify site_id is required in all tools
            assert "site_id" in tool.inputSchema["required"], \
                f"{tool.name} should require site_id"

            print(f"✓ {tool.name}: Schema valid")
        except AssertionError as e:
            print(f"✗ {tool.name}: {e}")
            raise


async def test_tool_call_without_credentials():
    """Test that tools fail gracefully without credentials."""
    print("\nTesting tool calls without credentials...")

    # Clear environment variables if set
    old_url = os.environ.pop("MATOMO_URL", None)
    old_token = os.environ.pop("MATOMO_TOKEN", None)

    # Force reset of global client
    import matomo_mcp.server as server_module
    server_module.matomo_client = None

    try:
        result = await call_tool("get_site_info", {"site_id": 1})

        # Should return error message
        assert len(result) == 1
        assert result[0].type == "text"
        assert "Error:" in result[0].text
        print(f"✓ Gracefully handles missing credentials")
        print(f"  Error message: {result[0].text[:80]}...")
    finally:
        # Restore environment variables
        if old_url:
            os.environ["MATOMO_URL"] = old_url
        if old_token:
            os.environ["MATOMO_TOKEN"] = old_token


async def test_client_functionality():
    """Test the Matomo client with mock data."""
    print("\nTesting Matomo client...")
    from matomo_mcp.client import MatomoClient

    client = MatomoClient("https://demo.matomo.org", "test_token")

    assert client.base_url == "https://demo.matomo.org"
    assert client.token_auth == "test_token"
    assert client.api_url == "https://demo.matomo.org/index.php"
    print("✓ Client initialization correct")

    # Test URL normalization
    client2 = MatomoClient("https://demo.matomo.org/", "test_token")
    assert client2.base_url == "https://demo.matomo.org"
    assert client2.api_url == "https://demo.matomo.org/index.php"
    print("✓ URL normalization works")


async def test_tool_parameters():
    """Test that tool parameters are correctly defined."""
    print("\nTesting tool parameters...")
    tools = await list_tools()

    # Test get_visits_summary parameters
    visits_tool = next(t for t in tools if t.name == "get_visits_summary")
    props = visits_tool.inputSchema["properties"]

    assert "period" in props
    assert props["period"].get("enum") == ["day", "week", "month", "year", "range"]
    assert props["period"].get("default") == "day"
    print("✓ Period parameter correctly defined")

    assert "date" in props
    assert props["date"].get("default") == "today"
    print("✓ Date parameter correctly defined")

    # Test get_page_urls limit parameter
    pages_tool = next(t for t in tools if t.name == "get_page_urls")
    props = pages_tool.inputSchema["properties"]

    assert "limit" in props
    assert props["limit"]["type"] == "integer"
    assert props["limit"]["default"] == 10
    print("✓ Limit parameter correctly defined")

    # Test query_custom_report
    custom_tool = next(t for t in tools if t.name == "query_custom_report")
    props = custom_tool.inputSchema["properties"]

    assert "method" in props
    assert "additional_params" in props
    assert "method" in custom_tool.inputSchema["required"]
    print("✓ Custom query tool correctly defined")


async def run_all_tests():
    """Run all tests."""
    print("=" * 70)
    print("MATOMO MCP SERVER TEST SUITE")
    print("=" * 70)

    try:
        await test_server_initialization()
        await test_list_tools()
        await test_tool_schemas()
        await test_tool_parameters()
        await test_client_functionality()
        await test_tool_call_without_credentials()

        print("\n" + "=" * 70)
        print("ALL TESTS PASSED ✓")
        print("=" * 70)
        return True

    except Exception as e:
        print("\n" + "=" * 70)
        print(f"TEST FAILED ✗")
        print(f"Error: {e}")
        print("=" * 70)
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = asyncio.run(run_all_tests())
    exit(0 if success else 1)
