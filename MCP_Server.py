from mcp.server.fastmcp import FastMCP
from openbb import obb

mcp = FastMCP("Basic MCP Server")

# Add a resource, e.g. a greeting of a user 

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    return f"Hello {name}"

@mcp.tool()
def get_stock_price(ticker: str) -> str:

    quote_data = obb.equity.price.quote(symbol = ticker, provider = "yfinance")
    return f"Stock price {ticker} : {quote_data.results[0].last_price}"

@mcp.prompt()
def echo_prompt(message:str) -> str:
    return f"You are a helpful AI assistant. \
          You can help with general queries \
          and questions about the stock market. \
          Answer the following question: {message}"

if __name__ ==  "__main__":
    mcp.run(transport = "stdio")
