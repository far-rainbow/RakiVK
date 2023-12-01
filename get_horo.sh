#!/bin/bash

cd "$(dirname "$0")"

horodir=horoscopes

echo y | lynx -accept-all-cookies -dump https://horo.mail.ru/prediction/cancer/today/ | grep -A20 "Гороскоп на сегодня: Рак" > $horodir/cancer.today
echo y | lynx -accept-all-cookies -dump https://horo.mail.ru/prediction/virgo/today/ | grep -A20 "Гороскоп на сегодня: Дева" > $horodir/virgo.today
sleep 1
echo y | lynx -accept-all-cookies -dump https://horo.mail.ru/prediction/leo/today/ | grep -A20 "Гороскоп на сегодня: Лев" > $horodir/leo.today
echo y | lynx -accept-all-cookies -dump https://horo.mail.ru/prediction/scorpio/today/ | grep -A20 "Гороскоп на сегодня: Скорпион" > $horodir/scorpio.today
sleep 1
echo y | lynx -accept-all-cookies -dump https://horo.mail.ru/prediction/capricorn/today/ | grep -A20 "Гороскоп на сегодня: Козерог" > $horodir/capricorn.today
echo y | lynx -accept-all-cookies -dump https://horo.mail.ru/prediction/libra/today/  | grep -A20 "Гороскоп на сегодня: Весы" > $horodir/libra.today
sleep 1
echo y | lynx -accept-all-cookies -dump https://horo.mail.ru/prediction/taurus/today/  | grep -A20 "Гороскоп на сегодня: Телец" > $horodir/taurus.today
echo y | lynx -accept-all-cookies -dump https://horo.mail.ru/prediction/pisces/today/  | grep -A20 "Гороскоп на сегодня: Рыбы" > $horodir/pisces.today
sleep 1
echo y | lynx -accept-all-cookies -dump https://horo.mail.ru/prediction/gemini/today/ | grep -A20 "Гороскоп на сегодня: Близнецы" > $horodir/gemini.today
echo y | lynx -accept-all-cookies -dump https://horo.mail.ru/prediction/sagittarius/today/  | grep -A20 "Гороскоп на сегодня: Стрелец" > $horodir/sagittarius.today
sleep 1
echo y | lynx -accept-all-cookies -dump https://horo.mail.ru/prediction/aquarius/today/  | grep -A20 "Гороскоп на сегодня: Водолей" > $horodir/aquarius.today
echo y | lynx -accept-all-cookies -dump https://horo.mail.ru/prediction/aries/today/  | grep -A20 "Гороскоп на сегодня: Овен" > $horodir/aries.today

#TODO:
# horoscopes -> DB

cd $horodir

sed -i '4d' *.today
sed -i '/\]Вчера/d' *.today
sed -i '/Подробнее о знаке/d' *.today
sed -i '/Одноклассники/d' *.today
sed -i '/полезных дел/d' *.today
sed -i '/Гадания на Таро/d' *.today
sed -i '/\]Бизнес/d' *.today
sed -i '/^   свиданий/d' *.today

sed -i '$d' *.today
sed -i '$d' *.today


cat *.today
