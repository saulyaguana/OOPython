from TV import TV

# Main code
tv1 = TV()

# Turn the TV on and show the status
tv1.power()
tv1.show_info()

# Change the channel up twice, raise the volume twice, show status
tv1.channel_up()
tv1.channel_up()
tv1.volume_up()
tv1.volume_up()

# Turn the TV off, show status, turn the TV on, show status
tv1.power()
tv1.show_info()
tv1.power()
tv1.show_info()

# Lower the volume, mute the sound, show status
tv1.volume_down()
tv1.mute()
tv1.show_info()

# Change the channel to 11, mute the sound, show status
tv1.set_channel(11)
tv1.mute()
tv1.show_info()