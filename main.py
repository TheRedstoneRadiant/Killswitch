import keyboard, json, requests

if __name__ == "__main__":
    while True:
        key = keyboard.read_key()

        if key == config["key"]:
            with open("config.json") as file:
                config = json.load(file)

            for index, user in enumerate(config):
                r = requests.patch(
                    "https://discord.com/api/v9/users/@me",
                    json={
                        "password": user["password"],
                        "new_password": user["password"],
                    },
                    headers={"Authorization": user["token"]},
                )

                user = r.json()

                if r.status_code == 200:
                    new_token = user["token"]
                    config[index]["token"] = new_token
                    with open("config.json", "w") as file:
                        json.dump(config, file, indent=4)

                

                requests.post(
                    config["webhook_url"],
                    json={
                        "content": f"Changing <@{user.get('id')}>'s token",
                        "embeds": [
                            {
                                "title": str(r),
                                "description": f"```json\n{json.dumps(user, indent=4)}\n```",
                                "color": None,
                            }
                        ],
                        "attachments": [],
                    },
                )
