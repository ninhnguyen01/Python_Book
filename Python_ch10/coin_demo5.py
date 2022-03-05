import coin

def main():
    coin1 = coin.Coin()
    coin2 = coin.Coin()
    coin3 = coin.Coin()
    print('I have three coins with these sides up:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()
    print('I am tossing all three coins...')
    print()
    coin1.toss()
    coin2.toss()
    coin3.toss()
    print('Now here are the sides that are up:')
    print(coin1.get_sideup())
    print(coin2.get_sideup())
    print(coin3.get_sideup())
    print()

if __name__ == '__main__':
    main()
