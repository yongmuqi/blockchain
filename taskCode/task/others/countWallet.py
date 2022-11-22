from eth_account import Account

if __name__ == '__main__':
    # 创建钱包，address:钱包地址  key：钱包私钥
    # account = Account.create()
    # print(account.address)
    # print(account.key.hex())
    i = 0
    while i in range(20):
        i = i + 1
        # 创建助记词必须先开始功能
        Account.enable_unaudited_hdwallet_features()
        # 创建钱包，address:钱包地址   mnemonic：钱包助记词
        account, mnemonic = Account.create_with_mnemonic()
        print('地址：' + account.address, '私钥：' + account.key.hex(), '助记词:' + mnemonic)
