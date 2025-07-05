
#1

from datetime import datetime
from dateutil.relativedelta import relativedelta

Tugilgan_Yil_Oy_Kun=input("Tug'ilgan yil, oy sanani kiriting (YYYY-MM-DD): " )
# print(Tugilgan_Yil_Oy_Kun)

try:
    tugilgan= datetime.strptime(Tugilgan_Yil_Oy_Kun, "%Y-%m-%d")
    bugun=datetime.today()

    umumiy_yosh=relativedelta(bugun, tugilgan)
    print(f"Sizning yoshingiz {umumiy_yosh.years} yil, {umumiy_yosh.months} oy, {umumiy_yosh.days} kun da")
except ValueError:
    print("Bu yosda odam yashamaydi")

#2
from datetime import datetime, date, timedelta

birthdate_input = input("Enter your birthdate (YYYY-MM-DD): ")

birthdate = datetime.strptime(birthdate_input, "%Y-%m-%d").date()
today = date.today()

this_year_birthday = birthdate.replace(year=today.year)

if this_year_birthday < today:
    next_birthday = birthdate.replace(year=today.year + 1)
else:
    next_birthday = this_year_birthday

days_remaining = (next_birthday - today).days

print(f"Your next birthday is in {days_remaining} day(s).")


#3
from datetime import datetime, timedelta

hozirgi_vaqt=input("Hozirgi Yil, Oy, Sana, Soat, Minutni kirit (YYYY-MM-DD HH:MM ) :")

soat=int(input("Uchrashuvga ketadigan vaqt (soat): "))
minut=int(input("Uchrashuvga ketadigan vaqt (daqiqa): "))

hozirgi_vaqt_int=datetime.strptime(hozirgi_vaqt,"%Y-%m-%d %H:%M")

ketadigan_vaqt=timedelta(hours=soat, minutes=minut)


umumiy_vaqt=hozirgi_vaqt_int+ketadigan_vaqt





print(ketadigan_vaqt)

print(hozirgi_vaqt_int)

print(umumiy_vaqt)

print(f"Marakaga ketgan vaqt {umumiy_vaqt.strftime("%Y-%m-%d %H:%M")}")



#4

from datetime import datetime
import pytz

mening_kunim=input("Kerakli Yil, Oy, Sanani, Soat, Daqiqani kiriting(YYYY-MM-DD HH:MM): ")
kerakli_zona=input("Qaysi mahalladasiz(masalan: Amerika/New_York): ")
nishondagi_zona=input("Qaysi mahalla kerak (masalan Europa/Parij)")


mening_kunim_str=datetime.strptime(mening_kunim, "%Y-%m-%d %H:%M")
zonadan=pytz.timezone(kerakli_zona)
zonaga=pytz.timezone(nishondagi_zona)

zonadan_kun=zonadan.localize(mening_kunim_str)

zonaga_zon=zonadan_kun.astimezone(zonaga)

# zonaga_zon_str=zonaga_zon.strftime("%Y-%m-%d %H:%M")
print(f"\n {kerakli_zona} bo'yicha vaqt {zonadan_kun.strftime('%Y-%m-%d %H:%M')} ")
print(f"{nishondagi_zona} bo'yicha vaqt: {zonaga_zon.strftime('%Y-%m-%d %H:%M')}")




#5
from datetime import datetime
import time

# Foydalanuvchidan kelajakdagi sana va vaqtni olish
maqsad_str = input("Kelajakdagi sana va vaqtni kiriting (YYYY-MM-DD HH:MM:SS): ")

try:
    # Matndan datetime formatiga o'tkazish
    maqsad_vaqti = datetime.strptime(maqsad_str, "%Y-%m-%d %H:%M:%S")

    print("\n⏳ Taymer ishga tushdi:\n")

    while True:
        hozir = datetime.now()
        farq = maqsad_vaqti - hozir

        # Agar taymer tugagan bo‘lsa
        if farq.total_seconds() <= 0:
            print("\n⏰ Vaqt tugadi!")
            break

        # Qolgan vaqtni kun, soat, daqiqa, soniyalarga ajratish
        kunlar = farq.days
        soat, qoldiq = divmod(farq.seconds, 3600)
        daqiqa, soniya = divmod(qoldiq, 60)

        # Terminalni yangilab chiqish
        print(f"\rQolgan vaqt: {kunlar} kun, {soat:02} soat, {daqiqa:02} daqiqa, {soniya:02} soniya", end="")

        time.sleep(1)

except ValueError:
    print("❌ Format xato. Iltimos, sana va vaqtni quyidagicha kiriting: YYYY-MM-DD HH:MM:SS")


#6
import re

# Emailni tekshiruvchi oddiy regex (regulyar ifoda)
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# Foydalanuvchidan email olish
email = input("Email manzilini kiriting: ")

# Tekshirish
if re.match(email_pattern, email):
    print("✅ Email manzili to‘g‘ri formatda.")
else:
    print("❌ Email manzili noto‘g‘ri formatda.")


#7
# Foydalanuvchidan raqam olish
phone = input("Telefon raqamini kiriting (faqat raqamlar): ")

# Faqat raqamlardan iboratligini va 10 ta raqam ekanligini tekshirish
if len(phone) == 13:
    formatted = f"({phone[:4]}) {phone[4:6]}-{phone[6:]}"
    print("Formatlangan raqam:", formatted)
else:
    print("❌ Noto‘g‘ri format! Iltimos, 10 xonali faqat raqamlardan iborat telefon raqam kiriting.")




import re

# Foydalanuvchidan telefon raqami olish
phone_input = input("Telefon raqamini kiriting (masalan: +998937269765 yoki 93 726 97 65): ")

# Faqat raqamlarni ajratib olish
digits = re.sub(r'\D', '', phone_input)

# O'zbekiston telefoni bo‘lsa (998 bilan boshlanadi)
if digits.startswith("998") and len(digits) == 12:
    operator = digits[3:5]
    part1 = digits[5:8]
    part2 = digits[8:10]
    part3 = digits[10:]
    formatted = f"+998 ({operator}) {part1}-{part2}-{part3}"
    print("Formatlangan raqam:", formatted)

# Agar faqat 9 xonali raqam bo‘lsa (mahalliy format, masalan: 937269765)
elif len(digits) == 9:
    operator = digits[:2]
    part1 = digits[2:5]
    part2 = digits[5:7]
    part3 = digits[7:]
    formatted = f"+998 ({operator}) {part1}-{part2}-{part3}"
    print("Formatlangan raqam:", formatted)

else:
    print("❌ Noto‘g‘ri format! Iltimos, 9 yoki 12 xonali raqam kiriting.")





#8
import re

# Parolni tekshiruvchi funksiya
def tekshir_parol(parol):
    uzunlik = len(parol) >= 8
    katta = re.search(r'[A-Z]', parol)
    kichik = re.search(r'[a-z]', parol)
    raqam = re.search(r'[0-9]', parol)
    
    if uzunlik and katta and kichik and raqam:
        return True
    else:
        return False

# Foydalanuvchidan parol olish
parol = input("Parolni kiriting: ")

# Tekshirish
if tekshir_parol(parol):
    print("✅ Parol kuchli!")
else:
    print("❌ Parol kuchsiz. Talablar:")
    print("- Kamida 8 ta belgi")
    print("- Kamida 1 ta katta harf (A-Z)")
    print("- Kamida 1 ta kichik harf (a-z)")
    print("- Kamida 1 ta raqam (0-9)")




#9
import re

# Foydalanuvchidan matn va izlanayotgan so‘zni olish
matn = input("Matnni kiriting: ")
soz = input("Qaysi so‘zni izlashni xohlaysiz? ")

# Regex bilan barcha mos keladigan joylarni topish (to‘liq so‘z sifatida)
mosliklar = list(re.finditer(rf'\b{re.escape(soz)}\b', matn, re.IGNORECASE))

# Natijalarni chiqarish
if mosliklar:
    print(f"\n✅ So‘z '{soz}' {len(mosliklar)} marta topildi. Joylashuvlar:")
    for i, match in enumerate(mosliklar, start=1):
        start = match.start()
        end = match.end()
        print(f"{i}) Pozitsiya: {start}-{end} → '{matn[start:end]}'")
else:
    print(f"\n❌ So‘z '{soz}' matnda topilmadi.")


10.
import re

# Sana topuvchi regexlar (bir nechta formatni qo‘llab-quvvatlaydi)
date_patterns = [
    r'\b\d{4}-\d{2}-\d{2}\b',       # YYYY-MM-DD
    r'\b\d{2}/\d{2}/\d{4}\b',       # DD/MM/YYYY
    r'\b\d{2}\.\d{2}\.\d{4}\b',     # DD.MM.YYYY
    r'\b\d{2}-\d{2}-\d{4}\b'        # DD-MM-YYYY
]

# Foydalanuvchidan matn olish
matn = input("Matnni kiriting: ")

# Barcha mos sanalarni to‘plash
found_dates = []
for pattern in date_patterns:
    found_dates.extend(re.findall(pattern, matn))

# Natijani chiqarish
if found_dates:
    print(f"\n✅ Topilgan sanalar ({len(found_dates)} ta):")
    for i, sana in enumerate(found_dates, start=1):
        print(f"{i}) {sana}")
else:
    print("\n❌ Matnda sana topilmadi.")
