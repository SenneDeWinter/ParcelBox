import de2120_barcode_scanner
import time

def scan_barcode():
    my_scanner = de2120_barcode_scanner.DE2120BarcodeScanner()


    scan_buffer = ""
    barcode = ""

    while True:
        scan_buffer = my_scanner.read_barcode()
        if scan_buffer:
            barcode = str(scan_buffer)
            print(barcode)
            scan_buffer = ""

        time.sleep(0.02)

if __name__ == '__main__':
    scan_barcode()