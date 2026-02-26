import os
import hashlib
import time

def calculate_file_hash(filepath):
    """Generates a SHA-256 hash for a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception:
        return None

def create_baseline(directory):
    print(f"[*] Creating baseline for: {directory}")
    with open("baseline.txt", "w") as f:
        for root, dirs, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                file_hash = calculate_file_hash(filepath)
                if file_hash:
                    f.write(f"{filepath}|{file_hash}\n")
    print("[+] Baseline created successfully.")

def monitor_directory(directory):
    print(f"[*] Monitoring started on: {directory} (Press Ctrl+C to stop)")
    baseline = {}
    with open("baseline.txt", "r") as f:
        for line in f:
            path, file_hash = line.strip().split("|")
            baseline[path] = file_hash

    while True:
        time.sleep(1) 
        for root, dirs, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                current_hash = calculate_file_hash(filepath)

                if filepath not in baseline:
                    print(f"[!] ALERT: New file created: {filepath}")
                    baseline[filepath] = current_hash
                
                elif baseline[filepath] != current_hash:
                    print(f"[!] ALERT: File modified: {filepath}")
                    baseline[filepath] = current_hash

if __name__ == "__main__":
    folder = input("Enter directory to monitor: ")
    choice = input("Choose (B)aseline or (M)onitor: ").upper()
    
    if choice == 'B':
        create_baseline(folder)
    elif choice == 'M':
        monitor_directory(folder)
