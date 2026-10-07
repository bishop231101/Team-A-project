# Week 8 Weekly Journal - Ifeanyi Emeka

## What I Did
This week, I conducted midterm platform compatibility testing for our zero-width Unicode steganography project. I tested the encoded message across Gmail, Microsoft Word, Windows Notepad, the Browser Console, and Discord. I recorded the number of zero-width codec characters that survived each platform and tested whether the original secret message could still be decoded.

## What I Learned
I learned that different platforms handle zero-width Unicode characters differently. Windows Notepad and the Browser Console preserved all 206 codec characters and successfully decoded `CS481-WEEK8`. Gmail preserved only 25 of the 206 characters, while Microsoft Word and Discord removed the zero-width payload completely.

## Problems Encountered
The main problem was that some platforms modified or removed the hidden zero-width characters during transfer. This caused the decoder to fail because there were not enough codec characters remaining to recover the secret message.

## Next Week's Plan
Next week, I will continue analyzing the platform compatibility results and work on improving the robustness and recovery strategy for platforms that modify or remove zero-width Unicode characters.