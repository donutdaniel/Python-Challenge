# Python-Challenge  
[Challenges here](wwww.pythonchallenge.com)  
**Run in python 3.x**  
By Daniel Ho  
  
  
  
### **Problem 0**  
* using key = 1 in the url directs to another page, telling me that 2^38 is much bigger.  
* Produce 2^38 as key. (274877906944)  
  
### **Problem 1**  
* picture shows a mapping k->m, o->q, e->g. This defines a map of the alphabet. Each letter is mapped to the letter two down (effectively 2 down).  
* Issue: python does not recognize char addition.
	* Solution: Use ord() and chr().  
* Translate sentence, says use on url.  
* map -> ocr  
  
### **Problem 2**  
* Find unique characters in a long comment in the html file.  
* Issue: cannot copy paste simply as string. Too long, and some characters interrupt the string formatting.
	* Solution: store data in input file.  
* Parse the datafile to delete all punctuation. Output: equality.  
  
### **Problem 3**  
* Again, data to search for is in page source html.  
* Run through each 9-length string in data, looking for a format like so: xAAAbCCCx. Letters are arbitrary.  
* Runtime: O(n), n is length of data 	
* Concatenate all the middle "small" letters to get: linkedlist	
	
### **Problem 4**	
* In url, replace nothing=xxxxx with the current number.	
* Effectively, create a web crawler.	
* Runtime: O(n), n is size of linkedlist	
* Issue: when going through list, several problems arose:
	* First: one page said divide and move on. I initially implemented a state machine, but after no luck, I figured out it was supposed to be a one-time thing		
	* Second: Misleading numbers. There would be multiple numbers in a page, and the correct one is in the format "the next nothing is ...". Use regex search function	
* peak.html is the tail	
	
### **Problem 5**	
* Wow, this one was difficult... mostly because I didn't know what pickle was. Thanks Obama.	
* At first I tried unpickling the image, but it wouldn't work. I realized there was a different file inside the source, and unpickled that.	
* Printing the object revealed that it was a list...of lists...of even more lists. Spacing and #'s screamed ASCII art, so I put it through a nested loop to print it out. 	
* Runtime: O(n^2), n is lists/characters on a line (doesn't necessarily have to be the same, but for sake of simplicity, n^2)	
* ASCII art shows "channel"	

### **Problem 6**	
* Source comment says "zip", so I thought okay... python zip() function... zip file... maybe changing the key to zip?	
* changing channel to zip in the url only tells me to "find the zip". I tried zipper, and got something really weird, telling me [:n] is to take first n characters. Turns out, changing the .html to .zip gives me a downloadable zip file.		
* In that zip was a folder, and it contained another linkedlist type problem (nothing=xxxxx). The end says "collect the comments"	
* Zipfile artifacts have comments in them. Putting it all together prints another ascii art: hockey.
* hockey is not the correct answer. Looking closer, hockey is spelled out with letters in oxygen.
	
### **Problem 7**	
* Image processing. Originally, I used pypng module, but PIL (pillow in python 3.x) is much better. 	
* Use the getpixel() function for the greyscale line in the middle of the image. Every 7 steps, translate the color code to ASCII characters. The ending characters give an array of numbers, which then translate to ASCII chars again.
* Key is integrity

### **Problem 8**
* Absolutely no idea what format the username and password was in. I had to google some hints in order to know to use bzip2 (bz2). 
* Convert string to bytes, then decompress it. Username is huge, password is file.
	
### **Problem 9**
* 