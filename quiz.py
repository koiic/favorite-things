from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABc-Axc_HWzu_nB7rwGBEAcd5CnpocrFW6PFxDv14WgtoGzOCDfTEB6W5lES5VonD56X4M1C63TFGkQR5aj0rzCRs0G0XL2iq8J-V7gisKcOa_gwtz8EuAYXSvTpw6dB0Uxul1S56Crbjo0zTlFcaUKuAMXOq4wgAClgji_SjIuauzaFo4='

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
