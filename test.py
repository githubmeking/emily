b = """Her ağlayan güçsüz değildir. Tıpkı her gülenin mutlu olmadığı gibi.

Silgi kullanmadan resim çizme sanatına hayat diyoruz

Her şeyi yapabilirsin! Sadece kalk ve yap!

Üç şeyini bozma; Karakterini, kalbini, vicdanını...

Sözünü tartmadan söyleyen, aldığı cevaptan incinmesin. Mevlana

Güven bir ayna gibidir. Bir kez çatladı mı, hep çizik gösterir.

Aşağı bakarsan asla gökkuşağı bulamazsın.

İyi insan ol, fakat bunu ispatlamak için vakit harcama."

Herkes aynı geceyi yaşar ama herkesin karanlığı farklıdır..."

Senin suçun değil, ben o yolun Çıkmaz olduğunu bile bile yürüdüm."

Sevmesini bilene kahverengi gözler bile okyanus olur."

Kimseye boyun eğmedim, sana yerle bir oldum."

İyi olan, kaybetse de kazanır."

Güçlü kal, bırak nasıl üstesinden geldiğini görsünler

Düne tövbe bugüne secde yarına dua yakışır.

Bir kum tanesiyim ama çölün derdini taşıyorum

Seni gören şairler bile adına günlerce şiir yazar.

Gözlerinle baharı getirdin garip gönlüme.

Her bildiğini söyleme, her söylediğini bil

Mutluluğu tatmanın tek çaresi, onu paylaşmaktır.

Canı yanan sabretsin. Can yakan, canının yanacağı günü beklesin

Gülmek için mutlu olmayı beklemeyin belki de gülmeden ölürsünüz.

Kalbinde sevgiyi koru. Onsuz bir hayat, çiçekler öldüğü zaman güneşsiz bir bahçe gibidir.

Derdi dünya olanın, dünya kadar derdi olur.

İyiler kaybetmez ama kaybedilir

Ağırlayamayacağın misafiri yüreğine konuk etme

Elbisesi kirli olandan değil, düşüncesi kirli olandan korkacaksınız

Sakın unutma, ellerin cebindeyken başarı merdivenlerini çıkamazsın.

Ümit, mutluluktan alınmış bir miktar borçtur.

Kusursuz dost arayan dostsuz kalır

Güzeli güzel yapan edeptir, edep ise güzeli sevmeye sebeptir.

Zihin paraşüt gibidir. Açık değilse işe yaramaz

Bilgelik, herhangi bir zenginlikten daha önemlidir.

Hayat bir öyküye benzer, önemli olan yani eserin uzun olması değil, iyi olmasıdır.

Bilinmeyen yerleri bulmak için, önce kaybolmak gerekir.

Zayıf insanlar intikam alır, güçlü insanlar affeder, zeki insanlar umursamazlar.

Nereye gittiğini bilmiyorsan, hangi yoldan gittiğinin hiçbir önemi yoktur.

Öğrenmek, yaşamın tek kanıtıdır

Seni hayallerine ulaştıracak en önemli şey, cesaretindir.

Çok şükür ki gökyüzü henüz hiçbir cüzdana sığmıyor.

Az insan çok huzur

Mutluluğu sende bulan senindir ötesi misafir.

Ne kadar yaşadığımız değil, nasıl yaşadığımız önemlidir.

Hepimiz birinin hikayesinde kötüyüz

Hiç Kimse senin karanlığını aydınlatmak için yıldızlar arasından çıkıp gelmeyecek

Her şey göründüğü gibi olsaydı eline aldığın deniz suyu mavi olurdu

Bir bulut gibisin yakın ama dokunulamaz

Düşlerimden öp beni.
Belki sen kokar yarınlarım

Herkese selam sana hasret gönderiyorum

Hayatın değerini bilin

Yaşam geriye bakarak anlaşılır, ileriye bakarak yaşanır.

En karanlık gece bile sona erer ve güneş tekrar doğar.

Umudunu kaybetme! En karanlık an şafak sökmeden önceki andır.

Hayat hesapla değil nasiple yaşanır.

İsteyen dağları aşar, istemeyen tümseği bile geçemez"""
a = []
for i in b.split("\n"):
    if i != "":
        a.append(i)
print(a)
