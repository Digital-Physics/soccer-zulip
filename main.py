import zulip

def main():
    client = zulip.Client(config_file="./zuliprc")
    client.send_message({"type": "private", "content": "test string", "to": "jdkhanlian@gmail.com"})

    # figure out which function to call to subscribe bot to test bot channel 

    # client has methods call_on_each_message, etc. (pass function)

    # https://recurse.zulipchat.com/api/configuring-python-bindings
    # https://pypi.org/project/zulip/
    # https://github.com/aadriien/pronoun-proofer/
    # https://recurse.zulipchat.com/#settings/your-bots

    print("Hello from soccer-zulip!")


if __name__ == "__main__":
    main()
