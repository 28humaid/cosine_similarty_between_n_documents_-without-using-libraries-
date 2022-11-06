#ek document ko list of n documents bna diya
listOfDocuments=[]
with open('britannicaCricket.txt','r') as document:
  for line in document:
    listOfDocuments.append(line.lower())
#printing listing for testing    
#print(listOfDocuments)

#function to create list from a document
def creatingListFromDoc(doc):
  return(doc.split())
#list of list of documents isme store hogi
outerDocList=[]
#list of documents mei se ek item(document) liya
for document in listOfDocuments:
  #us bni hui list ko ek list of lists mei append kr diya 
  outerDocList.append(creatingListFromDoc(document))
#printing list for testing 
#print(outerDocList)

stopWords=['being','each','from','its','his','be','there','their','with','then','where','when','a','an','the','is','was','for','but','this','that','it','by','have','has','had','and','or','not','to','on','of','so','are','they','at','either','if','in','as']
#stop words wo extra words jinse bina wajh similarity badhne k chance badh jaate hain

#clean list of list of documents ko store krne k liye
outerCleanDocList=[]
#function for cleaning
def listCleaning(list1,list2):
  cleanList=[]
  for item1 in list1:
    present=False
    for item2 in list2:
      if item1 == item2:
        present=True
        break
    if present is False:
      cleanList.append(item1)
  return cleanList

for document in outerDocList:
  outerCleanDocList.append(listCleaning(document,stopWords))

#printing cleaned list of lists for testing
#for item in outerCleanDocList:
#  print(item)

#selecting set of unique words from all lists  
setOfCleanWords=set().union(*outerCleanDocList)
#print('set of clean words : ',setOfCleanWords)

#creating term frequency for each document
def createTermFrequencies(ourList,cleanList):
  termFrequency={}
  for item1 in cleanList:
    termFrequency[item1]=0
    for item2 in ourList:
      if item1 == item2:
        termFrequency[item1]+=1
  return termFrequency

#list of all term frequencies
termFrequencies=[]
for document in outerCleanDocList:
  termFrequencies.append(createTermFrequencies(document,setOfCleanWords))
#printing term frequencies for testing
#for item in termFrequencies:
#  print(item)

#function for calculating dot product
def dot(A,B):
  return (sum(a*b for a,b in zip(A.values(),B.values())))
#function for calculating cosine similarity
def cosine_similarity(a,b):
  return dot(a,b) / ( (dot(a,a) **.5) * (dot(b,b) ** .5) )

for tf1,i in zip(termFrequencies,range(len(termFrequencies))):
  for tf2,j in zip(termFrequencies,range(i+1,len(termFrequencies))):
    print('cosine similarity between ',i,' and ',j,' document : ',cosine_similarity(tf1,tf2)) 