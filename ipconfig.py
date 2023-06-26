import subprocess
import re

result = subprocess.check_output(['ipconfig'])
data = result.decode('cp950', errors='ignore').split('\n')

adapter_regex = r'^([^:]+)'
ip_regex = r'IPv4 Address.*: ([\d.]+)'

adapters = []

print("="*40, "Network Configuration", "="*40)

for line in data:
    adapter_match = re.match(adapter_regex, line.strip())
    if adapter_match:
        adapter_name = adapter_match.group(1).strip()
        adapters.append(adapter_name)

    ip_match = re.search(ip_regex, line)
    if ip_match:
        ip_address = ip_match.group(1)
        if adapters:
            print( adapters[-4])
            print("IP Address:", ip_address)
            print()

