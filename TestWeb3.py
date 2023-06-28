import requests

url = 'https://blockscout.scroll.io/api?module=account&action=txlistinternal&txhash={transactionHash}'

# Thay thế {transactionHash} bằng mã giao dịch cụ thể bạn muốn truy vấn

# Gửi yêu cầu GET đến API
response = requests.get(url)

# Kiểm tra mã trạng thái của phản hồi
if response.status_code == 200:
    # Dữ liệu được trả về dưới dạng JSON
    data = response.json()

    # Kiểm tra xem dữ liệu có tồn tại hay không
    if 'result' in data:
        transactions = data['result']

        # Lặp qua danh sách các giao dịch và in thông tin ra màn hình
        for transaction in transactions:
            tx_hash = transaction['hash']
            tx_value = transaction['value']

            print(f'Transaction Hash: {tx_hash}')
            print(f'Transaction Value: {tx_value}')
            print('---')
    else:
        print('No transactions found.')
else:
    print('Failed to retrieve data from the API.')
ư