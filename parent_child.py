# 複利計算器

# 輸入初始金額、年利率和投資期限
principal = float(input("請輸入初始金額："))
annual_interest_rate = float(input("請輸入年利率（以小數形式，例如0.05代表5%）："))
years = int(input("請輸入投資期限（年數）："))

# 計算複利
final_amount = principal * (1 + annual_interest_rate)**years

# 輸出結果
print(f"{years} 年後，您的投資將增長為 {final_amount:.2f} 元。")
