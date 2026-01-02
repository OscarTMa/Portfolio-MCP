# MCP Server Portfolio 🔌

A collection of Model Context Protocol (MCP) servers connecting LLMs like Claude to local systems, databases, and external APIs.

## 🚀 Projects Included

### 1. Crypto Price Assistant 🪙
Real-time cryptocurrency tracker.
- **Functionality:** Fetches live prices for Bitcoin, Ethereum, and more using the CoinGecko API.
- **Tech Stack:** Python, Requests, REST API integration.

### 2. SQLite Data Explorer 📊
Natural Language Interface for Database (Text-to-SQL).
- **Functionality:** Allows the AI to query a business database using read-only SQL commands.
- **Tech Stack:** Python, SQLite3.

### 3. System Monitor 🖥️
Local hardware monitoring bridge.
- **Functionality:** Provides real-time CPU, RAM usage, and system time to the LLM.
- **Tech Stack:** Python, psutil.

## 🛠️ Installation

1. Clone the repository.
2. Create a virtual environment inside each project folder.
3. Install dependencies:
   ```bash
   pip install mcp psutil requests
   ```                                                   
   
4. Configure your claude_desktop_config.json following the example in claude_config_example.json.  
