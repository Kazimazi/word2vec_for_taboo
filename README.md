# Taboo játék

## Bevezető

Mi az a Taboo? [Itt egy 2 perces videóösszefoglaló.](https://www.youtube.com/watch?v=4QeA4nrcQV0)

Célom különböző modelleket felhasználva, Taboo játékhoz számítógép által megoldást találni.

A játék adatokat [github](https://github.com/Kovah/Taboo-Data)-ról töltöttem le.

## Felhasználás és Telepítés

Python 3.10-et használtam Gensim libray-vel.

Sok GB szabad helyre lehet szükség a modellekhez.

A logika nem tökéletes, néha megszegi a szabályt, pl ha a kitalálandó szó _wolf_ akkor megoldásban benne lesz a _wolves_.

Futtatni:
```
python taboo.py
```

Nem mindegyik inputra lesz találat a model-ünkben, akkor hibát kapunk.

## Megfigyelések

Állatokra Google news más állatokat ad. Ami akár jó is lehet, ha a kulcsszó ily módon áll elő:
```
zebra = horse + tuxedo
```
de a gyakorlatban ez nem tapasztalható.

Például a kulcsszó _wolf_-ot elég nehéz kitalálni, ha a számítógép _grizzly_-t és _elk_-et adja tippként. Twitter-ről készített model se jobb, ez esetben a népszerű Twilight filmsorozatból kapunk találatokat, például _vampire_.

Talán ha wikipédiát használnánk jobb eredményeket kapunk.

De nem igazán, más módszert kell keresni.

## Használt segédeszközök

- Gensim dokumentáció
- [Codenames blogpost](https://jamesmullenbach.github.io/2018/01/02/codenames-fun.html)

## TODOs

- [ ] load once run multiple times
- [ ] allow other taboos than animals
- [ ] use Python notebooks
