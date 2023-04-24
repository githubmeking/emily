# -*- coding: utf-8 -*-

# (c) @aylak-github (Github) | https://t.me/ayIak | @BasicBots (Telegram)

# ==============================================================================
#
# Project: CallToneBot
# Copyright (C) 2021-2022 by aylak-github@Github, < https://github.com/aylak-github >.
#
# This file is part of < https://github.com/aylak-github/CallTone > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/aylak-github/CallTone/blob/master/LICENSE >
#
# All rights reserved.
#
# ==============================================================================
#
# Proje: CallToneBot
# Telif Hakkı (C) 2021-2022 aylak-Github@Github, <https://github.com/aylak-github>.
#
# Bu dosya <https://github.com/aylak-github/CallTone> projesinin bir parçası,
# ve "GNU V3.0 Lisans Sözleşmesi" kapsamında yayınlanır.
# Lütfen bkz. < https://github.com/aylak-github/CallTone/blob/master/LICENSE >
#
# Her hakkı saklıdır.
#
# ========================================================================

import os
from asyncio import sleep
from typing import List, Tuple, Union

from pyrogram import Client, filters
from pyrogram.enums import *
from pyrogram.types import (
    CallbackQuery,
    ChatMember,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from Config import *

from ..database import delcmd_is_on
from ..languages import get_str, lan

kalpler = "❤ 🧡 💛 💚 💙 💜 🤎 🖤 🤍 ❣ 💕 💞 💓 💗 💖 💘 💝".split()

listem = [
    "Tüm mevsimleri tek güne, tüm yılları tek mevsime sığdırmaya razıyım. Ömrünün en güzel yıllarını benimle geçirmen dileğiyle iyi ki doğmuşsun sevgilim",
    "Hayatının geri kalanında tüm kötülükler senden uzak olsun. Üzüntüler sana yasak mutluluklar yanında olsun. Doğum günün kutlu olsun.",
    "Elini kalbimin üzerinde hissettiğim zaman, üzüntülerimi alıp onların yerine şimdiye kadar kimsenin başaramadığı o sıcaklığı koymayı başardığın için, hayatımda sen olduğun için çok şanslıyım. İyi ki doğdun, doğum günün kutlu olsun.",
    "Gülmek gülenin, yıldızlar gecenin, mutluluk sadece senin olsun. Tüm kötülükler senden uzak, doğum günün kutlu olsun sevgilim.",
    "Sen yaşadığım ömür, en güzel günlerimsin. Nice yaşlarını birlikte geçirmemiz dileğiyle doğum günün kutlu olsun sevgilim.",
    "Yaşanacak güzellikler gözlerindeki ışık gibi umut verici, umutların kalbin gibi temiz olsun. Umutların seni huzurla doldursun, doğum günün kutlu olsun. İyi ki varsın, iyi ki yanımdasın...",
    "Dünyada eşi benzeri olmayan bir güzellik varsa o da sensin. Kalbinden geçen ne varsa yeni yaşında seninle gelsin. İyi ki benimlesin Sevgilim. Doğum günün kutlu olsun.",
    "İyiye, güzele dair ne varsa o da kalbindedir. Hayatinin bundan sonrası kalbinin güzelliği gibi geçsin. İyi ki varsın ve iyi ki doğdun sevgilim!",
    "Sadece bugün değil, seninle geçen her gün çok değerli. Hayatımın parçası olduğun için çok mutluyum. İyi ki doğdun!",
    "Bugün gökyüzü daha berrak, denizler daha sakin, güneş bir başka neşeli...Bugün senin günün. Ömrüme ömür diye kattığım aşkım doğum günün kutlu olsun.",
]


caractres = [
    "Ben10 ",
    "Caillou ",
    "Küçük Kamyon Leo",
    "Tsubasa",
    "Atom Karınca",
    "Öcük",
    "Böcük",
    "Arı Maya",
    "Gwen Tennyson",
    "Garfield",
    "Casper",
    "Barbie",
    "Kevin Levin",
    "Şeker Kız Candy",
    "Vilgax",
    "Dr.Animo",
    "Blum",
    "Aisha",
    "Stella",
    "Layla",
    "Roxy",
    "Pepee",
    "Rosie",
    "Arthur",
    "Drago",
    "Dan Kuso",
    "Bugs Bunny",
    "LadyBug",
    "Mickey Mouse",
    "Şila",
    "Süngerbob",
    "Daffy Duck",
    "Domuz Porky",
    "Pembe Panter",
    "Tom",
    "Jerry",
    "Zulu",
    "Ralph",
    "Superman",
    "Batman",
    "Spiderman",
    "Sonic",
    "Müfettiş Gadget",
    "Red Kit",
    "Homer Simpson",
    "Şirin kız",
    "Gargamel",
    "Güçlü şirin",
    "Şirin baba",
    "Johnny Bravo",
    "Samuray Jack",
    "Milo",
    "Niloya",
    "Snoopy",
    "Minyon",
    "Tweety",
    "Pikachu",
    "Jake",
    "Sikpper",
    "Kowalski",
    "Rico",
    "Alex",
    "Melman",
    "Marty",
    "Gloria",
    "Dave ",
    "Eva",
    "McQueen",
    "Mater",
    "Harris",
    "Hamis",
    "Hubert",
    "Shrek",
    "Baymax",
    "Tadashi Hamada",
    "Abigail",
    "Desk Segeant",
    "Wasabi",
    "Hiro Hamada",
    "Aladdin",
    "Aladdin'in cini",
    "Moana",
    "Rapunzel",
    "Külkedisi",
    "Jasmine",
    "Tazmanya Canavarı",
    "Pocahontas",
    "Merida",
    "Keloğlan",
    "Sivri",
    "Kara Vezir",
    "Cadı",
    "Uzun",
    "Huysuz",
    "Bilgecan Dede",
    "Malefiz",
    "Bambi",
    "Pluto",
    "Harley",
    "Quinn",
    "Buzz Lightyear",
    "Doc Hudson",
    "Sally",
    "Chick Hicks",
    "Ramone",
    "Mack",
    "Guido",
    "Flo",
    "Sid",
    "Woody",
    "Slinky Dog",
    "Davis",
    "Temel Reis",
    "Voltran",
    "Kabasakal",
    "Safinaz",
    "Pooky",
    "Odie",
    "Jhon",
    "Scooby",
    "Shaggy",
    "Fred",
    "Velma",
    "Daphne",
    "George",
    "Sylvester",
    "Dr. Robotnik",
    "Marsupilami",
    "Afacan Dennis",
    "Düldül",
    "Küçük dalton kardeş",
    "Ortancıl dalton kardeş",
    "Büyük dalton kardeş",
    "Heidi",
    "Ateş Kol",
    "Elmas Kafa",
    "Dört Kol",
    "Gölge Hayalet",
    "Gri Madde",
    "Güncelleme",
    "Şimşek Hız",
    "Yaban Köpek",
    "Pul Kanat",
    "Yüzen Çene",
    "Leonardo",
    "Raphael",
    "Michelangelo",
    "Donatello",
    "Suzie ",
    "Carl",
    "Roadrunner",
    "Coyote",
    "Winny",
    "Christopher Robin",
    "Baykuş",
    "Küçük Kanguru Roo",
    "Gözlüklü Şirin",
    "Usta Şirin",
    "Süslü Şirin\xa0",
    "Wilma",
    "Dino",
    "Çakıl",
    "Beti",
    "Lucky",
    "Rolly",
    "Spot",
    "Ayı Yogi",
    "He-man",
    "TenTen",
    "Andy Larkin",
    "Charlie Brown",
    "Kai Hiwatari",
    "Roberto Hongo",
    "Misaki",
    "Optimus Prime",
    "Müfettiş Clouseau",
    "Bumblebee",
    "Megatron",
    "Bender",
    "Elma",
    "Soğan",
    "Nane",
    "Limon",
    "Felix",
    "Cosmo",
    "Wanda",
    "Stan",
    "Dipper",
    "Popeye",
    "Phineas",
    "Ferb",
    "Pinky",
    "Harley Quinn",
    "Mordecai",
    "Rigby",
    "Rick",
    "Morty",
    "Dr. Doofenshmirtz",
    "Blossom",
    "Bubbles",
    "Buttercup",
    "Horseman",
    "Steven Universe",
    "Zuko",
]

emojiler = "💋 💘 💝 💖 💗 💓 💞 💕 💌 ❣️ 💔 ❤️ 🧡 💛 💚 💙 💜 🖤 💟 💍 💎 💐 💒 🌸 💮 🏵️ 🌹 🥀 🌺 🌻 🌼 🌷 🌱 🌲 🌳 🌴 🌵 🌾 🌿 ☘️ 🍀 🍁 🍂 🍃 🍄 🥭 🍇 🍈 🍉 🍊 🍋 🍌 🍍 🍎 🍏 🍐 🍑 🍒 🥬 🍓 🥝 🍅 🥥 🥑 🍆 🥔 🥕 🌽 🌶️ 🥯 🥒 🥦 🥜 🌰 🍞 🥐 🥖 🥨 🥞 🧀 🍖 🍗 🥩 🥓 🍔 🍟 🍕 🌭 🥪 🌮 🌯 🥙 🥚 🧂 🍳 🥘 🍲 🥣 🥗 🍿 🥫 🍱 🍘 🍙 🍚 🍛 🍜 🥮 🍝 🍠 🍢 🍣 🍤 🍥 🍡 🥟 🥠 🥡 🍦 🍧 🍨 🍩 🍪 🧁 🎂 🍰 🥧 🍫 🍬 🍭 🍮 🍯 🍼 🥛 ☕️ 🍵 🍶 🍾 🍷 🍸 🍹 🍺 🍻 🥂 🥃 🥤 🥢 🍽️ 🍴 🥄 🏺 🙈 🙉 🦝 🐵 🐒 🦍 🐶 🐕 🐩 🐺 🦊 🐱 🐈 🦁 🐯 🐅 🐆 🐴 🐎 🦄 🦓 🦌 🐮 🦙 🐂 🐃 🐄 🐷 🦛 🐖 🐗 🐽 🐏 🐑 🐐 🐪 🐫 🦒 🐘 🦏 🐭 🐁 🐀 🦘 🐹 🦡 🐰 🐇 🐿️ 🦔 🦇 🐻 🐨 🐼 🐾 🦃 🐔 🦢 🐓 🐣 🐤 🦚 🐥 🐦 🦜 🐧 🕊️ 🦅 🦆 🦉 🐸 🐊 🐢 🦎 🐍 🐲 🐉 🦕 🦖 🐳 🐋 🐬 🐟 🐠 🐡 🦈 🐙 🐚 🦀 🦟 🦐 🦑 🦠 🐌 🦋 🐛 🐜 🐝 🐞 🦗 🕷️ 🕸️ 🦂 🦞 👓 🕶️ 👔 👕 👖 🧣 🧤 🧥 🧦 👗 👘 👙 👚 👛 👜 👝 🛍️ 🎒 👞 👟 👠 👡 👢 👑 👒 🎩 🎓 🧢 ⛑️ 📿 💄 🌂 ☂️ 🎽 🥽 🥼 🥾 🥿 🧺 🚂 🚃 🚄 🚅 🚆 🚇 🚈 🚉 🚊 🚝 🚞 🚋 🚌 🚍 🚎 🚐 🚑 🚒 🚓 🚔 🚕 🚖 🚗 🚘 🚙 🚚 🚛 🚜 🚲 🛴 🛵 🚏 🛣️ 🛤️ ⛵️ 🛶 🚤 🛳️ ⛴️ 🛥️ 🚢 ✈️ 🛩️ 🛫 🛬 🚁 🚟 🚠 🚡 🛰️ 🚀 🛸 🌍 🌎 🌏 🌐 🗺️ 🗾 🏔️ ⛰️ 🗻 🏕️ 🏖️ 🏜️ 🏝️ 🏞️ 🏟️ 🏛️ 🏗️ 🏘️ 🏚️ 🏠 🏡 🏢 🏣 🏤 🏥 🏦 🏨 🏩 🏪 🏫 🏬 🏭 🏯 🏰 🗼 🗽 ⛪️ 🕌 🕍 ⛩️ 🕋 ⛲️ ⛺️ 🏙️ 🎠 🎡 🎢 🎪 ⛳️ 🗿 💦 🌋 🌁 🌃 🌄 🌅 🌆 🌇 🌉 🌌 🌑 🌒 🌓 🌔 🌕 🌖 🌗 🌘 🌙 🌚 🌛 🌜 🌡️ ☀️ 🌝 🌞 🌟 🌠 ☁️ ⛅️ ⛈️ 🌤️ 🌥️ 🌦️ 🌧️ 🌨️ 🌩️ 🌪️ 🌫️ 🌬️ 🌀 🌈 ☔️ ❄️ ☃️ ⛄️ ☄️ 💧 🌊 🎑 👁️‍🗨️ 💤 💥 💨 💫 💬 🗨️ 🗯️ 💭 🕳️ 🚨 🛑 ⭐️ 🎃 🎄 ✨ 🎈 🎉 🎊 🎋 🎍 🎎 🎏 🎐 🎀 🎁 🃏 🀄️ 🦷 🦴 🛀 👣 💣 🔪 🧱 🛢️ ⛽️ 🛹 🚥 🚦 🚧 🛎️ 🧳 ⛱️ 🔥 🧨 🎗️ 🎟️ 🎫 🧧 🔮 🎲 🎴 🎭 🖼️ 🎨 🎤 🔍 🔎 🕯️ 💡 🔦 🏮 📜 🧮 🔑 🗝️ 🔨 ⛏️ ⚒️ 🛠️ 🗡️ ⚔️ 🔫 🏹 🛡️ 🔧 🔩 ⚙️ 🗜️ ⚖️ ⛓️ ⚗️ 🔬 🔭 📡 💉 💊 🚪 🛏️ 🛋️ 🚽 🚿 🛁 🛒 🚬 ⚰️ ⚱️ 🧰 🧲 🧪 🧴 🧷 🧹 🧻 🧼 🧽 🧯 💠 ♟️ ⌛️ ⏳ ⚡️ 🎆 🎇".split(
    " "
)
bayraklar = (
    "🇿🇼 🇿🇲 🇿🇦 🇾🇹 🇾🇪 🇽🇰 🇼🇸 🇼🇫 🏴󠁧󠁢󠁷󠁬󠁳󠁿 🇻🇺 🇻🇳 🇻🇮 🇻🇬 🇻🇪 🇻🇨 🇻🇦 🇺🇿 🇺🇾 🇺🇸 🇺🇳 🇺🇬 🇺🇦 🇹🇿 🇹🇼 🇹🇻 🇹🇹 🇹🇷 🇹🇴 🇹🇳 🇹🇲 🇹🇱 🇹🇰 🇹🇭 🇹🇫 🇹🇨 🇹🇦 🇸🇿 🇸🇾 🇸🇽 "
    "🇸🇻 🇸🇸 🇸🇴 🇸🇲 🇸🇱 🇸🇰 🇸🇮 🇸🇭 🇸🇬 🇸🇪 🇸🇩 🏴󠁧󠁢󠁳󠁣󠁴󠁿 🇸🇦 🇷🇼 🇷🇺 🇷🇸 🇷🇴 🇷🇪 🇶🇦 🇵🇾 🇵🇼 🇵🇹 🇵🇸 🇵🇷 🇵🇳 🇵🇲 🇵🇱 🇵🇰 🇵🇭 🇵🇫 🇵🇪 "
    "🇵🇦 🇴🇲 🇳🇿 🇳🇷 🇳🇵 🇳🇴 🇳🇱 🇳🇮 🇳🇬 🇳🇫 🇳🇪 🇳🇨 🇳🇦 🇲🇾 🇲🇽 🇲🇼 🇲🇻 🇲🇹 🇲🇷 🇲🇶 🇲🇵 🇲🇴 🇲🇳 🇲🇰 🇲🇭 🇲🇬 🇲🇪 🇲🇩 🇲🇨 🇲🇦 🇱🇾 🇱🇻 "
    "🇱🇺 🇱🇸 🇱🇷 🇱🇰 🇱🇮 🇱🇨 🇱🇧 🇱🇦 🇰🇿 🇰🇾 🇰🇼 🇰🇷 🇰🇵 🇰🇳 🇰🇲 🇰🇮 🇰🇭 🇰🇬 🇰🇪 🇯🇵 🇯🇴 🇯🇲 🇯🇪 🇮🇹 🇮🇸 🇮🇷 🇮🇶 🇮🇴 🇮🇳 🇮🇲 🇮🇱 🇮🇪 "
    "🇮🇩 🇮🇨 🇭🇺 🇭🇹 🇭🇷 🇭🇳 🇭🇰 🇬🇺 🇬🇹 🇬🇸 🇬🇷 🇬🇶 🇬🇵 🇬🇲 🇬🇱 🇬🇮 🇬🇬 🇬🇪 🇬🇧 🇬🇦 🇫🇷 🇫🇴 🇫🇲 🇫🇰 🇫🇮 🇪🇺 🇪🇸 🇪🇷 🇪🇭 🇪🇪 "
    "🏴󠁧󠁢󠁥󠁮󠁧󠁿 🇪🇨 🇩🇿 🇩🇴 🇩🇲 🇩🇰 🇩🇯 🇩🇪 🇨🇿 🇨🇾 🇨🇽 🇨🇼 🇨🇻 🇨🇺 🇨🇷 🇨🇭 🇨🇦 🇦🇿 ".split(" ")
)

renkler = " 🔴 🟠 🟡 🟢 🔵 🟣 🟤 ⚫ ⚪".split(" ")


sozler = [
    "Her ağlayan güçsüz değildir. Tıpkı her gülenin mutlu olmadığı gibi.",
    "Silgi kullanmadan resim çizme sanatına hayat diyoruz",
    "Her şeyi yapabilirsin! Sadece kalk ve yap!",
    "Üç şeyini bozma; Karakterini, kalbini, vicdanını...",
    "Sözünü tartmadan söyleyen, aldığı cevaptan incinmesin. Mevlana",
    "Güven bir ayna gibidir. Bir kez çatladı mı, hep çizik gösterir.",
    "Aşağı bakarsan asla gökkuşağı bulamazsın.",
    'İyi insan ol, fakat bunu ispatlamak için vakit harcama."',
    'Herkes aynı geceyi yaşar ama herkesin karanlığı farklıdır..."',
    'Senin suçun değil, ben o yolun Çıkmaz olduğunu bile bile yürüdüm."',
    'Sevmesini bilene kahverengi gözler bile okyanus olur."',
    'Kimseye boyun eğmedim, sana yerle bir oldum."',
    'İyi olan, kaybetse de kazanır."',
    "Güçlü kal, bırak nasıl üstesinden geldiğini görsünler",
    "Düne tövbe bugüne secde yarına dua yakışır.",
    "Bir kum tanesiyim ama çölün derdini taşıyorum",
    "Seni gören şairler bile adına günlerce şiir yazar.",
    "Gözlerinle baharı getirdin garip gönlüme.",
    "Her bildiğini söyleme, her söylediğini bil",
    "Mutluluğu tatmanın tek çaresi, onu paylaşmaktır.",
    "Canı yanan sabretsin. Can yakan, canının yanacağı günü beklesin",
    "Gülmek için mutlu olmayı beklemeyin belki de gülmeden ölürsünüz.",
    "Kalbinde sevgiyi koru. Onsuz bir hayat, çiçekler öldüğü zaman güneşsiz bir bahçe gibidir.",
    "Derdi dünya olanın, dünya kadar derdi olur.",
    "İyiler kaybetmez ama kaybedilir",
    "Ağırlayamayacağın misafiri yüreğine konuk etme",
    "Elbisesi kirli olandan değil, düşüncesi kirli olandan korkacaksınız",
    "Sakın unutma, ellerin cebindeyken başarı merdivenlerini çıkamazsın.",
    "Ümit, mutluluktan alınmış bir miktar borçtur.",
    "Kusursuz dost arayan dostsuz kalır",
    "Güzeli güzel yapan edeptir, edep ise güzeli sevmeye sebeptir.",
    "Zihin paraşüt gibidir. Açık değilse işe yaramaz",
    "Bilgelik, herhangi bir zenginlikten daha önemlidir.",
    "Hayat bir öyküye benzer, önemli olan yani eserin uzun olması değil, iyi olmasıdır.",
    "Bilinmeyen yerleri bulmak için, önce kaybolmak gerekir.",
    "Zayıf insanlar intikam alır, güçlü insanlar affeder, zeki insanlar umursamazlar.",
    "Nereye gittiğini bilmiyorsan, hangi yoldan gittiğinin hiçbir önemi yoktur.",
    "Öğrenmek, yaşamın tek kanıtıdır",
    "Seni hayallerine ulaştıracak en önemli şey, cesaretindir.",
    "Çok şükür ki gökyüzü henüz hiçbir cüzdana sığmıyor.",
    "Az insan çok huzur",
    "Mutluluğu sende bulan senindir ötesi misafir.",
    "Ne kadar yaşadığımız değil, nasıl yaşadığımız önemlidir.",
    "Hepimiz birinin hikayesinde kötüyüz",
    "Hiç Kimse senin karanlığını aydınlatmak için yıldızlar arasından çıkıp gelmeyecek",
    "Her şey göründüğü gibi olsaydı eline aldığın deniz suyu mavi olurdu",
    "Bir bulut gibisin yakın ama dokunulamaz",
    "Düşlerimden öp beni.",
    "Belki sen kokar yarınlarım",
    "Herkese selam sana hasret gönderiyorum",
    "Hayatın değerini bilin",
    "Yaşam geriye bakarak anlaşılır, ileriye bakarak yaşanır.",
    "En karanlık gece bile sona erer ve güneş tekrar doğar.",
    "Umudunu kaybetme! En karanlık an şafak sökmeden önceki andır.",
    "Hayat hesapla değil nasiple yaşanır.",
    "İsteyen dağları aşar, istemeyen tümseği bile geçemez",
    "Ö𝑙𝑚𝑒𝑘 𝐵𝑖 ş𝑒𝑦 𝑑𝑒ğ𝑖𝑙 𝑦𝑎ş𝑎𝑚𝑎𝑚𝑎𝑘 𝑘𝑜𝑟𝑘𝑢𝑛ç",
    "𝑁𝑒 𝑖ç𝑖𝑚𝑑𝑒𝑘𝑖 𝑠𝑜𝑘𝑎𝑘𝑙𝑎𝑟𝑎 𝑠ığ𝑎𝑏𝑖𝑙𝑑𝑖𝑚 𝑁𝑒 𝑑𝑒 𝑑ış𝑎𝑟ı𝑑𝑎𝑘𝑖 𝑑ü𝑛𝑦𝑎𝑦𝑎",
    "İ𝑛𝑠𝑎𝑛 𝑠𝑒𝑣𝑖𝑙𝑚𝑒𝑘𝑡𝑒𝑛 ç𝑜𝑘 𝑎𝑛𝑙𝑎şı𝑙𝑚𝑎𝑦ı 𝑖𝑠𝑡𝑖𝑦𝑜𝑟𝑑𝑢 𝑏𝑒𝑙𝑘𝑖 𝑑𝑒",
    "𝐸𝑘𝑚𝑒𝑘 𝑝𝑎ℎ𝑎𝑙ı 𝑒𝑚𝑒𝑘 𝑢𝑐𝑢𝑧𝑑𝑢",
    "𝑆𝑎𝑣𝑎ş𝑚𝑎𝑦ı 𝑏ı𝑟𝑎𝑘ı𝑦𝑜𝑟𝑢𝑚 𝑏𝑢𝑛𝑢 𝑣𝑒𝑑𝑎 𝑠𝑎𝑦",
    "𝐾𝑎𝑙𝑏𝑖 𝑔ü𝑧𝑒𝑙 𝑜𝑙𝑎𝑛ı𝑛 𝑔ö𝑧ü𝑛𝑑𝑒𝑛 𝑦𝑎ş 𝑒𝑘𝑠𝑖𝑘 𝑜𝑙𝑚𝑎𝑧𝑚ış",
    "İ𝑦𝑖𝑦𝑖𝑚 𝑑𝑒𝑠𝑒𝑚 𝑖𝑛𝑎𝑛𝑎𝑐𝑎𝑘 𝑜 𝑘𝑎𝑑𝑎𝑟 ℎ𝑎𝑏𝑒𝑟𝑠𝑖𝑧 𝑏𝑒𝑛𝑑𝑒𝑛",
    "𝑀𝑒𝑠𝑎𝑓𝑒𝑙𝑒𝑟 𝑈𝑚𝑟𝑢𝑚𝑑𝑎 𝐷𝑒ğ𝑖𝑙, İç𝑖𝑚𝑑𝑒 𝐸𝑛 𝐺ü𝑧𝑒𝑙 𝑌𝑒𝑟𝑑𝑒𝑠𝑖𝑛",
    "𝐵𝑖𝑟 𝑀𝑢𝑐𝑖𝑧𝑒𝑦𝑒 İℎ𝑡𝑖𝑦𝑎𝑐ı𝑚 𝑉𝑎𝑟𝑑ı 𝐻𝑎𝑦𝑎𝑡 𝑆𝑒𝑛𝑖 𝐾𝑎𝑟şı𝑚𝑎 Çı𝑘𝑎𝑟𝑑ı",
    "Ö𝑦𝑙𝑒 𝑔ü𝑧𝑒𝑙 𝑏𝑎𝑘𝑡ı 𝑘𝑖 𝑘𝑎𝑙𝑏𝑖 𝑑𝑒 𝑔ü𝑙üşü𝑛 𝑘𝑎𝑑𝑎𝑟 𝑔ü𝑧𝑒𝑙 𝑠𝑎𝑛𝑚ış𝑡ı𝑚",
    "𝐻𝑎𝑦𝑎𝑡 𝑛𝑒 𝑔𝑖𝑑𝑒𝑛𝑖 𝑔𝑒𝑟𝑖 𝑔𝑒𝑡𝑖𝑟𝑖𝑟 𝑛𝑒 𝑑𝑒 𝑘𝑎𝑦𝑏𝑒𝑡𝑡𝑖ğ𝑖𝑛 𝑧𝑎𝑚𝑎𝑛ı 𝑔𝑒𝑟𝑖 𝑔𝑒𝑡𝑖𝑟𝑖𝑟",
    "𝑆𝑒𝑣𝑚𝑒𝑘 𝑖ç𝑖𝑛 𝑠𝑒𝑏𝑒𝑝 𝑎𝑟𝑎𝑚𝑎𝑑ı𝑚 ℎ𝑖ç 𝑠𝑒𝑠𝑖 𝑦𝑒𝑡𝑡𝑖 𝑘𝑎𝑙𝑏𝑖𝑚𝑒",
]

kartlar = "♤ ♡ ♢ ♧ 🂱 🂲 🂳 🂴 🂵 🂶 🂷 🂸 🂹 🂺 🂻 🂼 🂽 🂾 🂡 🂢 🂣 🂤 🂥 🂦 🂧 🂨 🂩 🂪 🂫 🂬 🂭 🂮 🃁 🃂 🃃 🃄 🃅 🃆 🃇 🃈 🃉 🃊 🃋 🃌 🃍 🃎 🃑 🃒 🃓 🃔 🃕 🃖 🃗 🃘 🃙 🃚 🃛 🃜 🃝 🃞 🃟 ".split(
    " "
)


class FILE_CONTROL:
    def __init__(self, file_name: str) -> None:
        self.variable = file_name

    def set(self, value: str):
        try:
            with open(f"files/{self.variable}.txt", "w") as file:
                file.write(str(value))
                file.close()
        except Exception as e:
            return e
        return True

    def get(self):
        try:
            with open(f"files/{self.variable}.txt", "r") as file:
                data = file.read()
                file.close()
        except Exception as e:
            return e
        return str(data)

    def del_(self, value=None):
        if value:
            try:
                with open(f"files/{self.variable}.txt", "w") as file:
                    file.write("")
                    file.close()
            except Exception as e:
                return print(e)
            return True
        else:
            try:
                os.remove(f"files/{self.variable}.txt")
            except Exception as e:
                return e
            return True


def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND)


# =================================================================
# @G4rip - < https://t.me/G4rip >
# Copyright (C) 2022
# © @G4rip (Telegram) - All Rights Reserved
# The features of this file are not available in the new version.
# You can contact @G4rip (Telegram) for this feature.
# =================================================================
# @G4rip - < https://t.me/G4rip >
# Telif hakkı (C) 2022
# © @G4rip (Telegram) - Tüm hakları saklıdır.
# Bu özellik yeni versiyonda kaldırılmıştır.
# Bu özellik için @G4rip (Telegram) ile iletişime geçebilirsiniz.
# =================================================================
#
#   def msg_link(message: Message):
#       if str(message.chat.id).startswith("-100"):
#           return f"https://t.me/c/{str(message.chat.id)[4:]}/{message.message_id}"
#       elif str(message.chat.id).startswith("-"):
#           return f"https://t.me/c/{str(message.chat.id)[1:]}/{message.message_id}"
#       else:
#           return f"https://t.me/c/{message.chat.id}/{message.message_id}"


async def clean_mode(chat_id: int, *args):
    if chat_id in CHATS_CLEAN_MODE_SETTINGS:
        if CHATS_CLEAN_MODE_SETTINGS[chat_id] == True:
            await sleep(3)
            for message in args:
                message: Message
                try:
                    await message.delete()
                except BaseException:
                    pass
        else:
            return
    else:
        chat_clean_mode = await delcmd_is_on(chat_id)
        if chat_clean_mode:
            CHATS_CLEAN_MODE_SETTINGS[chat_id] = True
            await sleep(3)
            for message in args:
                message: Message
                try:
                    await message.delete()
                except BaseException:
                    pass


def admin(mystic):
    global admins, BOT_ID

    async def wrapper(bot: Client, message: Message):
        if message.chat.type == ChatType.PRIVATE:
            return  # await mystic(bot, message)
        if BOT_ID[0] in admins:
            return await mystic(bot, message)
        else:
            a = await bot.get_chat_member(message.chat.id, BOT_USERNAME)
            lang = await get_str(message.chat.id)
            LAN = lan(lang)
            if a.status != ChatMemberStatus.ADMINISTRATOR and ADMIN:
                return await message.reply_text(LAN.NEED_ADMIN)
            #   if not a.privileges.can_delete_messages and ADMIN:
            #       await message.reply_text(LAN.NEED_DELETE_ADMIN)
            #       return
            #   if a.privileges.can_restrict_members:
            #       await message.reply_text(LAN.NOT_NEED_RESTRICT_ADMIN)
            #       return
        return await mystic(bot, message)

    return wrapper


def cbadmin(mystic):
    async def wrapper(bot: Client, query: CallbackQuery):
        if query.message.chat.type == ChatType.PRIVATE:
            return  # await mystic(bot, query)
        if BOT_ID[0] in admins:
            return await mystic(bot, query)
        else:
            a = await bot.get_chat_member(query.message.chat.id, BOT_USERNAME)
            lang = await get_str(query.message.chat.id)
            LAN = lan(lang)
            if a.status != ChatMemberStatus.ADMINISTRATOR and ADMIN:
                return await query.answer(LAN.NEED_ADMIN)
        #   if not a.privileges.can_delete_messages and ADMIN:
        #       await query.answer(LAN.NEED_DELETE_ADMIN)
        #       return
        #   if a.privileges.can_restrict_members:
        #       await query.answer(LAN.NOT_NEED_RESTRICT_ADMIN)
        #       return
        return await mystic(bot, query)

    return wrapper


def sudo(mystic):
    async def wrapper(bot: Client, message: Message):
        # print(SUDOS)
        if message.from_user.id not in SUDOS:
            return  # await mystic(bot, message)
        return await mystic(bot, message)

    return wrapper


def cbsudo(mystic):
    async def wrapper(bot: Client, query: CallbackQuery):
        if query.from_user.id not in SUDOS:
            return  # await mystic(bot, query)
        else:
            return await mystic(bot, query)

    return wrapper


def block(mystic):
    async def wrapper(bot: Client, message: Message):
        if message.from_user is None:
            return  # await message.reply_text("You are banned!")
        if message.from_user.id in black_list_users:
            return  # await message.reply_text("You are banned!")
        if message.chat.id in black_list_chats:
            return  # await message.reply_text("This chat is banned!")
        if bakim[0]:
            # print(bakim[0])
            return  # await message.reply_text("Bot bakımda!")
        return await mystic(bot, message)

    return wrapper


def cbblock(mystic):
    async def wrapper(bot: Client, query: CallbackQuery):
        if query.message.from_user is None:
            return  # await message.reply_text("You are banned!")
        if query.from_user.id in black_list_users:
            return
        if query.message.chat.id in black_list_chats:
            return
        if bakim[0]:
            return  # await query.message.reply_text("Bot bakımda!")
        return await mystic(bot, query)

    return wrapper


async def reload(client: Client, message: Message, chat_id: int = None):
    global admins
    if message.chat.type == ChatType.PRIVATE == ChatType.PRIVATE:
        return
    if chat_id is not None:
        if chat_id in admins:
            return

    new_admins = []

    async for now_admins in client.get_chat_members(
        message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
    ):
        now_admins: ChatMember
        new_admins.append(now_admins.user.id)
    admins[message.chat.id] = new_admins


async def count(client: Client, chat_id):
    deleted = 0
    bot = 0
    total = await client.get_chat_members_count(chat_id)
    async for usr in client.get_chat_members(chat_id):
        if usr.user.is_bot:
            bot += 1
        elif usr.user.is_deleted:
            deleted += 1
    return bot, deleted, total


async def admincount(client: Client, chat_id):
    deleted = 0
    bot = 0
    total = 0
    async for usr in client.get_chat_members(
        chat_id, filter=ChatMembersFilter.ADMINISTRATORS
    ):
        usr: ChatMember
        if usr.user.is_bot:
            bot += 1
        elif usr.user.is_deleted:
            deleted += 1
        else:
            total += 1
    return bot, deleted, total


async def check_admin_and_edit(bot: Client, query: CallbackQuery):
    user_id = query.from_user.id
    lang = await get_str(user_id)
    LAN = lan(lang)
    await reload(bot, query.message, query.from_user.id)
    text = LAN.ADMINS
    if query.from_user.id not in admins[query.message.chat.id]:
        return await bot.answer_callback_query(
            callback_query_id=query.id,
            text=LAN.CALLBACK_WARN.format(query.from_user.first_name),
            show_alert=True,
        )
    else:
        async for user in bot.get_chat_members(
            query.message.chat.id, filter="administrators"
        ):
            user: ChatMember
            if user.user.is_bot:
                pass
            elif user.user.is_deleted:
                pass
            else:
                if user.status == "creator":
                    text += (
                        f"[{user.user.first_name}](tg://user?id={user.user.id}) 👑 \n"
                    )
                else:
                    text += (
                        f"**[{user.user.first_name}](tg://user?id={user.user.id})\n**"
                    )
        await query.edit_message_text(text=text)


def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "K", 2: "M", 3: "G", 4: "T"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


# extract user from message // Copyright @G4ip (Telegram) - All Rights Reserved
def extract_user(message: Message) -> Tuple[int, str]:
    user_id = None
    user_first_name = None

    if len(message.command) > 1:
        if len(message.entities) > 1 and message.entities[1].type == "text_mention":
            required_entity = message.entities[1]
            user_id = required_entity.user.id
            user_first_name = required_entity.user.first_name
        else:
            user_id = message.command[1]
            user_first_name = user_id

        try:
            user_id = int(user_id)
        except ValueError:
            pass

    elif message.reply_to_message:
        user_id, user_first_name = basicbots(message.reply_to_message)

    elif message:
        user_id, user_first_name = basicbots(message)

    return (user_id, user_first_name)


def basicbots(message: Message) -> Tuple[int, str]:
    user_id = None
    user_first_name = None

    if message.from_user:
        user_id = message.from_user.id
        user_first_name = message.from_user.first_name

    elif message.sender_chat:
        user_id = message.sender_chat.id
        user_first_name = message.sender_chat.title

    return (user_id, user_first_name)


# =================================================================
# @G4rip - < https://t.me/G4rip >
# Copyright (C) 2022
# © @G4rip (Telegram) - All Rights Reserved
# The features of this file are not available in the new version.
# You can contact @G4rip (Telegram) for this feature.
# =================================================================
# @G4rip - < https://t.me/G4rip >
# Telif hakkı (C) 2022
# © @G4rip (Telegram) - Tüm hakları saklıdır.
# Bu özellik yeni versiyonda kaldırılmıştır.
# Bu özellik için @G4rip (Telegram) ile iletişime geçebilirsiniz.
# =================================================================
#
#    @Client.on_message()
#    async def _(bot: Client, cmd: Message):
#        await handle_user_status(bot, cmd)


@Client.on_message(command(["bitir", "cancel", "stop"]))
@block
async def bitir(client: Client, message: Message):
    if message.chat.type == ChatType.PRIVATE:
        return
    global calisan
    chat_id = message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    await reload(client, message, message.from_user.id)
    if message.from_user.id not in admins[chat_id]:
        a = await message.reply_text(
            LAN.U_NOT_ADMIN.format(message.from_user.first_name)
        )
        await clean_mode(message.chat.id, a, message)
        return
    if chat_id not in calisan:
        b = await message.reply_text(LAN.ISLEM_YOK.format(message.from_user.mention))
        await clean_mode(message.chat.id, b, message)
        return
    if chat_id in calisan:
        c = await message.reply_text(LAN.ISLEM_IPTAL.format(message.from_user.mention))
        calisan.remove(chat_id)
        await clean_mode(message.chat.id, c, message)
        return


@Client.on_message(command(["reload"]))
@block
async def update_admin(client: Client, message: Message):
    global admins
    chat_id = message.chat.id
    lang = await get_str(chat_id)
    LAN = lan(lang)
    if message.chat.type == ChatType.PRIVATE:
        return
    new_admins = []
    async for now_admins in client.get_chat_members(
        message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
    ):
        now_admins: ChatMember
        new_admins.append(now_admins.user.id)
    admins[message.chat.id] = new_admins
    # print(new_admins)
    await message.reply_text(
        LAN.RELOADED + str(new_admins),
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(LAN.ADMINS, callback_data="admins"),
                ],
            ],
        ),
    )


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False
