# File: main.py

from src.emulators import CHIP8, PygameDisplay, Config

def main():
    config = Config("config.json")
    emulator = CHIP8(config.config_path)
    
    if not emulator.load_rom("path/to/your/rom.ch8"):
        print("Failed to load ROM")
        return

    display = PygameDisplay(64, 32, CHIP8.get_key_map(), config.config_path)

    running = True
    while running:
        frame = emulator.run_frame()
        display.update(frame)
        
        keys = display.get_keys()
        emulator.set_keys(keys)
        
        if display.handle_input():
            running = False

    display.close()

if __name__ == "__main__":
    main()