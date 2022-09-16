'''
A teacher asks the class to open their books to a page number. 
A student can either start turning pages from the front of the book or from the back of the book. 
They always turn pages one at a time. When they open the book, page 1 is always on the right side:


When they flip page , they see pages 2 and 3. Each page except the last page will always be printed on both sides. 
The last page may only be printed on the front, given the length of the book. If the book is n pages long, and a student wants to turn to page

p, what is the minimum number of pages to turn? They can start at the beginning or the end of the book.

Given n and p, find and print the minimum number of pages that must be turned in order to arrive at page . 


'''
def pageCount(n, p):
    # Create a dictionary (hash map) of page turns and respective pages 
    page_turns = {}
    pages = (n//2) + 1
    
    #inititalize page turns dictionary starting with key 0 with the values being an array of page numbers
    for page in range(pages + 1):
        page_no = page * 2
        key = '{}'.format(page)
        page_turns[key] = [page_no, page_no + 1]
    
    
    #get the last key in the page turns dictionary
    last_key = int(list(page_turns.keys())[-1])
    
    #Loop through the keys
    for page in list(page_turns.keys()):
        #Find the key with the value of p
        if p in page_turns[page]:
            print('key found: ', page)
            key = int(page)
            #Check if page turns from behind would be less. 
            #Subtract one because you dont need to turn the first page even from behind
            from_last_key = (last_key - key) - 1
            if from_last_key < key:
                return from_last_key
            else:
                return key

print(pageCount(5,4))

#simpler version
def page_count(n, p):
    #No of turns from start to finish
    startFinish = n//2
    #Number of turns from front to page
    fromFront = p // 2
    #No of turns from back to page
    fromBack = startFinish - fromFront

    #Return minimum value
    return min(fromFront, fromBack)

print(page_count(5,4))