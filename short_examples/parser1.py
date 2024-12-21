import argparse
import urllib3
from urllib3 import util
import json
import math

LIMIT = 120
SATOSHI = 1e8


def check_balance(fi, fo):
    print("loading addresses...")
    f1 = open(fi)
    f2 = open(fo, "w")
    addresses = []
    for l in f1:
        addresses.append(l.strip())
    print("addresses loaded:", len(addresses))
    print("getting balances info...")
    f1.close()
    http = urllib3.PoolManager(timeout=util.Timeout(10))
    total = len(addresses)
    steps = math.floor(total / LIMIT)
    remind = total % LIMIT
    for step in range(steps + 1):
        url = "https://blockchain.info/balance?active="
        if step < steps:
            for a in range(LIMIT):
                url += addresses[a] + "|"
        else:
            for a in range(remind):
                url += addresses[a] + "|"
        url = url[:-1]
        res = http.request("GET", url, timeout=util.Timeout(10), retries=util.Retry(10))
        data = json.loads(res.data.decode("utf-8"))
        for address in data:
            balance = data[address]["final_balance"] / SATOSHI
            n_tx = data[address]["n_tx"]
            b = "{0:.8f} ".format(balance)
            f2.write(address + "\t\t\t" + b + "\t\t\t" + str(n_tx) + "\n")
        print("%.2f" % ((step / (steps if steps > 0 else 1)) * 100), "%")
    f2.close()
    print("complete")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("fi", nargs='?', default="/storage/0123-4567/LOST.DIR/addresses.txt", help="Input file path")
    parser.add_argument("fo", nargs='?', default="/storage/0123-4567/LOST.DIR/results.txt", help="Output file path")
    args = parser.parse_args()
    fi = args.fi
    fo = args.fo
    check_balance(fi, fo)
