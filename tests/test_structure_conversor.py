import unittest
from unittest.mock import patch
from structure_conversor import (
    get_inchi_from_smiles,
    get_inchikey_from_inchi,
    get_smiles_from_inchi,
    get_inchi_from_inchikey
)

class TestChemSpiderFunctions(unittest.TestCase):
    # Test get_inchi_from_smiles function
    @patch('requests.post')
    def test_get_inchi_from_smiles(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.text = '<?xml version="1.0" encoding="utf-8"?><string xmlns="http://www.chemspider.com/">InChI=1S/C4H10O/c1-3-4(2)5/h4-5H,3H2,1-2H3</string>'
        
        smiles = "C(C(=O)O)N"
        inchi = get_inchi_from_smiles(smiles)
        
        self.assertEqual(inchi, "InChI=1S/C4H10O/c1-3-4(2)5/h4-5H,3H2,1-2H3")

    # Test get_inchikey_from_inchi function
    @patch('requests.post')
    def test_get_inchikey_from_inchi(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.text = '<?xml version="1.0" encoding="utf-8"?><string xmlns="http://www.chemspider.com/">OTMSDBZUPAUEDD-UHFFFAOYSA-N</string>'
        
        inchi = "InChI=1S/C4H10O/c1-3-4(2)5/h4-5H,3H2,1-2H3"
        inchikey = get_inchikey_from_inchi(inchi)
        
        self.assertEqual(inchikey, "OTMSDBZUPAUEDD-UHFFFAOYSA-N")

    # Test get_smiles_from_inchi function
    @patch('requests.post')
    def test_get_smiles_from_inchi(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.text = '<?xml version="1.0" encoding="utf-8"?><string xmlns="http://www.chemspider.com/">C(C(=O)O)N</string>'
        
        inchi = "InChI=1S/C4H10O/c1-3-4(2)5/h4-5H,3H2,1-2H3"
        smiles = get_smiles_from_inchi(inchi)
        
        self.assertEqual(smiles, "C(C(=O)O)N")

    # Test get_inchi_from_inchikey function
    @patch('requests.post')
    def test_get_inchi_from_inchikey(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.text = '<?xml version="1.0" encoding="utf-8"?><string xmlns="http://www.chemspider.com/">InChI=1S/C4H10O/c1-3-4(2)5/h4-5H,3H2,1-2H3</string>'
        
        inchi_key = "OTMSDBZUPAUEDD-UHFFFAOYSA-N"
        inchi = get_inchi_from_inchikey(inchi_key)
        
        self.assertEqual(inchi, "InChI=1S/C4H10O/c1-3-4(2)5/h4-5H,3H2,1-2H3")

if __name__ == '__main__':
    unittest.main()