import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def totales():
    items = os.listdir()
    bc = 0
    for item in items:
        bc += os.path.getsize(item)

    with open('test.text', 'w') as f:
        f.write(f"Total Bytes {bc/1048576} \n File list: \n -----------\n")
        for item in items:
            f.write(f"{item} \n")


if __name__ == '__main__':
    totales()
