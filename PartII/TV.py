class TV():
    def __init__(self):
        self.is_on = False
        self.is_muted = False
        self.channel_list = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.n_channels = len(self.channel_list)
        self.channel_index = 0
        self.VOLUME_MINIMUM = 0
        self.VOLUME_MAXIMUM = 10
        self.volume = self.VOLUME_MAXIMUM // 2
        
    def power(self):
        self.is_on = not self.is_on
        
    def volume_up(self):
        if not self.is_on:
            return
        if self.is_muted:
            self.is_muted = False
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume += 1
            
    def volume_down(self):
        if not self.is_on:
            return
        if self.is_muted:
            self.is_muted = False
        if self.volume > self.VOLUME_MINIMUM:
            self.volume -= 1
            
    def channel_up(self):
        if not self.is_on:
            return
        self.channel_index += 1
        if self.channel_index > self.n_channels:
            self.channel_index = 0
            
    def channel_down(self):
        if not self.is_on:
            return
        self.channel_index -= 1
        if self.channel_index < 0:
            self.channel_index = self.n_channels - 1
            
    def mute(self):
        if not self.is_on:
            return
        self.is_mute = not self.is_muted
        
    def set_channel(self, new_channel):
        if new_channel in self.channel_list:
            self.channel_index = self.channel_list.index(new_channel)
        # if the new_channel is not in our list of channels, don't do anything
        
    def show_info(self):
        print()
        print("TV status:")
        if self.is_on:
            print("TV is: On")
            print(f"Channel is: {self.channel_list[self.channel_index]}")
            if self.is_muted:
                print(f"Volume is: {self.volume}, (sound is muted)")
            else:
                print(f"Volume is: {self.volume}")
        else:
            print("TV is off")