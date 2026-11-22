import aiomcrcon

from farenus_api import config

host = config.MINECRAFT_RCON_HOST
port = int(config.MINECRAFT_RCON_PORT)
password = config.MINECRAFT_RCON_PASSWORD


async def whitelist_add(player):
    client = aiomcrcon.Client(host, port, password)
    await client.connect()
    await client.send_cmd(f"whitelist add {player}")
    await client.close()
    return {"player": player}
