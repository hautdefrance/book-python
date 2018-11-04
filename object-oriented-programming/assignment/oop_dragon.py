class Dragon:
    pass


# Do not modify anything below!
wawelski = Dragon(name='Wawelski', position_x=50, position_y=120)

wawelski.set_position(x=10, y=20)
wawelski.move(left=10, down=20)
wawelski.move(left=10, right=15)
wawelski.move(right=15, up=5)
wawelski.move(down=5)

wawelski.take_damage(10)
wawelski.take_damage(50)
wawelski.take_damage(35)
wawelski.take_damage(20)
wawelski.take_damage(25)
