# Krampus Controller

### What is this?

Krampus is a controller to drive and control neoPixel LEDS using the WS281x protocol.  Krampus models LEDs to be arranged as a Christmas Tree or on a tree.  
Web interface is able to start and stop the tree lights.  You can manually create a sequeuence of effects and start the loop of animation.

### Equipment Needed
* NeoPixel supporting WS281x protocol
* 5v DC power supply (1 amp per 50 lights)
* Raspberry PI

### Getting started

1. Clone repo
2. sudo pip3 install -r requirements.txt
3. sudo python3 krampus/server.py
4. Open localhost

### PI Hookup Configuration
* Default GPIO data port 18
* Common ground between raspberry pi and power supply
 
![NeoPixel PI wiring](https://cdn-learn.adafruit.com/assets/assets/000/064/122/medium640/led_strips_raspi_NeoPixel_Diode_bb.jpg?1540315941 "NeoPixel Hookup")]

### Auto Startup on PI
* Open crontab, type in terminal
``
 crontab -e
``
* Add to bottom of crontab file
``
 @reboot sudo python3 {path-to-project}/krampus/server.py
``

### Ideas for Improvements
* Seperate out Effects into their own files and auto-load them on start
* Add web sockets to broadcast changes to the backend tree modules status
* Add ability to create custom color palettes 
* Show current effect sequences and allow editing in the web interface
