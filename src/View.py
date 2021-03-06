

class View():

    def visualize_board(self, board):
        # Letters from: http://patorjk.com/software/taag/#p=display&f=Blocks&t=e
        title = "Welcome to\n" \
                " .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.\n" \
                "| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |\n" \
                "| |    _______   | || |     ______   | || |  _______     | || |      __      | || |   ______     | || |   ______     | || |   _____      | || |  _________   | |\n" \
                "| |   /  ___  |  | || |   .' ___  |  | || | |_   __ \    | || |     /  \     | || |  |_   _ \    | || |  |_   _ \    | || |  |_   _|     | || | |_   ___  |  | |\n" \
                "| |  |  (__ \_|  | || |  / .'   \_|  | || |   | |__) |   | || |    / /\ \    | || |    | |_) |   | || |    | |_) |   | || |    | |       | || |   | |_  \_|  | |\n" \
                "| |   '.___`-.   | || |  | |         | || |   |  __ /    | || |   / ____ \   | || |    |  __'.   | || |    |  __'.   | || |    | |   _   | || |   |  _|  _   | |\n" \
                "| |  |`\____) |  | || |  \ `.___.'\  | || |  _| |  \ \_  | || | _/ /    \ \_ | || |   _| |__) |  | || |   _| |__) |  | || |   _| |__/ |  | || |  _| |___/ |  | |\n" \
                "| |  |_______.'  | || |   `._____.'  | || | |____| |___| | || ||____|  |____|| || |  |_______/   | || |  |_______/   | || |  |________|  | || | |_________|  | |\n" \
                "| |              | || |              | || |              | || |              | || |              | || |              | || |              | || |              | |\n" \
                "| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |\n" \
                " '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' "

        star = [" ------------------ ",
                "|         .        |",
                "|        / \       |",
                "|    ___/   \___   |",
                "|   '.         .'  |",
                "|     '.     .'    |",
                "|      / .'. \     |",
                "|     /.'   '.\    |",
                "|                  |",
                "|                  |",
                " ------------------ "]

        blank = [" ------------------ ",
                 "|                  |",
                 "|                  |",
                 "|                  |",
                 "|                  |",
                 "|                  |",
                 "|                  |",
                 "|                  |",
                 "|                  |",
                 "|                  |",
                 " ------------------ "]

        a = [" ------------------ ",
             "| .--------------. |",
             "| |      __      | |",
             "| |     /  \     | |",
             "| |    / /\ \    | |",
             "| |   / ____ \   | |",
             "| | _/ /    \ \_ | |",
             "| ||____|  |____|| |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        b = [" ------------------ ",
             "| .--------------. |",
             "| |   ______     | |",
             "| |  |_   _ \    | |",
             "| |    | |_) |   | |",
             "| |    |  __'.   | |",
             "| |   _| |__) |  | |",
             "| |  |_______/   | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        c = [" ------------------ ",
             "| .--------------. |",
             "| |     ______   | |",
             "| |   .' ___  |  | |",
             "| |  / .'   \_|  | |",
             "| |  | |         | |",
             "| |  \ `.___.'\  | |",
             "| |   `._____.'  | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        d = [" ------------------ ",
             "| .--------------. |",
             "| |  ________    | |",
             "| | |_   ___ `.  | |",
             "| |   | |   `. \ | |",
             "| |   | |    | | | |",
             "| |  _| |___.' / | |",
             "| | |________.'  | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        e = [" ------------------ ",
             "| .--------------. |",
             "| |  _________   | |",
             "| | |_   ___  |  | |",
             "| |   | |_  \_|  | |",
             "| |   |  _|  _   | |",
             "| |  _| |___/ |  | |",
             "| | |_________|  | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        f = [" ------------------ ",
             "| .--------------. |",
             "| |  _________   | |",
             "| | |_   ___  |  | |",
             "| |   | |_  \_|  | |",
             "| |   |  _|      | |",
             "| |  _| |_       | |",
             "| | |_____|      | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        g = [" ------------------ ",
             "| .--------------. |",
             "| |    ______    | |",
             "| |  .' ___  |   | |",
             "| | / .'   \_|   | |",
             "| | | |    ____  | |",
             "| | \ `.___]  _| | |",
             "| |  `._____.'   | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        h = [" ------------------ ",
             "| .--------------. |",
             "| |  ____  ____  | |",
             "| | |_   ||   _| | |",
             "| |   | |__| |   | |",
             "| |   |  __  |   | |",
             "| |  _| |  | |_  | |",
             "| | |____||____| | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        i = [" ------------------ ",
             "| .--------------. |",
             "| |     _____    | |",
             "| |    |_   _|   | |",
             "| |      | |     | |",
             "| |      | |     | |",
             "| |     _| |_    | |",
             "| |    |_____|   | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        j = [" ------------------ ",
             "| .--------------. |",
             "| |     _____    | |",
             "| |    |_   _|   | |",
             "| |      | |     | |",
             "| |   _  | |     | |",
             "| |  | |_' |     | |",
             "| |  `.___.'     | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        k = [" ------------------ ",
             "| .--------------. |",
             "| |  ___  ____   | |",
             "| | |_  ||_  _|  | |",
             "| |   | |_/ /    | |",
             "| |   |  __'.    | |",
             "| |  _| |  \ \_  | |",
             "| | |____||____| | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        l = [" ------------------ ",
             "| .--------------. |",
             "| |   _____      | |",
             "| |  |_   _|     | |",
             "| |    | |       | |",
             "| |    | |   _   | |",
             "| |   _| |__/ |  | |",
             "| |  |________|  | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        m = [" ------------------ ",
             "| .--------------. |",
             "| | ____    ____ | |",
             "| ||_   \  /   _|| |",
             "| |  |   \/   |  | |",
             "| |  | |\  /| |  | |",
             "| | _| |_\/_| |_ | |",
             "| ||_____||_____|| |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        n = [" ------------------ ",
             "| .--------------. |",
             "| | ____  _____  | |",
             "| ||_   \|_   _| | |",
             "| |  |   \ | |   | |",
             "| |  | |\ \| |   | |",
             "| | _| |_\   |_  | |",
             "| ||_____|\____| | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        o = [" ------------------ ",
             "| .--------------. |",
             "| |     ____     | |",
             "| |   .'    `.   | |",
             "| |  /  .--.  \  | |",
             "| |  | |    | |  | |",
             "| |  \  `--'  /  | |",
             "| |   `.____.'   | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        p = [" ------------------ ",
             "| .--------------. |",
             "| |   ______     | |",
             "| |  |_   __ \   | |",
             "| |    | |__) |  | |",
             "| |    |  ___/   | |",
             "| |   _| |_      | |",
             "| |  |_____|     | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        q = [" ------------------ ",
             "| .--------------. |",
             "| |    ___       | |",
             "| |  .'   '.     | |",
             "| | /  .-.  \    | |",
             "| | | |   | |    | |",
             "| | \  `-'  \_   | |",
             "| |  `.___.\__|  | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        r = [" ------------------ ",
             "| .--------------. |",
             "| |  _______     | |",
             "| | |_   __ \    | |",
             "| |   | |__) |   | |",
             "| |   |  __ /    | |",
             "| |  _| |  \ \_  | |",
             "| | |____| |___| | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        s = [" ------------------ ",
             "| .--------------. |",
             "| |    _______   | |",
             "| |   /  ___  |  | |",
             "| |  |  (__ \_|  | |",
             "| |   '.___`-.   | |",
             "| |  |`\____) |  | |",
             "| |  |_______.'  | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        t = [" ------------------ ",
             "| .--------------. |",
             "| |  _________   | |",
             "| | |  _   _  |  | |",
             "| | |_/ | | \_|  | |",
             "| |     | |      | |",
             "| |    _| |_     | |",
             "| |   |_____|    | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        u = [" ------------------ ",
             "| .--------------. |",
             "| | _____  _____ | |",
             "| ||_   _||_   _|| |",
             "| |  | |    | |  | |",
             "| |  | '    ' |  | |",
             "| |   \ `--' /   | |",
             "| |    `.__.'    | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        v = [" ------------------ ",
             "| .--------------. |",
             "| | ____   ____  | |",
             "| ||_  _| |_  _| | |",
             "| |  \ \   / /   | |",
             "| |   \ \ / /    | |",
             "| |    \ ' /     | |",
             "| |     \_/      | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        w = [" ------------------ ",
             "| .--------------. |",
             "| | _____  _____ | |",
             "| ||_   _||_   _|| |",
             "| |  | | /\ | |  | |",
             "| |  | |/  \| |  | |",
             "| |  |   /\   |  | |",
             "| |  |__/  \__|  | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        x = [" ------------------ ",
             "| .--------------. |",
             "| |  ____  ____  | |",
             "| | |_  _||_  _| | |",
             "| |   \ \  / /   | |",
             "| |    > `' <    | |",
             "| |  _/ /'`\ \_  | |",
             "| | |____||____| | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        y = [" ------------------ ",
             "| .--------------. |",
             "| |  ____  ____  | |",
             "| | |_  _||_  _| | |",
             "| |   \ \  / /   | |",
             "| |    \ \/ /    | |",
             "| |    _|  |_    | |",
             "| |   |______|   | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]

        z = [" ------------------ ",
             "| .--------------. |",
             "| |   ________   | |",
             "| |  |  __   _|  | |",
             "| |  |_/  / /    | |",
             "| |     .'.' _   | |",
             "| |   _/ /__/ |  | |",
             "| |  |________|  | |",
             "| |              | |",
             "| '--------------' |",
             " ------------------ "]



        display_board = "Current Board\n"
        for row in board:
            for sub in range(0, len(a)):
                for tile in row:
                    if tile == "":
                        display_board += blank[sub]
                    if tile == "A":
                        display_board += a[sub]
                    if tile == "B":
                        display_board += b[sub]
                    if tile == "C":
                        display_board += c[sub]
                    if tile == "D":
                        display_board += d[sub]
                    if tile == "E":
                        display_board += e[sub]
                    if tile == "F":
                        display_board += f[sub]
                    if tile == "G":
                        display_board += g[sub]
                    if tile == "H":
                        display_board += h[sub]
                    if tile == "I":
                        display_board += i[sub]
                    if tile == "J":
                        display_board += j[sub]
                    if tile == "K":
                        display_board += k[sub]
                    if tile == "L":
                        display_board += l[sub]
                    if tile == "M":
                        display_board += m[sub]
                    if tile == "N":
                        display_board += n[sub]
                    if tile == "O":
                        display_board += o[sub]
                    if tile == "P":
                        display_board += p[sub]
                    if tile == "Q":
                        display_board += q[sub]
                    if tile == "R":
                        display_board += r[sub]
                    if tile == "S":
                        display_board += s[sub]
                    if tile == "T":
                        display_board += t[sub]
                    if tile == "U":
                        display_board += u[sub]
                    if tile == "V":
                        display_board += v[sub]
                    if tile == "W":
                        display_board += w[sub]
                    if tile == "X":
                        display_board += x[sub]
                    if tile == "Y":
                        display_board += y[sub]
                    if tile == "Z":
                        display_board += z[sub]
                    if tile == "star":
                        display_board += star[sub]


                display_board += "\n"

        return display_board
