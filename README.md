<h1 align="center">
  Reset Token Hotkey
  <br>
</h1>

<h4 align="center">A simple Python script to reset your Discord token on keypress.</h4>

<p align="center">
  <a href="https://github.com/TheRedstoneRadiant/Reset-Token-Hotkey/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue?logo=gitbook&logoColor=blue">
  </a>
  <a>
</p>
  
<br><br><br><br>

### Installation

Make sure you have <a href="https://python.org">Python 3</a> and Git installed.

##### Clone the repo (or download as zip instead of cloning)
```bash
git clone https://github.com/TheRedstoneRadiant/Reset-Token-Hotkey
cd Reset-Token-Hotkey
```
  
##### Install dependencies (requests, keyboard)

Windows: 
```bash
python -m pip install -r requirements.txt
```

Linux & Mac: 
```bash
python -m pip install -r requirements.txt
```
###### Note: You will have to run the script as sudo on Linux
  
### config.json
```json
{
    "tokens": [
        {
            "token": "current token",
            "password": "current password"
        },
        {
            "token": "current token",
            "password": "current password"
        }
    ],
    "hotkey": "f1",
    "webhook_url": "https://discord.com/xxxxxxxxx/xxxxxxxxx"
}
```

- `tokens`: An array of objects containing Discord tokens.
- `hotkey`: Trigger the script once the hotkey is pressed.
- `webhook_url`: A Discord webhook URL to send nicely formatted response JSON.
