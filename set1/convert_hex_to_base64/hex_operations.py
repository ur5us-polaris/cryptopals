from base64 import b64encode
import binascii


class HexOperations:
    @staticmethod
    def hex_string_to_base64(hex_string: str) -> bytes:
        # Convert the hex string into bytes
        hex_string_b = binascii.unhexlify(hex_string)
        # Base64 encode the bytes and return the result
        return b64encode(hex_string_b)

