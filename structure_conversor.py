import requests

def get_inchi_from_smiles(smiles):
    """
    Convert a SMILES string to its corresponding InChI representation using the ChemSpider web service.

    Args:
        smiles (str): The SMILES string to be converted.

    Returns:
        str or None: The corresponding InChI representation if the conversion is successful, 
                     otherwise None.

    Raises:
        requests.HTTPError: If the HTTP request fails.

    Example:
        >>> smiles = "C(C(=O)O)N"
        >>> inchi = get_inchi_from_smiles(smiles)
        >>> print("InChI:", inchi)
    """
    url = "http://www.chemspider.com/InChI.asmx/SMILESToInChI"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'smiles': smiles}
    
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:

        inchi = response.text.replace('<?xml version="1.0" encoding="utf-8"?>', '').strip()
        inchi = inchi.replace('<string xmlns="http://www.chemspider.com/">', '').replace('</string>', '').strip()
        return inchi
    else:
        response.raise_for_status()



def get_inchikey_from_inchi(inchi):
    """
    Convert an InChI string to its corresponding InChIKey representation using the ChemSpider web service.

    Args:
        inchi (str): The InChI string to be converted.

    Returns:
        str or None: The corresponding InChIKey representation if the conversion is successful, 
                     otherwise None.

    Raises:
        requests.HTTPError: If the HTTP request fails.

    Example:
        >>> inchi = "InChI=1S/C4H10O/c1-3-4(2)5/h4-5H,3H2,1-2H3"
        >>> inchikey = get_inchikey_from_inchi(inchi)
        >>> print("InChIKey:", inchikey)
    """
    url = "http://www.chemspider.com/InChI.asmx/InChIToInChIKey"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'inchi': inchi}
    
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        inchikey = response.text.replace('<?xml version="1.0" encoding="utf-8"?>', '').strip()
        inchikey = inchikey.replace('<string xmlns="http://www.chemspider.com/">', '').replace('</string>', '').strip()
        return inchikey
    else:
        response.raise_for_status()



def get_smiles_from_inchi(inchi):
    """
    Convert an InChI string to its corresponding SMILES representation using the ChemSpider web service.

    Args:
        inchi (str): The InChI string to be converted.

    Returns:
        str or None: The corresponding SMILES representation if the conversion is successful, 
                     otherwise None.

    Raises:
        requests.HTTPError: If the HTTP request fails.

    Example:
        >>> inchi = "InChI=1S/C4H10O/c1-3-4(2)5/h4-5H,3H2,1-2H3"
        >>> smiles = get_smiles_from_inchi(inchi)
        >>> print("SMILES:", smiles)
    """
    url = "https://www.chemspider.com/InChI.asmx/InChIToSMILES"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'inchi': inchi}
    
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        smiles = response.text.replace('<?xml version="1.0" encoding="utf-8"?>', '').strip()
        smiles = smiles.replace('<string xmlns="http://www.chemspider.com/">', '').replace('</string>', '').strip()
        return smiles
    else:
        response.raise_for_status()


def get_inchi_from_inchikey(inchi_key):
    """
    Convert an InChIKey to its corresponding InChI representation using the ChemSpider web service.

    Args:
        inchi_key (str): The InChIKey string to be converted.

    Returns:
        str or None: The corresponding InChI representation if the conversion is successful, 
                     otherwise None.

    Raises:
        requests.HTTPError: If the HTTP request fails.

    Example:
        >>> inchi_key = "OTMSDBZUPAUEDD-UHFFFAOYSA-N"
        >>> inchi = get_inchi_from_inchikey(inchi_key)
        >>> print("InChI:", inchi)
    """
    url = "http://www.chemspider.com/InChI.asmx/InChIKeyToInChI"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = {'inchi_key': inchi_key}
    
    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        inchi = response.text.replace('<?xml version="1.0" encoding="utf-8"?>', '').strip()
        inchi = inchi.replace('<string xmlns="http://www.chemspider.com/">', '').replace('</string>', '').strip()
        return inchi
    else:
        response.raise_for_status()


def main(): 
    smiles = "C(C(=O)O)N"
    
    try:
        inchi = get_inchi_from_smiles(smiles)
        print("InChI:", inchi)
    except requests.HTTPError as e:
        print("HTTP error occurred:", e)

    inchi = "InChI=1S/C4H10O/c1-3-4(2)5/h4-5H,3H2,1-2H3"
    try:
        inchikey = get_inchikey_from_inchi(inchi)
        print("InChIKey:", inchikey)
    except requests.HTTPError as e:
        print("HTTP error occurred:", e)


    inchi = "InChI=1S/C4H10O/c1-3-4(2)5/h4-5H,3H2,1-2H3"
    try:
        smiles = get_smiles_from_inchi(inchi)
        print("SMILES:", smiles)
    except requests.HTTPError as e:
        print("HTTP error occurred:", e)

    inchi_key = "OTMSDBZUPAUEDD-UHFFFAOYSA-N"
    try:
        inchi = get_inchi_from_inchikey(inchi_key)
        print("InChI:", inchi)
    except requests.HTTPError as e:
        print("HTTP error occurred:", e)

if __name__ == "__main__":
    main()
