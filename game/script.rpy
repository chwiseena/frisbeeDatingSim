# Sweet Pea Frisbee

define a = Character("Alabama", color="#77c23e")
define aUnknown = Character("???", color="#77c23e")
image a = "characters/a/alabama.png"

define f = Character("Frodo", color="#f75364")
define fUnknown = Character("???", color="#f75364")
image f = "characters/f/frodo.png"

define j = Character("Justin")
image j = "characters/j/justin.png"

define sd = Character("SD", color="#c2633e")
define sdUnknown = Character("???", color="#c2633e")
image sd = "characters/sd/spiritDerek.png"

define so = Character("Snakeoil", color="#be46f5")
define soUnknown = Character("???", color="#be46f5")
image so = "characters/so/snakeOil.png"

define v = Character("Vegeta", color="#c23e77")
define vUnknown = Character("???", color="#c23e77")
image v = "characters/v/vegeta.png"

define wm = Character("Walter", color="#3eb0c2")
define wmUnknown = Character("???", color="#3eb0c2")
image wm = "characters/wm/walterMehlongelo.png"

define name = ""
define major = ""

transform slightleft:
    xalign 0.10
    yalign 1.0

transform left:
    xalign 0.25
    yalign 1.0

transform slightright:
    xalign 0.90
    yalign 1.0

transform right:
    xalign 0.75
    yalign 1.0

label start:

    call intro

    call practice1

    return
