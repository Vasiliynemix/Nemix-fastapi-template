def with_uow(func):
    async def wrapper(self, *args, **kwargs):
        if kwargs.get("uow") is None:
            return await func(self, *args, **kwargs)
        async with kwargs.get("uow"):
            return await func(self, *args, **kwargs)

    return wrapper


class WithUOWDecorator(type):
    def __new__(cls, name, bases, attrs):
        for i, func in attrs.items():
            if callable(func):
                attrs[i] = with_uow(func)
        return super(WithUOWDecorator, cls).__new__(cls, name, bases, attrs)
