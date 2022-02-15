import sys
from sploitus import Menu, Sploitus

s = Sploitus()


def search(verbose=False):
    search_term = ""
    while not search_term:
        search_term = input("Exploit Search > ").rstrip("")
        
    results = s.search(search_term, verbose=verbose)
    for exp in results:
        print(exp)


def generate_menu():
    m = Menu("SPLOITUS")
    m.add_item(1, "Search", "Search sploitus.com for exploits", search)
    m.add_item(2, "Download Exploit", "Download an exploit from sploitus.com", s.download_exploit)
    m.add_item(0, "Exit", "", sys.exit)
    return m


def main():
    if len(sys.argv) < 2:
        m = generate_menu()
        m.input_choice()
    else:
        verbose = False
        if '-v' in sys.argv:
            sys.argv.pop(sys.argv.index('-v'))
            verbose = True
        
        search_term = ' '.join(sys.argv[1:])
        print(f"[*] - Searching for Exploits against {search_term}")
        results = s.search(search_term, verbose=verbose)
        
        for exp in results:
            print(exp)

        print(f"[+] - {len(results)} Exploits Found!")


if __name__ == '__main__':
    main()
