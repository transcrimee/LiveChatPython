import pytchat
import twitchio
import os
import time
import curses

def clear_screen():
    # Check the operating system name and run the appropriate command
    if os.name == 'nt':
        _ = os.system('cls') # Windows
    else:
        _ = os.system('clear') # Linux/macOS/Posix

print("Overlay for chat is starting...\n please link your video ID for your youtube live stream")
video_id = input("╰─▸")
print("clearing text in 3 seconds...") 
time.sleep(3)
clear_screen()

def cli_overlay_chat(stdscr):
    

    stdscr.nodelay(True)
    chat = pytchat.create(video_id=video_id)
    
    input_buffer = ""
    messages = []    # Clear screen
   
    
    # Create a sub-window (height, width, begin_y, begin_x)
    # This creates a box in the middle of the screen
    height, width = 30, 70,
    begin_y, begin_x = 5, 5
    win = curses.newwin(height, width, begin_y, begin_x)
    
    # Draw the box around the window's perimeter
    win.box()
    win.addstr(2, 2, "Chat Overlay Active!")
    while chat.is_alive():
         # 1. Check for New Chat Messages (Non-Blocking)
        for c in chat.get().sync_items():
            msg = f"[{c.author.name}]: {c.message}"
            messages.append(msg)
            if len(messages) > 10: messages.pop(0)
    
    # Add text inside the box (relative to the window's 0,0)
     
          

    # Create a sub-window for input
   
    # Refresh the window to show the box and text

        stdscr.erase()
        for i, m in enumerate(messages):
         stdscr.addstr(i, 0, m)
        stdscr.refresh()
        
        curses.napms(50) # Small sleep to save CPU (50ms)
    # Wait for a key press before exiting
 

curses.wrapper(cli_overlay_chat)



#print("Overlay for chat is starting...\n please link your video ID for your youtube live stream")
#video_id = input("╰─▸") 
#print("clearing text in 3 seconds...")
#time.sleep(3)
#clear_screen()
#print("┏━°⌜ CHAT ⌟°━┓")                         
#chat = pytchat.create(video_id=video_id)
#while chat.is_alive():
    #for c in chat.get().sync_items():
        #print(f"{c.datetime} [{c.author.name}]- {c.message}")
        # Here you can add code to overlay the chat message on your video stream
        # This could involve using a graphics library to render the text on screen