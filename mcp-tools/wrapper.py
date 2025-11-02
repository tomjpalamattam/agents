from mcp.server.fastmcp import FastMCP
import subprocess

# Create the MCP server
mcp = FastMCP("JobTools")

@mcp.tool()
def generate_resume() -> str:
    """Run the local resume.py script and return its output."""
    try:
        result = subprocess.run(
            ["python",
             "code.py"],
            text=True,
            capture_output=True,
            check=False
        )
        output = result.stdout.strip()
        if result.stderr:
            output += f"\n\nSTDERR:\n{result.stderr.strip()}"
        return output or "resume.py executed successfully."
    except Exception as e:
        return f"Error running resume.py: {e}"

@mcp.tool()
def generate_cover_letter() -> str:
    """Run the local cover-letter.py script and return its output."""
    try:
        result = subprocess.run(
            ["python",
             "cover-letter.py"],
            text=True,
            capture_output=True,
            check=False
        )
        output = result.stdout.strip()
        if result.stderr:
            output += f"\n\n⚠️ STDERR:\n{result.stderr.strip()}"
        return output or "✅ cover-letter.py executed successfully."
    except Exception as e:
        return f"Error running cover-letter.py: {e}"

if __name__ == "__main__":
    # Launch FastMCP over stdio (for MultiServerMCPClient compatibility)
    mcp.run(transport="stdio")