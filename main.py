from samp_server import SAMPServer
from samp_server.handlers import handle_server_info, handle_server_rules, handle_server_ping

def main():
    server = SAMPServer()
    server.init('0.0.0.0', 7777)

    server.server_info.set(handle_server_info)
    server.server_rules.set(handle_server_rules)
    server.server_ping.set(handle_server_ping)
    try:
        server.monitor()
    except KeyboardInterrupt:
        print('server shutting down')
    finally:
        server.shutdown()

if __name__ == "__main__":
    main()