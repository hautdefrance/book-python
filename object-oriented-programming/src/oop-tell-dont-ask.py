# Good
class Rocket:
    status = 'off'

    def ignite(self):
        self.status = 'on'


soyuz = Rocket()
soyuz.ignite()


# Bad
class Rocket:
    status = 'off'


soyuz = Rocket()
soyuz.status = 'on'
