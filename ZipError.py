def ZipError():
    """判断汉化包是否损坏"""

    import zipfile
    VERSION = "V2.0"
    try:
        f=zipfile.ZipFile("MTE_PatchCHS"+VERSION+".part1.cjxpak")
        f=zipfile.ZipFile("MTE_PatchCHS"+VERSION+".part2.cjxpak")
        f=zipfile.ZipFile("MTE_PatchCHS"+VERSION+".part3.cjxpak")
    except zipfile.BadZipFile:
        return False
    return True
