def classify_risk(predicted_price, brent, usd_vnd):
    if predicted_price >= 26000 or brent >= 95 or usd_vnd >= 26000:
        return "RỦI RO CAO", "red", "Rà soát giá cước, phụ phí nhiên liệu và kế hoạch mua nhiên liệu."
    if predicted_price >= 23000 or brent >= 85 or usd_vnd >= 25500:
        return "RỦI RO TRUNG BÌNH", "yellow", "Theo dõi Brent và USD/VND; chuẩn bị kịch bản tăng chi phí."
    return "RỦI RO THẤP", "green", "Biến động tương đối ổn định; tiếp tục theo dõi định kỳ."
