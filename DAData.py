import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('Int Monthly Visitor (data).xlsx')

del df[' Brunei Darussalam ']
del df[' Indonesia ']
del df[' Malaysia ']
del df[' Philippines ']
del df[' Thailand ']
del df[' Viet Nam ']
del df[' Myanmar ']
del df[' Japan ']
del df[' Hong Kong ']
del df[' China ']
del df[' Taiwan ']
del df[' Korea, Republic Of ']
del df[' India ']
del df[' Pakistan ']
del df[' Sri Lanka ']
del df[' Saudi Arabia ']
del df[' Kuwait ']
del df[' UAE ']
del df[' United Kingdom ']
del df[' Germany ']
del df[' France ']
del df[' Italy ']
del df[' Netherlands ']
del df[' Greece ']
del df[' Belgium & Luxembourg ']
del df[' Switzerland ']
del df[' Austria ']
del df[' Scandinavia ']
del df[' CIS & Eastern Europe ']

df = df.drop([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
              20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
              40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63,
              64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87,
              88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108,
              109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126,
              127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144,
              145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162,
              163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180,
              181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198,
              199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216,
              217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234,
              235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252,
              253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270,
              271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288,
              289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306,
              307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324,
              325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342,
              343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359])

df1 = df.head(12).sum()
df2 = df.loc[372:383].sum()
df3 = df.loc[384:395].sum()
df4 = df.loc[396:407].sum()
df5 = df.loc[408:419].sum()
df6 = df.loc[420:431].sum()
df7 = df.loc[432:443].sum()
df8 = df.loc[444:455].sum()
df9 = df.loc[456:467].sum()
df10 = df.tail(11).sum()

new_df = {' Years ': ['2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017'],
          ' USA ': [396631, 370704, 417195, 440576, 477213, 491946, 484912, 499509, 516458, 511059],
          ' Canada ': [80044, 70034, 75142, 82932, 87795, 92685, 92827, 96247, 98474, 94769],
          ' Australia ': [833156, 830299, 880558, 956039, 1050373, 1125179, 1074878, 1043568, 1027314, 976915],
          ' New Zealand ': [110772, 93834, 95790, 122995, 123701, 120447, 118688, 127618, 121100, 120436],
          ' Africa ': [90631, 75540, 75540, 73390, 67994, 66634, 66070, 67453, 72535, 65231]
          }
df = pd.DataFrame(new_df)

df.index = df[' Years ']
del df[' Years ']

df_des = df.describe()


class dfplots():

    def usa(self):
        plt.scatter(df.index, df[' USA '], label="USA")
        plt.legend(loc="best")
        plt.xlabel("Years", fontsize=12)
        plt.ylabel("No. Of Visitors", fontsize=11)
        plt.title("Int Monthly Visitor(USA)", fontsize=12)
        plt.grid()
        plt.show()
        # plt.savefig('Int Monthly Visitor(USA).png')

    def ca(self):
        plt.scatter(df.index, df[' Canada '], label="Canada")
        plt.legend(loc="best")
        plt.xlabel("Years", fontsize=12)
        plt.ylabel("No. Of Visitors", fontsize=11)
        plt.title("Int Monthly Visitor(Canada)", fontsize=12)
        plt.grid()
        plt.show()
        # plt.savefig('Int Monthly Visitor(Canada).png')

    def au(self):
        plt.scatter(df.index, df[' Australia '], label="Australia")
        plt.legend(loc="best")
        plt.xlabel("Years", fontsize=12)
        plt.ylabel("No. Of Visitors", fontsize=11)
        plt.title("Int Monthly Visitor(Australia)", fontsize=12)
        plt.grid()
        plt.show()
        # plt.savefig('Int Monthly Visitor(Australia).png')

    def nz(self):
        plt.scatter(df.index, df[' New Zealand '], label="New Zealand")
        plt.legend(loc="best")
        plt.xlabel("Years", fontsize=12)
        plt.ylabel("Avg No. Of Visitors", fontsize=11)
        plt.title("Avg Int Monthly Visitor(New Zealand)", fontsize=12)
        plt.grid()
        plt.show()
        # plt.savefig('Int Monthly Visitor(New Zealand).png')

    def aa(self):
        plt.scatter(df.index, df[' Africa '], label="Africa")
        plt.legend(loc="best")
        plt.xlabel("Years", fontsize=12)
        plt.ylabel("No. Of Visitors", fontsize=11)
        plt.title("Int Monthly Visitor(Africa)", fontsize=12)
        plt.grid()
        plt.show()
        # plt.savefig('Int Monthly Visitor(Africa).png')

    def usa_des(self):
        plt.scatter(df_des.index, df_des[' USA '], label="USA")
        plt.legend(loc="best")
        plt.xlabel("Years", fontsize=12)
        plt.ylabel("Avg No. Of Visitors", fontsize=11)
        plt.title("Avg Int Monthly Visitor(USA)", fontsize=12)
        plt.grid()
        plt.show()
        # plt.savefig('Int Monthly Visitor(USA)(AVG).png')

    def ca_des(self):
        plt.scatter(df_des.index, df_des[' Canada '], label="Canada")
        plt.legend(loc="best")
        plt.xlabel("Years", fontsize=12)
        plt.ylabel("Avg No. Of Visitors", fontsize=11)
        plt.title("Avg Int Monthly Visitor(Canada)", fontsize=12)
        plt.grid()
        plt.show()
        # plt.savefig('Int Monthly Visitor(Canada)(AVG).png')

    def au_des(self):
        plt.scatter(df_des.index, df_des[' Australia '], label="Australia")
        plt.legend(loc="best")
        plt.xlabel("Years", fontsize=12)
        plt.ylabel("Avg No. Of Visitors", fontsize=11)
        plt.title("Avg Int Monthly Visitor(Australia)", fontsize=12)
        plt.grid()
        plt.show()
        # plt.savefig('Int Monthly Visitor(Australia)(AVG).png')

    def nz_des(self):
        plt.scatter(df_des.index, df_des[' New Zealand '], label="New Zealand")
        plt.legend(loc="best")
        plt.xlabel("Years", fontsize=12)
        plt.ylabel("Avg No. Of Visitors", fontsize=11)
        plt.title("Avg Int Monthly Visitor(New Zealand)", fontsize=12)
        plt.grid()
        plt.show()
        # plt.savefig('Int Monthly Visitor(New Zealand)(AVG).png')

    def aa_des(self):
        plt.scatter(df_des.index, df_des[' Africa '], label="Africa")
        plt.legend(loc="best")
        plt.xlabel("Years", fontsize=12)
        plt.ylabel("Avg No. Of Visitors", fontsize=11)
        plt.title("Avg Int Monthly Visitor(Africa)", fontsize=12)
        plt.grid()
        plt.show()
        # plt.savefig('Int Monthly Visitor(Africa)(AVG).png')

    def avg_des(self):
        ax1 = df_des.plot(kind='bar', title="Avg Int Monthly Visitor(ALL)", figsize=(15, 15), legend=True, fontsize=15,
                          grid=True)
        my_fig = ax1.get_figure()
        my_fig.savefig('Avg Int Monthly Visitor(ALL).png')

    def avg_df(self):
        ax2 = df.plot(kind='bar', title="Int Monthly Visitor(ALL)", figsize=(15, 15), legend=True, fontsize=15,
                      grid=True)
        my_fig = ax2.get_figure()
        my_fig.savefig('Int Monthly Visitor(ALL).png')


# print(df)  # DF
# print(df_des) # Describe DF

alldf = dfplots()