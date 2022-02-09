# Hotspot

 - Create a Business User 
 - Create a Consumer User

 - Process for each day (Loop):
 - At the beginning of the day, Businesses set their quotas
 - At the beginning of the day, Consumers set their preferences by choosing three types of places they are interested in visiting that night, and preferred location
 - Based on their interests, they are shown their daily curated list (three businesses [one at a time])
       If they are interested, they will then be prompted to share their total party size attending, and get details about the event (which is all that they will   then see for the rest of the night. This resets every day, and the next day they are prompted to select interests and preferred location again)
       if they are not interested, they will be shown the next business on the list, and are unable to go back to the first business.
 - Once the consumer sends in their party size, they are then put on the business' Consumer list, which lists all the consumers coming to the business that night
 - the Party size is then subtracted from the business' total quota
 - the business' consumer list is reset at the end of the day

 CRUD: Create - Read - Update - Delete. How can the users transform the data your API accesses?
     - Have 2 separate  "create" functions, one for each type of user [Business and Consumer]
     - Read through both user types to match the consumers to businesses, to fulfill business quotas.
     - Update Business Quotas depending on their daily requirements
     - Update Consumer recommendations depending on their interests and their location requirements each day
     - Delete: each type of User can delete their profiles

 ## Design

 - Use flask_restx to build an API server
 - Multiple clients possible -- TBD
 - Handle each major requirement with an API endpoint
 - Use Test-Driven-Development (TDD) to make sure we have testing.
 - Use Swagger for initial interaction with server.
 - Use Swagger, pydoc and good docstrings for documentation.
 - Endpoints:
    - ‘/bUsers/create/<username>‘ — Creates a business user. Inputs: username, Business Name, Age Restrictions, Business Type (POST)
    - ‘/bUsers/bQuota - Creates the daily quota for the business. Input: Quota - Amount of people that the business requires for the night (POST)
    - ‘/bUsers/eventInfo - Creates the events details. Input: Event Name, Business Name, Location, Pictures, Price Range, Event Hours (POST)
    - ‘/bUsers/delete - Allows the businesses to delete their account. Input: NA (POST??)
    - ‘/cUsers/create/<username>’— Create a consumer user. Inputs: username,full name, age, gender (POST)
    - ‘/cUsers/cDaily - Creates the users daily preferences. Inputs: Interests (x3), Desired Neighborhood for business to be in (POST)
    - ‘/cUsers/partySize - Creates the total party size from the consumer. Inputs: the size of the party attending [not including the user] (POST)
    - ‘/cUsers/delete - Allows the consumers to delete their account. Input: NA (POST??)

    - ‘/bList’— Fetch list of all business users. Inputs: N/A
    - ‘/cList'— Returns all consumers. Inputs: N/A
    - ‘/endpoints’— Returns list of all possible endpoints. Inputs: N/A
