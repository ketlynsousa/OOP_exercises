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
                    content += f'[yellow on yellow] [/]'

        tv = Panel(content, title='[ TV ]', width=35)
        print(tv)

    def turn_on_off(self):
        self.tv_on = not self.tv_on


c = RemoteControl(4,5)
c.turn_on_off()
c.show_screen()
