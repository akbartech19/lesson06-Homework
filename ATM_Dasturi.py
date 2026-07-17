balance = 100000

while True:
    print("\n===== ATM =====")
    print("1. Pul to'ldirish")
    print("2. Pul yechish")
    print("3. Balansni ko'rish")
    print("4. Chiqish")

    tanlov = input("Tanlovni kiriting: ")

    if tanlov == "1":
        try:
            summa = int(input("To'ldiriladigan summani kiriting: "))

            if summa <= 0:
                print("Musbat summa kiriting!")
            else:
                balance += summa
                print(f"{summa} so'm hisobingizga qo'shildi.")

        except ValueError:
            print("Faqat son kiriting!")

        finally:
            print("Amal yakunlandi.")
            chek = input("Chek kerakmi? (ha/yo'q): ")

            if chek.lower() == "ha":
                print("\n------ CHEK ------")
                print("Amal: Pul to'ldirish")
                print("Joriy balans:", balance, "so'm")
                print("------------------")

    elif tanlov == "2":
        try:
            summa = int(input("Yechiladigan summani kiriting: "))

            if summa <= 0:
                print("Musbat summa kiriting!")
            elif summa > balance:
                print("Hisobingizda mablag' yetarli emas!")
            else:
                balance -= summa
                print(f"{summa} so'm yechildi.")

        except ValueError:
            print("Faqat son kiriting!")

        finally:
            print("Amal yakunlandi.")
            chek = input("Chek kerakmi? (ha/yo'q): ")

            if chek.lower() == "ha":
                print("\n------ CHEK ------")
                print("Amal: Pul yechish")
                print("Joriy balans:", balance, "so'm")
                print("------------------")

    elif tanlov == "3":
        print(f"Joriy balans: {balance} so'm")

        chek = input("Chek kerakmi? (ha/yo'q): ")

        if chek.lower() == "ha":
            print("\n------ CHEK ------")
            print("Amal: Balansni ko'rish")
            print("Joriy balans:", balance, "so'm")
            print("------------------")

    elif tanlov == "4":
        print("ATM xizmatidan foydalanganingiz uchun rahmat!")
        break

    else:
        print("Noto'g'ri tanlov! Qaytadan urinib ko'ring.")