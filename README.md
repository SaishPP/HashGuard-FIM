HashGuard: File Integrity Monitor (FIM)

Project Overview
HashGuard is a host-based intrusion detection tool (HIDS) concept. It monitors critical system directories for unauthorized changes using SHA-256 cryptographic hashing. This mirrors functionality found in enterprise tools like Wazuh and Tripwire.

How it Works
1. **Baselines:** The tool scans a directory and records the unique "fingerprint" (hash) of every file.
2. **Monitoring:** It continuously re-calculates hashes in real-time.
3. **Alerting:** If a hash changes (modification) or a new file appears (malware drop), an alert is triggered immediately.

Skills Demonstrated
- **Data Integrity:** Implementation of the "I" in the CIA Triad.
- **Cryptography:** Utilizing the SHA-256 algorithm for verification.
- **Defensive Programming:** Handling file system permissions and recursive directory walking.

How to Use
1. Run `python hashguard.py`.
2. Enter the path of a folder you want to protect.
3. Type `B` to create a baseline.
4. Run it again and type `M` to start monitoring. 
5. Try editing a file in that folder to see the alert!
