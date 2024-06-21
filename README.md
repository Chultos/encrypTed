Here is how the cipher works:
- You can input any text (probably not weird ASCII characters, i did not check)
- It will randomly generate X and Y, these numbers are used to translate the letters and numbers to different spots in the alphabet, it does not loop the alphabet / 0-9 numbers if you have an X or Y value that is too high, instead, it bounces back when it reaches the end/start (like a ball between two walls)
- You can add a number of useless binary characters in the key to make the cipher even stronger
- At the end, you will get the encrypted text and the binary paragraph used to decipher the text


Example:
- Text: This is a test, all punctu4ti0n will stay in this mess@ge because its funny :)
- X value: 56
- Y value: 404
- Amount of useless characters: 10

Result:
- Encrypted text: PNEYOOGPAYP,GHRLYJIZQ4ZO2TWORHOPEUETZNEYIKOO@MKHAIEYOKOPYLQJTU:)

- Binary Paragraph (spaces are for the explanation):
![image](https://github.com/Chultos/encrypTed/assets/65951441/ea62f056-8e8d-4fdc-9ef6-e4da7524b397)

- Deciphering result: THISISATEST,ALLPUNCTU4TI0NWILLSTAYINTHISMESS@GEBECAUSEITSFUNNY:)

I am not knowledgeable in ciphers at all (basically watched 1 or 2 Youtube videos) but i think this is a pretty robust one.
It shouldn't be possible to guess the language by looking at the most common letters because they are randomized and the number of possible solutions is extremely huge.

I worked on this for about a day (~8hrs) in total counting the thinking part and looking up Python syntax.  
