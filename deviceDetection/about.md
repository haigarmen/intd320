<h2>Device Detection using Bluetooth on a RaspberryPi 3</h2>
Before you get started you'll need to make sure your Raspberry Pi has access to the internet, either through a wired or wireless connection.  In addition you'll want to be familiar with accessing a command terminal on the Pi, like with the SSH tool.

You will also need to make sure your Raspberry Pi is running the latest version of the Raspbian Stretch operating system (either the full or lite version).  These instructions will work with the older Jessie release--but not Wheezy.
For this to work you need to install the latest "Bluez" library for the Pi as this handles the low level bluetooth stuff.

<h3>Install Dependencies</h3>
But first let's intall the dependencies for the Bluez library. Run the following commands to install these dependencies:
<pre>
sudo apt-get update
sudo apt-get install -y libusb-dev libdbus-1-dev libglib2.0-dev libudev-dev libical-dev libreadline-dev
</pre>

<h3>Download Bluez</h3>
To install bluez you'll need to download and compile the latest version of its source code.  You could install bluez from a prebuilt package in the Raspbian repository however the version in the repository almost certainly is out of date.  If you're using Bluetooth low energy features you really want to be running the absolute latest version of bluez to get the latest bug fixes and features.  Compiling bluez from source will ensure you have the latest and greatest release.
Visit the [bluez download page](http://www.bluez.org/download) and copy the link to the latest source release (under the User Space BlueZ Package section).  For example at the time of this guide's writing the latest version of bluez is 5.37 and can be downloaded from: 


<h3>Install bluez:</h3>

<pre>
sudo wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.41.tar.xz
sudo tar -xJf bluez-5.41.tar.xz
cd bluez-5.41
sudo ./configure --disable-systemd 
sudo make 
sudo make install
</pre>

Reference:
This information was originally at an Adafruit tutorial:
[https://learn.adafruit.com/install-bluez-on-the-raspberry-pi/installation]
