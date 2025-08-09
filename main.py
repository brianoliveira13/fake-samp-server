from samp_server import SAMPServer
from samp_server.handlers import handle_server_info, handle_server_rules, handle_player_list

def main():
    server = SAMPServer()
    server.init(7777)

    server.server_info.set(handle_server_info)
    server.server_rules.set(handle_server_rules)
    server.player_list.set(handle_player_list)

    print("Starting SAMP server on port 7777...")

if __name__ == "__main__":
    main()