import unittest
import DAData as da


class MyTestCase(unittest.TestCase):
    def test_data(self):
        da.alldf.usa()
        # da.alldf.ca()
        # da.alldf.au()
        # da.alldf.nz()
        # da.alldf.aa()
        # da.alldf.usa_des()
        # da.alldf.ca_des()
        # da.alldf.au_des()
        # da.alldf.nz_des()
        # da.alldf.aa_des()
        # da.alldf.avg_df()
        # da.alldf.avg_des()


if __name__ == '__main__':
    unittest.main()
