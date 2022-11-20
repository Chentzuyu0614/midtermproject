# 購物車

## DB Schema
```
商品{
    id,         # 編號
    name,       # 名稱
    price,      # 價格
    amount      # 數量
}
```

## 系統架構
* 購物頁面
    * 加入購物車
        * 商品庫存減少
    * 移出購物車
        * 商品庫存增加
    *管理庫存
        * 管理者身分認證
            * 上架商品
            * 下架商品
