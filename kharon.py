from src.enum.web_enum import web_enum
from src.tool_check import get_list, check_if_exist
from src.scan_loop import is_scan_complete
from src.utils.ascii import get_ascii
from src.utils.colors import colors
import time
import os
import sys

""" Settings """
# terminal_type = "gnome" | set this var to your OS' terminal
terminal_type = "mate" # I'm on parrotsec thus I use mate-terminal
""" Settings """

intensity_lev = None
complete = False
n = 1
report_asking = True

def main():
    global intensity_lev, complete, n, terminal_type, report_asking
    display_menu()
    list = get_list()
    sys.stdout.write('\33]0;Kharon - CTF Website Scanner\a')
    sys.stdout.flush()

    for tool in list:
        if check_if_exist(tool) == False:
            display_menu()
    addr = str(input("└──────⮞ IP-Address : "))

    display_menu()
    print("├─" + colors.FAIL + "⮞" + colors.WARNING + " IP-Address : {}".format(addr))
    print("│")
    intensity_lev = int(input("└──────⮞ Scan intensity (1-3) : "))
    enum = web_enum(addr, intensity_lev, terminal_type)
    os.system(f"mkdir ressources/output/{addr}-{intensity_lev}/")
    enum.nmap_scan()
    enum.ffuf_scan()
    enum.nikto_scan()

    while complete != True:
        display_menu()
        do_graphic_loop(addr)
        scan = is_scan_complete(addr, intensity_lev)
        if scan[0]:
            complete = True
        elif len(scan[1]) != 0 and len(scan[1]) < 3:
            display_menu()
            print("├─" + colors.FAIL + "⮞" + colors.WARNING + " IP-Address : {}".format(addr))
            print("│")
            print("├─" + colors.FAIL + "⮞" + colors.WARNING + " Scan intensity : {}".format(intensity_lev))
            print("│")
            print("├─" + colors.FAIL + "⮞" + colors.WARNING + " Scan still running...")
            print("│")
            report = input("└──────⮞ Choose report ({}, q) : ".format(", ".join(scan[1])))

            if report in scan[1]:
                display_menu()
                print("├─" + colors.FAIL + "⮞" + colors.WARNING + " IP-Address : {}".format(addr))
                print("│")
                print("├─" + colors.FAIL + "⮞" + colors.WARNING + " Scan intensity : {}".format(intensity_lev))
                print("│")
                print("├─" + colors.FAIL + "⮞" + colors.WARNING + " App report : {}".format(report))
                print("│")
                file = open(f"ressources/output/{addr}-{intensity_lev}/{report}.txt", "r")

                for file_line in file.readlines():
                    print("│ " + file_line, end='')
                file.close()
                print("│")
                quit = input("└──────⮞ Press (q) to quit : ")
                continue
            elif report == 'q':
                print("")
                print(colors.FAIL + "💀" + colors.WARNING + " Closing Kharon... Bye !")
                report_asking = False
            else:
                continue
        elif len(scan[1]) == 3:
            break
        time.sleep(1)

    while report_asking:
        display_menu()
        print("├─" + colors.FAIL + "⮞" + colors.WARNING + " IP-Address : {}".format(addr))
        print("│")
        print("├─" + colors.FAIL + "⮞" + colors.WARNING + " Scan intensity : {}".format(intensity_lev))
        print("│")
        report = input("└──────⮞ Choose report (nmap, ffuf, nikto, q) : ")

        if report in ("nmap", "ffuf", "nikto"):
            display_menu()
            print("├─" + colors.FAIL + "⮞" + colors.WARNING + " IP-Address : {}".format(addr))
            print("│")
            print("├─" + colors.FAIL + "⮞" + colors.WARNING + " Scan intensity : {}".format(intensity_lev))
            print("│")
            print("├─" + colors.FAIL + "⮞" + colors.WARNING + " App report : {}".format(report))
            print("│")
            file = open(f"ressources/output/{addr}-{intensity_lev}/{report}.txt", "r")

            for file_line in file.readlines():
                print("│ " + file_line, end='')
            file.close()
            print("│")
            quit = input("└──────⮞ Press (q) to quit : ")
        elif report == 'q':
            print("")
            print(colors.FAIL + "💀" + colors.WARNING + " Closing Kharon... Bye !")
            report_asking = False
        else:
            continue

def display_menu():
    os.system("clear")
    print(colors.FAIL+ "💀" + colors.WARNING + " Starting Kharon...")
    print(colors.OKORANGE + get_ascii())
    print(colors.FAIL + "💀" + colors.WARNING + " Basic & automated Web-Server CTF enumeration.")
    print("┌──────────────────────────────────────────────────")
    print("│")

def do_graphic_loop(addr):
    global intensity_lev, n
    print("├─" + colors.FAIL + "⮞" + colors.WARNING + " IP-Address : {}".format(addr))
    print("│")
    print("├─" + colors.FAIL + "⮞" + colors.WARNING + " Scan intensity : {}".format(intensity_lev))
    print("│")
    if n == 1:
        print("└──────⮞ Scan Started ...")
        n += 1
    elif n == 2:
        print("└──────⮞ Scan Started #..")
        n += 1
    elif n == 3:
        print("└──────⮞ Scan Started .#.")
        n += 1
    elif n == 4:
        print("└──────⮞ Scan Started ..#")
        n = 1

    
if __name__ == "__main__":
    main()