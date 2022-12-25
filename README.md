# AnyPortScan

Description and Purpose:

A user-friendly port scanner that accepts target FQDN or IP address and target port number(s) as input from the user and scans the ports accordingly.

To start using:

1. Install Python on your machine:

sudo apt-get update

sudo apt-get install python3.9

2. Download the script to your machine:

git clone https://github.com/Darkscr1pt/AnyPortScan.git

3. Make the script executable:

chmod +x AnyPortScan.py

4. Run the script: 

python3 AnyPortScan.py

5. The script will ask you to provide the name of the target server (IP address or FQDN).

6. The script will scan a predefined list of ports on the target server. The list can be modified in line 17 (port_numbers). Alternatively, if you prefer to be prompted to enter the port numbers manually (as user input) you can comment line 17 and uncomment line 15.

7. The script will return all the scanned ports and their status (Open or Closed).

