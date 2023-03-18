import sys

# ASCII art
print("""
             _               ____  _   _ _   _ _  _______ ____  
   ___ _   _| |__|  ___ _ __|  _ \| | | | \ | | |/ / ____|  _ \ 
  / __| | | | '_ \ / _ \ '__| |_) | | | |  \| | ' /|  _| | | | |
 | (__| |_| | |_) |  __/ |  |  __/| |_| | |\  | . \| |___| |_| |
  \___|\__, |_.__/ \___|_|  |_|    \___/|_| \_|_|\_\_____|____/ 
       |___/                                                    
""")


# Wait for the user to press Enter or q to quit
while True:
    user_input = input("Press Enter to start the scan or q to quit: ")
    if user_input == "":
        break
    elif user_input.lower() == "q":
        print("Exiting...")
        sys.exit()

# Define a function to ping an IP address
def ping(ip):
    result = subprocess.run(['ping', '-c', '1', '-t', '1', ip], capture_output=True)
    is_online = result.returncode == 0
    status = "ONLINE" if is_online else "OFFLINE"
    print(f"{ip} is {status}.")
    return (ip, is_online)

# Open the output file
with open("onlinedevices.txt", "w") as output_file:
    # Create a flag for keyboard input
    exit_flag = threading.Event()

    # Define a function to check for the Esc key
    def check_exit():
        while True:
            if keyboard.is_pressed('esc'):
                exit_flag.set()
                break

    # Start the keyboard input checking thread
    exit_thread = threading.Thread(target=check_exit, daemon=True)
    exit_thread.start()

    # Use a thread pool to ping multiple IPs at once
    with ThreadPoolExecutor() as executor:
        # Ping each possible IP address
        for ip, is_online in executor.map(ping, (f"10.0.2.{i % 256}" for i in range(2**24))):
            if is_online:
                # Write the online device to the output file
                output_file.write(ip + "\n")

        print("Scan complete.")
        # Wait for the user to input "q" before exiting
        while True:
            user_input = input("Enter q to quit: ")
            if user_input.lower() == "q":
                print("Exiting...")
                sys.exit()

print("Goodbye!")
input('Press ENTER to exit')