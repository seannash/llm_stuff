from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Simple MCP Server")

@mcp.tool()
def MeaningOfLife() -> int:
    """Returns the meaning of life, the universe, and everything."""
    return 42

if __name__ == "__main__":
    # Run with HTTP transport using Server-Sent Events (SSE)
    mcp.run(transport="sse")