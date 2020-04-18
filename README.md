## ExploderBot Testbed

### Host Requirements
* Operating System (OS)
  * Linux Derivative - Successfully tested with RHEL/CENTOS and Debian-based Distributions
* Packages
  * git
  * aws-cli
  * ansible
  * python3 - Confirmed compatability with Python 3.6 and above
  * python3-pip
  * virtualenv
* Infrastructure Requirements
  * Amazon Web Services (AWS) Account
  * AWS - Vitual Private Cloud
  * AWS - Subnet
  * AWS - Intenet Gateway

### Clone ExploderBot Repository
 All necessary source-code to replicate the ExploderBot Fast Flux Infrastructure is hosted via a
Github repository. Utilize the git command-line interface (cli) to clone the repository:
```
# git clone https://github.com/cristabela/exploderbot-ffn
```

### Create Python Virtual Envionment
Utilizing the virtualenv utility, create and activate a virtual environment:
```
# virtualenv [virtualenv name]
# source [virtualenv name]/bin/activate
```

### Install Python Packages
Utilize pip3 to install all necessary packages list in the “requirements.txt” file:
```
(virtualenv)# pip3 install -r requirements.txt
```

### Available Ansible Playbooks
The ExploderBot Fast Flux Infrastructure repository include multiple ansible playbooks designed
to automate the deployment of key pieces of infrastructure:
* DNS Management & Analysis Playbook – dns_server_playbook.yml
  * The following playbook provides the following capabilities:
    * Functioning DNS Server With Preconfigured Forward Zone: This forward zone currently contains records for an artificial domain: exploderbot-uah.com; however, this may be modified as needed.
    * Automated DNS Data Collection Service: A service configured to execute on startup collects all DNS queries and responses from the DNS server and stores them in a packet capture (PCAP) format. Additionally, the service will restart after running for 24 hours. PCAP files may be located within the /tmp directory, writted as: "/tmp/${DATE}.pcap.
    * Automated AWS EC2 Elastic IP Utility: A Python script that utilizes AWS APIs to interact with a specified EC2 instance. Leverages Elastic IP services to associate a new public IP Address to a specified EC2 instance at a user-defined interval. This concept provides the fast-flux emulation capability.
    
* C2 Server Playbook – c2_playbook.yml
  * The following playbook provides multiple utilities to emulate malicious activity:
    * DNS Tunneling/C2
    * TCP/HTTP(s) C2
    * Malware Hosting

### AWS - Create Identity Access Management (IAM) Users
AWS IAM enables secure access to AWS resources. Using IAM, multiple users may interact with a single subscription and can be managed through groups and permissions. Create an IAM user by accessing the IAM Dashboard:
![alt-text](https://github.com/cristisabela/explorderbot-ffn/blob/master/images/my_security_credentials.png)
* The IAM Dashboard is most easily access by clicking the account’s username, located in the AWS navigation bar, and selecting “My Security Credentials”
![alt-text](https://github.com/cristisabela/explorderbot-ffn/blob/master/images/add_user.png)
* Select the “Users” option located under the “Access management” tab within the IAM Dashboard’s Sidebar and then select “Add user”
![alt-text](https://github.com/cristisabela/explorderbot-ffn/blob/master/images/user_details.png)
* Fill out the form with the appropriate username and password settings. Ensure that the “Programmatic access” and “AWS Management Console access” check boxes are both selected and select “Permissions” to proceed.
![alt-text](https://github.com/cristisabela/explorderbot-ffn/blob/master/images/set_permissions.png)
* Set the desired permissions the created users by either creating a user group, or attaching existing AWS policies directly to a user. 
 * Note: Standard Users of this infrastructure will only need the “AmazonEC2FullAccess” policy selected to replicate the Fast Flux infrastructure.
* After selecting policies, proceed to “Tags” and provide IAM tags as needed. Finally, proceed to “Review” and finish by clicking “Create user”
![alt-text](https://github.com/cristisabela/explorderbot-ffn/blob/master/images/user_review.png)

### AWS - Maintaining User Access Keys
![alt-text](https://github.com/cristisabela/explorderbot-ffn/blob/master/images/user_keys.png)
* After successfully creating a new user(s), a unique Access key ID and Secret access key will be generated. This is only time that these credentials will be accessible to review. Ensure that these are securely stored and disseminated to the appropriate user.

### AWS - Create SSH Public Key Pair
* AWS Elastic Compute Cloud (EC2) instances utilize Secure Shell (SSH) public keys for authentication. During EC2 creation, an SSH key is associated with an instance. Create an SSH Key for the user:
![alt-text](https://github.com/cristisabela/explorderbot-ffn/blob/master/images/services_ec2.png)
* Select the “Services” tab from the AWS navigation bar and click “EC2” under the “Compute” tab.
![alt-text](https://github.com/cristisabela/explorderbot-ffn/blob/master/images/create_key_pair.png)
* Under the EC2 Dashboard, select “Key Pairs” under the “Network and Security” tab.
[alt-text](https://github.com/cristisabela/explorderbot-ffn/blob/master/images/key_pair_name.png)
* Enter a key pair name and ensure that the “pem” File format is selected. Click “Create key pair” to finish. Download and store the public key.
* Note – This will be the only time in which the newly create public key will be available for download. 
[alt-text](https://github.com/cristisabela/explorderbot-ffn/blob/master/images/ansible_key_pair_name.png)
* To utilize the new keypair, edit an Ansible Playbook and modify the keypair variable with the new key pair name.

### Create an Ansible Vault
Ansible Vault is a feature of ansible that provides encrypted storages of sensitive passwords or keys, rather than as plaintext values in a playbook or role. These vault files can then be distributed or placed in source control. Create a new ansible vault to store the AWS Access Key ID and Secret Access Key for a user:
```
(virtualenv)# ansible-vault create [vault_name].yml
New Vault password:
Confirm New Vault password:
```
![alt-text](https://github.com/cristisabela/explorderbot-ffn/blob/master/images/vault.png)
* This will open a text editor. Ensure to utilize aws_access_key: and aws_secret_key: as variables and provide the respective values for each. Once saved, the file’s content will be encrypted.
![alt-text](https://github.com/cristisabela/explorderbot-ffn/blob/master/images/cat_vault.png)

### Run an Ansible Playbook
Run an Ansible playbook by executing the following:
```
(virtualenv)# ansible-playbook -i hosts --ask-vault-pass dns_sever_playbook.yml
```

### AWS EC2 Elastic IP Utility
Execte the Elastic IP by running the following:
```
(virtualenv)# allocate.py -i [Instance ID] -t [time]
```

