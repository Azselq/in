import re


def normalize_phone_in_line(line: str) -> str:
    line = line.strip()

    if not line:
        return line

    digits = re.findall(r'\d', line)

    if len(digits) < 10:
        return line

    digits = digits[-10:]

    area = ''.join(digits[:3])

    rest = ''.join(digits[3:])

    return f"+1 ({area}) {rest}"


def main():
    input_file = "input.txt"
    output_file = "output.txt"

    with open(input_file, "r", encoding="utf-8") as fin, \
         open(output_file, "w", encoding="utf-8") as fout:

        for line in fin:
            normalized = normalize_phone_in_line(line)
            fout.write(normalized + "\n")""





if __name__ == "__main__":
    main()
