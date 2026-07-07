def classify_risk(price,brent,usd):
    if price>=26000 or brent>=95 or usd>=26000:return "RỦI RO CAO","red","Rà soát giá cước, phụ phí nhiên liệu và kế hoạch mua nhiên liệu."
    if price>=23000 or brent>=85 or usd>=25500:return "RỦI RO TRUNG BÌNH","yellow","Theo dõi Brent và USD/VND; chuẩn bị kịch bản tăng chi phí."
    return "RỦI RO THẤP","green","Biến động tương đối ổn định; tiếp tục theo dõi định kỳ."
