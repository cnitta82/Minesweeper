# Journal Entry Microservice
This microservice returns the word count of a given journal entry

## Requesting Data: 
Make sure that wordcounter.py is running. 
To request data, write a journal entry to the text file journalentry.txt.
The entry can be any length or types of characters, aside from a single integer. 


 ## Receiving Data: 
 The microservice will replace the file with a single integer, as the word count of the journal entry.
 It will only do this if the text file contains any text that is not a single integer.
 A journal entry with 50 words will write `50` to journalentry.txt.


 ## Sequence Diagram
 ![image](https://github.com/cnitta82/Minesweeper/assets/16845803/884b54aa-567c-46c2-9410-5ffffb63ea4f)
