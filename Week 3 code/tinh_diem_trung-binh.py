overall = float(input("Nhập Điểm Toán: ")) + float(input("Nhập Điểm Văn: ")) + float(input("Nhập Điểm Ngoại Ngữ: ")); multication = overall / 3
if 0 > multication < 4.0: print("trượt mẹ mày rồi")
elif multication < 6.5: print("may mắn nhé, mày đỗ rồi")
elif multication < 8.0: print("khá đấy")
elif multication <= 10: print("quá ghê gớm")
else: print(f"Sai cú pháp rồi{multication}")