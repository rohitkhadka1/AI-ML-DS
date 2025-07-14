from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
path = r"E:\AI-ML-DS\MCP_Server.py"
async def run():
  # Commands to create server parameters for stdio connection
  server_params = StdioServerParameters(
    command="python",
    args=[path],   # path to the mcp server file
    env=None,  # Optional environment variables
  )
  print("Starting client...")

  
  async with stdio_client(server_params) as (read, write):
    print(1)
    async with ClientSession(read, write) as session:
      # Initialize the connection
      print(3)
      await session.initialize()
      print(2)
      # List available tools
      tools = await session.list_tools()
      print(tools)

      # List available resources
      resources = await session.list_resources()
      print(resources)

      # List available prompts
      prompts = await session.list_prompts()
      print(prompts)

      # Call a tool
      result = await session.call_tool("get_stock_price", arguments={"ticker": "TSLA"})
      print(result)

      # Read a resource
      content, mime_type = await session.read_resource("greeting://tinztwins")
      print(mime_type)
      print(content)

      # Get a prompt
      prompt = await session.get_prompt(
          "echo_prompt", arguments={"message": "What are bollinger bands?"}
      )
      print(prompt)

if __name__ == "__main__":
  asyncio.run(run())