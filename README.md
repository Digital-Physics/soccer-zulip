# Soccer Zulip Bot

This is repo for a Recurse Center [zulip](https://en.wikipedia.org/wiki/Zulip) bot that will interact in Zulip discussion forums when called upon.The bot's response includes a classic World Cup video and notes how many days are remaining until the start of the 2026 World Cup.

Tech Notes:  
-To call the bot, start the post with @wc2026-bot@recurse.zulipchat.com  
-Make sure your bot is subcribed to Zulip channels you want it to listen to
-There is another README.md in the ansible directory (from @rafl)
-If all else fails, reach out to @rafl

### running locally for testing
```
PYTHONPATH=. uv run zulip-run-bot wc2026 --config-file ./zuliprc
```

### to redeploy after to the Recurse Center's "Heap" cluster
#### (create a username and ssh key on the RC site first)
```
ansible-playbook -i ansible/inventory ansible/deploy.yml
```

### for debugging stuff as the 'service user' on the cluster
```
sudo -u svc-soccer-bot bash
```

### to do things like look at status, etc. we needed to set XDG_RUNTIME_DIR
```
svc-soccer-bot@broome:~/soccer-bot$ export XDG_RUNTIME_DIR=/run/user/$(id -u)
svc-soccer-bot@broome:~/soccer-bot$ systemctl --user status
```

### this was put into the ansible yaml file for the svc task, so not needed
```
PYTHONPATH=. /home/svc-soccer-bot/.local/bin/uv run zulip-run-bot wc2026 --config-file ./zuliprc
```

### you can see stdout and stderror of program on server
#### (must first ssh in as user, change user to service user, set up XDG_RUNTIME_DIR)
```
journalctl --user -u soccer-bot.service
```

### to see new stdout and stderror going forward (to see live messages)
```
journalctl --user -u soccer-bot.service -f
```