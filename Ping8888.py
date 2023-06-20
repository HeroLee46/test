import subprocess

def ping_google_dns():
    try:
        result = subprocess.run(['ping', '-n', '4', '8.8.8.8'], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

print("="*40, "Network function check", "="*40)

ping_result = ping_google_dns()
print(ping_result)
