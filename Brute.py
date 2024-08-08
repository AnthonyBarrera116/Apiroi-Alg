import time
"""
Brute class:
    Stores all combinations before doing confidence and support
"""
class Brute():
    
    def __init__(self,min_s,min_c,num_itemset): 
        self.transactions = []
        self.frequent_sets = []
        self.min_support = min_s
        self.min_confidence = min_c
        self.unique = []
        self.all_combos = []
        self.number_of_itemsets = num_itemset
        self.unique_value_dict = {}

    """
    Reads text file of the transactions 
    NOTE: It can take all data as one and do each indivudal and into different arrays
    """
    def readTest(self,text):
        
        # Open and reads file witht that name
        with open(text, "r") as file:

            # made for the split so it give array of transactions indivdually
            holder = []

            # Read contents of file
            file_contents = file.readlines()

            # goes through each line and strips \n and split data from commas
            # EX: [['toaster', 'backpack', 'laptop', 'diapers'], ['vacuum cleaner', 'shampoo', 'toaster', 'water bottle']]
            for line in file_contents:
                    
                # stripes the \n from the text file at the end
                line = line.rstrip('\n')

                # Splits the data seperate into commas into array of that transaction
                holder.append(line.split(','))

            # Prints transactions data and prints transactions of array
            # EX: [['toaster', 'backpack', 'laptop', 'diapers'], ['vacuum cleaner', 'shampoo', 'toaster', 'water bottle']]
            #print("\nTRANSACTION DATA : ", text_file_name, "\n")
            #print(holder)

            # This store them if you  have more than one transaction it will store the array each data with the split data above
            #EX: [ [ [ 'toaster', 'backpack', 'laptop', 'diapers' ], [ 'vacuum cleaner', 'shampoo', 'toaster', 'water bottle' ] ], [ ['toaster', 'backpack', 'laptop', 'diapers'], ['vacuum cleaner', 'shampoo', 'toaster', 'water bottle'] ] ]
            self.transactions = holder
        

    """
    Get unique values from all the days. If all days it will get all of them even if that day of transactions doesn't have it
    NOTE: even though if there is a value not in a different day the support will remove it since it won't be frequent set since value never appears
    """
    def get_unique(self):

        # get the 1 transaction of the specific transactions
        for transaction in self.transactions:

            # Loops through transactions and checks and imports all values once into unique list
            for item in transaction:

                # if value is not inside uique put it in array
                if item not in self.unique:

                    # append unique into array
                    self.unique.append(item)     
  

    """
    Calculatates for one combination
    
    """
    def support(self, combinations):

        # tracks count
        count = 0

        # Brute force calculate all combos
        for comb in combinations:

            # loops transactions
            for transaction in self.transactions:
                
                # check if in transaction
                if set(comb).issubset(set(transaction)):
                    
                    # increrase
                    count +=1
            
            # calculate support
            support = count/len(self.transactions)
            
            
            # check threshold and add to frequenct sets map to dict for support value
            if support >= self.min_support:

                # hold support for later calculate confidence
                self.unique_value_dict[str(comb)] = support

                # Add to frequent 
                self.frequent_sets.append(comb)
            
            # reset count for next combo
            count = 0



    """
    Calculates confidence from calculated supports and prints asscociation rules
    """
    def confidence_assocition(self):

        # prints rules
        print("Association rules : \n")
        
         # gets Frequent sets
        for fre in self.frequent_sets:
            
            # calculates confidence
            c = self.unique_value_dict[str(fre)] / self.unique_value_dict[str([fre[-1]])]

            # Threshold for confidence
            if c > self.min_confidence:

                # just for checking of printing 1 value or combination support and confidence
                if len(fre) == 1:
                    #print("\n",str(fre), " ---> ", fre[-1], ":\n support: ", self.unique_value_dict[str(fre)],"  confidence:  ", c)
                    continue
                else:
                    print("\n",str(fre[:len(fre) - 1 ]), " ---> ", fre[-1], ":\n support: ", self.unique_value_dict[str(fre)],"  confidence:  ", c)
        

    """
    Get combinations of all values using for loop to go though and uses the amount of itemset you want to go up to
    NOTE: I did this all with for loops and appending to arrays, I do not know how efficent this is. For 4 itemsets it takes a minute to produce total number
    """
    def bruteForce(self):
        
       # loop through k itemsets (1,2,3)
        for k in range(1, self.number_of_itemsets + 1):

            # holder for combinations for each k itemset
            combos = [[]]
            
            # loop through unique values
            for item in range(len(self.unique)):

                # just to hold all combos of the k itemset with duplicates to add them to combos
                new_combos = []

                # loop combos at intilize empty but after first run it has the first n vales
                for combo in range(len(combos)):
                    
                    # if k equals 1 just put in unique values
                    if k == 1:

                        # only used for brute but used for debugging
                        self.all_combos.append([self.unique[item]])

                    # else if k is greater than 1 than you need to make combinations from combinations of the previous combinations
                    else:

                        # hold the combination made                        
                        combination_holder = combos[combo] + [self.unique[item]]

                        # if len is equal two it means it lenght of k itemset
                        if len(combination_holder) == k:

                            # than check if it has already been placed into all combos we don't want duplicates
                            if set(combination_holder) not in [set(x) for x in self.all_combos]:
                                
                                # only used for brute but used for debugging
                                self.all_combos.append(combination_holder)

                        else:
                            # apends all combos no matter what
                            new_combos.append(combination_holder)

                # sets the combos made for that k itemset to combois to be used to add unique values at the end of previous combos of the k - 1 itemset
                combos += new_combos
            

        # Prints all combos and length Debugging
        #print(self.all_combos)
        # print(len(self.all_combos))

        # calucaltes all combinations brute
        self.support(self.all_combos)

        # Calculates confidence and creates association rules
        self.confidence_assocition()

    
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

        print("\n\nDOING TEXT FILE: ", text,"\n")
        
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