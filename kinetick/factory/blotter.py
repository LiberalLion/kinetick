from kinetick.blotter import Blotter


class MainBlotter(Blotter):
    pass  # we just need the name


def build():
    return MainBlotter()


# ===========================================
if __name__ == "__main__":
    build().run()
