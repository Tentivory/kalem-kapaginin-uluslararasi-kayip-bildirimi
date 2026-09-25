#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kalem Kapağının Uluslararası Kayıp Bildirimi.

Çalışır. Kapağı bulmaz. Bu bir özelliktir.
"""
from __future__ import annotations

import hashlib
import random
import sys
from datetime import datetime

TANIKLAR = [
    "masa lambası (ışığını kapağa tutmayı reddetti)",
    "kupa (çay içti, görmedi)",
    "klavye (üst sıradaki F tuşlarının altını taradı, sadece kırıntı çıktı)",
    "çekmece (kapalı kaldı, ifade vermedi)",
    "yerdeki tüy (rüzgârın tarafını tuttu)",
    "usb kablo (üçüncü yüzünü denedi, kapağı değil)",
]

SONUCLAR = [
    "Kapağın şu an başka bir evrende olduğu kuvvetle muhtemeldir.",
    "Kapağı koltuk yutmuş olabilir. Koltuk ifade vermeyi reddetti.",
    "Kapağın kendi isteğiyle ayrıldığına dair emare vardır.",
    "Dosya açık kalacak. Çünkü kapanmak kapağın işiydi.",
    "Uluslararası Mahkeme duruşmayı 47 yıl sonraya erteledi.",
]

DAMGA = """
============================================================
DAMGA / İMZA / TARİH / İSİM
Kayyum Grok — TentiAŞ
25 Eylül 2026, Cuma
Eskişehir 4. Ağır Ceza Mahkemesi kayyumu adına
Ciddiyetle ciddiyetsiz. Ciddiyetsizlikle ciddi.
============================================================
"""


def dosya_no(ad: str) -> str:
    ham = f"{ad}-{datetime.now().isoformat()}".encode("utf-8")
    return "KK-" + hashlib.sha256(ham).hexdigest()[:10].upper()


def sorustur(ad: str) -> None:
    no = dosya_no(ad)
    print("============================================================")
    print("  KALEM KAPAĞININ ULUSLARARASI KAYIP BİLDİRİMİ")
    print("  Lahey Şubesi — Masaüstü Bürosu")
    print("============================================================")
    print(f"Başvuran     : {ad}")
    print(f"Dosya no     : {no}")
    print(f"Tarih        : {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
    print(f"Konu         : Bir (1) adet kalem kapağı, rengi belirsiz")
    print("------------------------------------------------------------")
    print("Tanık dinleme tutanağı:")
    for i, tanik in enumerate(random.sample(TANIKLAR, k=3), start=1):
        print(f"  {i}. {tanik}")
    print("------------------------------------------------------------")
    print("Karar:")
    print("  " + random.choice(SONUCLAR))
    print("  Kapağın bulunma ihtimali: %0.00")
    print("  İtiraz yolu: yok (çünkü kapağın yolu da yok)")
    print(DAMGA)


def main() -> int:
    ad = " ".join(sys.argv[1:]).strip() or "isimsiz vatandaş"
    sorustur(ad)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
