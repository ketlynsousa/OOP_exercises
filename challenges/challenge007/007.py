# Create a class called RemoteControl, where we will simulate the operation of a simple remote control (channel, volume, and on/off).
from rich import print
from rich.panel import Panel

class RemoteControl:
    min_channel:int = 1
    max_channel:int = 6
    min_volume:int = 1
    max_volume:int = 8

    def __init__(self, channel = 1, volume = 2):
        self.current_channel:int = channel
        self.current_volume:int = volume
        self.tv_on:bool = False

    def show_screen(self):
        if not self.tv_on:
            content = ':prohibited: [red]TV IS TURNED OFF[/]'
        else:
            content = f'CHANNEL = '
            for channel in range(RemoteControl.min_channel, RemoteControl.max_channel + 1):
                if channel == self.current_channel:
                    content += f'[yellow on yellow] {channel} [/]'
                else:
                    content += f' {channel} '

            content += f'\nVOLUME  = '
            for volume in range(RemoteControl.min_volume, RemoteControl.max_volume + 1):
                if volume <= self.current_volume:
                    content += f'[black on cyan] [/]'
                else:
                    content += f'[black on white] [/]'

        tv = Panel(content, title='[ TV ]', width=35)
        print(tv)

    def turn_on_off(self):
        self.tv_on = not self.tv_on

    def more_channel(self):
        if self.tv_on:
            if self.current_channel == RemoteControl.max_channel:
                self.current_channel = RemoteControl.min_channel
            else:
                self.current_channel += 1

    def less_channel(self):
        if self.tv_on:
            if self.current_channel == RemoteControl.min_channel:
                self.current_channel = RemoteControl.max_channel
            else:
                self.current_channel -= 1

    def more_volume(self):
        if self.tv_on:
            if self.current_volume != RemoteControl.max_volume:
                self.current_volume += 1

    def less_volume(self):
        if self.tv_on:
            if self.current_volume != RemoteControl.min_volume:
                self.current_volume -= 1


# Main Program
c = RemoteControl()
c.turn_on_off()

# Increasing and Decreasing channels
c.more_channel()
c.more_channel()
c.more_channel()
c.less_channel()

# Increasing and Decreasing volume
c.more_volume()
c.more_volume()
c.more_volume()
c.less_volume()

# Display tv screen
c.show_screen()
