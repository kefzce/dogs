
- **Automated Reward Claims**: Automatically claim.
- **Detailed Logging**: Keep track of your claims and any issues that arise.
- **CSV Integration**: Manage proxies and user IDs easily through a CSV file.

### 1. Clone or Download the Repository
```sh
git clone https://github.com/kefzce/dogs.git
cd dogs
```
### 2. Install the Required Dependencies
```sh
pip3 install -r requirements.txt
```

### 3. Move the Folder to the Desired Location
```sh
sudo mv dogs /root/dogs/
```

### 4. Move the Service File to the Systemd Directory
```
sudo mv dogs.service /etc/systemd/system/
```
### 5. Reload the Systemd Daemon
```sh
sudo systemctl daemon-reload
```

### 6. Start and Enable the Service
```sh
sudo systemctl start dogs.service
sudo systemctl enable dogs.service
```

### 7. CSV Format
```sh
disc,http proxy,telegram_user_id
```

### 8. Example CSV File
```sh
account1,http://proxy1:port1,telegram_user_id1
account2,http://proxy2:port2,telegram_user_id2
account3,http://proxy3:port3,telegram_user_id3
```

### How to get my telegram_user_id ?
https://t.me/getmyid_bot