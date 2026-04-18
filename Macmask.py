import subprocess
import sys

def mask(interface):
    try:
        subprocess.run(["sudo", "ip", "link", "set", interface, "down"], check=True)
        subprocess.run(["sudo", "macchanger", "-r", interface], check=True)
        subprocess.run(["sudo", "ip", "link", "set", interface, "up"], check=True)

        print(f"MAC Address changed for {interface}. You are now a ghost! 👻")
    except subprocess.CalledProcessError as e:
        print(f"Error during execution: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target_interface = sys.argv[1]
    else:
        target_interface = "wlan0"
        
    mask(target_interface)
