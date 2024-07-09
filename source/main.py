from time import sleep
from port_scan import scan_ports
from mysql import phping_inclusion
from http_trigger import phping_trigger
from sniff import icmp_sniff

def main():
    target_ip = input('Target IP: ')
    print()
    while True:
        sleep(3)
        print('--=[ Victorgeek ]=--')
        print('1. Port Scan')
        print('2. MySQL Payload')
        print('3. HTTP Trigger')
        print('4. ICMP Sniffer')
        print('0. Exit')

        option = input("\nChoose an option: ")

        if option == '1':
            first = int(input('first port: '))
            last = int(input('last port: '))
            print('\n-----------------------\n')
            scan_ports(target_ip, first, last)
            print('\n-----------------------\n')
        elif option == '2':
            print('\n-----------------------\n')
            phping_inclusion(target_ip)
            print('\n-----------------------\n')

        elif option == '3':
            print('\n-----------------------\n')
            phping_trigger(target_ip)
            print('\n-----------------------\n')

        elif option == '4':
            print('\n-----------------------\n')
            icmp_sniff()
            print('\n-----------------------\n')

        elif option == '0':
            print("\nFollow...")
            break
        else:
            print("\nHerer,right results...\n")

if __name__ == "__main__":
    main()
