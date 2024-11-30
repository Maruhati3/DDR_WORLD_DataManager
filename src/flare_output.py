with open('row_output.txt', 'r') as in_file:
    with open('flare_output.csv', 'w') as out_file:
        version_line = 0
        out_file.write("バージョン;楽曲名;難易度;レベル;フレアランク;フレアスキル;プレー日時\n")
        for n, line in enumerate(in_file):
            if n == version_line:
                version = line.strip()
            elif line.strip().find("---") != -1:
                version_line = n + 1
            elif n > version_line + 2:
                if (n - version_line) % 3 == 0:
                    name = line.strip()
                elif (n - version_line) % 3 == 1:
                    dif = line.strip()
                else:
                    info = line.strip().replace(" ", ";")
                    out_file.write(f"{version};{name};{dif};{info}\n")