def deneme():
  a = 5
  print(a)
  deger = "buyuk" if a > 5 else "kucuk"
  print(deger)
  dizi = [ "breaking bad", "dexter", "dark", "oa", "ozark", "arka sokaklar"]
  subDizi = dizi[1:-2]
  print(subDizi)
  i = 0
  for myDizi in dizi:
    if i % 2 == 0:
      print(myDizi)
    i += 1
  print("*********************")
  for j in range(1,5):
    print(dizi[j])
  print("*********************")
  for k in range(0, len(dizi), 2):
    print(dizi[k])

deneme()