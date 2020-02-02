from handler.views import user_send_to_user


class MessageHandler:
    def parser(self, route):
        router = {
            "/message/send": user_send_to_user
        }
        return router[route]

    def handle(self, request):
        route = request["data"]["route"]
        func = self.parser(route)
        return func(request["data"])
