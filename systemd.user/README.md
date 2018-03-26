## Some notes:

### Selenium User Service ###
```
# enable the user service
systemctl --user enable selenium.service
# start the selenium service
systemctl --user start selenium.service
# check the status of the service
systemctl --user status selenium.service
# stop the selenium user service
systemctl --user stop selenium.service
# restart the service
systemctl --user restart selenium.service
```

### SSH Tunnel User Service ###
Copy the file `.ssh/config-madison` to your home folder : ~/.ssh where `madison` is the ssh destination hostname or host-ip
```
# enable the Stunnel to a server named `madison`
systemctl --user enable stunnel@madison.service
# start the Stunnel to `mandison`
systemctl --user start stunnel@madison
# check the status of the above service
systemctl --user status stunnel@madison
```

__NOTE__: the extension .service can be ignored when running the above command lines.

### How to select After= and Wantedby= ###

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

**Note:** When setting up the systemd system services, you will need to do the similar command with `systemctl list-dependencies` to check the exact order and hierachy you need.

For more examples, check the following folders for `user` and `system` subfolders: 
```
- Centos 7: /usr/lib/systemd
- Ubuntu 17.10: /lib/systemd
```

