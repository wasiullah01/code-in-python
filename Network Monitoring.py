class SecurityDevice:
    def __init__(self, device_name, status, threat_level):
        self.device = device_name
        self.status = status
        self.threat = threat_level
        self.logs = []  

    def activate(self):
        print(f"{self.device} is activated")
        
    def deactivate(self):
        print(f"{self.device} is deactivated")

    def log_event(self, message):
        self.logs.append(message)  
        print(f"[{self.device}] Event logged: {message}")


class Firewall(SecurityDevice):
    def __init__(self, device_name, status, threat_level):
        super().__init__(device_name, status, threat_level)
        self.blocked_ips = ["192.1.1.1", "192.2.2.2", "192.3.3.3"]
        self.allowed_ips = ["127.0.0.0", "127.1.1.1", "127.2.2.2"]

    def block_ip(self, ip):
        if ip not in self.blocked_ips:
            self.blocked_ips.append(ip)
        print(f"IP {ip} has been blocked")
        self.log_event(f"Blocked IP: {ip}")

    def allow_ip(self, ip):
        if ip in self.blocked_ips:
            self.blocked_ips.remove(ip)
        print(f"IP {ip} has been allowed")
        self.log_event(f"Allowed IP: {ip}")

    def check_ip(self, ip):
        if ip in self.blocked_ips:
            print(f"IP {ip} is BLOCKED")
        elif ip in self.allowed_ips:
            print(f"IP {ip} is ALLOWED")
        else:
            print(f"IP {ip} is UNKNOWN")

    def get_status(self):
        print(f"Firewall: {self.device}")
        print(f"Status: {self.status}")
        print(f"Threat Level: {self.threat}")
        print(f"Blocked IPs: {self.blocked_ips}")


class AntiVirus(SecurityDevice):
    def __init__(self, device_name, status, threat_level):
        super().__init__(device_name, status, threat_level)
        self.threats_detected = 0
        self.quarantined_threats = []

    def scan(self):
        self.threats_detected = self.threat
        print(f"Scanning... Found {self.threats_detected} threats!")
        self.log_event(f"Scan completed: {self.threats_detected} threats found")

    def quarantine(self, threat_name):
        self.quarantined_threats.append(threat_name)
        print(f"Threat {threat_name} has been quarantined")
        self.log_event(f"Quarantined: {threat_name}")

    def get_status(self):
        print(f"AntiVirus: {self.device}")
        print(f"Status: {self.status}")
        print(f"Threats Detected: {self.threats_detected}")
        print(f"Quarantined: {self.quarantined_threats}")


class IDS(SecurityDevice):
    def __init__(self, device_name, status, threat_level):
        super().__init__(device_name, status, threat_level)
        self.alerts_received = []
        self.suspicious_activity = False

    def monitor(self):
        print(f"Monitoring network activity...")
        if self.threat > 2:
            self.suspicious_activity = True
            self.send_alert("HIGH THREAT DETECTED!")
        else:
            print("No suspicious activity detected")
        self.log_event("Network monitoring completed")

    def send_alert(self, alert_message):
        self.alerts_received.append(alert_message)
        print(f"ALERT: {alert_message}")
        self.log_event(f"Alert sent: {alert_message}")

    def get_status(self):
        print(f"IDS: {self.device}")
        print(f"Status: {self.status}")
        print(f"Suspicious Activity: {self.suspicious_activity}")
        print(f"Alerts: {self.alerts_received}")


# TEST
print("=== FIREWALL ===")
firewall1 = Firewall("Firewall_01", "Active", 2)
firewall1.activate()
firewall1.check_ip("127.0.0.0")
firewall1.check_ip("192.1.1.1")
firewall1.block_ip("10.0.0.1")
firewall1.get_status()

print("\n=== ANTIVIRUS ===")
antivirus1 = AntiVirus("AntiVirus_01", "Active", 3)
antivirus1.activate()
antivirus1.scan()
antivirus1.quarantine("Trojan.exe")
antivirus1.get_status()

print("\n=== IDS ===")
ids1 = IDS("IDS_01", "Active", 4)
ids1.activate()
ids1.monitor()
ids1.get_status()

print("\n=== ALL LOGS ===")
print("Firewall Logs:", firewall1.logs)
print("AntiVirus Logs:", antivirus1.logs)
print("IDS Logs:", ids1.logs)