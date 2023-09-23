# 簡單零用錢支配試算器

# 輸入零用錢金額
allowance = float(input("請輸入您的每周零用錢金額："))

# 初始化支出比例字典
expenses = {}

# 輸入支出項目和分配比例
while True:
    expense = input("請輸入支出項目（按Enter結束）：")
    if not expense:
        break
    expense_ratio = float(input(f"請輸入 {expense} 的分配比例（小數形式，例如0.3代表30%）："))
    expenses[expense] = expense_ratio

# 初始化實際支出金額和超支列表
actual_expenses = {}
overspending = []

# 計算支出金額，並檢查是否超過分配比例
for expense, ratio in expenses.items():
    expense_amount = allowance * ratio
    actual_expense = float(input(f"請輸入實際{expense}的金額："))
    actual_expenses[expense] = actual_expense
    if actual_expense > expense_amount:
        overspend = actual_expense - expense_amount
        overspending.append((expense, ratio, overspend))

# 計算總支出金額和剩餘預算
total_expenses = sum(actual_expenses.values())
remaining_budget = allowance - total_expenses

# 顯示支出明細
print("\n支出明細：")
for expense, actual_amount in actual_expenses.items():
    print(f"{expense}: 實際支出 {actual_amount:.2f}，分配比例 {expenses[expense]:.2%}")

# 顯示超支項目
if overspending:
    print("\n超支項目：")
    for expense, ratio, overspend in overspending:
        print(
            f"{expense} 超支 {overspend:.2f}，實際支出比例 {actual_expenses[expense]/allowance:.2%}")

# 顯示未超支項目和實際支出比例，以及還差多少錢才會超支
underspending = {expense: (expenses[expense] * allowance) - actual_expenses[expense]
                 for expense in expenses if actual_expenses[expense] <= allowance * expenses[expense]}
if underspending:
    print("\n未超支項目：")
    for expense, difference in underspending.items():
        actual_ratio = actual_expenses[expense] / allowance
        print(f"{expense} 實際支出比例 {actual_ratio:.2%}，還差 {difference:.2f} 以達到分配比例")

# 顯示剩餘預算
print(f"\n剩餘預算： {remaining_budget:.2f}")
