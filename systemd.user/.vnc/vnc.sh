#!/bin/bash

dn=${1?"Usage: missing display number!"}

rm -rf /tmp/.X11-unix/X$dn

/usr/bin/vncserver :$dn
