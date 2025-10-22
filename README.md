# Zota

*Created with love by willicc & Qwen*

# Auto Submit Script

This Python script automatically submits random Twitter/X usernames paired with wallet addresses to the website `https://zotachain.fun/`. The number of submissions made will correspond to the number of wallet addresses listed in the `address.txt` file.

## Prerequisites

Before running this script, ensure you have Python version 3.x or higher installed on your computer.

## Installation

1.  **Clone this repository (if applicable):**
    If you store this script in a GitHub repository, clone it first.
    ```bash
    git clone https://github.com/willicc/zota.git
    cd zota
    ```

2.  **(Optional) Create a Virtual Environment (Recommended):**
    It's recommended to create a virtual environment to isolate project dependencies.
    ```bash
    # Create a virtual environment (e.g., named 'venv')
    python3 -m venv venv

    # Activate the virtual environment
    # On Linux/macOS:
    source venv/bin/activate
    # On Windows:
    # venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    The script uses the `requests` module, which might not be installed by default. Install it using pip.
    ```bash
    pip install requests
    ```

## Preparing Data

1.  Create a text file named `address.txt`.
2.  Add your wallet addresses to this file, placing one address on each line.
    Example content of `address.txt`:
    ```
    7RyP3P2Ji4ExampleAddress1
    9ffmHMt1PeExampleAddress2
    AnotherWalletAddress3...
    ```
3.  Save the `address.txt` file in the *same* directory as your Python script (`bot.py` or whatever name you gave it).

## How to Run the Script

After completing the prerequisites and data preparation, you can run the script using the following command in your terminal or command prompt:

```bash
python3 main.py
