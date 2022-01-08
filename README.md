# Hotspot

 Create a Business User (Demographic best associated with them needs to be chosen) (Needs to be updated based on deals going on each day)
 - Create a Consumer User (Demographic preferences need to be chosen) (18+, 21+ - Businesses would choose which they would be allowed to take)
 - Generate an list of recommendations for Consumer (Needs to continue to update for Consumer based on choices)
 - Keep track of Business's Quota for how many people they want for the night
 - Send Quota Amount of "Invites" to Users depending if they fit that Business's Preferences
 - Keep track of Users choices ("Like" Businesses they want, so they can access favorite clubs)
 - Allow Consumers to Accept or Deny Invites
 - Retrieve User's Location -> (Map to help visualize distance)
 - Keep track if user has visited location (Review based on Thumbs up or down)

 CRUD: Create - Read - Update - Delete. How can the users transform the data your API accesses?
     - Have 2 separate  "Create" functions, one for each type of user.
     - Read through both user types to create recommendations for Comsumers, and invites to give on night of for businesses
     - Update Business Quotas depending on number of invites that were invited - based on given demographics
     - Update Consumer recommendations depending on their "Likes" of Businesses
     - Delete: each type of User can delete their profiles

 ## Design

 - Use flask_restx to build an API server
 - Multiple clients possible -- TBD
 - Handle each major requirement with an API endpoint
 - Use Test-Driven-Development (TDD) to make sure we have testing.
 - Use Swagger for initial interaction with server.
 - Use Swagger, pydoc and good docstrings for documentation.
 - Endpoints:
    - ‘/Inv’- Fetch all invites. Inputs: N/A
    - ‘/Inv_Response’— Returns the response to an invite. Inputs: N/A
    - ‘/buser/interest’— Returns business’s categories of interest. Inputs: N/A
    - ‘/buser/promos’— Returns business’s promos. Inputs: N/A
    - ‘/busers/create/<username>‘ — Creates a business user. Inputs: username 
    - ‘/users/create/<username>’— Create a consumer user. Inputs: username
    -  ‘/busers/all’— Fetch list of all business users. Inputs: N/A
    - ‘/clientHist’— Returns list of all previous clients from the business year. Inputs: N/A
    - ‘/clientList’—  Returns list of clients for a business user. Inputs: N/A
    - ‘/cusers/all'— Returns all consumers. Inputs: N/A
    - ‘/endpoints’— Returns list of all possible endpoints. Inputs: N/A
    - ‘/recList’ — returns list of recommendations for consumer.  Inputs: N/A
    - ‘/revHist’ — returns all reviews that a customer inputted. Inputs: N/A
