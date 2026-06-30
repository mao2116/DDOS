
import os
import sys
import platform

# --- Open Telegram Link (Marketing/Credit) ---
os.system("xdg-open https://t.me/cybersecurityteam_cst")

def main():
    os.system('clear')
    print('\033[1;32m[>] Checking Device Architecture...')
    
    # Check bit architecture
    bit = platform.architecture()[0]
    
    try:
        if bit == '64bit':
            print('\033[1;32m[>] 64-bit Architecture Detected.')
            # Import from the 64-bit encrypted file
            try:
                import core_64 as core
                core.NovaStrike().menu()
            except ImportError:
                print('\033[1;31m[x] Error: core_64.so not found!')
                
        elif bit == '32bit':
            print('\033[1;32m[>] 32-bit Architecture Detected.')
            # Import from the 32-bit encrypted file
            try:
                import core_32 as core
                core.NovaStrike().menu()
            except ImportError:
                print('\033[1;31m[x] Error: core_32.so not found!')
        else:
            print('\033[1;31m[x] Sorry, Device Architecture Not Supported.')
            
    except Exception as e:
        print(f'\033[1;31m[!] Fatal Error: {e}')

if __name__ == "__main__":
    main()
