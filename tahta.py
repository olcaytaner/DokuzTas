self.tahta = np.zeros((7, 7), dtype=tuple)
        #print(self.tahta)
        for i in range(0, 7):
            for j in range(0, 7):
                self.tahta[i][j] = (0, "-1")
                if i == 0 or i == 6:
                    if j == 0 or j == 3 or j == 6:
                        self.tahta[i][j] = (0, "p0")
                if i == 1 or i == 5:
                    if j == 1 or j == 3 or j == 5:
                        self.tahta[i][j] = (0, "p0")
                if i == 2 or i == 4:
                    if j == 2 or j == 3 or j == 4:
                        self.tahta[i][j] = (0, "p0")
                if i == 3:
                    if j != 3:
                        self.tahta[i][j] = (0, "p0")