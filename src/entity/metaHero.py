class metaHero(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    __instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None: cls.__instance = super(metaHero, cls).__call__(*args, **kwargs)

        return cls.__instance
