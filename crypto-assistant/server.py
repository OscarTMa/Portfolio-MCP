import requests
from mcp.server.fastmcp import FastMCP

# Initialize the MCP server
mcp = FastMCP("Crypto Price Assistant")

@mcp.tool()
def get_crypto_price(cryptocurrency: str, currency: str = "usd") -> str:
    """
    Fetches the current price of a cryptocurrency from the CoinGecko API.
    
    Args:
        cryptocurrency: The name or id of the crypto (e.g., 'bitcoin', 'ethereum', 'solana').
        currency: The target currency for the price (default: 'usd', can be 'eur', 'mxn').
    """
    # API Endpoint configuration
    base_url = "https://api.coingecko.com/api/v3/simple/price"
    
    # Prepare query parameters
    params = {
        "ids": cryptocurrency.lower(),
        "vs_currencies": currency.lower()
    }
    
    try:
        # Make the external API request with a timeout
        response = requests.get(base_url, params=params, timeout=10)
        data = response.json()
        
        # Check if the cryptocurrency was found in the response
        if cryptocurrency.lower() not in data:
            return f"Error: Cryptocurrency '{cryptocurrency}' not found. Please try with the full name (e.g., 'bitcoin' instead of 'btc')."
        
        # Extract the price
        price = data[cryptocurrency.lower()][currency.lower()]
        
        return f"The current price of {cryptocurrency} is {price} {currency.upper()}."

    except requests.exceptions.RequestException as error:
        return f"API Connection Error: {str(error)}"

if __name__ == "__main__":
    mcp.run()