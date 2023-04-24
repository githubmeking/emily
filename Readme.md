.<h1 align="center" style="color: #ffffff;"> 👑 <b>Call Tone Tagger Bot</i> </b>👑</h1>

### ![Call Tone Tagger](https://telegra.ph/file/7f38e4feabad9e5b92e8f.jpg)
<br>
<h3 align="center"><b><i>Bu bot, telegram gruplarınızda sizin yerinize üyeleri etiketleyebilir!</i></b></h3>
<br>
<br>
<details>
  <summary><br> <h1> <b> 🧩 Özellikleri </b> </h1></br></summary>
   • Gruplarınızda sizin yerinize üyeleri (normal - emojili - karakterli - tekli / çoklu) etiketleyebilir, </br> 
<br> • Botunuzun bulunduğu grupların toplam sayısını, gruplarda bulunan üye sayısını, toplam erişebileceğiniz aktif üye sayısını ve daha bir çok şeyi görebilirsiniz.</br>
<br> • Kullanıcıları veya grupları botunuzun kullanımından yasaklayabilirsiniz. </br>
<br> • 'stag' ve 'itag' ile grup içerisinde eğlenebilirsiniz.</br>
<br> • Gruplara / kişilere yayın yapabilirsiniz.</br>
<br> • Daha fazla bilgi için komutlara bakın.

<br><br>
</details>

<details>
  <summary><br> <h1> <b> 🧩 Komutlar </b> </h1></br></summary>

| Komut | Açıklama |
| ------ | ------ |
| start | Botu başlatır. |
| help | Yardım menüsünü açar. |
| tag | Normal etiketleme işlemini başlatır. |
| etag | Emojili etiketleme işlemini başlatır. |
| atag | Yöneticileri etiketeme işlemini başlatır. |
| ctag | Dizi/film/oyun/anime karakterler ile etiketlemeyi başlatır. |
| stag | Verdiğiniz sticker/fotoğraf ve kullanıcı ile kullanıcıyı sticker ile birlikte gizli bir şekilde etiketler |
| itag | Verdiğiniz kullanıcı ile rastgele bir emoji ile tek seferlik etiketler. |
| ship | Gruptaki üyeleri shipler. |
| reload | Grubunuzun yönetici listesini günceller. |
| cancel | Devam eden işlemi durdurur. Eğer işlem yoksa uyarı verecektir. |
| info | Verdiğiniz kullanıcı hakkında detaylı bilgi verir. |
| list | Komutu kullandığınız gruptaki üyelerin verilerini bir dosya olarak verir. |
| ping | Botunuzun anlık pingini ölçer. |

| Sahip Komutları | Açıklama |
| ------ | ------ |
| broadcast | Botunuzun olduğu gruplara ve özel sohbetlere yayın yapar. |
| stats | Botunuzun anlık istatistiklerini verir. |
| gstats | Botunuzun olduğu gruplar hakkında detaylı veri verir. |
| block | Bir kullanıcı ya da grubu botunuzdan yasaklar. |
| unblock | Bir kullanıcı ya da grubu botunuzdaki yasağını kaldırır. |
| bloacklist | Botunuzda ki toplam yasaklı kullanıcılar hakkında bilgi verir. |
|  |  |

<br><br>
</details>


<details>
  <summary><b><br> <h1> <b> 📍 Gereksinimler  </b> </h1></b></summary><br>
  <details>
    <br><summary><br> ♻️ DATABASE_URL </br></summary>
    <p align="left">
    Veritabanı olarak MongoDB kullanıldığı için MongoDB url almanız gerekmektedir. Nasıl alınacağını bilmiyorsanız, <a href="https://t.me/LuciTools/12">burayı</a> kontrol edebilir ya da <a href="https://t.me/repohanex">destek grubuna</a> gelerek yardım alabilirsiniz.</br>
    </details><br>

  <details><summary><br> ♻️ BOT_NAME </br></summary> <br>
    <p align="left">
    Botunuzun kendini tanıtmasını istediğiniz adı.
    </details><br>

  <details><summary><br> ♻️ DURATION </br></summary> <br>
    <p align="left">
    Her bir etiket sonrasında yeni etiketleme mesajı arasındaki süre. Varsayılan olarak 3 saniyedir.
    </details><br>

  <details><summary><br> ♻️ API_HASH & API_ID </br></summary> <br>
    <p align="left">
    <a href="https://my.telegram.org">my.telegram.org</a>'dan oluşturduğunuz uygulamanın değerleri.
    </details><br>

  <details><summary><br> ♻️ COUNT </br></summary> <br>
    <p align="left">
    Her mesajda etiketlenecek üye sayısı. Varsayılan olarak 6 hesap etiketler.
    </details><br>

  <details><summary><br> ♻️ BOT_USERNAME </br></summary> <br>
    <p align="left">
    <a href="https://t.me/botfather">@BotFather</a>'dan oluşturduğunuz botun kullanıcı adı.
    </details><br>

  <details><summary><br> ♻️ LOG_CHANNEL</br></summary>
    <p align="left">
    <br> Botun eylemleri kaydedeceği grub'un kimliği. Kimliği elde etmek için, bir grup oluşturun ve <a href="https://t.me/missrose_bot">@MissRose_bot</a>'u gruba ekleyin ve <code>/id</code> yazın.</br>
    </details><br>

  <details><summary><br> ♻️ GROUP_SUPPORT</br></summary> 
    <p align="left">
    <br>Kullanıcıların herhangi bir şey önermesi, herhangi bir hatayı bildirmesi için bir grup kimliği yazın. Eğer ayarlanmazsa, bot sahibine yönlendirir.</br>
    </details><br>

  <details><summary><br>♻️ ADMIN</br></summary>
    <p align="left">
    <br>Botunuzun gruplarda admin olmadan çalışmasını istemiyorsanız bu değeri 'True' yapın. Aksi takdirde admin olmadan çalışmasını istemiyorsanız 'False' yapın.</br>
   </details><br>

  <details><summary><br>♻️ COMMAND</br></summary>
    <p align="left">
    <br>Botunuzun komutlarını çalıştırabilmek için komut girdisi. Örnek: '/start'. Varsayılan olarak '/' işaretidir.</br>
   </details><br>

  <details><summary><br>♻️ OWNER_ID</br></summary>
    <p align="left">
    <br>Botun sahibinin id'si</br>
   </details><br>

<details><summary><br>♻️ LANGUAGE</br></summary>
    <p align="left">
    <br>Dört dil mevcuttur, Türkçe, Azerbaycanca, Rusça ve İngilizce. Eğer herhangi bir dil ayarlanmazsa otomatik olarak Türkçe dili kullanılır.</br>
   </details><br>

<details><summary><br>♻️ BROADCAST_AS_COPY</br></summary>
    <p align="left">
    <br>Gönderilen mesajın ne şekilde gönderileceğini ayarlamak içindir. <code>False</code> olarak ayarlarsanız iletir, <code>True</code> olarak ayarlarsanız kopyasını gönderir.</br>
   </details><br>
   </details>


<details>
  <summary><b><br> <h1> <b> Kurulum </b> </h1></b></summary><br>

<br>
<details><summary>
<h1 align="center"> <b>🚀 Heroku'ya deploy - Deploy to Heroku </b></h1></summary>
<p align="center"> <a href="https://heroku.com/deploy?template=https://github.com/Yusuf6521/emilytag"> 
<img src="https://www.herokucdn.com/deploy/button.svg" width="500"></a>

</details>
<br>
<br>
<details><summary>
<h1 align="center"> <b>🚀 Railway'e deploy - Deploy to Railway </b></h1></summary>

<p align="center"> <a href="https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Faylak-github%2FCallTone&envs=API_ID%2CAPI_HASH%2CBOT_TOKEN%2CBOT_USERNAME%2COWNER_ID&API_IDDesc=Bu+de%C4%9Feri+my.telegram.org%27dan+al%C4%B1n.&API_HASHDesc=Bu+de%C4%9Feri+my.telegram.org%27dan+al%C4%B1n.&BOT_TOKENDesc=%40BotFather%27dan+olu%C5%9Fturdu%C4%9Funuz+botun+bot+token+de%C4%9Feri.&BOT_USERNAMEDesc=%40BotFather%27dan+olu%C5%9Fturdu%C4%9Funuz+botun+kullan%C4%B1c%C4%B1+ad%C4%B1.&OWNER_IDDesc=Sizin+Telegram+hesab%C4%B1n%C4%B1z%C4%B1n+ID%27si.&referralCode=aylak">
<img src="https://railway.app/button.svg" width="500">
</a>

</details>
</details>
<br>



<br>


### **🪐 Lisans - Licence :**

📅 ***2022 (c) [GNU Affero General Public License v3.0](https://github.com/aylak-github/CallTone/blob/master/LICENSE)***

<br>
<br>

### **📡 İletişim - Communication :**
[![Github](https://img.shields.io/badge/Github-525252?style=for-the-badge&logo=github)](https://github.com/aylak-github) [![Opensource](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/G4rip)

<br>
<br>

### **🎯 Teşekkürler - Credits**

- _[Dan](https://github.com/delivrance) for [Pyrogram](https://github.com/pyrogram/pyrogram)_
- _[Fragment](https://t.me/FR46M3N7) for Azerbaijani translation_
- _[Abdurəhman](https://t.me/abdurehmanofff)  for English translation_
