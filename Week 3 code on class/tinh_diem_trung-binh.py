overall = float(input("Nhập Điểm Toán: ")) + float(input("Nhập Điểm Văn: ")) + float(input("Nhập Điểm Ngoại Ngữ: ")); multication = overall / 3
if  multication <= 4.0: print("trượt mẹ mày rồi")
elif 4 < multication < 6: print("may mắn nhé, mày đỗ rồi")
elif 6 < multication < 8: print("khá đấy")
elif 8 < multication <= 10: print("quá ghê gớm")
else: print(f"Sai cú pháp rồi{multication}")