import keyboard, json, requests, sys, os


def clear():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    try:
        clear()

        with open("config.json") as file:
            config = json.load(file)

        print(
            f"""\033[0;31m
       _ _ _              _ _       _     
  /\ /(_) | |_____      _(_) |_ ___| |__  
 / //_/ | | / __\ \ /\ / / | __/ __| '_ \ 
/ __ \| | | \__ \\\\ V  V /| | || (__| | | |
\/  \/|_|_|_|___/ \_/\_/ |_|\__\___|_| |_|
                                          
Loaded {len(config['tokens'])} token{"s" if len(config['tokens']) != 1 else ""}.
Hotkey: "{config["hotkey"]}\""""
        )

        valid_tokens = {}

        for index, user in enumerate(config["tokens"]):
            r = requests.get(
                "https://discord.com/api/v9/users/@me",
                headers={"Authorization": user["token"]},
            )

            if r.status_code != 200:
                print(f"\nInvalid Token: {user['token'][:25]}...")

            else:
                valid_tokens[index] = user

        if not valid_tokens:
            print("No tokens valid!")
            exit(input("\nPress enter to exit..."))

        requests.post(
            config["webhook_url"],
            json={
                "embeds": [
                    {
                        "title": "**Killswitch online!**",
                        "description": f"Hotkey: `{config['hotkey']}`",
                        "color": 16711680,
                    }
                ],
                "attachments": [],
                "username": "Killswitch",
                "avatar_url": "https://i.imgur.com/KpQwkQq.png",
            },
        )

        while True:
            print("\nListening for keypress.", end="\r")

            keyboard.wait(config["hotkey"])

            print("Keypress detected. Executing payload.")

            with open("config.json") as file:
                config = json.load(file)

            for index, user in valid_tokens.items():
                r = requests.patch(
                    "https://discord.com/api/v9/users/@me",
                    json={
                        "password": user["password"],
                        "new_password": user["password"],
                    },
                    headers={"Authorization": user["token"]},
                )

                response = r.json()

                print(f"Token: {response.get('token')} | Response: {r.status_code}")

                if r.status_code == 200:
                    new_token = response["token"]
                    config["tokens"][index]["token"] = new_token
                    valid_tokens[index]["token"] = new_token

                    with open("config.json", "w") as file:
                        json.dump(config, file, indent=4)

                requests.post(
                    config["webhook_url"],
                    json={
                        "content": f"Changing <@{response.get('id', 404)}>'s token",
                        "embeds": [
                            {
                                "title": str(r),
                                "description": f"```json\n{json.dumps(response, indent=4)}\n```",
                                "color": 16711680,
                            }
                        ],
                        "attachments": [],
                        "username": "Killswitch",
                        "avatar_url": "https://i.imgur.com/KpQwkQq.png",
                    },
                )

    except KeyboardInterrupt:
        pass

    finally:
        print("\033[0;0m\n")  # reset terminal color

        clear()
