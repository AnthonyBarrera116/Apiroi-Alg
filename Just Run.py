from Apriori import Apriori
from Brute import Brute
import time

def main():

    # Text
    texts = ['Transactions 1.txt','Transactions 2.txt','Transactions 3.txt','Transactions 4.txt','Transactions 5.txt']
    
    # k item set 
    number_of_itemset = 3

    # min thres for support
    min_s = .20
    
    # min thres for confidence
    min_c = .50
    
    # goes through all text
    for text in texts:

        print("\n\nDOING TEXT FILE (Aprori): ", text,"\n")
    
        # intilize function same fro Aprori and brute
        ap = Apriori(min_s,min_c ,number_of_itemset)

        # read text file
        ap.readTest(text)
        
        # get unique values from all transactioins
        ap.get_unique()

        # start time of aprori
        start = time.time()
        
        # start aprori
        ap.aprori()

        # end time
        end = time.time()

        # time it took
        print("\nTIME IT TOOK: ",end - start)

        #_______________________Brute__________________________

        
        print("\n\nDOING TEXT FILE (Brute): ", text,"\n")

        # intilizes class for burte
        brute = Brute(min_s,min_c ,number_of_itemset)

        # reads transaction file
        brute.readTest(text)

        brute.get_unique()

        # start time of aprori
        start = time.time()
        
        # start aprori
        brute.bruteForce()

        # end time
        end = time.time()

        # time it took
        print("\nTIME IT TOOK: ",end - start)

if __name__ == "__main__":

    main()