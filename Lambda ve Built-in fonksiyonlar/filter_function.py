#ALIŞTIRMA 1
sayilar = [-5,4,-9,10,-6,8]

pozitif = list(filter(lambda x : x>0,sayilar))
cift = list(filter(lambda x : x%2==0,sayilar))

print(cift)
print(pozitif)

#ALIŞTIRMA 2

isimler = ["ali","ayşe","ibrahim","melisa"]

basharfi_i_veya_m = list(filter(lambda n : n[0]=="i" or n[0]=="m",isimler))
basharfi_i_veya_m_buyuk_harf = list(map(str.upper,basharfi_i_veya_m))

print(basharfi_i_veya_m_buyuk_harf)

#ALIŞTIRMA 3
users = [{"username" : "ibrahim", "posts": ["post1","post2","post3"]},
         {"username" : "melisa", "posts": ["post1"]},
         {"username" : "ahmet", "posts": ["post1","post2"]}
         ]

post_sayisi_birden_fazla = list(filter(lambda a : len(a["posts"])>1, users))
post_sayisi_birden_fazla_usernames = list (map(lambda a : a["username"],post_sayisi_birden_fazla))

print(post_sayisi_birden_fazla)
print(post_sayisi_birden_fazla_usernames)