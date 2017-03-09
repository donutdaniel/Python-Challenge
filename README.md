# Python-Challenge  
[Challenges here](wwww.pythonchallenge.com)  
**Run in python 3.x**  
By Daniel Ho  
  
  
  
### **problem 0**  
* using key = 1 in the url directs to another page, telling me that 2^38 is much bigger.  
* Produce 2^38 as key. (274877906944)  
  
### **problem 1**  
* picture shows a mapping k->m, o->q, e->g. This defines a map of the alphabet. Each letter is mapped to the letter two down (effectively 2 down).  
* Issue: python does not recognize char addition. have to use ord() and chr().  
* Translate sentence, says use on url.  
* map -> ocr  
  
### **problem 2**  
* Find unique characters in a long comment in the html file.  
* Issue: cannot copy paste simply as string. Too long, and some characters interrupt the string formatting. Solution: store data in input file.  
* Parse the datafile to delete all punctuation. Output: equality.  
  
### **problem 3**  
* Again, data to search for is in page source html.  
* Run through each 9-length string in data, looking for a format like so: xAAAbCCCx. Letters are arbitrary.  
* Runtime: O(n)  
* Concatenate all the middle "small" letters to get: linkedlist  
  
### **problem 4**	
* In url, replace nothing=xxxxx with the current number.	
* Effectively, create a web crawler.	
* Issue: when going through list, several problems arose:
	* First, one page said divide and move on. I initially implemented a state machine, but after no luck, I figured out it was supposed to be a one-time thing		
	* Second: Misleading numbers. There would be multiple numbers in a page, and the correct one is in the format "the next nothing is ...". Use regex search function
* peak.html is the tail
