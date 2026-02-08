from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.text import Text
from rich.markup import escape
from stylelibrary import style, color
import pytchat
import twitchio
import os
import time

def clear_screen():
    # Check the operating system name and run the appropriate command
    if os.name == 'nt':
        _ = os.system('cls') # Windows
    else:
        _ = os.system('clear') # Linux/macOS/Posix

print(color.rgb_text(255, 255, 255, "Overlay for chat is starting...\n please link your video ID for your youtube live stream"))
print(color.rgb_text(255, 255, 255, f"Note https://www.youtube.com/watch?v={style.bold_style(color.rgb_text(255, 105, 180, "-OL13v2EAK8"))}!"))
video_id = input(color.rgb_text(255, 255, 255,"╰─▸ "))
print(color.rgb_text(255, 255, 255,"clearing text in 1 seconds...")) 
time.sleep(1)
clear_screen() # clear the screen for better visibility

header_text = Text("Live Stream Chat", justify="center", style="bold white on purple") # Add very nice header_text looking very sleek
header_panel = Panel(header_text, height=3)

chat_area = Text()
content_panel = Panel(chat_area, title="Chat", style="bold white") # Create the main content panel for chat messages

# 3. Create a Layout object to structure the console
layout = Layout()

# Define the layout structure: one top pane, one bottom pane
layout.split_column(
    Layout(header_panel, name="header", size=3),
    Layout(content_panel, name="main")
)

author = []
messages = [] 
chat_area = []
chat = pytchat.create(video_id=video_id) # Initiate a connection and fetch live chat messages from a specific YouTube live stream

console = Console()
with Live(layout, screen=True, redirect_stderr=False, redirect_stdout=False) as live:
    # Continuously add new lines to the log area
    while chat.is_alive():
        # 1. Check for New Chat Messages (Non-Blocking)
        for c in chat.get().sync_items(): 
            
            author_name = c.author.name if c.author.name else "Unknown User" # If no author name for some reason set it to unknown user
            
            msg = f"[{c.author.name}]: {c.message}"
            chat_area.append(escape(msg)+ "\n")
            #if len(log_area) > 20: log_area.pop(0)
            if len(chat_area) >= (content_panel.height or 20) - -30:
             chat_area.pop(0) 
     
        # Update the content panel with the new text
        layout["main"].update(Panel("".join(chat_area), title="Chat", style="bold white"))
        # Manually refresh the screen with the new layout
        live.refresh()
        
        time.sleep(0.5) 

    # Keep the output visible after the loop finishes
    time.sleep(5)