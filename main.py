import filecmp
import os


def text_file_comparison(f1, f2):
    path1 = os.path.join(r"")
    path2 = os.path.join(r"")
    result = filecmp.cmp(f1, f2, shallow=False)
    print(result)


def main():
    text_file_comparison()


if __name__ == '__main__':
    main()

