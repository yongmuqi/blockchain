import os
import time

from eth_account import Account
from pywebio.input import input, FLOAT, TEXT, radio
from pywebio.output import put_text, put_html
from web3 import Web3, HTTPProvider

import usdt_abi

"""
    使用方法：
    # 转账其他代币时，需要输入代币的合约地址
    1、修改27行网络，输入钱包密钥
    2、修改29行，填入你要转账的网络
    2、修改72行，修改链路ID（'chainId': 5 ）
    3、修改95行，修改区块链浏览器（https://goerli.etherscan.io/tx/）改成对应的浏览器
"""

ethereum = "https://eth.llamarpc.com"
optimism = "https://optimism-mainnet.public.blastapi.io"
arbitrum = "https://arb-mainnet.g.alchemy.com/v2/n4lfes1HN70o5pZojZYZm_KIGXWFkCSb"
polygon = "https://polygon-bor.publicnode.com"
bsc = "https://bscrpc.com"
goerli = "https://eth-goerli.g.alchemy.com/v2/LhJLf40dSUOO24uW5Ei_UXrn5dCPVP3A"
scroll = "https://alpha-rpc.scroll.io/l2"
zkSync = "https://mainnet.era.zksync.io"

private_key = '87d5afba6db019c057282b26d68674dc742a3e6bc6f856351cc55cdf79be6534'
w3 = Web3(HTTPProvider(goerli))  # 连接网络,选择上面的网络，或者自己添加rpc
erc20token_contract = None
print('web3版本：%s' % w3.api)
print(w3.is_connected())
acc = Account.from_key(private_key=private_key)
fromAddress = Web3.to_checksum_address(acc.address)
put_text('钱包地址:' + fromAddress)
try:
    put_text('主网币余额:' + str(Web3.from_wei(w3.eth.get_balance(acc.address), 'ether')))
except Exception as e:
    put_text('查询到余额' + str(e))

toAddress = input("转账目的地址：""*多个地址用单个空格分开""*或者每行一列的排序从记事本复制出来", type=TEXT)
transfer_type = radio('转账类型', options=['主网币', '其他代币'])
toAddress_list = [addr.strip() for addr in toAddress.split(' ') if addr.strip() != '']
toAddress_confrim = str(toAddress_list)
trans_value = input("数量：（如：0.0001）\r*交易所充币有最低额度", type=FLOAT)
put_text('转账地址:' + toAddress_confrim)
put_text('转账数量:' + str(trans_value))
put_text('转账类型:' + transfer_type)
confrim = input('请确认以上参数,输入ok', type=TEXT)
if confrim == 'ok':
    no = 1
    for toAddress in toAddress_list:
        if not toAddress:
            continue
        toAddress = Web3.to_checksum_address(toAddress)
        nonce = w3.eth.get_transaction_count(fromAddress)
        gasPrice = w3.eth.gas_price
        trans_value = float(trans_value)  # 以太坊数量
        value = Web3.to_wei(trans_value, 'ether')
        if transfer_type == '主网币':
            gas = w3.eth.estimate_gas({'from': fromAddress, 'to': toAddress, 'value': value})
            trans_eth = {
                'to': toAddress,
                'from': fromAddress,
                'value': value,
                'gasPrice': gasPrice,
                'gas': gas,
                'data': '',
                'nonce': nonce,
                'chainId': 5  # 对应链ID
            }
            txn_signed = w3.eth.account.sign_transaction(trans_eth, private_key)
            txn_hash = w3.eth.send_raw_transaction(txn_signed.rawTransaction)
        if transfer_type == '其他代币':
            if erc20token_contract is None:
                erc20token_contract = input("输入代币合约", type=TEXT)
            erc20token_contract = Web3.to_checksum_address(erc20token_contract)
            erc20_contract_abi = w3.eth.contract(address=erc20token_contract, abi=usdt_abi.usdtabi)
            trans_value_erc20 = trans_value * 10 ** erc20_contract_abi.functions.decimals().call()
            gas = erc20_contract_abi.functions.transfer(toAddress, int(trans_value_erc20)).estimate_gas(
                {'from': fromAddress})
            transaction_contract_erc20 = erc20_contract_abi.functions.transfer(toAddress,
                                                                               int(trans_value_erc20)).build_transaction(
                {'gasPrice': gasPrice, 'gas': gas, 'nonce': nonce})
            txn_signed_erc20 = w3.eth.account.sign_transaction(transaction_contract_erc20, private_key)  # erc20代币
            txn_hash = w3.eth.send_raw_transaction(txn_signed_erc20.rawTransaction)

        put_text(
            '-----------------------------------当前第%s笔%s转账----------------------------------' % (no, transfer_type))
        no += 1
        put_text('转账hash：' + Web3.to_hex(txn_hash))
        put_html(
            '<a target="view_window" href=\"https://goerli.etherscan.io/tx/' + Web3.to_hex(txn_hash) + '\">查看转账信息</a>')
        if transfer_type == '主网币':
            put_text(trans_eth)
            put_text('主网币转账数量：{:.10f} (小数点后保留10位)'.format(trans_value))
        elif transfer_type == '其他代币':
            put_text(erc20_contract_abi.functions.name().call() + '转账数量：' + str(
                trans_value) + erc20_contract_abi.functions.name().call())
        time.sleep(6.5)  # 避免nonce错误
    put_text('转账完毕！')
else:
    put_text('转账取消')
