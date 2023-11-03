import json

def read_listings_from_file(filename):
    with open(filename, 'r') as f:
        all_listings = json.load(f)
    return all_listings

def main():
    listings = read_listings_from_file('auctionListings.json')
    prompt = f'''
    /~~~/*/ Welcome to TheAuctionHouse! /*/~~~/\n
     {len(listings)} Unique Items Available!\n
    Search By Entering An Item Name!\n
    '''

if __name__ == "__main__":
    main()
