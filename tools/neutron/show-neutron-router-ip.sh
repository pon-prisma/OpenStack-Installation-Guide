#!/bin/bash

if [ $# -eq 0 ]
then
   echo "Specificare l'ID del router"
else
   ip netns exec qrouter-$1 ip addr list
fi

