# set1 / Convert hex to base64
The first challenge in `cryptopals` teaches us an important lesson:
> Always operate on raw bytes, never on encoded strings.

In order to fully understand this fundamental lesson, we first need to understand what wrong it comes to correct.
Basically, when we encounter a string, we have at least 4 ways to interpret it. Let's take "facedad" for an example.
This could mean:
* The **actual english words** "face dad"
* Ascii encoded bytes, which after decoding is 0x66 0x61 0x63 0x65 0x64 0x61 0x64 in hexadecimal base.
* **Base64 encoded bytes**, which after decoding is 0x7da71e75a7 in hexadecimal base, or 539674703271 in decimal
* **Hex encoded bytes** 0xfacedad, which is 262991277 in decimal

Of course, sometimes we might get a hint for the right interpretation. For example, a '==' suffix will almost always
indicate the string is a base64 encoding of some bytes, and seeing characters that are not digits or
in range of 'a' to 'f' will rule out hex encoding. But as seen with "face dad", many strings will not be so kind with us.

With this in mind, and in context of `cryptopals` challenges, we will need to understand right from the start what exactly
we were asked to encrypt/decrypt or encode/decode. Right from this first challenge, this is a possible pitfall.
We are give the INPUT string `49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d`
and asked to base64 encode it to a given OUTPUT string.
The naive approach will be converting the INPUT string to bytes by characters ascii value (0x34 0x39 0x32 0x37 etc.), but
base64 encoding these bytes will return the wrong string!

On the other hand, after examining the INPUT string, we see it is **made of characters that correspond to hexadecimal digits**,
and therefore **we will treat it as ascii encoded bytes** (0x49 0x27 0x6d 0x20 etc.). Accordingly, we will use `binascii.unhexlify` to convert each 2
characters to a byte with the corresponding value, and than base64 encode the resulting bytes using `base64.b64encode`.
The resulting ascii string returned from `unhexlify` is a treat enough (try printing it out!), but base64 decoding it is
extra fulfilling as we get the correct OUTPUT.

We will encapsulate the `unhexlify` to `base64` operation in a function, as we expect to use it many times in the challenges ahead. 
 


