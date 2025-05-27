# Linux-Automation-Scripts
Bash scripts for server health checks, log analysis, and patch automation.
# 1. Server Health Checks
- CPU, memory, and disk usage summaries
- Running processes and load averages
- Network connectivity checks (ping, DNS resolution)
- Uptime and reboot tracking

# 2. Log Analysis
- Parse and filter system logs (`/var/log/messages`, `syslog`, `secure`, `auth.log`)
- Identify and summarize critical, warning, and error messages
- Failed login attempt summaries and security alerts

# 3. Patch Automation
- Automated YUM/DNF-based patching with pre- and post-checks
- Package update verification and reporting
- Backup of package lists and current versions before applying patches

#Prerequisites
- Linux system (RHEL, CentOS, or similar)
- Bash shell
- Root or sudo privileges (for patching)

Run a script by shell scripting
health_check.sh
analyze_logs.sh
patch_system.sh
