import subprocess
import sys

def unmask(interface):
    try:
        print(f"Restoring original MAC address for {interface}...")
        
        subprocess.run(["sudo", "ip", "link", "set", interface, "down"], check=True)
        
        subprocess.run(["sudo", "macchanger", "-p", interface], check=True)
        
        subprocess.run(["sudo", "ip", "link", "set", interface, "up"], check=True)

        print(f"Identity restored. You are no longer a ghost on {interface}. 🏠")
    except subprocess.CalledProcessError as e:
        print(f"Error during execution: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_interface = sys.argv[1]
    else:
        target_interface = "wlan0"
        
    unmask(target_interface)
