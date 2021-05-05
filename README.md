## Tutorial

### Requirements

An **Ubuntu 18.04** VM with Python installed.

### Setup

Run the following commands to install chromium and chromedriver:

Installing Chrome
```bash
sudo apt install chromium-browser -y
```

Installing the Driver
```
sudo apt install wget unzip -y
wget https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip -d /usr/bin
rm chromedriver_linux64.zip
```



