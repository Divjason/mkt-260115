import random

class RandomUserAgentMiddleware:
    USER_AGENTS = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
    ]

    def process_request(self, request, spider) :
        request.headers.setdefault("Accept-Language", "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7")
        request.headers["User-Agent"] = random.choice(self.USER_AGENTS).encode("utf-8")
        return None