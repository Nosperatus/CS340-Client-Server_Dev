# -*- coding: utf-8 -*-
from pymongo import MongoClient
from bson.objectid import ObjectId

#Class to handle connection to MongoDB with fixed connection information in the constructor
#Class will also handle CRUD operations in MongoDB
class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30313 #fixed port
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# 'CREATE' function to insert documents into MongoDB (C)RUD
    def create(self, data):
        #If data is passed successfully, try to add it to the database
        if data:
            #Try for exception handling
            try:
                print("Starting import...")
                self.database.animals.insert_one(data)  # data should be dictionary
                print("Success!")
                return True
                
            #Catch for exception handling
            except Exception as e:
                print('Something went wrong: '+ str(e))
                return False
        else:
            print("Nothing to create, because data parameter is empty")
            return False
        
# 'READ' function to retrieve & read document data C(R)UD
    def read(self, search):
        #If search parameters were passed into find(), attempt to search under the constraints
        if search:
            #Try for exception handling
            try:
                #Take search results and create a new list from it by appending each search result
                result = self.database.animals.find(search)
                resultList = []
                for cursor in result:
                    resultList.append(cursor)
                
                #Return the new list for the user, will return an empty list if no search results found
                return resultList
            
            #Catch for exception handling    
            except Exception as e:
                print('Something went wrong: '+ str(e))
                return exception
            
        #If no search parameters passed to find(), perform a search all   
        else:
            #Try for exception handling
            try:
                #Take search all results and create a new list from it by appending each search result
                result = self.database.animals.find()
                resultList = []
                for cursor in result:
                    resultList.append(cursor)
                
                #Return the new list for the user
                return resultList
            
            #Catch for exception handling    
            except Exception as e:
                print('Something went wrong: '+ str(e))
                return exception
            
# 'UPDATE ONE' function to update an existing document CR(U)D - Uses update_one MongoDB method
    def updateOne(self, targetDoc, dataToUpdate):
        if targetDoc and dataToUpdate:
            #Try for exception handling
            try:
                result = self.database.animals.update_one(targetDoc, dataToUpdate)
                totalUpdates = result.modified_count
                if totalUpdates > 0:
                    print("The following number of documents were updated successfully:")
                    return totalUpdates
                
                else:
                    print("Failed to update, number of documents updated:")
                    return totalUpdates
                
            #Catch for exception handling    
            except Exception as e:
                print('Something went wrong: '+ str(e))
                return exception
            
# 'UPDATE MANY' function to update an existing document CR(U)D - Uses update_many MongoDB method
    def updateMany(self, targetDocs, dataToUpdate):
        if targetDocs and dataToUpdate:
            #Try for exception handling
            try:
                result = self.database.animals.update_many(targetDocs, dataToUpdate)
                totalUpdates = result.modified_count
                if totalUpdates > 0:
                    print("The following number of documents were updated successfully:")
                    return totalUpdates
                
                else:
                    print("Failed to update, number of documents updated:")
                    return totalUpdates
                
            #Catch for exception handling    
            except Exception as e:
                print('Something went wrong: '+ str(e))
                return exception

# 'DELETE ONE' function to delete an existing document CRU(D) - Uses delete_one MongoDB method
    def deleteOne(self, docToDelete):
        if docToDelete:
            #Try for exception handling
            try:
                result = self.database.animals.delete_one(docToDelete)
                totalDeletions = result.deleted_count
                if totalDeletions > 0:
                    print("The following number of documents were deleted successfully:")
                    return totalDeletions
                
                else:
                    print("Failed to delete, number of documents deleted:")
                    return totalDeletions
                
            #Catch for exception handling    
            except Exception as e:
                print('Something went wrong: '+ str(e))
                return exception
            
# 'DELETE MANY' function to delete an existing document CRU(D) - Uses delete_many MongoDB method
    def deleteMany(self, docsToDelete):
        if docsToDelete:
            #Try for exception handling
            try:
                result = self.database.animals.delete_many(docsToDelete)
                totalDeletions = result.deleted_count
                if totalDeletions > 0:
                    print("The following number of documents were deleted successfully:")
                    return totalDeletions
                
                else:
                    print("Failed to delete, number of documents deleted:")
                    return totalDeletions
                
            #Catch for exception handling    
            except Exception as e:
                print('Something went wrong: '+ str(e))
                return exception

            
###SPECIFIC QUERY FILTERS###
###Used for filter buttons 1,2,3 on user dashboard###

#Water Rescue filter method:
    def waterRescueFilter(self):
        try:
            #Search for suitable Water Rescue dogs based on client provided parameters
            result = self.database.animals.find({"animal_type":"Dog",
                                                 "breed":{"$in":["Labrador Retriever Mix",
                                                                 "Chesa Bay Retr Mix",
                                                                 "Newfoundland Mix",]},
                                                 "sex_upon_outcome":"Intact Female",
                                                 "age_upon_outcome_in_weeks":{"$gte":26, "$lte":156}})
            
            #Take search results and create a new list from it by appending each search result
            resultList = []
    #        totalDocs = 0  #Used for debugging
            for cursor in result:
                resultList.append(cursor)
      #          totalDocs = totalDocs + 1 #Used for debugging
                
            #Return the new list for the user, will return an empty list if no search results found
       #     print(totalDocs) #Used for debugging
            return resultList
            
        #Catch for exception handling    
        except Exception as e:
            print('Something went wrong: '+ str(e))
            return exception
        
#Mountain or Wilderness Rescue filter method:
    def mountainOrWildernessRescueFilter(self):
        try:
            #Search for suitable Water Rescue dogs based on client provided parameters
            result = self.database.animals.find({"animal_type":"Dog",
                                                 "breed":{"$in":["German Shepherd",
                                                                 "Alaskan Malamute",
                                                                 "Old English Sheepdog",
                                                                 "Siberian Husky",
                                                                 "Rottweiler"]},
                                                "sex_upon_outcome":"Intact Male",
                                               "age_upon_outcome_in_weeks":{"$gte":26, "$lte":156}})
            
            #Take search results and create a new list from it by appending each search result
            resultList = []
        #    totalDocs = 0  #Used for debugging
            for cursor in result:
                resultList.append(cursor)
       #         totalDocs = totalDocs + 1 #Used for debugging
                
            #Return the new list for the user, will return an empty list if no search results found
      #      print(totalDocs) #Used for debugging
            return resultList
            
        #Catch for exception handling    
        except Exception as e:
            print('Something went wrong: '+ str(e))
            return exception

# Disaster or Individual Tracking
    def disasterOrIndividualTrackingFilter(self):
        try:
            #Search for suitable Water Rescue dogs based on client provided parameters
            result = self.database.animals.find({"animal_type":"Dog",
                                                 "breed":{"$in":["Doberman Pinsch",
                                                                 "German Shepherd",
                                                                 "Golden Retriever",
                                                                 "Bloodhound",
                                                                 "Rottweiler"]},
                                                "sex_upon_outcome":"Intact Male",
                                               "age_upon_outcome_in_weeks":{"$gte":20, "$lte":300}})
            
            #Take search results and create a new list from it by appending each search result
            resultList = []
       #     totalDocs = 0  #Used for debugging
            for cursor in result:
                resultList.append(cursor)
             #   totalDocs = totalDocs + 1 #Used for debugging
                
            #Return the new list for the user, will return an empty list if no search results found
        #    print(totalDocs) #Used for debugging
            return resultList
            
        #Catch for exception handling    
        except Exception as e:
            print('Something went wrong: '+ str(e))
            return exception