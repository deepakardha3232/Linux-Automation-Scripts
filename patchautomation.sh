#!/bin/bash

# Patch Automation Script for RHEL/CentOS
# Author: Deepak Reddy Ardha
# Date: $(date)
# Description: Automates patch checking, installation, and logging.

# Variables
LOG_FILE="/var/log/patch_automation_$(date +%F).log"
EMAIL="your-email@example.com"  # Set your notification email

# Ensure the script is run as root
if [[ $EUID -ne 0 ]]; then
  echo "This script must be run as root." | tee -a "$LOG_FILE"
  exit 1
fi

echo "Starting patch process: $(date)" | tee "$LOG_FILE"

# Step 1: Check for available updates
echo "Checking for available updates..." | tee -a "$LOG_FILE"
yum check-update >> "$LOG_FILE" 2>&1

# Step 2: Install updates
echo "Installing available patches..." | tee -a "$LOG_FILE"
yum update -y >> "$LOG_FILE" 2>&1

# Step 3: Clean up
yum clean all >> "$LOG_FILE" 2>&1

# Step 4: Reboot prompt (optional)
read -p "Reboot system after patching? (y/n): " REBOOT
if [[ "$REBOOT" == "y" ]]; then
  echo "Rebooting system..." | tee -a "$LOG_FILE"
  reboot
else
  echo "Reboot skipped. Manual reboot recommended if kernel was updated." | tee -a "$LOG_FILE"
fi

# Step 5: Notify (Optional: requires mailx or sendmail configured)
if command -v mail >/dev/null 2>&1; then
  cat "$LOG_FILE" | mail -s "Patch Automation Report - $(hostname)" "$EMAIL"
fi

echo "Patch automation completed at $(date)" | tee -a "$LOG_FILE"
