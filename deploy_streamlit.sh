#!/bin/bash

# Function to check if VPN is connected
check_vpn() {
    VPN_STATUS=$(curl -s https://ipinfo.io)
    if [[ $VPN_STATUS == *"VPN_PROVIDER"* ]]; then
        echo "VPN is connected."
    else
        echo "VPN is not connected."
        exit 1
    fi
}

# Step 1: Start VPN
echo "${VPN_CONFIG}" > vpnconfig.ovpn
sudo apt-get update
sudo apt-get install -y openvpn
sudo openvpn --config vpnconfig.ovpn --daemon
sleep 10  # Give the VPN time to connect

# Step 2: Check VPN connection
check_vpn

# Step 3: Install Python dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# Step 4: Deploy Streamlit app
streamlit run app.py
z