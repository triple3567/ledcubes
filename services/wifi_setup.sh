#!/bin/bash
connmanctl disable wifi
sleep 5
connmanctl enable wifi
connmanctl scan wifi
sleep 5
connmanctl connect wifi_1cbfce109733_463831434336_managed_psk 
