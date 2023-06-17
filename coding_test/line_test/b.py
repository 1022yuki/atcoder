class Item:
    def __init__(self, item_id, seller_id, minimum_price, BIN_price, end_time):
        self.item_id = item_id
        self.seller_id = seller_id
        self.minimum_price = minimum_price
        self.BIN_price = BIN_price
        self.end_time = end_time
        self.bid_history = [{'price': minimum_price, 'bidder_id': None}]  # 初期入札価格を設定

    def add_bid(self, new_bid_price, bidder_id):
        # print(new_bid_price, self.get_now_price())
        if new_bid_price > self.get_now_price():  # 新しい入札価格が現在の価格より高い場合のみ追加
            # print('add!!!!!!!!')
            self.bid_history.append({'price': new_bid_price, 'bidder_id': bidder_id})
            # print(self.bid_history)

    def cancel_bid(self, bidder_id):
        self.bid_history = [bid for bid in self.bid_history if bid['bidder_id'] != bidder_id]
        if not self.bid_history:  # 入札がすべて取り消された場合は、最低入札価格を再設定
            self.bid_history.append({'price': self.minimum_price, 'bidder_id': None})

    def get_now_price(self):
        # print(self.bid_history)
        return self.bid_history[-1]['price']

    def get_now_bidder_ID(self):
        return self.bid_history[-1]['bidder_id']
    
    def flag_end(self, time_now):
        return self.end_time < time_now


from collections import defaultdict

# 生成済みのインスタンス名を管理する集合
used_id = set()
# インスタンスを管理する辞書
items = defaultdict(int)

try:
  while True:
      # 入力が終了したことの判定
      
      # 入力を受け取る
      inp =  list(map(str, input().split()))

      request_time = inp[0]

      # 入力の時間を見て終了するオークションを出力
      # for item in items.values():
      #     if item!=0 and item.flag_end(inp[0]):
      #         print(f"AUCTION_FINISHED: {item.end_time} {item.item_id} {item.get_now_price()} {item.BIN_price} {item.get_now_bidder_ID()}")
      #         del items[item.item_id]

      if inp[1] == 'SELL':
          # request_time = inp[0]
          user_id = inp[2]
          item_id = inp[3]
          minimum_price = int(inp[4])
          if inp[5] == '-':
            BIN_price = inp[5]
          else:
            BIN_price = int(inp[5])
          end_time = inp[6]

          if item_id in used_id:
              print('SELL: this item_id is already in use')
              continue
          else:
              # インスタンスを生成
              items[item_id] = Item(item_id, user_id, minimum_price, BIN_price, end_time)
              used_id.add(item_id)
              print('SELL: accepted')
      
      if inp[1] == 'SELL_CANCEL':
          # request_time = inp[0]
          user_id = inp[2]
          item_id = inp[3]

          if items[item_id]==0:
            #  delした後にちゃんと初期値の0になってるかわからない
              print('SELL_CANCEL: this item is currently not for sale')
              continue
          if items[item_id].seller_id != user_id:
              print('SELL_CANCEL: user is not the seller of this item')
              continue
          # インスタンスを削除
          del items[item_id]
          print('SELL_CANCEL: accepted')

      if inp[1] == 'BID':
          # request_time = inp[0]
          user_id = inp[2]
          item_id = inp[3]
          price = int(inp[4])
          
          if items[item_id]==0:
              print('BID: this item is currently not for sale')
              continue
          if items[item_id].seller_id == user_id:
              print('BID: user is the seller of this item')
              continue
          if price < items[item_id].minimum_price:
              print('BID: the bid is lower than the minimum price')
              continue
          if items[item_id].BIN_price!='-' and price > items[item_id].BIN_price:
              print('BID: the bid is higher than the BIN price')
              continue
          if price < items[item_id].get_now_price():
              print("BID: the price must higher than the user's previous highest bid")
              continue
          items[item_id].add_bid(price, user_id)
          now_price = items[item_id].get_now_price()
          BIN_price = items[item_id].BIN_price
          highest_bidder = items[item_id].get_now_bidder_ID()
          print(f"BID: {now_price} {BIN_price} {highest_bidder}")

          # 最高金額で入札されオークション終了だった場合
          if BIN_price!='-' and BIN_price==now_price:
              print(f"AUCTION_FINISHED: {request_time} {item_id} {now_price} {BIN_price} {highest_bidder}")
              del items[item_id]


      if inp[1] == 'BID_CANCEL':
          # request_time = inp[0]
          user_id = inp[2]
          item_id = inp[3]

          if items[item_id]==0:
              print('BID_CANCEL: this item is currently not for sale')
              continue
          # その商品に入札していない場合flagを立てる
          flag = True
          for bid in items[item_id].bid_history:
              if bid['bidder_id'] == user_id:
                  flag = False
          if flag:
              print('BID_CANCEL: user has not bid on the item')
              continue
          items[item_id].cancel_bid(user_id)
          if len(items[item_id].bid_history) == 1:
              current_price = '-'
              highest_bidder = '-'
              print(f'BID_CANCEL: {current_price} {items[item_id].BIN_price} {highest_bidder}')
          else:
              print(f'BID_CANCEL: {items[item_id].get_now_pricee()} {items[item_id].BIN_price} {items[item_id].get_now_bidder_ID()}')

except EOFError:
  pass