import subprocess

def ping_google_dns():
    try:
        result = subprocess.run(['ping', '-n', '4', 'www.google.com.tw'], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

print("="*40, "Network Ping Test", "="*40)

ping_result = ping_google_dns()
print(ping_result)
