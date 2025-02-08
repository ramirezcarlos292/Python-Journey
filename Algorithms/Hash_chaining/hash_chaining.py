# Function to display the hash table
def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")
        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")
        print()

# Creating a hash table as a nested list
HashTable = [[] for _ in range(10)]

# Hashing function to return the key for every value
def Hashing(keyvalue):
    return keyvalue % len(HashTable)

# Insert function to add values to the hash table
def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

# Driver Code
insert(HashTable, 10, 'Allahabad')
insert(HashTable, 25, 'Mumbai')
insert(HashTable, 5, 'Delhi')
insert(HashTable, 20, 'Chennai')

# Display the hash table
display_hash(HashTable)