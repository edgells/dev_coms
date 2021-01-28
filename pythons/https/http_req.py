import httpx


def main():
    try:
        resp = httpx.get("https://www.baidu.com")
        print(resp.status_code)
        print(resp.content)
        return

    finally:
        print("resp close....")
        resp.close()


if __name__ == '__main__':
    main()
