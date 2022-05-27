<h1 align="center">
  <a href="https://github.com/TheRedstoneRadiant/Killswitch"><img src="https://i.imgur.com/KpQwkQq.png" width=128 height=128 alt="logo"></a>
  <br>
  Killswitch
  <br>
  </a>
</h1>

<h4 align="center">
  A simple Python script to reset your Discord token on keypress.
  <br><br>
  <a href="https://github.com/TheRedstoneRadiant/Killswitch/blob/master/LICENSE">
  <img src="https://img.shields.io/badge/license-MIT-blue?logo=gitbook&logoColor=blue">
</a>
</h4>

<br><br><br><br>
## Notice: I'll add proxies at 10 stars. Make sure to star the repo!
<br><br>

<img src="[drawing.jpg](https://user-images.githubusercontent.com/76220359/170635393-6125c756-8643-4cd5-9ed8-7302d996b70b.gif)" alt="Killswitch Usage" width="200"/>
<img src="[drawing.jpg](https://user-images.githubusercontent.com/76220359/170634160-6c9b6ef4-103a-4582-a695-fd8e82746cd3.png)" alt="Killswitch Webhook" width="200"/>

### Installation

Make sure you have <a href="https://python.org">Python 3</a> and Git installed.

##### Clone the repo (or download as zip instead of cloning)
```bash
git clone https://github.com/TheRedstoneRadiant/Killswitch
cd Killswitch
```
  
##### Install dependencies (requests, keyboard)

Windows: 
```bash
python -m pip install -r requirements.txt
```

Linux & Mac: 
```bash
python3 -m pip install -r requirements.txt
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
