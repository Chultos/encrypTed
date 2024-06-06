I am not very knowledgeable in ciphers but i think this is a pretty robust one

Here is how the cipher works:
- You can input any text (probably not weird ASCII characters, i did not check)
- It will ask you for X and Y, these numbers are used to translate the letters and numbers to different spots in the alphabet, t does not loop the alphabet / 0-9 numbers if you have an X or Y value that is too high, instead, it bounces back when it reaches the end/start (like a ball against a wall)
- You can add a number of useless binary characters in the key to make the cipher even stronger
- At the end, you will get the encrypted text and the binary paragraph used to decipher the text


Example:
Text: This is a test, all punctu4ti0n will stay in this mess@ge because its funny :)
X value: 56
Y value: 404
Amount of useless characters: 10

Result:
Encrypted text: PNEYOOGPAYP,GHRLYJIZQ4ZO2TWORHOPEUETZNEYIKOO@MKHAIEYOKOPYLQJTU:)
Binary Paragraph (spaces are for the explanation): 
Reversed binary key (useless characters are at the beginning when reversed)  X value      Y value      Reverse Indicator for each character (depends on text size)
01000110001111001101101010111100101011101000011111110011010101001001011010   0000111000   0110010100   0000000000000000100001000010000011000000000000000011000000000100

Deciphering result: THISISATEST,ALLPUNCTU4TI0NWILLSTAYINTHISMESS@GEBECAUSEITSFUNNY:)


I worked on this for about a day (~8hrs) in total counting the thinking part