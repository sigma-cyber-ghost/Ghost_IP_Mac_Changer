#!/usr/bin/env python3
import os
import re
import random
import subprocess
import time
import sys

# Terminal colors
RED = "\033[91m"
CYAN = "\033[96m"
WHITE = "\033[97m"
YELLOW = "\033[93m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Final Banner (animated)
ANIMATED_BANNER = [
    f"{CYAN}⠉⠉⠉⠉⠉⠉⠓⠒⠒⠒⠒⠶⠤⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{RESET}",
    f"{CYAN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠻⢤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{RESET}",
    f"{CYAN}⠀⠠⠤⠒⠶⠶⠤⠖⠚⠉⠉⠉⠉⢉⣉⣉⣉⣙⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{RESET}",
    f"{CYAN}⠀⠀⠀⠀⠀⠀⢀⣀⡄⠤⠒⠒⠉⠛⠁⠀⠀⠀⠳⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{RESET}",
    f"{CYAN}⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠛⠛⠉⠛⠛⠶⢦⣤⡐⢀⠀⠀⠀⠀⠀{RESET}",
    f"{CYAN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⢳⣦⠀⠀⠀⠀{RESET}",
    f"{CYAN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⡤⠀⠀{RESET}",
    f"{CYAN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{RESET}",
    f"{CYAN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀{RESET}",
    f"{CYAN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠳⠶⢶⣦⢤⣄⡀⠀⠀⠀{RESET}",
    f"{CYAN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠉⠳⣄⠀{RESET}",
    f"{CYAN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡀⠀⢇{RESET}",
    f"{CYAN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⠀{RESET}",
    f"{CYAN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀{RESET}",
    f"{CYAN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇{RESET}",
    f"{RED}{BOLD}     SIGMA GHOST — BLACK HAT - LOCAL NETWORK CHANGER                {RESET}\n"
]

# Social branding
SOCIAL = f"""{WHITE}
░▒▓█ SIGMA GHOST █▓▒░
🐦 Twitter:   https://twitter.com/safderkhan0800_
📸 Instagram: https://www.instagram.com/safderkhan0800_/
📺 YouTube:   https://www.youtube.com/@sigma_ghost_hacking
🛡️ Telegram:  https://t.me/Sigma_Cyber_Ghost
{RESET}
"""

def type_out(text, delay=0.002):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_banner():
    os.system("clear")
    for line in ANIMATED_BANNER:
        print(line)
        time.sleep(0.04)

def get_interfaces():
    result = subprocess.check_output("ip link", shell=True).decode()
    return [line.split(":")[1].strip() for line in result.splitlines() if ": " in line and "lo" not in line]

def random_mac():
    return "02:%02x:%02x:%02x:%02x:%02x" % tuple(random.randint(0, 0x7f) for _ in range(5))

def random_ip():
    return f"192.168.{random.randint(0, 254)}.{random.randint(2, 254)}"

def backup_original(interface):
    try:
        mac = subprocess.check_output(f"cat /sys/class/net/{interface}/address", shell=True).decode().strip()
        ip = subprocess.check_output(f"ip addr show {interface} | grep 'inet ' | awk '{{print $2}}'", shell=True).decode().strip()
        with open("/etc/sigma_backup.conf", "w") as f:
            f.write(f"{interface}\n{mac}\n{ip}\n")
        print(f"{YELLOW}[~] Original MAC and IP backed up to /etc/sigma_backup.conf{RESET}")
    except Exception as e:
        print(f"{RED}[!] Backup failed: {e}{RESET}")

def change_mac(interface, mac):
    subprocess.run(["ip", "link", "set", interface, "down"])
    subprocess.run(["ip", "link", "set", interface, "address", mac])
    subprocess.run(["ip", "link", "set", interface, "up"])
    type_out(f"{CYAN}[+] MAC Address changed to: {mac}{RESET}")

def change_ip(interface, ip):
    subprocess.run(["ip", "addr", "flush", "dev", interface])
    subprocess.run(["ip", "addr", "add", f"{ip}/24", "dev", interface])
    subprocess.run(["ip", "link", "set", interface, "up"])
    type_out(f"{RED}[+] IP Address changed to: {ip}{RESET}")

def menu():
    animate_banner()
    interfaces = get_interfaces()
    if not interfaces:
        print(f"{RED}[-] No interfaces found. Exiting...{RESET}")
        return
    print(f"{YELLOW}[+] Detected Interfaces:{RESET}")
    for i, iface in enumerate(interfaces):
        print(f"  [{i}] {WHITE}{iface}{RESET}")
    try:
        index = int(input(f"\n{CYAN}Select your interface number: {RESET}"))
        iface = interfaces[index]
    except:
        print(f"{RED}[-] Invalid selection.{RESET}")
        return

    while True:
        print(f"""\n{WHITE}{BOLD}What would you like to do?{RESET}
{CYAN}[1]{RESET} Change IP Address
{CYAN}[2]{RESET} Change MAC Address
{CYAN}[3]{RESET} Change BOTH IP & MAC
{CYAN}[4]{RESET} Exit""")
        choice = input(">> ").strip()

        if choice == "1":
            backup_original(iface)
            ip = random_ip()
            change_ip(iface, ip)
        elif choice == "2":
            backup_original(iface)
            mac = random_mac()
            change_mac(iface, mac)
        elif choice == "3":
            backup_original(iface)
            ip = random_ip()
            mac = random_mac()
            change_mac(iface, mac)
            change_ip(iface, ip)
        elif choice == "4":
            type_out(f"{YELLOW}[~] Disappearing into the void...{RESET}")
            break
        else:
            print(f"{RED}[-] Invalid option. Try again.{RESET}")

    type_out(SOCIAL, delay=0.001)

if __name__ == "__main__":
    if os.geteuid() != 0:
        print(f"{RED}[-] Run this tool as root (sudo).{RESET}")
        exit(1)
    menu()
