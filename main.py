import requests
import random
import string
import time

def generate_random_username():
    """Generate a random Twitter-like username."""
    username = ''.join(random.choices(string.ascii_lowercase, k=random.randint(6, 8)))
    username += str(random.randint(10, 999))
    return username

def read_addresses_from_file(filename):
    """Read wallet addresses from a text file."""
    try:
        with open(filename, 'r') as f:
            addresses = [line.strip() for line in f if line.strip()]
        return addresses
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return []

def submit_form(username, wallet_address, session):
    """Submit the form with given username and wallet address."""
    # Perbaiki URL (hapus spasi ekstra)
    url = "https://zotachain.fun/wp-admin/admin-ajax.php"
    
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'id,en-US;q=0.9,en;q=0.8,it;q=0.7',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryl2a3WiuwON6J1hXd',
        # Perbaiki origin (hapus spasi ekstra)
        'origin': 'https://zotachain.fun',
        # Perbaiki referer (hapus spasi ekstra)
        'referer': 'https://zotachain.fun/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    boundary = "----WebKitFormBoundaryl2a3WiuwON6J1hXd"
    payload = (
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"post_id\"\r\n\r\n"
        f"12\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"form_id\"\r\n\r\n"
        f"e1886e6\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"referer_title\"\r\n\r\n"
        f"\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"queried_id\"\r\n\r\n"
        f"12\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"form_fields[field_969b7aa]\"\r\n\r\n"
        f"@{username}\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"form_fields[field_e8b59ad]\"\r\n\r\n"
        f"{wallet_address}\r\n"
        f"--{boundary}\r\n"
        f"Content-Disposition: form-data; name=\"action\"\r\n\r\n"
        f"elementor_pro_forms_send_form\r\n"
        f"--{boundary}\r\n"
        # Perbaiki referrer (hapus spasi ekstra)
        f"Content-Disposition: form-data; name=\"referrer\"\r\n\r\n"
        f"https://zotachain.fun/\r\n"
        f"--{boundary}--\r\n"
    ).encode('utf-8')

    headers['content-length'] = str(len(payload))

    try:
        response = session.post(url, headers=headers, data=payload)
        response.raise_for_status()

        try:
            json_response = response.json()
            if json_response.get('success'):
                print(f"Success: Submitted for @{username} with address {wallet_address[:10]}... -> {json_response.get('data', {}).get('message', 'Submission successful.')}")
                return True
            else:
                print(f"Failed: Submission for @{username} with address {wallet_address[:10]}... -> {json_response.get('data', {}).get('message', 'Unknown error')}")
                return False
        except ValueError:
            print(f"Warning: Non-JSON response for @{username} with address {wallet_address[:10]}... -> {response.text[:200]}...")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Error submitting for @{username} with address {wallet_address[:10]}... -> {e}")
        return False

def main():
    """Main function to run the script."""
    addresses_file = "address.txt"
    addresses = read_addresses_from_file(addresses_file)

    if not addresses:
        print(f"No wallet addresses found in '{addresses_file}'. Exiting.")
        return

    num_addresses = len(addresses)
    print(f"Loaded {num_addresses} wallet addresses from '{addresses_file}'.")
    print(f"Will attempt to make {num_addresses} submissions (one per address)...")

    session = requests.Session()

    successful_submissions = 0
    total_attempts = 0

    # Iterasi sebanyak jumlah alamat yang ada
    for i in range(num_addresses):
        username = generate_random_username()
        wallet_address = addresses[i] # Gunakan alamat ke-i secara langsung

        print(f"Attempt {i+1}: Submitting for @{username} with {wallet_address[:10]}...")

        if submit_form(username, wallet_address, session):
            successful_submissions += 1

        total_attempts += 1

        # Tambahkan delay antar permintaan
        time.sleep(random.uniform(1, 3))

    print(f"\nScript finished.")
    print(f"Total attempts: {total_attempts}")
    print(f"Successful submissions: {successful_submissions}")
    print(f"Failed submissions: {total_attempts - successful_submissions}")

if __name__ == "__main__":
    main()
