import base64, time
def main(): answer = input(decodeAndPrintB64("V2lsbCB5b3UgZ28gdG8gcHJvbSB3aXRoIG1lPwo=")); print(decodeAndPrintB64("TEVUUyBHT09PISBJJ2xsIHNlZSB5b3UgdGhlbiE=")) if("yes" in answer) else print(decodeAndPrintB64("QXcgbWFuLiBJIHJlYWxseSB3YW50ZWQgdG8gZ28gd2l0aCB5b3UuIEkgaG9wZSB5b3UgZmluZCBzb21lb25lIG5pY2UgdGhvdWdoLg==")) if("no" in answer) else print(decodeAndPrintB64("aG1tLCBJIGNvdWxkbid0IHRlbGwgd2hhdCB5b3VyIGFuc3dlciB3YXMuIHBsZWFzZSByZXR1cm4gaXQgaW4gYSBib29sZWFuIGZvcm0gPDM="))
def decodeAndPrintB64(text): decoded_bytes = base64.b64decode(text); decoded_text = decoded_bytes.decode('utf-8'); return decoded_text
if __name__ == "__main__":main(); time.sleep(4)
