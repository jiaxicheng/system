## Some notes:

**How to select After= and Wantedby=**

For most systemd user services, you can just use *Wantedby=default.target* and leave out the *After=* directive unless you need a specific boot-start order among your own user services. you can run the following command to check what targets, services etc: 

```
$ systemctl --user list-dependencies
default.target
● ├─selenium.service
● ├─stunnel@madison.service
● └─basic.target
●   ├─paths.target
●   ├─sockets.target
●   │ └─dbus.socket
●   └─timers.target
```

**__Note:__** When setting up the systemd system services, you will need to do the similar command with `systemctl list-dependencies` to check the exact order and hierachy you need.

For more examples, check the following folders for `user` and `system` subfolders: 
```
---
- Centos 7: /usr/lib/systemd
- Ubuntu 17.10: /lib/systemd
```

